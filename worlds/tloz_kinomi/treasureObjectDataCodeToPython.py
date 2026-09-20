import sys
import os

from .patching.Util import world_path
from .common.patching.z80asm.Assembler import Z80Assembler
from .common.patching.z80asm.Assembler import GameboyAddress

class sym():
    def __init__(self):
        with open(world_path("disasm/ages.sym"), "rt") as f:
            property = False
            self.info = {}
            for code in f.readlines():
                line = code.splitlines()[0]
                if line:
                    if line.find("[") > -1 and line.find("]") > -1:
                        property = line.split("[")[1].split("]")[0]
                        self.info[property] = {}
                    elif property:
                        number = line.split(" ")[0]
                        self.info[property][number] = line[(len(number) + 1):]
        
    def get_labels(self):
        info = {}
        for address, label in self.info["labels"].items():
            bank, addr = address.split(":")
            if int("0x0" + addr[:1], 16) > 11:
                continue
            info[label] = GameboyAddress(int("0x" + bank, 16), int("0x" + addr, 16))
        return info
    
    def get_sections(self):
        array = []
        for full_address, others in self.info["sections"].items():
            bank_and_address, address, size, label = others.split(" ")
            bank, addr = bank_and_address.split(":")
            if int("0x0" + addr[:1], 16) > 11:
                continue
            gameboy_address = GameboyAddress(int("0x" + bank, 16), int("0x" + addr, 16))
            array.append({
                "full_address": full_address,
                "bank_and_address": [int("0x0" + s, 16) for s in bank_and_address.split(":")],
                "address": address,
                "size": size,
                "label": label
            })
        return array

newFilePath = world_path("patching/treasureAddresses.py")

class treasureAddressMaker():
    # for file creation
    newFile = open(newFilePath, "w")

    # Variables for the loop
    count = 0
    addresses: list[int | str | list[int]] = []
    TREASURE_ADDRESSES: list[int | str | list[int] | list[str]] = []
    startWriteCode = False
    i = 0

    # variables for the base address
    mainLabel = "treasureObjectData"

    def __init__(self, own_labels):
        self.base_address = own_labels[self.mainLabel].address_in_rom()
        # Reads the contents of the treasureObjectData.s file and appends it's address from the base to an array
        with open(world_path("disasm/data/ages/treasureObjectData.s"), "rt") as f:
            array = f.readlines()
            listLen = len(array)
            def appendAddress(): # First, we have to look for a line in the code called treasureObjectData, then append addresses based on the bytes written to the file from the base address in GB perspective.
                code = array[self.i]

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
                        array[self.i - 3].find(f"/* ${hex(len(self.addresses) - 1)[2:]} */") > -1
                        and array[self.i - 3].find(f"/* ${hex(len(self.addresses))[2:]} */") == -1
                    ):
                        return # end function when it's done.

                if self.i != listLen - 1: # To prevent us from going out of range.
                    self.i += 1
                    appendAddress()

            appendAddress()

            for i in range(len(self.addresses)):
                addr = self.addresses[i]
                if type(addr) == int:
                    self.TREASURE_ADDRESSES.append(hex(addr))
                else:
                    addresses: list[int] = []
                    count = self.count
                    print(count)
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

                    addresses_in_hex = [hex(addr) for addr in addresses]
                    self.TREASURE_ADDRESSES.append(addresses_in_hex)


