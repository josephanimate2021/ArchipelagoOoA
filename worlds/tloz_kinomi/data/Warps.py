# Format is [label, lineNumber] (found in the warpSources.s file inside oracles-disasm/data/{game} after you begin with the label and count down the line). 
# line count starts at 1 and onward after the label. setting it to zero breaks things.
# This also has to be in dungeon order to prevent the user from getting confused by dungeon name.

ALL_WARPS = {
    "dungeons": [
        {
            "entrance": ["group0WarpSources", 35],
            "exit": ["group5WarpSources", 76],
            "name": "summer villa",
            "group": 0
        },
        {
            "entrance": ["group0WarpSources", 42],
            "exit": ["group4WarpSources", 1],
            "name": "spirit's grotto",
            "group": 0
        },
        {
            "entrance": ["warpSource4a39", 2],
            "exit": ["group4WarpSources", 44],
            "name": "lost labyrinth",
            "group": 0
        },
        {
            "entrance": ["group0WarpSources", 68],
            "exit": ["group5WarpSources", 78],
            "name": "four corners cave",
            "group": 0
        },
        {
            "entrance": ["group0WarpSources", 62],
            "exit": ["group5WarpSources", 70],
            "name": "seasons shrine",
            "group": 0
        },
    ]
}