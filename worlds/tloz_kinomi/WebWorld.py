from BaseClasses import Tutorial
from worlds.AutoWorld import WebWorld

class GiftsOfKinomiWeb(WebWorld):
    theme = "grass"
    tutorials = [Tutorial(
        "Multiworld Setup Guide",
        "A guide to setting up Gifts of Kinomi for Archipelago on your computer.",
        "English",
        "kinomi_setup_en.md",
        "kinomi_setup/en",
        ["josephanimate2021"]
    )]