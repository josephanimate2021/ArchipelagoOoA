from .LogicPredicates import *


def make_summerVilla_logic(player: int):
    return [
        ["enter summer villa", "d0 map chest", False, None],
        ["enter summer villa", "d0 compass chest", False, None],
        ["enter summer villa", "d0 small key chest 1f", False, None],
        ["enter summer villa", "d0 heartpiece inside water", False, None],
        ["enter summer villa", "solder trade", False, lambda state: state.has("Wood Clock", player)],
        ["enter summer villa", "d0 small key chest b1f", False, lambda state: kinomi_can_kill_armos(state, player)],
        ["enter summer villa", "d0 small key chest 2f", False, None],
        ["enter summer villa", "d0 heartpiece drop", False, lambda state: kinomi_can_kill_spiked_beetle(state, player)],
        ["enter summer villa", "d0 boss key chest", False, lambda state: all([
            kinomi_can_kill_spiked_beetle(state, player),
            kinomi_has_small_keys(state, player, 0, 1)
        ])],
        ["enter summer villa", "d0 shield chest", False, lambda state: kinomi_has_small_keys(state, player, 0, 1)],
        ["enter summer villa", "d0 boss", False, lambda state: all([
            kinomi_has_shield(state, player),
            kinomi_has_boss_key(state, player, 0)
        ])],
        ["d0 boss", "d0 sword chest", False, None],
    ] 

def make_spiritGrotto_logic(player: int):
    return [
        # LEFT SIDE OF SPIRIT'S GROTTO
        ["enter spirit's grotto", "d1 left side", False, lambda state: kinomi_can_kill_normal_enemy(state, player)],
        ["d1 left side", "d1 pots chest", False, lambda state: kinomi_can_break_pot(state, player)],
        ["d1 left side", "d1 platform chest", False, None],
        ["d1 left side", "d1 small key drop", False, None],
        ["d1 left side", "d1 heartpiece", False, lambda state: kinomi_can_press_nonhold_presure_plate_without_blocks(state, player, True)],
        ["d1 left side", "d1 compass chest", False, lambda state: all([
            kinomi_has_small_keys(state, player, 1, 2), # 2 keys = prevent softlock (due to keyblock ahead that leads to reharvesting bushes).
            kinomi_has_bombs(state, player)
        ])],
        ["d1 compass chest", "d1 heartpiece under pot", False, lambda state: all([
            kinomi_has_cane(state, player),
            kinomi_can_jump_pit(state, player),
            kinomi_can_break_pot(state, player)
        ])],
        ["d1 compass chest", "d1 hit blocks", False, lambda state: kinomi_has_sword(state, player)],
        ["d1 compass chest", "d1 colored tiles heartpiece", False, None],
        ["d1 compass chest", "d1 miniboss arena", False, lambda state: all([
            kinomi_has_small_keys(state, player, 1, 1),
            kinomi_generic_boss_and_miniboss_kill(state, player)
        ])],
        ["d1 miniboss arena", "d1 bracelet", False, lambda state: kinomi_can_press_nonhold_presure_plate_without_blocks(state, player, True)],

        # RIGHT SIDE OF SPIRIT'S GROTTO
        ["enter spirit's grotto", "d1 hit color block", False, lambda state: all([
            kinomi_can_break_pot(state, player),
            kinomi_has_sword(state, player)
        ])],
        ["enter spirit's grotto", "d1 pully puzzle", False, lambda state: all([
            kinomi_has_small_keys(state, player, 1, 1),
            kinomi_has_bracelet(state, player)
        ])],
        ["d1 pully puzzle", "d1 rupee under pot", False, None],
        ["d1 pully puzzle", "d1 boss key chest", False, None],
        ["d1 pully puzzle", "d1 rupee under crystal", False, lambda state: all([
            kinomi_has_small_keys(state, player, 1, 1),
            kinomi_has_bombs(state, player)
        ])],
        ["d1 rupee under crystal", "d1 boss", False, lambda state: all([
            kinomi_has_bracelet(state, player),
            kinomi_has_boss_key(state, player, 1),
            kinomi_generic_boss_and_miniboss_kill(state, player)
        ])],
        ["d1 boss", "d1 final gift", False, None],
    ]

def make_fourCornersCave_logic(player: int):
    return [
        # DESCENDING DOWN
        ["enter four corners cave", "d3 compass chest", False, lambda state: kinomi_can_jump_pit(state, player)],
        ["enter four corners cave", "d3 first floor", False, lambda state: kinomi_has_bombs(state, player)],
        ["d3 first floor", "d3 compass chest", False, None],
        ["d3 first floor", "d3 small key chest in dark", False, lambda state: all([
            kinomi_has_small_keys(state, player, 3, 1),
            kinomi_can_trigger_far_switch(state, player, False, False),
            kinomi_can_kill_normal_enemy(state, player)
        ])],
        ["d3 first floor", "d3 boss", False, lambda state: all([
            kinomi_has_small_keys(state, player, 3, 1), # Placed this here anyway despite the availability to jump across the pit to prevent softlocks.
            kinomi_can_jump_pit(state, player),
            kinomi_has_boomerang(state, player),
            kinomi_has_boss_key(state, player, 3),
            kinomi_generic_boss_and_miniboss_kill(state, player)
        ])],
        ["d3 boss", "d3 final gift", False, None],

        # RIGHT SIDE OF CROSSPATH
        ["d3 first floor", "d3 armos small key chest", False, lambda state: all([
            kinomi_can_kill_normal_enemy(state, player),
            kinomi_can_kill_armos(state, player)
        ])],
        ["d3 first floor", "d3 dungeon map chest", False, lambda state: kinomi_has_small_keys(state, player, 3, 1)],
        ["d3 dungeon map chest", "d3 armos red rupee chest", False, lambda state: kinomi_can_kill_armos(state, player)],

        # LEFT SIDE OF CROSSPATH
        ["d3 first floor", "d3 first floor cross left side", False, lambda state: kinomi_can_trigger_far_switch(state, player, False, False)], # because the blue doors are closed by default upon entry
        ["d3 armos red rupee chest", "d3 first floor cross left side", False, lambda state: kinomi_can_trigger_switch(state, player)], # There is a switch in that room that can be triggered to open the blue door.
        ["d3 first floor cross left side", "d3 heartpiece chest", False, lambda state: any([
            kinomi_can_jump_pit(state, player),
            # I actually do not know any vanila way to do this puzzle, because the first time I played the bridge state did not save correctly.
        ])],
        ["d3 first floor cross left side", "d3 miniboss arena", False, None], # bomb requirement was ruled out earlier in the map, and thankfully that's what that miniboss needs.
        ["d3 first floor cross left side", "d3 25 rupee chest", False, lambda state: all([
            kinomi_has_small_keys(state, player, 3, 1),
            kinomi_can_trigger_far_switch(state, player, True, True)
        ])],
        ["d3 first floor cross left side", "d3 bemos region", False, lambda state: any([
            kinomi_can_jump_4_wide_pit(state, player),
            kinomi_has_cane(state, player)
        ])],
        ["d3 20 rupee chest", "d3 bemos region", False, None],
        ["d3 bemos region", "d3 bemos and armos chest", False, None],
        ["d3 bemos region", "d3 bommerang chest", False, lambda state: all([
            kinomi_has_small_keys(state, player, 3, 1),
            kinomi_can_trigger_far_switch(state, player, True, True)
        ])],

        # BOTTOM SIDE OF CROSSPATH
        ["d3 first floor cross left side", "d3 small key chest spiked beedle", False, lambda state: kinomi_can_kill_spiked_beetle(state, player)],
        ["d3 first floor cross left side", "d3 room 55D cross", False, lambda state: kinomi_has_boomerang(state, player)], # allows the user to open the red door inside room 55D.
        ["d3 room 55D cross", "d3 boss key chest", False, lambda state: kinomi_has_small_keys(state, player, 3, 1)],
        ["d3 room 55D cross", "d3 giant blade trap chest", False, lambda state: any([
            all([
                kinomi_has_cane(state, player),
                kinomi_can_trigger_switch(state, player)
            ]),
            kinomi_can_trigger_far_switch(state, player)
        ])],
        ["d3 room 55D cross", "d3 spikes drop", False, lambda state: kinomi_can_trigger_far_switch(state, player, False, False)],
    ]

def make_seasonsShrine_logic(player: int):
    return [

        # UNLOCK AUTUMN
        ["enter seasons shrine", "d4 summer small key drop", False, lambda state: kinomi_can_kill_normal_enemy(state, player)],
        ["enter seasons shrine", "d4 summer big rupee chest", False, lambda state: kinomi_can_trigger_far_switch(state, player, False, False)],
        ["d4 summer big rupee chest", "d4 autumn fall", False, lambda state: kinomi_has_small_keys(state, player, 4, 1)],
        ["d4 autumn fall", "d4 autumn compass chest", False, lambda state: any([
            kinomi_can_swim(state, player),
            kinomi_can_jump_pit(state, player)
        ])],
        ["d4 autumn compass chest", "d4 autumn small key chest", False, (
            # there is a bug in the code where the switch dosen't do anything in room 52b. So for the time being, we won't need to hit the switch.
            None
        )],
        ["d4 autumn compass chest", "d4 autumn heartpiece", False, lambda state: kinomi_can_jump_pit(state, player)],
        ["d4 autumn heartpiece", "d4 autumn to summer statue block puzzle", False, None],

        # UNLOCK WINTER
        ["d4 autumn fall", "d4 winter fall", False, lambda state: kinomi_has_small_keys(state, player, 4, 1)],
        ["d4 winter fall", "d4 winter small key drop", False, lambda state: kinomi_can_trigger_switch(state, player)],
        ["d4 winter fall", "d4 second crystal", False, lambda state: all([
            kinomi_has_small_keys(state, player, 4, 1),
            kinomi_can_break_d4_crystal(state, player)
        ])],

        # UNLOCK SPRING
        ["d4 winter fall", "d4 spring fall", False, lambda state: kinomi_can_jump_pit(state, player)],
        ["d4 spring fall", "d4 boss", False, lambda state: all([
            kinomi_has_boss_key(state, player, 4),
            kinomi_generic_boss_and_miniboss_kill(state, player)
        ])],
        ["d4 boss", "din's gift", False, None],
        ["d4 boss", "impa's seasons house chest", False, None],
        ["d4 spring fall", "d4 winter north stump region with barrier", False, lambda state: all([
            kinomi_can_break_flower(state, player),
            kinomi_has_small_keys(state, player, 4, 1)
        ])],
        ["d4 winter north stump region with barrier", "d4 first crystal", False, lambda state: kinomi_can_break_d4_crystal(state, player)],
        ["d4 winter north stump region without barrier", "d4 winter north stump switch", False, lambda state: all([
            kinomi_can_break_pot(state, player),
            kinomi_can_trigger_switch(state, player)
        ])],
        ["d4 winter north stump region with barrier", "d4 winter north stump switch", False, lambda state: all([
            kinomi_can_trigger_switch(state, player),
            kinomi_has_bombs(state, player)
        ])],
        ["d4 spring fall", "d4 spring small key chest", False, lambda state: all([
            kinomi_can_use_ember_seeds(state, player, True),
            any([
                kinomi_can_jump_pit(state, player),
                kinomi_has_slingshot(state, player, 2)
            ]),
            kinomi_can_kill_normal_enemy(state, player),
        ])],
        ["d4 spring small key chest", "d4 third crystal", False, lambda state: kinomi_can_break_d4_crystal(state, player)],

        # PATH TO MINIBOSS ARENA
        ["d4 winter fall", "d4 miniboss arena", False, lambda state: all([
            kinomi_has_small_keys(state, player, 4, 1),
            kinomi_generic_boss_and_miniboss_kill(state, player)
        ])],
        ["d4 miniboss arena", "d4 summer armos small key drop", False, lambda state: kinomi_can_kill_armos(state, player)],
        ["d4 miniboss arena", "d4 autumn miniboss arena chest", False, lambda state: kinomi_can_jump_pit(state, player)],
        ["d4 autumn miniboss arena chest", "d4 autumn north stump", False, lambda state: all([
            kinomi_can_break_mushroom(state, player),
            kinomi_can_break_pot(state, player),
            kinomi_can_trigger_switch(state, player),
        ])],
        ["d4 autumn north stump", "d4 autumn roc's cape chest", False, lambda state: all([
            any([
                kinomi_has_bombs(state, player),
                kinomi_can_jump_pit(state, player) # Incase the randomizer chooses this.
            ]),
            kinomi_can_break_mushroom(state, player),
            kinomi_has_small_keys(state, player, 4, 1) # Put this here to prevent softlocks even though it's possible to bypass the keyblock with the cape.
        ])],
        ["d4 autumn miniboss arena chest", "d4 spring north stump heartpiece", False, None],
        ["d4 winter north stump switch", "d4 spring miniboss arena statue puzzle", False, None],
        ["d4 winter north stump switch", "d4 fourth crystal", False, lambda state: all([
            kinomi_has_small_keys(state, player, 4, 1),
            kinomi_can_break_d4_crystal(state, player)
        ])],
        ["d4 miniboss arena", "d4 winter north stump region without barrier", False, lambda state: all([
            state.has("_hit_first_d4_crystal", player),
            state.has("_hit_second_d4_crystal", player),
            state.has("_hit_third_d4_crystal", player),
            state.has("_hit_fourth_d4_crystal", player),
            kinomi_has_small_keys(state, player, 4, 1),
        ])],
        ["d4 winter north stump region without barrier", "d4 boss key chest", False, lambda state: all([
            kinomi_can_jump_pit(state, player),
            kinomi_can_use_ember_seeds(state, player, True)
        ])]
    ]

def make_lostLabrinth_logic(player: int):
    return [
        # LOST LABYRINTH PRESENT MAIN ENTRANCE ROUTE
        ["enter lost labyrinth", "d2 present dungeon map chest", False, lambda state: kinomi_can_kill_normal_enemy(state, player, True)],
        ["d2 present dungeon map chest", "d2 present cross with cane", False, lambda state: any([
            kinomi_can_jump_4_wide_pit(state, player),
            kinomi_has_cane(state, player)
        ])],
        ["d2 present dungeon map chest", "nayru's house", False, None],
        ["lost labyrinth past entrance 4", "d2 present fix holes", False, lambda state: any([
            kinomi_has_cane(state, player),
            kinomi_has_bracelet(state, player)
        ])],
        ["d2 present fix holes", "d2 present cross with cane", False, None],
        ["d2 present fix holes", "d2 present color tiles", False, lambda state: kinomi_has_sword(state, player)],
        ["d2 present fix holes", "d2 present small key chest", False, None],
        ["d2 present fix holes", "d2 present color tiles 2", False, lambda state: kinomi_has_small_keys(state, player, 6, 1)],
        ["d2 present color tiles 2", "d2 present cane chest", False, lambda state: all([
            kinomi_has_small_keys(state, player, 5, 2),
            kinomi_can_kill_normal_enemy(state, player)
        ])],

        # LOST LABYRINTH PAST SMALL KEY CHEST PAST #1
        ["lost labyrinth past entrance 2", "d2 past kill moldorm", False, lambda state: kinomi_can_kill_moldorm(state, player)],

        # LOST LABYRINTH PAST ENTRANCE 3 ROUTE
        ["lost labyrinth past entrance 3", "d2 past bomb chest", False, lambda state: kinomi_has_boss_key(state, player, 4)],
        ["syrup's shop", "d2 past color tile puzzle", True, lambda state: kinomi_has_small_keys(state, player, 2, 1)],

        # LOST LABYRINTH PAST ENTRANCE 4 ROUTE
        ["lost labyrinth past entrance 4", "d2 past kill enemies chest", False, lambda state: all([
            kinomi_can_kill_normal_enemy(state, player),
            any([
                kinomi_has_cane(state, player),
                kinomi_can_jump_pit(state, player)
            ]),
            kinomi_has_small_keys(state, player, 2, 1)
        ])],
        ["d2 past kill enemies chest", "d2 past miniboss arena", False, None], # We already have a bracelet past this point, so theres no need to define logic for it.
        ["d2 past kill enemies chest", "d2 past fix holes past arena", False, None], # ^

        # LOST LABYRINTH PAST MAIN ENTRANCE ROUTE 
        ["lost labyrinth past entrance 3", "d2 past fix holes at entrance", False, lambda state: kinomi_has_cane(state, player)],
        ["lost labyrinth past entrance 3", "d2 past small key drop", False, lambda state: all([
            kinomi_has_bombs(state, player),
            kinomi_can_kill_normal_enemy(state, player),
            kinomi_can_kill_pols_voice(state, player)
        ])],
        ["lost labyrinth past entrance 5", "d2 past small key drop 2", False, lambda state: all([
            kinomi_has_small_keys(state, player, 2, 1),
            kinomi_has_cane(state, player)
        ])],
        ["lost labyrinth past entrance 5", "d2 past witch's chest", False, lambda state: all([
            kinomi_has_small_keys(state, player, 2, 1),
            state.has("Shield", player), # better to have it for defence with the moving floors.
            kinomi_can_kill_normal_enemy(state, player)
        ])],
        ["lost labyrinth past entrance 5", "d2 past compass chest", False, None],
        ["lost labyrinth past entrance 5", "d2 past color tile puzzle 2", False, None],
        ["lost labyrinth past entrance 5", "d2 past heartpiece", False, lambda state: kinomi_can_kill_normal_enemy(state, player)],

        # LOST LABYRINTH PAST RUPTURED MINE ENTRANCE ROUTE
        ["jiku clifs past springwater region", "d2 past color tiles puzzle", False, lambda state: all([
            kinomi_has_bombs(state, player),
            kinomi_has_cane(state, player),
            kinomi_has_glove(state, player),
            kinomi_can_jump_pit(state, player),
            state.has("Old Mining Key", player)
        ])],
        ["d2 past color tiles puzzle", "ganon beaten", False, lambda state: all([
            kinomi_has_small_keys(state, player, 2, 1),
            kinomi_has_sword(state, player),
            any([
                all([
                    # casual rules
                    kinomi_can_use_ember_seeds(state, player, False),
                    kinomi_can_use_mystery_seeds(state, player)
                ]),
                all([
                    kinomi_option_medium_logic(state, player),
                    any([
                        all([
                            kinomi_option_hard_logic(state, player),
                            kinomi_can_use_seeds(state, player),
                            # satchel can't use pegasus to damage, but all others work
                            any([
                                kinomi_has_ember_seeds(state, player),
                                kinomi_has_mystery_seeds(state, player),
                                kinomi_has_scent_seeds(state, player),
                                kinomi_has_gale_seeds(state, player)
                            ])
                        ])
                    ])
                ])
            ])
        ])],

        # LOST LABYRINTH PRESENT GRAVEYARD ENTRANCE ROUTE
        ["lost labyrinth graveyard entrance", "d2 present small key drop", False, lambda state: kinomi_can_kill_normal_enemy(state, player)],
        ["lost labyrinth graveyard entrance", "d2 present stairs maze chest", False, None],
        ["lost labyrinth graveyard entrance", "d2 present miniboss arena", False, lambda state: kinomi_generic_boss_and_miniboss_kill(state, player)],
        #["lost labyrinth graveyard entrance", "d2 present miniboss arena", False, lambda state: kinomi_generic_boss_and_miniboss_kill(state, player)],
        ["d2 present miniboss arena", "d2 present color block puzzle", False, lambda state: all([
            kinomi_has_sword(state, player),
            kinomi_can_jump_pit(state, player)
        ])],
        ["d2 present miniboss arena", "d2 present rupees chest", False, lambda state: kinomi_has_small_keys(state, player, 6, 1)]
    ]

def make_tokayTemple_logic(player: int):
    return [
        ["tokay desert", "d5 chest near first codepiece", False, lambda state: kinomi_has_small_keys(state, player, 5, 1)],
        ["tokay desert", "d5 chest near second codepiece", False, lambda state: kinomi_has_bombs(state, player)],
        ["tokay desert", "d5 chest near third codepiece", False, None],
        ["tokay desert", "d5 chest near fourth codepiece", False, lambda state: kinomi_can_kill_normal_enemy(state, player)],
        ["tokay desert", "d5 chest near fifth codepiece", False, lambda state: all([
            kinomi_has_small_keys(state, player, 5, 2),
            kinomi_has_cane(state, player)
        ])],
        ["tokay desert", "d5 color block downstairs area", False, lambda state: kinomi_has_enough_slates(state, player)],
        ["d5 color block downstairs area", "d5 color block puzzle", False, lambda state: kinomi_has_glove(state, player)],
        ["d5 color block downstairs area", "d5 boss", False, lambda state: all([
            kinomi_has_small_keys(state, player, 5, 1),
            any([
                kinomi_option_hard_logic(state, player), # Hard logic can use the ember seeds fast enough without removing keyblock. 
                all([ # It's possible to proceed without removing last keyblock.
                    kinomi_option_medium_logic(state, player),
                    kinomi_can_use_pegasus_seeds(state, player)
                ]),
                kinomi_has_small_keys(state, player, 5, 1),
            ]),
            kinomi_can_use_ember_seeds(state, player, False),
            kinomi_has_boss_key(state, player, 5),
            kinomi_has_cane(state, player)
        ])],
        ["d5 boss", "nayru's gift", False, None],
        ["tokay desert", "d5 armos puzzle", False, lambda state: all([
            kinomi_has_bombs(state, player),
            kinomi_has_cane(state, player)
        ])],
        ["tokay desert", "d5 chest near slate slots", False, lambda state: kinomi_has_cane(state, player)],
        ["d5 chest near slate slots", "d5 statue block puzzle", False, None],
        ["d5 chest near slate slots", "d5 fill holes", False, lambda state: kinomi_has_bombs(state, player)],
        ["d5 chest near slate slots", "d5 miniboss arena", False, None],
        ["d5 miniboss arena", "d5 statue block puzzle 2", False, None],

    ]