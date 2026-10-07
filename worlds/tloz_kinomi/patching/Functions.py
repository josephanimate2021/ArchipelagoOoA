from typing import List

import os
import random
import Utils
import json

from settings import get_settings
from ..common.patching.RomData import RomData
from .Util import *
from .treasureAddresses import sym
from ..common.patching.z80asm.Assembler import Z80Assembler
from ..common.patching.z80asm.Assembler import GameboyAddress
from ..common.patching.Util import simple_hex
from ..data.Constants import *
from .Constants import *
from pathlib import Path
from ..data.Warps import ALL_WARPS

from .. import LOCATIONS_DATA, GiftsOfKinomiMasterKeys


def get_treasure_addr(parsed_sym: sym, rom: RomData, item_name: str):
    item_id, item_subid = get_item_id_and_subid(item_name)
    addr = parsed_sym.find("section", "TreasureObjectData")["full_address"] + (item_id * 4)
    if rom.read_byte(addr) & 0x80 != 0:
        addr = parsed_sym.find("section", "Bank_15")["full_address"] + rom.read_word(addr + 1)
    return addr + (item_subid * 4)

def set_refill_npc(rom: RomData):
    if get_settings().tloz_kinomi_options.refill_npc in REFILL_NPCS:
        refill_npc_addr = REFILL_NPCS[get_settings().tloz_kinomi_options.refill_npc]
        rom.write_byte(refill_npc_addr, 0x01)
    elif get_settings().tloz_kinomi_options.refill_npc != "disabled":
        raise Exception(get_settings().tloz_kinomi_options.refill_npc + " is not a valid option for the refill npc.")

def modify_required_gifts_and_slates_count(parsed_sym: sym, rom: RomData, patch_data):

    # Firstly, modify the sign outside link's house that says the required gifts and slates count.
    rom.write_byte(GameboyAddress(0x22, 0x602c).address_in_rom(), 0x30 + patch_data["options"]["required_gifts"])
    if patch_data["options"]["required_gifts"] == 1:
        rom.write_byte(GameboyAddress(0x22, 0x6032).address_in_rom(), 0x20)
    rom.write_byte(GameboyAddress(0x22, 0x6051).address_in_rom(), 0x30 + patch_data["options"]["required_slates"])
    if patch_data["options"]["required_slates"] == 1:
        rom.write_byte(GameboyAddress(0x22, 0x6058).address_in_rom(), 0x20)

    # Then, we modify the amount of slates neeeded to open the stairs to the temple of the tokay boss room.
    rom.write_byte(GameboyAddress(0x0a, 0x6505).address_in_rom(), patch_data["options"]["required_slates"])

    # And the gifts required to beat ganon.
    rom.write_byte(GameboyAddress(0x04, 0x648c).address_in_rom(), patch_data["options"]["required_gifts"]) # For summoning a tree in forever falls.
    rom.write_byte(GameboyAddress(0x0b, 0x4eb2).address_in_rom(), patch_data["options"]["required_gifts"]) # For getting a din interaction responsible for the zelda getting kidnapped cutscene, which we'll use for the indication that a user got the exact gifts neexed.

def get_asm_files(patch_data):
    if patch_data["options"]["remove_extra_stairs_from_lost_labyrinth_past"]:
        ASM_FILES.append("asm/conditional/no_extra_stairs_for_lost_labyrinth.yaml")
    if patch_data["options"]["open_staircase_to_ancient_ages_locations"]:
        ASM_FILES.append("asm/conditional/add_some_ages_old_locations.yaml")
    return ASM_FILES

def set_treasure_data(parsed_sym: sym, rom: RomData,
                      item_name: str, text_id: int | None,
                      sprite_id: int | None = None,
                      param_value: int | None = None):
    addr = get_treasure_addr(parsed_sym, rom, item_name)
    if text_id is not None:
        rom.write_byte(addr + 0x02, text_id)
    if sprite_id is not None:
        rom.write_byte(addr + 0x03, sprite_id)
    if param_value is not None:
        rom.write_byte(addr + 0x01, param_value)

def alter_treasures(parsed_sym: sym, rom: RomData):

    set_treasure_data(parsed_sym, rom, "Potion", 0x6d)

    # Set data for remote Archipelago items
    set_treasure_data(parsed_sym, rom, "Archipelago Item", 0x57, 0x5a)
    set_treasure_data(parsed_sym, rom, "Archipelago Progression Item", 0x57, 0x59)
    #set_treasure_data(parsed_sym, rom, "King Zora's Potion", 0x45, 0x5e)

    # Make bombs increase max carriable quantity when obtained from treasures,
    # not drops (see asm/seasons/bomb_bag_behavior)
    set_treasure_data(parsed_sym, rom, "Bombs (10)", None, None, 0x90)


def write_chest_contents(parsed_sym: sym, rom: RomData, patch_data):
    """
    Chest locations are packed inside several big tables in the ROM, unlike other more specific locations.
    This puts the item described in the patch data inside each chest in the game.
    """
    for location_name, location_data in LOCATIONS_DATA.items():
        if (
            'collect' not in location_data 
            or 'room' not in location_data 
            or location_data['collect'] != TREASURE_SPAWN_CHEST
            or location_name not in patch_data["locations"]
        ):
            continue
        else:
            table_addr = parsed_sym.find("label", "chestDataGroupTable")
            chest_addr = rom.get_chest_addr(location_data['room'], table_addr.bank, table_addr.offset)
        item_name = patch_data["locations"][location_name]
        rom.write_bytes(chest_addr, get_item_id_and_subid(item_name))

def force_collect_mode_on_nonchest_items(parsed_sym: sym, rom: RomData, patch_data, treasure_object_addresss, asm_content, bank_caves):
    """
    Takes an item object code and changes it's collect mode to accomidate for the modifications
    """
    itemsCount = {}
    locations = {}
    item_name_replacements = {}
    new_item_collect_modes = {}
    existing_item_collect_subids = {}
    banks: dict[str, GameboyAddress] = {}
    for label, address in parsed_sym.get_labels().items():
        if label.startswith("treasureObjectData"):
            banks[label] = address

    # STEP 1: gather the count of each item in rooms without a chest.
    for location_name, location_data in LOCATIONS_DATA.items():
        if (
            'room' not in location_data
            or location_name not in patch_data["locations"]
            or "collect" not in location_data
            or location_data["collect"] == TREASURE_SPAWN_CHEST
        ):
            continue

        item_name = patch_data["locations"][location_name]

        if item_name.startswith("Rupees"):
            item_name_replacements[item_name] = "Rupees"

        for _, v in ITEM_GROUPS.items(): # Make dungeon items generic names for now.
            for e in v:
                if e == item_name:
                    item_name_replacements[item_name] = item_name.split(" (")[0]
                    break

        if item_name in item_name_replacements: # If there are any replacements made for the item name, inject them here.
            item_name = item_name_replacements[item_name]

        # Add count to the item name.
        if item_name not in itemsCount:
            itemsCount[item_name] = 1
        else:
            itemsCount[item_name] += 1

        
        locations[location_name] = location_data

    # STEP 2: force collect mode on counted items. I know this process is slow and inefficent but we have to use the same loop again in order make this new collect mode
    # mechanism work.
    for location_name, location_data in locations.items():

        item_name = patch_data["locations"][location_name]
        item_id, item_subid = get_item_id_and_subid(item_name)
        item_addr = treasure_object_addresss["objects"][item_id]

        if ('randomized' in location_data and not location_data['randomized']) or len(item_addr) == 0:
            continue

        if item_name in item_name_replacements:
            item_name = item_name_replacements[item_name]

        def set_static_item(s):
            staticItemsTable_addr_start = parsed_sym.find("label", "staticItemsReplacementsLookup@staticItemsReplacementsTable")
            bank, addr = staticItemsTable_addr_start.__str__().split(":")
            staticItemsTable_addr_end = parsed_sym.find_addr_end(bank, addr).address_in_rom()
            foundCheckFromRoom = False
            for i in range(staticItemsTable_addr_start.address_in_rom(), staticItemsTable_addr_end, 4):
                groupb, roomb = [int(i) for i in rom.read_bytes(i, 2)]
                group = location_data["room"] >> 8
                room = location_data["room"] & 0xff
                if groupb == group and room == roomb:
                    rom.write_bytes(i + 2, [item_id, s])
                    foundCheckFromRoom = True
                    break
            return foundCheckFromRoom
        def set_shop_item(s):
            count = 0
            itemPricesAddr = parsed_sym.find("label", "shopItemPrices").address_in_rom()
            giveTreasureAddr = parsed_sym.find("label", "shopItemTreasureToGive").address_in_rom()
            textTableAddr = parsed_sym.find("label", "shopItemTextTable").address_in_rom()
            addr = (
                int(item_addr, 0) if not isinstance(item_addr, list) else int(item_addr[s], 0)
            ) + 2
            for i in range(len(SHOP_NAMES_IN_ORDER)):
                if location_name == SHOP_NAMES_IN_ORDER[i]:
                    print(location_name, simple_hex(i))
                    rom.write_byte(itemPricesAddr + i, RUPEE_VALUES[patch_data["shop_prices"][location_data["symbolic_name"]]])
                    rom.write_bytes(giveTreasureAddr + count, [item_id, s])
                    rom.write_byte(textTableAddr + i, int(rom.read_byte(addr)))
                    break
                count += 2
        def set_npc_item(s):
            oldManItemsTableAddr = parsed_sym.find("label", "oldManLocationsTable").address_in_rom()
            foundCheckFromRoom = False
            count = 0
            for i in range(len(NPC_ITEM_ROOM_ORDER)):
                if location_data["room"] == NPC_ITEM_ROOM_ORDER[i]:
                    rom.write_bytes(oldManItemsTableAddr + count, [item_id, s])
                    foundCheckFromRoom = True
                    break
                count += 2
            return foundCheckFromRoom
        def set_boss_items(s, i=0, c=0):
            no_boss_dungeons = [2, 6]
            if i != 7:
                if i in no_boss_dungeons: # continue on if there are no bosses for that dungeon.
                    set_boss_items(s, i+1, c+2)
                elif location_data["dungeon"] == i: # write down the boss checks if there is a dungeon with a boss in it.
                    if location_name.endswith(" Boss"):
                        rom.write_bytes(parsed_sym.find("label", "bossItemTable").address_in_rom() + (
                            0x0c if i == 5
                            else i
                        ) + c, [item_id, s])
                        set_boss_items(s, i+1, c+2)
        def checkItemsWrite(subid):
            if not set_static_item(subid):
                if "dungeon" in location_data:
                    set_boss_items(subid)
                elif location_name not in SHOP_NAMES_IN_ORDER:
                    set_npc_item(subid)
                else:
                    set_shop_item(subid)

        def set_item_gfx():
            wroteBytes = False
            for room, array in APPLY_GFX_CHANGES_TO_INTERACTIONS.items():
                if wroteBytes:
                    break
                if room == location_data["room"] or room == location_name:
                    label, line = array
                    addr = parsed_sym.find("label", label)
                    byte_count = find_address_for_param_helper(line, 0, 3)
                    increamenter = 0
                    rom_addr = GameboyAddress(addr.bank, addr.offset + byte_count).address_in_rom()
                    for i in range(len(INTERACTION_LABEL_INDEXES)):
                        if label in INTERACTION_LABEL_INDEXES[i]:
                            increamenter += i
                            break
                    for id, data in GFX_ITEM_GROUPS.items():
                        if wroteBytes:
                            break
                        count = 0
                        for i, p in data.items():
                            size = p if "@" not in p else p.split("@")[1]
                            def writeBytes(color):
                                palette = ITEM_SPR_COLORS[color] | ITEM_SIZES[size] | (0x02 if "half" in p else 0x09 if "showThreeSprites" in p else 0x00)
                                bytess = [id, count, palette + increamenter]
                                rom.write_bytes(rom_addr, bytess)
                                return True
                            if i == item_name:
                                wroteBytes = writeBytes(p.split("@")[0])
                                break
                            elif "Rupees" in item_name: # Made specificly for Rupees. You may change this code if you need to.
                                rupee_small_subids = [i for i in range(0x04)]
                                rupee_small_subids.append(0x14)
                                rupee_medium_subids = [i for i in range(0x04, 0x0b)]
                                rupee_medium_subids.append(0x12)
                                rupee_large_subids = [i for i in range(0x0b, 0x12)]
                                rupee_large_subids.append(0x13)
                                rupee_colors = {
                                    "dark blue": [2, 5, 40, 30, 300],
                                    "all red": [10, 60, 70, 50, 400, 500, 900, 80, 999]
                                }
                                def itemAlignsWithGroup():
                                    return (
                                        item_subid in rupee_small_subids and i == "rupee_small"
                                    ) or (
                                        item_subid in rupee_medium_subids and i == "rupee_medium"
                                    ) or (
                                        item_subid in rupee_large_subids and i == "rupee_large"
                                    )
                                for color, array in rupee_colors.items():
                                    for j in array:
                                        if item_name == f"Rupees ({j})" and itemAlignsWithGroup():
                                            wroteBytes = writeBytes(color)
                                if not wroteBytes and itemAlignsWithGroup():
                                    wroteBytes = writeBytes("green") # Rupees will look weird because theres no green alternative for them.
                                if wroteBytes:
                                    break
                            elif i in item_name: # For any special case items.
                                if i == "Pearl":
                                    wroteBytes = writeBytes(item_name.split(" ")[0].lower())
                                    break
                            count += 4 if size == "big" else 2
                    break

        def findCollectModeInAddr(subid, add = False):
            if item_name not in existing_item_collect_subids:
                existing_item_collect_subids[item_name] = []
            item_addr_len = len(item_addr) if isinstance(item_addr, list) else 1
            if subid >= 0 and subid < item_addr_len:
                if item_name == "Rupees":
                    collect_mode = [
                        TREASURE_SPAWN_INSTANT,
                        TREASURE_SPAWN_DROP
                    ] # Collect mode is mixed up with the rupees for some reason, so make an array ourselves.
                    if location_data["collect"] not in collect_mode:
                        subid = -1 if not add else item_addr_len
                        return
                    else:
                        for i in range(len(collect_mode)):
                            if collect_mode[i] == location_data["collect"]:
                                subid += 0x16 * (i + 1)
                addr = int(item_addr, 0) if not isinstance(item_addr, list) else int(item_addr[subid], 0)
                collect_mode = int(rom.read_byte(addr))
                collectModeAlreadyExists = False
                for s in range(0x00, 0x70, 0x10):
                    if collectModeAlreadyExists:
                        break
                    for g in range(0x04):
                        if (s | g | TREASURE_SET_ITEM_ROOM_FLAG) == collect_mode:
                            collectModeAlreadyExists = s == location_data["collect"]
                            break
                if not collectModeAlreadyExists:
                    findCollectModeInAddr((subid - 1) if not add else (subid + 1), add)
                else:
                    existing_item_collect_subids[item_name].append(subid)
                    checkItemsWrite(subid)
            else:
                if add:
                    itemId = f"{0x11 if item_name == "Harp" else item_id}"
                    if itemId in treasure_object_addresss["pointers"]:
                        if item_name not in new_item_collect_modes:
                            new_item_collect_modes[item_name] = {}
                        addr_start = int(item_addr[0], 0)
                        offset = GameboyAddress.from_address(addr_start).offset
                        bank1, addr1 = treasure_object_addresss["pointers"][itemId].split(":")
                        for label, address in banks.items():
                            bank, addr = address.__str__().split(":")
                            if address.offset == offset:
                                addr_end = parsed_sym.find_addr_end(bank, addr).address_in_rom()
                                asmFunc = f"{bank}//{label}"
                                #if f"{bank1}/{addr1}/" not in asm_content:
                                    #asm_content[f"{bank1}/{addr1}/"] = f"dw {label}"
                                
                    else: # Using my old method of modifying the collect mode I once tried on mutiple subids (wasn't the best idea but should be fine since we have no pointers here).
                        collectModeModified = False
                        addr = int(item_addr, 0)
                        collect_mode = rom.read_byte(addr)
                        for s in range(0x00, 0x70, 0x10):
                            if collectModeModified:
                                break
                            for g in range(0x04):
                                if (s | g | TREASURE_SET_ITEM_ROOM_FLAG) == collect_mode:
                                    collectModeModified = True
                                    rom.write_byte(addr, location_data["collect"] | g | TREASURE_SET_ITEM_ROOM_FLAG)
                                    break
                else:
                    findCollectModeInAddr(item_subid + 1, True)

        findCollectModeInAddr(item_subid)
        set_item_gfx()

    
def inject_slot_name(rom: RomData, slot_name: str):
    slot_name_as_bytes = list(str.encode(slot_name))
    slot_name_as_bytes += [0x00] * (0x40 - len(slot_name_as_bytes))
    rom.write_bytes(0xfffc0, slot_name_as_bytes)

def set_newGame_stuff(parsed_sym: sym, rom: RomData):
    rom.write_byte(GameboyAddress(0x02, 0x420f).address_in_rom(), 0x02) # Skip the screen to select link, secret or new game and skip to new game
    rom.write_byte(GameboyAddress(0x01, 0x7fc1).address_in_rom(), 0x00) # Set starting bomb to 0.
    rom.write_byte(GameboyAddress(0x02, 0x792f).address_in_rom(), 0x14) # Sets the bank to 14 for the file select text.
    
def write_seed_tree_content(rom: RomData, patch_data):
    for _, tree_data in SEED_TREE_DATA.items():
        original_data = rom.read_byte(tree_data["codeAdress"])
        item_name = patch_data["locations"][tree_data["location"]]
        item_id, _ = get_item_id_and_subid(item_name)
        newdata = (original_data & 0x0f) | (item_id - 0x20) << 4
        rom.write_bytes(tree_data["codeAdress"], [newdata])

# helper function that adds param2 to i unless stopped by my base case, which is helpful for finding the right rom address for a certain param in a table despite changes in the disasm code.
def find_address_for_param_helper(lineNumber, param, param2 = 4, i=0,c=0):
    return i - param if c == lineNumber else find_address_for_param_helper(lineNumber, param, param2, i + param2, c + 1)

def set_warps(parsed_sym: sym, rom: RomData, warp_matchings, entrance_type):
    entrance_dest_groups = []
    exit_dest_groups = []
    warp_array_indexes = {}

    # Apply warp matchings expressed in the patch
    for i in range(len(warp_matchings)): # STEP 1: Get all of the necessary bytes appended to an array for the update.
        warp_array_indexes[warp_matchings[i][0]] = i
        dWarp = ALL_WARPS[entrance_type][i]
        def loop(t, update_array):
            label, index_lineNumber = dWarp[t]
            base_address = parsed_sym.find("label", label)
            if base_address is not None:
                bytes_count = find_address_for_param_helper(index_lineNumber, 2)
                update_array.append(rom.read_bytes(GameboyAddress(base_address.bank, base_address.offset + bytes_count).address_in_rom(), 2))
        for t in [["entrance", entrance_dest_groups], ["exit", exit_dest_groups]]:
            loop(t[0], t[1])
    for e in warp_matchings: # STEP 2: Apply all warps to their randomized position using all gathered bytes
        def modify_warp(from_index, to_index, t, array):
            entrance_label, from_index_lineNumber = ALL_WARPS[entrance_type][from_index][t]
            base_address = parsed_sym.find("label", entrance_label)
            if base_address is not None:
                addr = GameboyAddress(base_address.bank, base_address.offset + (find_address_for_param_helper(from_index_lineNumber, 2))).address_in_rom()
                rom.write_bytes(addr, array[to_index])
                # For some reason modifying the map text dosen't work in kinomi.
                #if t == "entrance" and entrance_type == "dungeons":
                    #group = ["present", "past"][ALL_WARPS[entrance_type][from_index]["group"]]
                    #map_tile = int(rom.read_byte(addr - 1))
                    #address = int("0xa" + parsed_sym.find("label", group + "MapTextIndices").__str__()[4:], 0) + map_tile
                    #print(to_index, (to_index << 3), hex(0x81 | to_index))
                    #rom.write_byte(address, 0x81 | to_index)
        for d in [[warp_array_indexes[e[0]], warp_array_indexes[e[1]], "entrance", entrance_dest_groups], [warp_array_indexes[e[1]], warp_array_indexes[e[0]], "exit", exit_dest_groups]]:
            modify_warp(d[0], d[1], d[2], d[3])

def set_entrance_warps(parsed_sym: sym, rom: RomData, patch_data):
    for p, v in patch_data["entrances"].items():
        dummy_vals = []
        i = 0
        for e in v: # If theres no logic for some warps, then change them every patch instead of rando gen to make up for rando gen logic issues afterward. NOTE: This means that those warps don't rely on logic, maing you have to patch your game every single time to get good RNG.
            if "dummy" in e[0]:
                dummy_vals.append(e[0] + str(i))
                i += 1
        if len(dummy_vals) > 0:
            og_dummy_vals = dummy_vals.copy()
            random.shuffle(dummy_vals)
            for e in v:
                if "dummy" in e[0]:
                    e[0] = og_dummy_vals[0]
                    e[1] = dummy_vals[0]
                    og_dummy_vals.remove(e[0])
                    dummy_vals.remove(e[1])
        edit_room(parsed_sym, rom, 0x0308, 0x1c, 0xa0)
        print(v)
        set_warps(parsed_sym, rom, v, p)

# Format for editing rooms:
# room is the exact room number you want to edit.
# the pos parameter is the XY position in hex you want the tile to be placed in.       
def edit_room(parsed_sym: sym, rom: RomData, room, pos, new_value):
    nLen = len(hex_str(room)[1:])
    zeros = ""
    for _ in range(nLen - (nLen - 1)):
        zeros += "0"
    addr_start = parsed_sym.find("label", f"room{zeros}{hex_str(room)}")
    if addr_start is None:
        raise ValueError(f"Room {hex_str(room)} does not exist")
    bank, addr = addr_start.__str__().split(":")
    addr_end = parsed_sym.find_addr_end(bank, addr).address_in_rom()
    if pos >= addr_end:
        raise ValueError(f"Position of tile in room {hex_str(room)} is not valid.")
    rom.write_byte(addr_start.address_in_rom() + (pos + 1), new_value)

def set_file_select_text(assembler: Z80Assembler, slot_name: str):
    def char_to_tile(c: str) -> int:
        if '0' <= c <= '9':
            return ord(c) - 0x20
        if 'A' <= c <= 'Z':
            return ord(c) + 0xa1
        if c == '+':
            return 0xfd
        if c == '-':
            return 0xfe
        if c == '.':
            return 0xff
        else:
            return 0xfc  # All other chars are blank spaces

    row_1 = [char_to_tile(c) for c in f"ARCHIP. {VERSION}".center(16, " ")]
    row_2 = [char_to_tile(c) for c in slot_name.replace("-", " ").upper().center(16, " ")]

    text_tiles = [0x74, 0x31]
    text_tiles.extend(row_1)
    text_tiles.extend([0x41, 0x40])
    text_tiles.extend([0x02] * 12)  # Offscreen tiles

    text_tiles.extend([0x40, 0x41])
    text_tiles.extend(row_2)
    text_tiles.extend([0x51, 0x50])
    text_tiles.extend([0x02] * 12)  # Offscreen tiles

    assembler.add_floating_chunk("dma_FileSelectStringTiles", text_tiles)

    
def set_heart_beep_interval_from_settings(rom: RomData):
    heart_beep_interval = get_settings()["tloz_kinomi_options"]["heart_beep_interval"]
    if heart_beep_interval == "half":
        rom.write_byte(0x914B, 0x3f * 2)
    elif heart_beep_interval == "quarter":
        rom.write_byte(0x914B, 0x3f * 4)
    elif heart_beep_interval == "disabled":
        rom.write_bytes(0x914B, [0x00, 0xc9])  # Put a return to avoid beeping entirely

def set_character_sprite_from_settings(parsed_sym, rom: RomData):
    sprite = get_settings()["tloz_kinomi_options"]["character_sprite"]
    sprite_dir = Path(Utils.local_path(os.path.join('data', 'sprites', 'oos_ooa')))
    if sprite == "random":
        sprite_filenames = [f for f in os.listdir(sprite_dir) if sprite_dir.joinpath(f).is_file() and f.endswith(".bin")]
        sprite = sprite_filenames[random.randint(0, len(sprite_filenames) - 1)]
    elif not sprite.endswith(".bin"):
        sprite += ".bin"
    if sprite != "link.bin":
        sprite_path = sprite_dir.joinpath(sprite)
        if not (sprite_path.exists() and sprite_path.is_file()):
            raise ValueError(f"Path '{sprite_path}' doesn't exist")
        sprite_bytes = list(Path(sprite_path).read_bytes())
        rom.write_bytes(0x68000, sprite_bytes)

    palette = get_settings()["tloz_kinomi_options"]["character_palette"]
    if palette == "random":
        palette = random.choice(get_available_random_colors_from_sprite_name(sprite))

    if palette == "green":
        return  # Nothing to change
    if palette not in PALETTE_BYTES:
        raise ValueError(f"Palette color '{palette}' doesn't exist (must be 'green', 'blue', 'red' or 'orange')")
    palette_byte = PALETTE_BYTES[palette]

    # Link palette restored after Medusa Head / Ganon stun attacks
    rom.write_byte(0x15271, 0x08 | palette_byte)


    # Link in file select (still and moving)
    fileSelectDrawLink = [parsed_sym.find("label", f"fileSelectDrawLink@sprites{i}").address_in_rom() + 4 for i in range(3)]
    for i in range(2):
        rom.write_byte(fileSelectDrawLink[i], palette_byte)
        rom.write_byte(fileSelectDrawLink[i] + 4, palette_byte)
    rom.write_byte(fileSelectDrawLink[2], 0x20 | palette_byte)
    rom.write_byte(fileSelectDrawLink[2] + 4, 0x20 | palette_byte)

def apply_misc_option(rom: RomData, patch_data):
    if patch_data["options"]["master_keys"] != GiftsOfKinomiMasterKeys.option_disabled:
        # Remove small key consumption on keydoor opened
        rom.write_byte(0x18366, 0x00)
        # Change obtention text
        rom.write_bytes(0x78247, [0x4d, 0x61, 0x73, 0x74, 0x65, 0x72, 0x20, 0x4b, 0x65, 0x79, 0x09, 0x01, 0x21, 0x00]) # I really wish that the dictionnay of ages would be more useful...
    if patch_data["options"]["master_keys"] == GiftsOfKinomiMasterKeys.option_all_dungeon_keys:
        # Remove boss key consumption on boss keydoor opened (boss door behave like normal locked door)
        rom.write_word(0x1835e, 0x0000)