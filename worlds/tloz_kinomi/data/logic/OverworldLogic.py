from .LogicPredicates import *


def make_overworld_logic(player: int):
    return [
        # KINOMI TOWN
        #######################################
        ["Menu", "kinomi town", False, None],
        ["kinomi town", "maple trade", False, lambda state: all([
            kinomi_can_kill_normal_enemy(state, player, True),
            state.has("Ghastly Doll", player)
        ])],
        ["kinomi town", "summer villa entrance", False, None],
        ["kinomi town", "ghost's house", False, lambda state: kinomi_can_use_ember_seeds(state, player, True)],
        ["kinomi town", "kinomi shop", False, None],
        ["kinomi town", "hidden shop", False, lambda state: kinomi_can_use_ember_seeds(state, player, False)], # You can just use ember seeds to burn bushes and a tree.
        ["kinomi town", "old man's library", False, lambda state: all([
            state.has("Sparring Book", player),
            state.has("Broken Sword", player)
        ])],
        ["kinomi town", "library employee", False, lambda state: kinomi_can_break_pot(state, player)],
        ["kinomi town", "link's house heartpiece", False, lambda state: kinomi_can_break_pot(state, player)],

        # FOREVER FALLS
        #######################################
        ["kinomi town", "forever falls old man", False, lambda state: kinomi_can_break_bush(state, player)],
        ["kinomi town", "forever falls enemy kill", False, lambda state: kinomi_can_kill_normal_enemy(state, player)],
        ["kinomi town", "forever falls cave", False, lambda state: kinomi_can_kill_normal_enemy(state, player)],
        ["kinomi town", "spirit's grotto entrance", False, lambda state: state.has("Falls Key", player)],
        ["kinomi town", "lost labyrinth forever falls entrance", False, lambda state: all([
            kinomi_can_use_ember_seeds(state, player, False),
            kinomi_has_gifts_for_zelda_kidnapped_cutscene(state, player)
        ])],

        # DAICHI PLAIN
        ####################################### 
        ["kinomi town", "weird guy's house", False, None],
        ["kinomi town", "daichi plain old man", False, lambda state: kinomi_can_use_ember_seeds(state, player, False)],
        ["daichi plain old man", "daichi plain old man's rupee", False, None],
        ["kinomi town", "daichi plain gravesite heartpiece", False, lambda state: any([
            state.has("Rod of Seasons", player), # NOTE: The Rod Of Seasons comes with all seasons by default, so there's no need to consider certain seasons in logic.
            kinomi_can_jump_pit(state, player)
        ])],
        ["kinomi town", "daichi plain", False, lambda state: state.has("Rod of Seasons", player)], # NOTE: The Rod Of Seasons comes with all seasons by default, so there's no need to consider certain seasons in logic.
        ["daichi plain", "daichi plain summer old man", False, lambda state: kinomi_has_bracelet(state, player)],
        ["daichi plain", "daichi plain gift under mushroom", False, lambda state: kinomi_can_break_mushroom(state, player)],
        ["daichi plain", "winter cave crystal chest", False, lambda state: kinomi_can_break_crystal(state, player)],
        ["daichi plain", "winter cave stone reward", False, lambda state: kinomi_can_kill_normal_enemy(state, player, True)],
        ["daichi plain", "daichi plain gravesite basement", False, lambda state: any([
            kinomi_can_jump_pit(state, player),
            kinomi_has_cane(state, player) # Remember, the cane can now fix holes.
        ])],
        ["daichi plain", "daichi plain underwater heartpiece", False, lambda state: kinomi_can_swim(state, player)],
        ["daichi plain underwater heartpiece", "fall stone reward", False, None],
        ["daichi plain summer old man", "daichi plain summer old man's rupee", False, None],
        ["daichi plain", "daichi plain chest", False, lambda state: kinomi_has_bracelet(state, player)],
        ["kinomi town", "four corners cave entrance", False, lambda state: kinomi_has_bombs(state, player)],

        # LAKE OF MEMORIES
        #######################################
        ["daichi plain", "lake of memories", False, lambda state: kinomi_can_break_mushroom(state, player)],
        ["lake of memories", "summer stone check", False, lambda state: all([
            kinomi_has_bombs(state, player),
            kinomi_can_break_crystal(state, player),
            kinomi_can_swim(state, player)
        ])],
        ["lake of memories", "lake of memories old man", False, lambda state: kinomi_can_use_ember_seeds(state, player, False)],
        ["lake of memories old man", "lake of memories old man's chest", False, None],
        ["lake of memories", "lake of memories underwater cave", False, None],
        ["lake of memories", "lake of memories heartpiece", False, None],
        ["lake of memories", "lake of memories scrapped chest", False, None],

        # HEDGE MAZE
        #######################################
        ["lake of memories", "hedge maze", False, lambda state: kinomi_can_kill_armos(state, player)],
        ["hedge maze", "hedge maze old man 1", False, None],
        ["hedge maze", "hedge maze old man 2", False, None],
        ["hedge maze", "hedge maze old man 2's rupee", False, lambda state: kinomi_can_break_pot(state, player)],
        ["hedge maze", "hedge maze stone", False, None],
        ["hedge maze", "hedge maze old man 1's chest", False, None],

        # DEEPER WOODS
        #######################################
        ["hedge maze", "deeper woods old man 1", False, lambda state: kinomi_can_use_ember_seeds(state, player, False)],
        ["deeper woods old man 1", "deeper woods old man 1's heartpiece", False, lambda state: kinomi_can_break_pot(state, player)],
        ["hedge maze", "deeper woods route 2", False, lambda state: any([
            # on basic logic, a player should keep a shield on them so that they can talk to the deku scrub in jiku clifs to get season directions. Those on medium logic don't have to do that.
            all([
                kinomi_has_shield(state, player),
                kinomi_has_bracelet(state, player)
            ]),
            kinomi_option_medium_logic(state, player)
        ])],
        ["hedge maze", "deeper woods route 1", False, lambda state: any([
            # on basic logic, a player should keep a shield on them so that they can talk to the deku scrub in jiku clifs to get season directions. Those on medium logic don't have to do that.
            kinomi_has_shield(state, player),
            kinomi_option_medium_logic(state, player)
        ])],
        ["hedge maze", "seasons shrine entrance", False, lambda state: all([ 
            # For some reason the game expects you to have all the stones to get to the seasons shrine. Tried getting there once on three stones and failed despite guessing correctly.
            state.has("Summer Stone", player),
            state.has("Winter Stone", player),
            state.has("Spring Stone", player),
            state.has("Autumm Stone", player)
        ])],
        ["deeper woods route 2", "deeper woods old man 2", False, lambda state: kinomi_can_use_ember_seeds(state, player, False)],
        ["deeper woods route 1", "deeper woods heartpiece under tree", False, lambda state: kinomi_can_use_ember_seeds(state, player, False)],
        ["deeper woods old man 2", "deeper woods old man 2's rupee", False, lambda state: kinomi_can_break_pot(state, player)],
        ["deeper woods old man 2", "deeper woods underground heartpiece", False, lambda state: kinomi_can_swim(state, player)],
        ["deeper woods underground heartpiece", "familar swamp gift", False, lambda state: all([
            kinomi_can_jump_pit(state, player),
            kinomi_has_bracelet(state, player),
            kinomi_can_break_bush(state, player),
            kinomi_can_kill_normal_enemy(state, player)
        ])],
        ["familar swamp gift", "subrosia dance", False, lambda state: all([
            kinomi_has_bombs(state, player),
            any([
                kinomi_has_cane(state, player),
                kinomi_can_jump_4_wide_pit(state, player)
            ])
        ])],
        ["deeper woods route 2", "deeper woods swordsman trade", False, lambda state: state.has("Broken Sword", player)],
        ["hedge maze", "deeper woods chest", False, None],

        # JIKU CLIFS
        #######################################
        ["kinomi town", "jiku clifs", False, lambda state: kinomi_has_bracelet(state, player)],
        ["jiku clifs", "jiku clifs heartpiece hidding in hole", False, lambda state: kinomi_has_cane(state, player)],
        ["jiku clifs", "heartpiece under rock", False, None], # You can lift up the bushes with a bracelet.
        ["jiku clifs", "old lady trade", False, lambda state: state.has("Life Potion", player)],
        ["jiku clifs", "jiku clifs shop", False, lambda state: all([
            any([
                kinomi_can_jump_pit(state, player),
                kinomi_has_bracelet(state, player) # Already in jiku clifs entry logic but defined anyway to not incorrect the logic.
            ]),
            kinomi_can_swim(state, player)
        ])],
        ["jiku clifs shop", "jiku clifs past", False, lambda state: kinomi_can_open_portal(state, player)],
        ["jiku clifs past", "jiku clifs past underwater heartpiece", False, None],
        ["lost labyrinth past entrance 3", "jiku clifs past fill holes", False, lambda state: kinomi_has_cane(state, player)],
        ["jiku clifs past fill holes", "jiku clifs past fill hole next to entrance", False, None],
        ["jiku clifs", "chest inside cave outside lost labyrinth present entrance", False, lambda state: kinomi_can_jump_pit(state, player)],
        ["jiku clifs", "heartpiece inside cave outside lost labyrinth present entrance", False, lambda state: any([
            kinomi_option_medium_logic(state, player), # hopefully you know that as long as you get a percise landing in the right place then you'll get the heartpiece. Tried it once and it worked.
            kinomi_can_jump_pit(state, player),
        ])],
        ["jiku clifs", "lost labyrinth entrance", False, lambda state: state.has("Old Labyrinth Key", player)],
        ["d2 past small key drop 2", "jiku clifs past springwater region", False, lambda state: all([
            kinomi_has_small_keys(state, player, 2, 1),
            any([
                kinomi_can_jump_pit(state, player),
                kinomi_has_cane(state, player)
            ])
        ])],
        ["jiku clifs past springwater region", "bomb fairy", False, lambda state: state.has("Bombs (10)", player)],
        ["jiku clifs past springwater region", "goron dance", False, None],
        ["jiku clifs past springwater region", "jiku clifs past heartpiece drop", False, lambda state: kinomi_can_kill_normal_enemy(state, player)],
        ["tokay desert", "jiku clifs past heartpiece", False, lambda state: kinomi_has_glove(state, player)],

        # LOST LABYRINTH PAST ENTRANCES
        #######################################
        ["jiku clifs past", "lost labyrinth past entrance 1", False, None],
        ["jiku clifs past", "lost labyrinth past entrance 2", False, lambda state: kinomi_can_use_ember_seeds(state, player, False)],
        ["jiku clifs past", "lost labyrinth past entrance 3", False, lambda state: any([
            kinomi_has_cane(state, player),
            kinomi_can_jump_pit(state, player)
        ])],
        ["lost labyrinth past entrance 1", "lost labyrinth past entrance 3", False, lambda state: all([
            kinomi_can_kill_normal_enemy(state, player, True),
            kinomi_can_use_ember_seeds(state, player, False)
        ])],
        ["lost labyrinth past entrance 3", "lost labyrinth past entrance 4", False, lambda state: kinomi_has_bombs(state, player)],
        ["lost labyrinth past entrance 4", "lost labyrinth present heartpiece", False, None],
        ["lost labyrinth past entrance 3", "zora's island", False, None],
        ["lost labyrinth past entrance 3", "syrup's shop", False, lambda state: state.has("Witch's Key", player)],
        ["d2 past bomb chest", "lost labyrinth past entrance 5", False, lambda state: kinomi_has_bombs(state, player)],
        ["d2 past small key drop 2", "syrup's shop", False, lambda state: kinomi_has_bombs(state, player)], # You can enter syrup's shop from the main entrance as well. Just don't try exiting the shop without using the Witch's key though.
        ["d2 past color tile puzzle", "lost labyrinth past entrance 5", True, lambda state: all([ # It's possible to enter the main past labyrinth from the stairs in syrup's shop.
            kinomi_has_cane(state, player),
            kinomi_has_bombs(state, player),
            kinomi_has_small_keys(state, player, 2, 1)
        ])],

        # TOKAY DESERT
        #######################################
        ["jiku clifs past springwater region", "tokay desert", False, lambda state: all([
            state.has("_has_access_to_syrups_shop", player),
            state.has("Mushroom", player)
        ])],
        ["tokay desert", "tokay desert outdoor chests", False, lambda state: kinomi_has_glove(state, player)],
        ["tokay desert outdoor chests", "tokay desert chest", False, None],
        ["tokay desert outdoor chests", "tokay desert second chest", False, lambda state: any([
            kinomi_can_jump_4_wide_pit(state, player),
            kinomi_has_cane(state, player)
        ])],
        ["tokay desert outdoor chests", "tokay desert third chest", False, lambda state: any([
            kinomi_can_jump_pit(state, player),
            kinomi_has_cane(state, player)
        ])],
        ["tokay desert outdoor chests", "tokay desert fourth chest", False, None],
        ["tokay desert", "chest inside first tokay house", False, None],
        ["d5 chest near slate slots", "chest in bottom screen of graveyard", False, None],
    ]
