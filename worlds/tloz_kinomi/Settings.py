import settings

from typing import Union
from .patching.ProcedurePatch import ROM_HASH
from .patching.Constants import REFILL_NPCS

def refillNPCInString(limit=-1) -> str:
    array = []
    for npc in REFILL_NPCS.keys():
        array.append(npc)
    if limit == -1:
        limit = len(array)
    string = ""
    for i in range(len(array)):
        if i == limit:
            break
        if ((limit - 1) == 0 and i == len(array) - 1) or ((limit - 1) != 0 and i == (limit - 1)):
            string += "and "
        string += f"{array[i] + (", " if i != limit - 1 else "")}"
    return string

print(refillNPCInString())
class KinomiSettings(settings.Group):
    class KinomiRomFileOOA(settings.UserFilePath):
        """File path of the OOA US rom"""
        description = "Oracle of Ages (USA) ROM File"
        copy_to = "Legend of Zelda, The - Oracle of Ages (USA).gbc"
        md5s = [ROM_HASH]

    class KinomiCharacterSprite(str):
        """
        The name of the sprite file to use (from "data/sprites/oos_ooa/").
        Putting "link" as a value uses the default game sprite.
        Putting "random" as a value randomly picks a sprite from your sprites directory for each generated ROM.
        """

    class KinomiCharacterPalette(str):
        """
        The color palette used for character sprite throughout the game.
        Valid values are: "green", "red", "blue", "orange", and "random"
        """

    class KinomiHeartBeepInterval(str):
        """
        A factor applied to the infamous heart beep sound interval.
        Valid values are: "vanilla", "half", "quarter", "disabled"
        """

    class KinomiRefillNPC(str):
        """
        Defines the NPC that refills your inventory when you talk to it. Valid values are: "impa", "rosa", and "disabled"
        """

    rom_file: KinomiRomFileOOA = KinomiRomFileOOA(KinomiRomFileOOA.copy_to)
    refill_npc: Union[KinomiRefillNPC, str] = refillNPCInString(1)
    heart_beep_interval: Union[KinomiHeartBeepInterval, str] = "vanilla"
    character_sprite: Union[KinomiCharacterSprite, str] = "link"
    character_palette: Union[KinomiCharacterPalette, str] = "green"