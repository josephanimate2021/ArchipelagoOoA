from dataclasses import dataclass

from Options import Choice, DeathLink, DefaultOnToggle, PerGameCommonOptions, Range, Toggle, StartInventoryPool, ItemSet, OptionSet, NamedRange, ItemsAccessibility

from .data.Items import ITEMS_DATA
from .data.Constants import TREES_TABLE
from .common.Options import *


class OracleOfAgesMinibossLocations(Toggle):
    """
    When enabled, each time you defeat a miniboss inside a dungeon, 
    a chest will appear in the miniboss room where if you open it, a randomized item will be inside.
    This is an option requested by Run_In_A_Week on discord over at the Archipelago Server.
    """
    display_name = "Miniboss Locations"

    include_in_patch = True
    include_in_slot_data = True

class OracleOfAgesLynnaGardener(Toggle):
    """
    When enabled, a friendly gardener will have trimmed the bushes outside of Lynna City and cleared the path
    so you don't have to! This will expand the sphere 0 checks to include everything past the bushes that you
    normally would need nothing for.
    """
    display_name = "Lynna Gardener"
    
    include_in_patch = True
    include_in_slot_data = True

class OracleOfAgesRequiredSlates(Range):
    """
    The amount of slate that need to be obtained in order to get to the boss of the eigth dungeons.
    """
    display_name = "Required Slates"
    range_start = 0
    range_end = 4
    default = 4

    include_in_patch = True
    include_in_slot_data = True


class OracleOfAgesDuplicateSeedTrees(OptionSet):
    """
    The game contains 10 seed trees (8 of which has valid choices), but only 5 types of seeds. This means that some types of seeds can appear on
    multiple trees. This setting lets you choose seed trees that will be guaranteed to not hold a unique type of
    seed. You can choose up to 3.
    Regardless of what you choose, each seed type will appear on at most 2 trees.
    Valid choices are:
    - Lynna City
    - Ambi's Palace
    - Deku Forest
    - Symmetry City
    - Crescent Island
    - Rolling Ridge West
    - Rolling Ridge East
    - Zora Village
    """
    display_name = "Duplicate Seed Trees"
    default = {"Crescent Island", "Zora Village", "Rolling Ridge East"}
    valid_keys = {key for key in TREES_TABLE.keys()}

    include_in_patch = True
    include_in_slot_data = True


class OracleOfAgesSlateShuffle(Toggle):
    """
    If enabled, Slates can be found anywhere instead of being confined in Dungeon 8.
    """
    display_name = "Slates Outside Dungeon 8"

    include_in_patch = True
    include_in_slot_data = True

@dataclass
class OracleOfAgesOptions(PerGameCommonOptions):
    accessibility: ItemsAccessibility
    start_inventory_from_pool: StartInventoryPool
    miniboss_locations: OracleOfAgesMinibossLocations
    lynna_gardener: OracleOfAgesLynnaGardener
    deterministic_gasha_locations: OraclesGashaLocations
    gasha_nut_kill_requirement: OraclesGashaNutKillRequirement
    goal: OraclesGoal
    shuffle_old_men: OraclesOldMenShuffle
    secret_locations: OraclesIncludeSecretLocations
    logic_difficulty: OraclesLogicDifficulty
    required_essences: OraclesRequiredEssences
    required_slates: OracleOfAgesRequiredSlates
    animal_companion: OraclesAnimalCompanion
    default_seed: OraclesDefaultSeedType
    duplicate_seed_trees: OracleOfAgesDuplicateSeedTrees
    enforce_potion_in_shop: OraclesEnforcePotionInShop
    shuffle_dungeons: OraclesDungeonShuffle
    master_keys: OraclesMasterKeys
    keysanity_small_keys: OraclesSmallKeyShuffle
    keysanity_boss_keys: OraclesBossKeyShuffle
    keysanity_maps_compasses: OraclesMapCompassShuffle
    keysanity_slates: OracleOfAgesSlateShuffle
    required_rings: OraclesRequiredRings
    excluded_rings: OraclesExcludedRings
    shop_prices: OraclesShopPrices
    advance_shop: OraclesAdvanceShop
    combat_difficulty: OraclesCombatDifficulty
    death_link: DeathLink
