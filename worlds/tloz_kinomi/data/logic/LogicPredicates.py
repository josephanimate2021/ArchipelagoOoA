from BaseClasses import CollectionState
from Options import Accessibility
from ..Constants import DUNGEON_NAMES, GIFTS


# Items predicates ############################################################

def kinomi_has_sword(state: CollectionState, player: int, accept_biggoron: bool = True):
    return any([
        state.has("Sword", player),
        accept_biggoron and state.has("Biggoron's Sword", player)
    ])


def kinomi_has_shield(state: CollectionState, player: int):
    return state.has("Shield", player)


def kinomi_has_satchel(state: CollectionState, player: int, level: int = 1):
    return state.has("Seed Satchel", player, level)

def kinomi_has_slingshot(state: CollectionState, player: int, level: int = 1):
    return state.has("Progressive Slingshot", player, level)

def kinomi_has_boomerang(state: CollectionState, player: int):
    return state.has("Boomerang", player)


def kinomi_has_cane(state: CollectionState, player: int):
    return state.has("Cane of Somaria", player)

def kinomi_has_bracelet(state: CollectionState, player: int):
    return state.has("Progressive Bracelet", player)

def kinomi_has_glove(state: CollectionState, player: int):
    return state.has("Progressive Bracelet", player, 2)

def kinomi_has_shovel(state: CollectionState, player: int):
    return state.has("Shovel", player)

def kinomi_has_flippers(state: CollectionState, player: int):
    return state.has("Zora's Flippers", player)


def kinomi_has_ember_seeds(state: CollectionState, player: int):
    return any([
        True
        #state.has("Ember Seeds", player),
        #state.multiworld.worlds[player].options.default_seed == "ember",
        #(state.has("_wild_ember_seeds", player) and kinomi_option_medium_logic(state, player))
    ])


def kinomi_has_scent_seeds(state: CollectionState, player: int):
    return True#state.has("Scent Seeds", player)


def kinomi_has_pegasus_seeds(state: CollectionState, player: int):
    return True#state.has("Pegasus Seeds", player)


def kinomi_has_mystery_seeds(state: CollectionState, player: int):
    return any([
        True
        #state.has("Mystery Seeds", player),
        #   state.multiworld.worlds[player].options.default_seed == "mystery",
        #(state.has("_wild_mystery_seeds", player) and kinomi_option_medium_logic(state, player))
    ])


def kinomi_has_gale_seeds(state: CollectionState, player: int):
    return True#state.has("Gale Seeds", player)# or state.multiworld.worlds[player].options.default_seed == "gale"


def kinomi_has_small_keys(state: CollectionState, player: int, dungeon_id: int, amount: int = 1):
    return (state.has(f"Small Key ({DUNGEON_NAMES[dungeon_id]})", player, amount)
            or state.has(f"Master Key ({DUNGEON_NAMES[dungeon_id]})", player))

def kinomi_has_boss_key(state: CollectionState, player: int, dungeon_id: int):
    return any([
        state.has(f"Boss Key ({DUNGEON_NAMES[dungeon_id]})", player),
        all([
            state.multiworld.worlds[player].options.master_keys == "all_dungeon_keys",
            state.has(f"Master Key ({DUNGEON_NAMES[dungeon_id]})", player)
        ])
    ])


# Options and generation predicates ###########################################

def kinomi_option_medium_logic(state: CollectionState, player: int):
    return state.multiworld.worlds[player].options.logic_difficulty in ["medium", "hard"]


def kinomi_option_hard_logic(state: CollectionState, player: int):
    return state.multiworld.worlds[player].options.logic_difficulty == "hard"


def kinomi_has_gifts(state: CollectionState, player: int, target_count: int):
    gift_count = [state.has(gift, player) for gift in GIFTS].count(True)
    return gift_count >= target_count


def kinomi_has_gifts_for_zelda_kidnapped_cutscene(state: CollectionState, player: int):
    return kinomi_has_gifts(state, player, state.multiworld.worlds[player].options.required_gifts.value)

def kinomi_has_slates(state: CollectionState, player: int, target_count):
    return state.has("Slate", player, target_count)
    
def kinomi_has_enough_slates(state: CollectionState, player: int):
    return kinomi_has_slates(state, player, state.multiworld.worlds[player].options.required_slates.value)


# Various item predicates ###########################################

def kinomi_has_rupees(state: CollectionState, player: int, amount: int):
    # Rupee checks being quite approximative, being able to farm is a
    # must-have to prevent any stupid lock
    if not kinomi_can_farm_rupees(state, player):
        return False

    rupees = state.count("Rupees (1)", player)
    rupees += state.count("Rupees (5)", player) * 5
    rupees += state.count("Rupees (10)", player) * 10
    rupees += state.count("Rupees (20)", player) * 20
    rupees += state.count("Rupees (50)", player) * 50
    rupees += state.count("Rupees (100)", player) * 100
    rupees += state.count("Rupees (200)", player) * 200

    # Secret rooms inside D2 and D6 containing loads of rupees, but only in medium logic
    if kinomi_option_medium_logic(state, player):
        if state.has("_reached_d2_rupee_room", player):
            rupees += 150
        if state.has("_reached_d6_rupee_room", player):
            rupees += 90

    ## Old men giving and taking rupees
    #world = state.multiworld.worlds[player]
    #for region_name, value in world.old_man_rupee_values.items():
    #    event_name = "rupees from " + region_name
    #    if state.has(event_name, player):
    #        rupees += value

    return rupees >= amount


def kinomi_can_farm_rupees(state: CollectionState, player: int):
    # Having Ember Seeds and a weapon or a shovel is enough to guarantee that we can reach
    # a significant amount of rupees
    return kinomi_has_sword(state, player) or kinomi_has_shovel(state, player)


def kinomi_can_press_nonhold_presure_plate_without_blocks(state: CollectionState, player: int, pots_around: bool):
    return any([
        all([
            pots_around,
            any([
                kinomi_has_bracelet(state, player),
                all([
                    kinomi_can_break_pot(state, player),
                    kinomi_has_cane(state, player)
                ])
            ])
        ]),
        kinomi_has_cane(state, player)
    ])



def kinomi_can_trigger_switch(state: CollectionState, player: int):
    return any([
        kinomi_has_boomerang(state, player),
        kinomi_has_bombs(state, player),
        kinomi_has_slingshot(state, player),
        all([
            kinomi_has_satchel(state, player),
            any([
                kinomi_has_ember_seeds(state, player),
                kinomi_has_scent_seeds(state, player),
                kinomi_has_mystery_seeds(state, player)
            ])
        ]),
        kinomi_has_sword(state, player),
        kinomi_can_punch(state, player),
    ])

def kinomi_can_trigger_far_switch(state: CollectionState, player: int, sword_allowed: bool = True, bombs_allowed: bool = True, slingshot_allowed: bool = True):
    return any([
        kinomi_has_boomerang(state, player),
        all([
            bombs_allowed,
            kinomi_has_bombs(state, player)
        ]),
        all([
            slingshot_allowed,
            kinomi_has_slingshot(state, player)
        ]),
        all([
            sword_allowed,
            kinomi_option_medium_logic(state, player),
            kinomi_has_sword(state, player, False),
            state.has("Energy Ring", player)
        ])
        # TODO: Regular beams?
    ])


def kinomi_has_bombs(state: CollectionState, player: int, amount: int = 1):
    return state.has("Bombs (10)", player, amount)

def kinomi_can_open_portal(state: CollectionState, player: int):
    return state.has("Harp", player)

# Jump-related predicates ###########################################


def kinomi_can_jump_pit(state: CollectionState, player: int):
    return state.has("Roc's Cape", player),

def kinomi_can_jump_4_wide_pit(state: CollectionState, player: int):
    return all([
        kinomi_can_jump_pit(state, player),
        any([
            all([
                kinomi_option_hard_logic(state, player),
                kinomi_has_bombs(state, player)
            ]),
            kinomi_can_use_pegasus_seeds(state, player)
        ])
    ])

def kinomi_can_jump_5_wide_pit(state: CollectionState, player: int):
    return all([
        kinomi_can_jump_pit(state, player),
        all([
            kinomi_option_hard_logic(state, player),
            kinomi_has_bombs(state, player),
            kinomi_can_use_pegasus_seeds(state, player)
        ])
    ])

# Seed-related predicates ###########################################

def kinomi_can_use_seeds(state: CollectionState, player: int):
    return kinomi_has_satchel(state, player) or kinomi_has_slingshot(state, player)

def kinomi_has_seed_kind_count(state: CollectionState, player: int, count: int):
    seedCount = 0
    seedCount += 1 if kinomi_has_ember_seeds(state, player) else 0
    seedCount += 1 if kinomi_has_mystery_seeds(state, player) else 0
    seedCount += 1 if kinomi_has_scent_seeds(state, player) else 0
    seedCount += 1 if kinomi_has_pegasus_seeds(state, player) else 0
    seedCount += 1 if kinomi_has_gale_seeds(state, player) else 0
    return seedCount >= count

def kinomi_can_use_ember_seeds(state: CollectionState, player: int, accept_mystery_seeds: bool):
    return all([
        kinomi_can_use_seeds(state, player),
        any([
            kinomi_has_ember_seeds(state, player),
            all([
                # Medium logic expects the player to know they can use mystery seeds
                # to randomly get the ember effect in some cases
                accept_mystery_seeds,
                kinomi_option_medium_logic(state, player),
                kinomi_has_mystery_seeds(state, player),
            ])
        ])
    ])


def kinomi_can_use_scent_seeds_offensively(state: CollectionState, player: int):
    return all([
        any([
            kinomi_has_slingshot(state, player),
            all([
                kinomi_option_hard_logic(state, player),
                kinomi_has_satchel(state, player)
            ])
        ]),
        kinomi_has_scent_seeds(state, player)
    ])

def kinomi_can_use_scent_seeds_for_smell(state: CollectionState, player: int):
    return all([
        kinomi_has_satchel(state, player),
        kinomi_has_scent_seeds(state, player)
    ])

def kinomi_can_use_pegasus_seeds(state: CollectionState, player: int):
    return all([
        # Unlike other seeds, pegasus only have an interesting effect with the satchel
        kinomi_has_satchel(state, player),
        kinomi_has_pegasus_seeds(state, player)
    ])

def kinomi_can_use_pegasus_seeds_for_stun(state: CollectionState, player: int):
    return kinomi_has_pegasus_seeds(state, player) and kinomi_has_slingshot(state, player)

def kinomi_can_warp_using_gale_seeds(state: CollectionState, player: int):
    return all([
        kinomi_has_satchel(state, player),
        kinomi_has_gale_seeds(state, player)
    ])


def kinomi_can_use_gale_seeds_offensively(state: CollectionState, player: int, ranged: bool = False):
    # If we don't have gale seeds or aren't at least in medium logic, don't even try
    if not kinomi_has_gale_seeds(state, player) or not kinomi_option_medium_logic(state, player):
        return False

    return any([
        kinomi_has_slingshot(state, player),
        all([
            not ranged,
            kinomi_has_satchel(state, player),
            any([
                kinomi_option_hard_logic(state, player),
                kinomi_can_jump_pit(state, player)
            ]),
        ])
    ])


def kinomi_can_use_mystery_seeds(state: CollectionState, player: int):
    return all([
        kinomi_can_use_seeds(state, player),
        kinomi_has_mystery_seeds(state, player)
    ])


# Break / kill predicates ###########################################

def kinomi_can_break_bush(state: CollectionState, player: int):
    return any([
        kinomi_can_break_flower(state, player),
        kinomi_has_bracelet(state, player),
    ])

def kinomi_can_break_mushroom(state: CollectionState, player: int):
    return any([
        kinomi_has_bracelet(state, player),
        all([
            kinomi_option_medium_logic(state, player),
            kinomi_has_boomerang(state, player)
        ])
    ])

def kinomi_can_break_flower(state: CollectionState, player: int):
    return any([
        kinomi_has_sword(state, player),
        all([
            # Consumables need at least medium logic, since they need a good knowledge of the game
            # not to be frustrating
            kinomi_option_medium_logic(state, player),
            any([
                kinomi_has_bombs(state, player, 2),
                kinomi_can_use_ember_seeds(state, player, False),
                (kinomi_has_slingshot(state, player) and kinomi_has_gale_seeds(state, player)),
            ])
        ]),
    ])


def kinomi_can_harvest_regrowing_bush(state: CollectionState, player: int, allow_bombs: bool = True):
    return any([
        kinomi_has_sword(state, player),
        (allow_bombs and kinomi_has_bombs(state, player))
    ])


def kinomi_can_break_pot(state: CollectionState, player: int):
    return any([
        kinomi_has_bracelet(state, player),
        all([
            kinomi_option_medium_logic(state, player), # When you get the L-2 sword from the item drop, you can break pots. For basic logic, i only added the bracelet to basic logic to prevent softlocks.
            kinomi_has_sword(state, player, False)
        ]),
        kinomi_has_sword(state, player)
    ])


def kinomi_can_break_flowers(state: CollectionState, player: int):
    return any([
        kinomi_has_sword(state, player),
        all([
            # Consumables need at least medium logic, since they need a good knowledge of the game
            # not to be frustrating
            kinomi_option_medium_logic(state, player),
            any([
                kinomi_has_bombs(state, player, 2),
                kinomi_can_use_ember_seeds(state, player, False),
                (kinomi_has_slingshot(state, player) and kinomi_has_gale_seeds(state, player)),
            ])
        ]),
    ])


def kinomi_can_break_crystal(state: CollectionState, player: int):
    return any([
        kinomi_has_sword(state, player),
        kinomi_has_bombs(state, player),
        kinomi_has_bracelet(state, player),
        all([
            kinomi_option_medium_logic(state, player),
            state.has("Expert's Ring", player)
        ])
    ])

def kinomi_can_break_d4_crystal(state: CollectionState, player: int):
    return any([
        kinomi_has_sword(state, player),
        kinomi_has_boomerang(state, player),
        state.has("Rod of Seasons", player)
    ])


def kinomi_can_break_sign(state: CollectionState, player: int):
    return any([
        kinomi_has_sword(state, player), # As long as you get the L-2 sword item drop.
        state.has("Biggoron's Sword", player),
        kinomi_has_bracelet(state, player),
        kinomi_can_use_ember_seeds(state, player, False),
    ])


def kinomi_can_harvest_tree(state: CollectionState, player: int):
    return all([
        kinomi_can_use_seeds(state, player),
        any([
            kinomi_has_sword(state, player),
            kinomi_can_punch(state, player)
        ])
    ])


def kinomi_can_push_enemy(state: CollectionState, player: int):
    return any([
        #kinomi_has_rod(state, player),
        kinomi_has_shield(state, player)
    ])


def kinomi_can_kill_normal_enemy(state: CollectionState, player: int, pit_available: bool = False):
    # If a pit is avaiable nearby, it can be used to put the enemies inside using
    # items that are usually non-lethal
    if pit_available and kinomi_can_push_enemy(state, player):
        return True

    return any([
        kinomi_has_sword(state, player),
        kinomi_can_kill_normal_using_satchel(state, player),
        (kinomi_option_medium_logic(state, player) and kinomi_has_bombs(state, player, 4)),
        (kinomi_option_medium_logic(state, player) and kinomi_has_cane(state, player)),
        kinomi_can_punch(state, player),
    ])

def kinomi_can_kill_moldorm(state:CollectionState, player:int, pit_available:bool=False):
    if pit_available and kinomi_can_push_enemy(state, player):
        return True

    return any([
        kinomi_has_sword(state, player),
        kinomi_can_use_scent_seeds_offensively(state, player),
        # Not including mystery seed, because even in hard logic this is just pure torture
        (kinomi_option_medium_logic(state, player) and kinomi_has_bombs(state, player, 4)),
        (kinomi_option_medium_logic(state, player) and kinomi_has_cane(state, player)),
        kinomi_can_punch(state, player)
    ])

def kinomi_can_kill_wizzrobes(state:CollectionState, player:int, pit_available:bool=False):
    if pit_available and kinomi_can_push_enemy(state, player):
        return True

    return any([
        kinomi_has_sword(state, player),
        kinomi_can_kill_normal_using_satchel(state, player),
        kinomi_can_kill_normal_using_seedshooter(state, player),
        (kinomi_option_medium_logic(state, player) and kinomi_has_bombs(state, player, 4)),
        kinomi_can_punch(state, player),
    ])

def kinomi_generic_boss_and_miniboss_kill(state:CollectionState, player:int):
    return any([
        kinomi_has_sword(state, player),
        kinomi_can_use_scent_seeds_offensively(state, player),
        # TODO : Check bombs damage on bosses
        #(kinomi_option_medium_logic(state, player) and kinomi_has_bombs(state, player, 4)),
        kinomi_can_punch(state, player)
    ])

def kinomi_can_kill_normal_using_satchel(state: CollectionState, player: int):
    # Expect a 50+ seed satchel to ensure we can chain dungeon rooms to some extent if that's our only kill option
    if not kinomi_has_satchel(state, player, 2):
        return False

    return any([
        # Casual logic => only ember
        kinomi_has_ember_seeds(state, player),
        all([
            # Medium logic => allow scent or gale+feather
            kinomi_option_medium_logic(state, player),
            any([
                kinomi_has_scent_seeds(state, player),
                kinomi_has_mystery_seeds(state, player),
                all([
                    kinomi_has_gale_seeds(state, player),
                    kinomi_can_jump_pit(state, player)
                ])
            ])
        ]),
        all([
            # Hard logic => allow gale without feather
            kinomi_option_hard_logic(state, player),
            kinomi_has_gale_seeds(state, player)
        ])
    ])


def kinomi_can_kill_normal_using_seedshooter(state: CollectionState, player: int):
    # Expect a 50+ seed satchel to ensure we can chain dungeon rooms to some extent if that's our only kill option
    if not kinomi_has_satchel(state, player, 2):
        return False

    return all([
        kinomi_has_slingshot(state, player),
        any([
            kinomi_has_ember_seeds(state, player),
            kinomi_has_scent_seeds(state, player),
            all([
                kinomi_option_medium_logic(state, player),
                any([
                    kinomi_has_mystery_seeds(state, player),
                    kinomi_has_gale_seeds(state, player),
                ])
            ])
        ])
    ])


def kinomi_can_kill_armored_enemy(state: CollectionState, player: int):
    return any([
        kinomi_has_sword(state, player),
        all([
            kinomi_has_satchel(state, player, 2),  # Expect a 50+ seeds satchel to be able to chain rooms in dungeons
            kinomi_has_scent_seeds(state, player),
            any([
                kinomi_has_slingshot(state, player),
                kinomi_option_medium_logic(state, player)
            ])
        ]),
        (kinomi_option_medium_logic(state, player) and kinomi_has_cane(state, player)),
        kinomi_can_punch(state, player)
    ])
    
def kinomi_can_kill_pols_voice(state: CollectionState, player: int, ranged: bool = False):
    return any([
        kinomi_can_open_portal(state, player),
        kinomi_has_bombs(state, player),
        kinomi_can_use_gale_seeds_offensively(state, player, ranged)
    ])

def kinomi_can_kill_armos(state: CollectionState, player: int, ranged: bool = False):
    return any([
        kinomi_has_bombs(state, player),
        kinomi_can_use_scent_seeds_offensively(state, player)
        # magic boomrang
    ])


def kinomi_can_punch(state: CollectionState, player: int):
    return all([
        kinomi_option_medium_logic(state, player),
        any([
            state.has("Fist Ring", player),
            state.has("Expert's Ring", player)
        ])
    ])


def kinomi_can_trigger_lever(state: CollectionState, player: int):
    return any([
        kinomi_can_trigger_lever_from_minecart(state, player),
        all([
            kinomi_option_medium_logic(state, player),
            kinomi_has_shovel(state, player)
        ])
    ])


def kinomi_can_trigger_lever_from_minecart(state: CollectionState, player: int):
    return any([
        kinomi_has_sword(state, player),
        kinomi_has_boomerang(state, player),

        # TODO: Test that to ensure our understanding is right
        kinomi_can_use_scent_seeds_offensively(state, player),
        kinomi_can_use_mystery_seeds(state, player),
        kinomi_has_slingshot(state, player)
    ])



def kinomi_can_flip_spiked_beetle(state: CollectionState, player: int):
    return any([
        kinomi_has_shield(state, player),
        all([
            kinomi_option_medium_logic(state, player),
            kinomi_has_shovel(state, player)
        ])
    ])


def kinomi_can_kill_spiked_beetle(state: CollectionState, player: int):
    return any([
        all([  # Regular flip + kill
            kinomi_can_flip_spiked_beetle(state, player),
            any([
                kinomi_has_sword(state, player),
                kinomi_can_kill_normal_using_satchel(state, player),
                kinomi_can_kill_normal_using_seedshooter(state, player)
            ])
        ]),
        # Instant kill using Gale Seeds
        kinomi_can_use_gale_seeds_offensively(state, player)
    ])

# Action predicates ###########################################

def kinomi_can_swim(state: CollectionState, player: int):
    return kinomi_has_flippers(state, player)

def kinomi_can_remove_rockslide(state: CollectionState, player: int, can_summon_companion: bool):
    return kinomi_has_bombs(state, player)

def kinomi_can_remove_dirt(state: CollectionState, player: int, can_summon_companion: bool):
    return kinomi_has_shovel(state, player)

def kinomi_can_toss_ring(state: CollectionState, player: int):
    return all([
        kinomi_option_medium_logic(state, player),
        kinomi_has_bracelet(state, player),
        state.has("Toss Ring", player)
    ])

# Self-locking items helper predicates ##########################################

def kinomi_self_locking_item(state: CollectionState, player: int, region_name: str, item_name: str):
    if state.multiworld.worlds[player].options.accessibility == Accessibility.alias_locations:
        return False

    region = state.multiworld.get_region(region_name, player)
    items_in_region = [location.item for location in region.locations if location.item is not None]
    for item in items_in_region:
        if item.name == item_name and item.player == player:
            return True
    return False


def kinomi_self_locking_small_key(state: CollectionState, player: int, region_name: str, dungeon: int):
    item_name = f"Small Key ({DUNGEON_NAMES[dungeon]})"
    return kinomi_self_locking_item(state, player, region_name, item_name)

