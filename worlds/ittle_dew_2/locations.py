from typing import Dict, NamedTuple, Set, Optional


class ID2LocationData(NamedTuple):
    region: str
    location_id_offset: int
    location_group: Optional[str] = None


location_base_id = 238492834

location_table: Dict[str, ID2LocationData] = {
    # Each area gets 100 reserved location IDs
    # 0: Fluffy Fields
    "Fluffy Fields Caves - Goldbun Combat Chest": ID2LocationData("Fluffy Fields Caves B", 0),
    "Fluffy Fields Caves - Portal Room Chest": ID2LocationData("Fluffy Fields Caves C", 1),
    "Fluffy Fields Caves - Timed Bridge Chest": ID2LocationData("Fluffy Fields Caves E", 2),
    "Fluffy Fields Caves - Hermit Hint Chest": ID2LocationData("Fluffy Fields Caves F", 3),
    "Fluffy Fields Caves - Laser Chest": ID2LocationData("Fluffy Fields Caves G", 4),
    "Fluffy Fields Caves - Number Blocks Chest": ID2LocationData("Fluffy Fields Caves J", 5),
    "Fluffy Fields Caves - Ice Blockade Chest": ID2LocationData("Fluffy Fields Caves K", 6),
    "Fluffy Fields Caves - Double Spikebun Combat Chest": ID2LocationData("Fluffy Fields Caves M", 7),
    "Fluffy Fields Caves - Potion Bar Chest": ID2LocationData("Fluffy Fields Caves P", 8),
    "Fluffy Fields Caves - Six Buns Combat Chest": ID2LocationData("Fluffy Fields Caves Q", 9),
    "Fluffy Fields Caves - Artist Backroom Chest": ID2LocationData("Fluffy Fields Caves X2", 10),
    # 100: Sweetwater Coast
    "Sweetwater Coast Caves - Feral Gates Combat Chest": ID2LocationData("Sweetwater Coast Caves G", 100),
    "Sweetwater Coast Caves - Three Teleporters Chest": ID2LocationData("Sweetwater Coast Caves H", 101),
    "Sweetwater Coast Caves - Four Candy Snakes Combat Chest": ID2LocationData("Sweetwater Coast Caves I", 102),
    "Sweetwater Coast Caves - Portal Spikes Chest": ID2LocationData("Sweetwater Coast Caves J", 103),
    "Sweetwater Coast Caves - Hint Hermit Chest": ID2LocationData("Sweetwater Coast Caves K", 104),
    "Sweetwater Coast Caves - Fake Chest Cave Chest": ID2LocationData("Sweetwater Coast Caves L", 105),
    "Sweetwater Coast Caves - Wooden Balls Spike Floor Chest": ID2LocationData("Sweetwater Coast Caves M", 106),
    "Sweetwater Coast Caves - Kung Fu Jenny Chest": ID2LocationData("Sweetwater Coast Caves N", 107),
    # 200: Fancy Ruins

    # 300: Star Woods

    # 400: Slippery Slope

    # 500: Pepperpain

    # 600: Frozen Court

    # 700: Lonely Road

    # 800: Pillow Fort
    "Pillow Fort - Treasure Chest": ID2LocationData("Pillow Fort I", 800, "Dungeons"),
    "Pillow Fort - Shellbun Nest Key": ID2LocationData("Pillow Fort J", 801, "Dungeons"),
    "Pillow Fort - Crayon Chest": ID2LocationData("Pillow Fort G", 802, "Dungeons"),
    "Pillow Fort - Safety Jenny Gate Key": ID2LocationData("Pillow Fort E", 803, "Dungeons"),
    "Pillow Fort - Boss Reward Chest": ID2LocationData("Pillow Fort C", 804, "Dungeons"),
    # 900: Sand Castle
    "Sand Castle - Crayon Chest": ID2LocationData("Sand Castle G", 900, "Dungeons"),
    "Sand Castle - Orbiting Balls Key": ID2LocationData("Sand Castle I", 901, "Dungeons"),
    "Sand Castle - Spikebun Dunes Key": ID2LocationData("Sand Castle D", 902, "Dungeons"),
    "Sand Castle - Treasure Chest": ID2LocationData("Sand Castle J", 904, "Dungeons"),
    "Sand Castle - Boss Reward Chest": ID2LocationData("Sand Castle A", 905, "Dungeons")
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
}

location_name_to_id: Dict[str, int] = {name: location_base_id + data.location_id_offset for name, data in location_table.items}

location_name_groups: Dict[str, Set[str]] = {}
for loc_name, loc_data in location_table.items():
    loc_group_name = loc_name.split(" - ", 1)[0]
    location_name_groups.setdefault(loc_group_name, set()).add(loc_name)
    if loc_data.location_group:
        location_name_groups.setdefault(loc_data.location_group, set()).add(loc_name)
