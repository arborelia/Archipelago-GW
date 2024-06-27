from typing import Dict, NamedTuple, Set, Optional
from .names_regions import RegionNames as rname


class ID2LocationData(NamedTuple):
    region: str
    location_id_offset: int
    location_group: Optional[str] = None


location_base_id = 238492834

location_table: Dict[str, ID2LocationData] = {
    # Each area gets 100 reserved location IDs
    # 0: Fluffy Fields
    "Fluffy Fields Caves - Goldbun Combat Chest": ID2LocationData(rname.ffc_b.value, 0),
    "Fluffy Fields Caves - Portal Room Chest": ID2LocationData(rname.ffc_c.value, 1),
    "Fluffy Fields Caves - Timed Bridge Chest": ID2LocationData(rname.ffc_e.value, 2),
    "Fluffy Fields Caves - Hermit Hint Chest": ID2LocationData(rname.ffc_f.value, 3),
    "Fluffy Fields Caves - Laser Chest": ID2LocationData(rname.ffc_g.value, 4),
    "Fluffy Fields Caves - Number Blocks Chest": ID2LocationData(rname.ffc_j.value, 5),
    "Fluffy Fields Caves - Ice Blockade Chest": ID2LocationData(rname.ffc_k.value, 6),
    "Fluffy Fields Caves - Double Spikebun Combat Chest": ID2LocationData(rname.ffc_m.value, 7),
    "Fluffy Fields Caves - Potion Bar Chest": ID2LocationData(rname.ffc_p.value, 8),
    "Fluffy Fields Caves - Six Buns Combat Chest": ID2LocationData(rname.ffc_q.value, 9),
    "Fluffy Fields Caves - Artist Backroom Chest": ID2LocationData(rname.ffc_x2.value, 10),
    "Fluffy Fields Caves - Jenny Berry House Outfit": ID2LocationData(rname.ffc_u.value, 11, "Super Secrets"),
    # 100: Sweetwater Coast
    "Sweetwater Coast Caves - White Gates Combat Chest": ID2LocationData(rname.scc_b.value, 100),
    "Sweetwater Coast Caves - Feral Gates Combat Chest": ID2LocationData(rname.scc_g.value, 101),
    "Sweetwater Coast Caves - Three Teleporters Chest": ID2LocationData(rname.scc_h.value, 102),
    "Sweetwater Coast Caves - Four Candy Snakes Combat Chest": ID2LocationData(rname.scc_i.value, 103),
    "Sweetwater Coast Caves - Portal Spikes Chest": ID2LocationData(rname.scc_j.value, 104),
    "Sweetwater Coast Caves - Hint Hermit Chest": ID2LocationData(rname.scc_k.value, 105),
    "Sweetwater Coast Caves - Fake Chest Cave Chest": ID2LocationData(rname.scc_l.value, 106),
    "Sweetwater Coast Caves - Wooden Balls Spike Floor Chest": ID2LocationData(rname.scc_m.value, 107),
    "Sweetwater Coast Caves - Kung Fu Jenny Chest": ID2LocationData(rname.scc_n.value, 108),
    # 200: Fancy Ruins

    # 300: Star Woods

    # 400: Slippery Slope

    # 500: Pepperpain

    # 600: Frozen Court

    # 700: Lonely Road

    # 800: Pillow Fort
    "Pillow Fort - Treasure Chest": ID2LocationData(rname.d1_i.value, 800, "Dungeons"),
    "Pillow Fort - Shellbun Nest Key": ID2LocationData(rname.d1_j.value, 801, "Dungeons"),
    "Pillow Fort - Crayon Chest": ID2LocationData(rname.d1_g.value, 802, "Dungeons"),
    "Pillow Fort - Safety Jenny Gate Key": ID2LocationData(rname.d1_e.value, 803, "Dungeons"),
    "Pillow Fort - Boss Reward Chest": ID2LocationData(rname.d1_c.value, 804, "Dungeons"),
    # 900: Sand Castle
    "Sand Castle - Crayon Chest": ID2LocationData(rname.d2_g.value, 900, "Dungeons"),
    "Sand Castle - Orbiting Balls Key": ID2LocationData(rname.d2_i.value, 901, "Dungeons"),
    "Sand Castle - Spikebun Dunes Key": ID2LocationData(rname.d2_d.value, 902, "Dungeons"),
    "Sand Castle - Treasure Chest": ID2LocationData(rname.d2_j.value, 904, "Dungeons"),
    "Sand Castle - Boss Reward Chest": ID2LocationData(rname.d2_a.value, 905, "Dungeons"),
    # 1000: Art Gallery

    # 1100: Trash Cave

    # 1200: Flooded Basement

    # 1300: Potassium Mines

    # 1400: Boiling Grave

    # 1500: Grand Library

    # 1600: Sunken Labyrinth

    # 1700: Machine Fortress

    # 1800: Dark Hypostyle

    # 1900: Tomb of Simulacrum

    # 2000: Syncope

    # 2100: Wizardry Lab

    # 2200: Antigram

    # 2300: Bottomless Tower

    # 2400: Quietus

    # 2500: Portal Worlds
    "Autumn Climb - Chest": ID2LocationData(rname.autumn_climb.value, 2500, "Portal Worlds")
    
    # 2600+: Misc Locations
}

location_name_to_id: Dict[str, int] = {name: location_base_id + data.location_id_offset for name, data in location_table.items()}

location_name_groups: Dict[str, Set[str]] = {}
for loc_name, loc_data in location_table.items():
    loc_group_name = loc_name.split(" - ", 1)[0]
    location_name_groups.setdefault(loc_group_name, set()).add(loc_name)
    if loc_data.location_group:
        location_name_groups.setdefault(loc_data.location_group, set()).add(loc_name)
