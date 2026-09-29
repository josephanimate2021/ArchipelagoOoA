# Format is [label, lineNumber] (found in the warpSources.s file inside oracles-disasm/data/{game} after you begin with the label and count down the line). 
# line count starts at 1 and onward after the label. setting it to zero breaks things.
# This also has to be in dungeon order to prevent the user from getting confused by dungeon name.
# Putting in name as a property in here adds that warp to the logic. Otherwise no logic is applied for that warp.
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
    ],
    "portals": [
        {
            "entrance": ["warpSource4a2d", 1],
            "exit": ["warpSource4a25", 1],
            "name": "lost labyrinth portal",
            "group": 0
        },        
        {
            "entrance": ["warpSource4fad", 2],
            "exit": ["group0WarpSources", 26],
            "name": "deeper woods library portal",
            "group": 3
        },
        {
            "entrance": ["warpSource4fb9", 2],
            "exit": ["group3WarpSources", 78],
            "group": 3
        },
        {
            "entrance": ["warpSource4fb5", 1],
            "exit": ["warpSource4fd1", 2],
            "group": 3
        },
        {
            "entrance": ["warpSource4a4d", 1],
            "exit": ["warpSource4fa9", 1],
            "name": "seasons swamp portal",
            "group": 0
        },
        {
            "entrance": ["warpSource4a51", 2],
            "exit": ["warpSource4abd", 1],
            "name": "seasons shrine portal",
            "group": 0
        },
        {
            "entrance": ["group3WarpSources", 76],
            "exit": ["warpSource4fc1", 1],
            "group": 3
        }
    ]
}