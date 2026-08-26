def make_regions():
    from ..Logic import make_logic_array
    regions = []
    for logic_array in make_logic_array(0):
        for region_desc in logic_array:
            for i in range(2):
                if region_desc[i] not in regions:
                    regions.append(region_desc[i])
    return regions

REGIONS = make_regions()
