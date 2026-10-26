from ...common.patching.RomData import RomData
from ...common.patching.Util import simple_hex
from ...common.patching.rooms.encoding import encode_group_data_small
from ..sym import sym


def encode_group_data(room_data: list[bytearray], group: int, seasons: bool = False) -> tuple[int, bytearray, bytearray]:
    first_room = group * 0x100
    big_room_group_start = 5 if seasons else 4
    if group < big_room_group_start:
        return encode_group_data_small(room_data, first_room)
    else:
        return 0, bytearray(), bytearray()


def write_room_data(rom: RomData, room_data: list[bytearray], parsed_sym: sym):
    current_firstroom = 0
    num_groups = 0
    for label, _ in parsed_sym.get_labels().items():
        if label == f"roomLayoutGroup{num_groups}Table":
            num_groups += 1

    for group in range(num_groups):
        room_type, room_infos, group_data = encode_group_data(room_data, group, num_groups == 7)
        
        if room_type == 1:
            group_layout_table = parsed_sym.find("label", f"roomLayoutGroup{group}Table")
            room_data_current = parsed_sym.find("label", f"room{simple_hex(current_firstroom, 4)}")

            # Room infos content
            rom.write_bytes(group_layout_table.address_in_rom(), room_infos)

            # Group's data content
            rom.write_bytes(room_data_current.address_in_rom(), group_data)
        current_firstroom += 0x100