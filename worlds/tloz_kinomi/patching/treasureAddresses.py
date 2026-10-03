import os
import json
import logging

from .Util import world_path
from .sym import sym
from ..common.patching.Util import simple_hex
from ..common.patching.RomData import RomData
        

newFilePath = world_path("patching/treasureAddresses.json")

class treasureAddressMaker():
    # Variables for the loop
    addresses: list[str | list[str]] = []
    TREASURE_ADDRESSES = {
        "objects": [],
        "pointers": {}
    }
    startWriteCode = False
    base_addr_end: int

    def __init__(self, parsed_sym: sym, rom: RomData):
        if os.path.isfile(newFilePath):
            self.TREASURE_ADDRESSES = json.loads(open(newFilePath, "rt").read())
            return
        
        self.newFile = open(newFilePath, "wt")
        base_addr_start = parsed_sym.find("label", "treasureObjectData")
        bank, offset = base_addr_start.__str__().split(":")
        self.base_addr_end = parsed_sym.find_addr_end(bank, offset).address_in_rom()
        looger = logging.getLogger()
        looger.info("Creating new treasureAddresses file since it dosen't exist.")
        self.count = 0

        def appendAddressLoop(f, update_array):
            if f < self.base_addr_end:
                bytes = [int(j) for j in rom.read_bytes(f, 3)]
                if bytes[0] == 0x80: # Address is a treasure pointer.
                    self.TREASURE_ADDRESSES["pointers"][self.count] = hex(f)
                    update_array.append(parsed_sym.find("label_findFromBankAndAddr", f"{bank}:{simple_hex(bytes[2]) +  simple_hex(bytes[1])}"))
                else:
                    update_array.append(f)
                self.count += 1
                appendAddressLoop(f + 4, update_array)
        appendAddressLoop(base_addr_start.address_in_rom(), self.addresses)
    
        for i in range(len(self.addresses)):
            addr = self.addresses[i]
            if type(addr) == int:
                self.TREASURE_ADDRESSES["objects"].append(hex(addr))
            else:
                addresses: list[int] = []
                if addr is not None:
                    base_addr_start = parsed_sym.find("label", addr)
                    bank, offset = base_addr_start.__str__().split(":")
                    self.base_addr_end = parsed_sym.find_addr_end(bank, offset).address_in_rom()
                    appendAddressLoop(base_addr_start.address_in_rom(), addresses)
                self.TREASURE_ADDRESSES["objects"].append([hex(a) for a in addresses])

        self.newFile.write(json.dumps(self.TREASURE_ADDRESSES, indent=4))
        self.newFile.close()
        looger.info(f"Saved treasure addresses array to {newFilePath} for later viewing.")


