# ArchipelagoOoA
Updates to and maintenance of the Oracle of Ages APWorld.

This is a re-hosting of the [code originally developed by SenPierre](https://github.com/SenPierre/ArchipelagoOoA). I'm not able to simply fork because I started work from a compatibility update created by Ishigh1.

## Updates

- Cleaning up location/item names. Location names now all follow a nice, consistent `region: specific location` format.
- Updated the "warp home" destination to beside the time portal near the Maku Tree. This is to save having to walk all the way through Maku Road to reach the past, which quickly becomes incredibly annoying to do.
- Added a new option `duplicate_seed_trees`, similar to the option in Oracle of Seasons: you get to pick 3 seed trees which must not hold a unique seed type. This helps prevent really annoying situations where difficult-to-reach trees (such as Zora Village) hold a unique seed type. Additionally, the seed placement logic now ensures that no seed type appears more than twice.
