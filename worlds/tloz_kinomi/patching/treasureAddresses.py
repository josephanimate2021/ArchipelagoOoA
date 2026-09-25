import os
import json
import logging

from .Util import world_path
from .sym import sym
        

newFilePath = world_path("patching/treasureAddresses.json")

class treasureAddressMaker():
    # Variables for the loop
    count = 0
    addresses: list[int | str | list[int]] = []
    TREASURE_ADDRESSES: list[int | str | list[int] | list[str]] = []
    startWriteCode = False

    # base address for treasure objects.
    base_address = sym().find("label", "treasureObjectData").address_in_rom()

    def __init__(self):
        if os.path.isfile(newFilePath):
            self.TREASURE_ADDRESSES = json.loads(open(newFilePath, "rt").read())
            return
        # Reads the contents of the treasureObjectData.s file and appends it's address from the base to an array
        with open(world_path("disasm/data/ages/treasureObjectData.s"), "rt") as f:
            self.newFile = open(newFilePath, "wt")
            looger = logging.getLogger()
            looger.info("Creating new treasureAddresses file since it dosen't exist.")
            array = f.readlines()
            for i in range(len(array)):

                # First, we have to look for a line in the code called treasureObjectData, 
                # then append addresses based on the bytes written to the file from the base address in GB perspective.
                code = array[i]

                if self.startWriteCode:
                    if code.find("m_TreasureSubid") > -1:
                        self.addresses.append(self.base_address + self.count)
                        self.count += 4
                    elif code.find("m_TreasurePointer") > -1:
                        self.addresses.append(code.split("m_TreasurePointer ")[1].split(" ")[0].splitlines()[0])
                        self.count += 4

                if code.startswith("treasureObjectData"):
                    if code.startswith("treasureObjectData:"):
                        self.startWriteCode = True
                    else:
                        self.startWriteCode = False
                    if not self.startWriteCode and (
                        array[i - 3].find(f"/* ${hex(len(self.addresses) - 1)[2:]} */") > -1
                        and array[i - 3].find(f"/* ${hex(len(self.addresses))[2:]} */") == -1
                    ):
                        break # break loop when all addresses are written.

            for i in range(len(self.addresses)):
                addr = self.addresses[i]
                if type(addr) == int:
                    self.TREASURE_ADDRESSES.append(hex(addr))
                else:
                    addresses: list[int] = []
                    count = self.count
                    self.startReadCode = False

                    for i in range(len(array)): # Same as the appendAddress function except we have to look for treasureObjectData{number}
                        code = array[i]
                        if self.startWriteCode or self.startReadCode:
                            if code.find("m_TreasureSubid") > -1:
                                if self.startWriteCode:
                                    addresses.append(self.base_address + count)
                                count += 4
                            if code.startswith("treasureObjectData") and self.startWriteCode:
                                self.startWriteCode = False
                                break
                        if addr == code.splitlines()[0].split(":")[0]:
                            self.startWriteCode = True
                        elif code.startswith("treasureObjectData") and not code.startswith("treasureObjectData:"):
                            self.startReadCode = True

                    self.TREASURE_ADDRESSES.append([hex(addr) for addr in addresses])

            self.newFile.write(json.dumps(self.TREASURE_ADDRESSES, indent=4))
            self.newFile.close()
            looger.info(f"Saved treasure addresses array to {newFilePath} for later viewing.")


