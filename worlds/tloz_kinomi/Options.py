from dataclasses import dataclass

from Options import Choice, DeathLink, DefaultOnToggle, PerGameCommonOptions, Range, Toggle, StartInventoryPool, ItemSet

from .data.Items import ITEMS_DATA


class GiftsOfKinomiLogicDifficulty(Choice):
    """
    The difficulty of the logic used to generate the seed.
    - Casual: expects you to know what you would know when playing the game for the first time
    - Medium: expects you to know well the alternatives on how to do basic things, but won't expect any trick
    - Hard: expects you to know difficult tricks such as bomb jumps
    """
    display_name = "Logic Difficulty"

    option_casual = 0
    option_medium = 1
    option_hard = 2

    default = 0


class GiftsOfKinomiRequiredGifts(Range):
    """
    The amount of gifts that need to be obtained in order to beat ganon.
    """
    display_name = "Required Gifts"
    range_start = 0
    range_end = 2
    default = 2

class GiftsOfKinomiRequiredSlates(Range):
    """
    The amount of slates that need to be obtained in order to get to the boss for the Temple of The Tokay.
    """
    display_name = "Required Slates"
    range_start = 0
    range_end = 8
    default = 8

class GiftsOfKinomiRemoveExtraStairsFromLostLabyrinth(Toggle):
    """
    Removes all of the extra stairs connecting to the Lost Labyrinth from the past, making the dungeon all in one and easier to navigate.
    """
    display_name = "Remove Extra Stairs From Lost Labyrinth"

    default = False


class GiftsOfKinomiDungeonShuffle(Choice):
    """
    - Vanilla: each dungeon entrance leads to its intended dungeon
    - Shuffle: each dungeon entrance leads to a random dungeon picked at generation time
    """
    display_name = "Shuffle Dungeons"

    option_vanilla = 0
    option_shuffle = 1

    default = 0


class GiftsOfKinomiMasterKeys(Choice):
    """
    - Disabled: All dungeon keys must be obtained individually, just like in vanilla
    - All Small Keys: Small Keys are replaced by a single Master Key for each dungeon which is capable of opening
      every small keydoor for that dungeon
    - All Dungeon Keys: the Master Key for each dungeon is also capable of opening the boss keydoor,
      removing Boss Keys from the item pool
    Master Keys placement is determined following the "Keysanity (Small Keys)" option.
    """
    display_name = "Master Keys"

    option_disabled = 0
    option_all_small_keys = 1
    option_all_dungeon_keys = 2

    default = 0

class GiftsOfKinomiSmallKeyShuffle(Toggle):
    """
    If enabled, dungeon Small Keys can be found anywhere instead of being confined in their dungeon of origin.
    """
    display_name = "Keysanity (Small Keys)"


class GiftsOfKinomiBossKeyShuffle(Toggle):
    """
    If enabled, dungeon Boss Keys can be found anywhere instead of being confined in their dungeon of origin.
    """
    display_name = "Keysanity (Boss Keys)"


class GiftsOfKinomiMapCompassShuffle(Toggle):
    """
    If enabled, Dungeon Maps and Compasses can be found anywhere instead of being confined in their dungeon of origin.
    """
    display_name = "Maps & Compasses Outside Dungeon"


class GiftsOfKinomiSlateShuffle(Toggle):
    """
    If enabled, Slates can be found anywhere instead of being confined in Dungeon 8.
    """
    display_name = "Slates Outside Dungeon 8"


class OracleOfSeasonsRequiredRings(ItemSet):
    """
    Forces a specified set of rings to appear somewhere in the seed.
    Adding too many rings to this list can cause generation failures.
    List of ring names can be found here: https://zeldawiki.wiki/wiki/Magic_Ring
    """
    display_name = "Required Rings"
    valid_keys = {name for name, idata in ITEMS_DATA.items() if "ring" in idata}


class OracleOfSeasonsExcludedRings(ItemSet):
    """
    Forces a specified set of rings to not appear in the seed.
    List of ring names can be found here: https://zeldawiki.wiki/wiki/Magic_Ring
    """
    display_name = "Excluded Rings"
    default = sorted({name for name, idata in ITEMS_DATA.items() if "ring" in idata and idata["ring"] == "useless"})
    valid_keys = {name for name, idata in ITEMS_DATA.items() if "ring" in idata}


class GiftsOfKinomiPricesFactor(Range):
    """
    A factor (expressed as percentage) that will be applied to all prices inside all shops in the game.
    - Setting it at 10% will make all items almost free
    - Setting it at 500% will make all items horrendously expensive, use at your own risk!
    """
    display_name = "Prices Factor (%)"

    range_start = 10
    range_end = 500
    default = 100


@dataclass
class GiftsOfKinomiOptions(PerGameCommonOptions):
    start_inventory_from_pool: StartInventoryPool
    logic_difficulty: GiftsOfKinomiLogicDifficulty
    required_gifts: GiftsOfKinomiRequiredGifts
    required_slates: GiftsOfKinomiRequiredSlates
    remove_extra_stairs_from_lost_labyrinth_past: GiftsOfKinomiRemoveExtraStairsFromLostLabyrinth
    shuffle_dungeons: GiftsOfKinomiDungeonShuffle
    master_keys: GiftsOfKinomiMasterKeys
    keysanity_small_keys: GiftsOfKinomiSmallKeyShuffle
    keysanity_boss_keys: GiftsOfKinomiBossKeyShuffle
    keysanity_maps_compasses: GiftsOfKinomiMapCompassShuffle
    keysanity_slates: GiftsOfKinomiSlateShuffle
    required_rings: OracleOfSeasonsRequiredRings
    excluded_rings: OracleOfSeasonsExcludedRings
    shop_prices_factor: GiftsOfKinomiPricesFactor
    death_link: DeathLink
