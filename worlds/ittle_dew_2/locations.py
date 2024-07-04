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
    "Fancy Ruins Caves - Two Torches Chest": ID2LocationData(rname.frc_a.value, 200),
    "Fancy Ruins Caves - Numbered Torches Chest": ID2LocationData(rname.frc_b.value, 201),
    "Fancy Ruins Caves - Two Crystals Chest": ID2LocationData(rname.frc_c.value, 202),
    "Fancy Ruins Caves - Big Ogler Combat Chest": ID2LocationData(rname.frc_d.value, 203),
    "Fancy Ruins Caves - Hint Turnip Chest": ID2LocationData(rname.frc_g.value, 204),
    "Fancy Ruins Caves - Rhythm Pillars Chest": ID2LocationData(rname.frc_h.value, 205),
    "Fancy Ruins Caves - Teleporter Puzzle Chest": ID2LocationData(rname.frc_i.value, 206),
    "Fancy Ruins Caves - Four Oglers Combat Chest": ID2LocationData(rname.frc_j.value, 207),
    "Fancy Ruins Caves - Spike Path Chest": ID2LocationData(rname.frc_k.value, 208),
    "Fancy Ruins Caves - Hiding Hermit Chest": ID2LocationData(rname.frc_l.value, 209),
    "Fancy Ruins Caves - Ice and Torch Chest": ID2LocationData(rname.frc_m.value, 210),
    # 300: Star Woods
    "Star Woods - Turnip Combat Chest": ID2LocationData(rname.swc_a.value, 300),
    "Star Woods - Barrel Blast Chest": ID2LocationData(rname.swc_b.value, 301),
    "Star Woods - Four Crystals Chest": ID2LocationData(rname.swc_c.value, 302),
    "Star Woods - Sleeping Safety Jenny Chest": ID2LocationData(rname.swc_d.value, 303),
    "Star Woods - Rotating Spikes Chest": ID2LocationData(rname.swc_f.value, 304),
    "Star Woods - Number Tiles Chest": ID2LocationData(rname.swc_g.value, 305),
    "Star Woods - Whirlwind Chest": ID2LocationData(rname.swc_h.value, 306),
    "Star Woods - Magic Crystal Chest": ID2LocationData(rname.swc_i.value, 307),
    "Star Woods - Artist Turnip Chest": ID2LocationData(rname.swc_j.value, 308),
    "Star Woods - Hint Bee Chest": ID2LocationData(rname.swc_k.value, 309),
    "Star Woods - Extinguish Flames Chest": ID2LocationData(rname.swc_o.value, 310),
    # 400: Slippery Slope
    "Slippery Slope - Volcanic Path Chest": ID2LocationData(rname.ssc_a.value, 400),
    "Slippery Slope - Ice and Barrels Chest": ID2LocationData(rname.ssc_b.value, 401),
    "Slippery Slope - Eight Crystals Chest": ID2LocationData(rname.ssc_d.value, 402),
    "Slippery Slope - Forgetful Jennies Chest": ID2LocationData(rname.ssc_e.value, 403),
    "Slippery Slope - Push the Crystals Chest": ID2LocationData(rname.ssc_f.value, 404),
    "Slippery Slope - Exhausted Turnip Chest": ID2LocationData(rname.ssc_g.value, 405),
    "Slippery Slope - Bee Nest Combat Chest": ID2LocationData(rname.ssc_i.value, 406),
    "Slippery Slope - Pushable Fan Chest": ID2LocationData(rname.ssc_j.value, 407),
    "Slippery Slope - Moving Crystals Chest": ID2LocationData(rname.ssc_k.value, 408),
    "Slippery Slope - Shark House": ID2LocationData(rname.ssc_l.value, 409),
    # 500: Pepperpain
    "Pepperpain Caves - Cowbun Combat Chest": ID2LocationData(rname.ppc_a.value, 500),
    "Pepperpain Caves - Brutus Combat Chest": ID2LocationData(rname.ppc_b.value, 501),
    "Pepperpain Caves - Torch Disappearing Path Chest": ID2LocationData(rname.ppc_f.value, 502),
    "Pepperpain Caves - Spiky Hint Bee Chest": ID2LocationData(rname.ppc_g.value, 503),
    "Pepperpain Caves - Cannon Path Chest": ID2LocationData(rname.ppc_h.value, 504),
    "Pepperpain Caves - Volcano Trail Chest": ID2LocationData(rname.ppc_j.value, 505),
    "Pepperpain Caves - Barrel Hint Bee Chest": ID2LocationData(rname.ppc_k.value, 506),
    "Pepperpain Caves - Haunted Guns Chest": ID2LocationData(rname.ppc_l.value, 507),
    "Pepperpain Caves - Buzzsaw Path Chest": ID2LocationData(rname.ppc_o.value, 508),
    "Pepperpain Caves - Number Tiles Chest": ID2LocationData(rname.ppc_p.value, 509),
    "Pepperpain Caves - Pacifist Brute Chest": ID2LocationData(rname.ppc_u.value, 510),
    # 600: Frozen Court
    "Frozen Court Caves - Bushfire Chest": ID2LocationData(rname.fcc_a.value, 600),
    "Frozen Court Caves - Cannon Spinner Chest": ID2LocationData(rname.fcc_b.value, 601),
    "Frozen Court Caves - Mimicbuns Combat Chest": ID2LocationData(rname.fcc_c.value, 602),
    "Frozen Court Caves - Teleporter Maze Chest": ID2LocationData(rname.fcc_e.value, 603),
    "Frozen Court Caves - Chilly Roger Combat Chest": ID2LocationData(rname.fcc_f.value, 604),
    "Frozen Court Caves - Rickety Bridge Chest": ID2LocationData(rname.fcc_h.value, 605),
    "Frozen Court Caves - Titans Combat Chest": ID2LocationData(rname.fcc_i.value, 606),
    "Frozen Court Caves - Crystal Path Chest": ID2LocationData(rname.fcc_j.value, 607),
    "Frozen Court Caves - Teleporter Grate Chest": ID2LocationData(rname.fcc_k.value, 608),
    "Frozen Court Caves - Hint Hermit Chest": ID2LocationData(rname.fcc_l.value, 609),
    # 700: Lonely Road
    "Lonely Road Caves - Timed Platforms Chest": ID2LocationData(rname.lrc_b.value, 700),
    "Lonely Road Caves - Timed Number Tiles Chest": ID2LocationData(rname.lrc_c.value, 701),
    "Lonely Road Caves - Volcano Chest": ID2LocationData(rname.lrc_d.value, 702),
    "Lonely Road Caves - Lava Fans Chest": ID2LocationData(rname.lrc_k.value, 703),
    "Lonely Road Caves - Force Turrets Chest": ID2LocationData(rname.lrc_m.value, 704),
    "Lonely Road Caves - Hint Shark Chest": ID2LocationData(rname.lrc_p.value, 705),
    "Lonely Road Caves - Teleporter Cube Chest": ID2LocationData(rname.lrc_r.value, 706),
    "Lonely Road Caves - Dark Maze Chest": ID2LocationData(rname.lrc_s.value, 707),
    "Lonely Road Caves - Block Factory": ID2LocationData(rname.lrc_t.value, 708),
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
    # 1000: Art Exhibit
    "Art Exhibit - Entry Combat Key": ID2LocationData(rname.d3_r.value, 1000, "Dungeons"),
    "Art Exhibit - Evil Easels Key": ID2LocationData(rname.d3_n.value, 1001, "Dungeons"),
    "Art Exhibit - Treasure Chest": ID2LocationData(rname.d3_l.value, 1002, "Dungeons"),
    "Art Exhibit - Crayon Chest": ID2LocationData(rname.d3_f.value, 1003, "Dungeons"),
    "Art Exhibit - Spike Floor Key": ID2LocationData(rname.d3_e.value, 1004, "Dungeons"),
    "Art Exhibit - Business Casual Man Key": ID2LocationData(rname.d3_a.value, 1005, "Dungeons"),
    "Art Exhibit - Boss Reward Chest": ID2LocationData(rname.d3_d.value, 1006, "Dungeons"),
    # 1100: Trash Cave
    "Trash Cave - Crayon Chest": ID2LocationData(rname.d4_m.value, 1100, "Dungeons"),
    "Trash Cave - Ice Barricade Key": ID2LocationData(rname.d4_n_lower.value, 1101, "Dungeons"),
    "Trash Cave - Rotnip Combat Key": ID2LocationData(rname.d4_g_left.value, 1102, "Dungeons"),
    "Trash Cave - Treasure Chest": ID2LocationData(rname.d4_d.value, 1103, "Dungeons"),
    "Trash Cave - Mimic Combat Key": ID2LocationData(rname.d4_h.value, 1104, "Dungeons"),
    "Trash Cave - Block Maze Key": ID2LocationData(rname.d4_e.value, 1105, "Dungeons"),
    "Trash Cave - Boss Reward Chest": ID2LocationData(rname.d4_b.value, 1106, "Dungeons"),
    # 1200: Flooded Basement
    "Flooded Basement - Portal Cube Key": ID2LocationData(rname.d5_a.value, 1200, "Dungeons"),
    "Flooded Basement - Crossway Combat Key": ID2LocationData(rname.d5_l.value, 1201, "Dungeons"),
    "Flooded Basement - Land Sharks Key": ID2LocationData(rname.d5_u.value, 1202, "Dungeons"),
    "Flooded Basement - Treasure Chest": ID2LocationData(rname.d5_h.value, 1203, "Dungeons"),
    "Flooded Basement - Crayon Chest": ID2LocationData(rname.d5_g.value, 1204, "Dungeons"),
    "Flooded Basement - Keeled Fishbun Key": ID2LocationData(rname.d5_r.value, 1205, "Dungeons"),
    "Flooded Basement - Number Blocks Key": ID2LocationData(rname.d5_m.value, 1206, "Dungeons"),
    "Flooded Basement - Boss Reward Chest": ID2LocationData(rname.d5_c.value, 1207, "Dungeons"),
    # 1300: Potassium Mines
    "Potassium Mines - Hub Room Key": ID2LocationData(rname.d6_m.value, 1300, "Dungeons"),
    "Potassium Mines - South conveyor Key": ID2LocationData(rname.d6_t.value, 1301, "Dungeons"),
    "Potassium Mines - Crayon Chest": ID2LocationData(rname.d6_h.value, 1302, "Dungeons"),
    "Potassium Mines - West Minecart Track Key": ID2LocationData(rname.d6_l.value, 1303, "Dungeons"),
    "Potassium Mines - Number Tiles Key": ID2LocationData(rname.d6_n.value, 1304, "Dungeons"),
    "Potassium Mines - Treasure Chest": ID2LocationData(rname.d6_j.value, 1305, "Dungeons"),
    "Potassium Mines - Ice Tutorial Key": ID2LocationData(rname.d6_d.value, 1306, "Dungeons"),
    "Potassium Mines - Boss Reward Chest": ID2LocationData(rname.d6_a.value, 1307, "Dungeons"),
    # 1400: Boiling Grave
    "Boiling Grave - Skullnips Combat Key": ID2LocationData(rname.d7_t.value, 1400, "Dungeons"),
    "Boiling Grave - Titans Combat Key": ID2LocationData(rname.d7_z.value, 1401, "Dungeons"),
    "Boiling Grave - Treasure Chest": ID2LocationData(rname.d7_w.value, 1402, "Dungeons"),
    "Boiling Grave - Roll Pillars Key": ID2LocationData(rname.d7_o.value, 1403, "Dungeons"),
    "Boiling Grave - Royal Tomb Key": ID2LocationData(rname.d7_k.value, 1404, "Dungeons"),
    "Boiling Grave - Crayon Chest": ID2LocationData(rname.d7_b.value, 1405, "Dungeons"),
    "Boiling Grave - Chilly Roger Combat Key": ID2LocationData(rname.d7_d.value, 1406, "Dungeons"),
    "Boiling Grave - Boss Reward Chest": ID2LocationData(rname.d7_e.value, 1407, "Dungeons"),
    # 1500: Grand Library
    "Grand Library - Treasure Chest": ID2LocationData(rname.d8_g.value, 1500, "Dungeons"),
    "Grand Library - Crayon Chest": ID2LocationData(rname.d8_aa.value, 1501, "Dungeons"),
    "Grand Library - Patient Key": ID2LocationData(rname.d8_ac.value, 1502, "Dungeons"),
    "Grand Library - Hidden Key": ID2LocationData(rname.d8_t.value, 1503, "Dungeons"),
    "Grand Library - Fighter's Combat Key": ID2LocationData(rname.d8_ad.value, 1504, "Dungeons"),
    "Grand Library - Storied Key": ID2LocationData(rname.d8_ae.value, 1505, "Dungeons"),
    "Grand Library - Delayed Key": ID2LocationData(rname.d8_u.value, 1506, "Dungeons"),
    "Grand Library - Carrot Lobotomy Key": ID2LocationData(rname.d8_ab.value, 1507, "Dungeons"),
    "Grand Library - Crystals and Buttons Key": ID2LocationData(rname.d8_q.value, 1508, "Dungeons"),
    "Grand Library - Hexrot Combat Key": ID2LocationData(rname.d8_a.value, 1509, "Dungeons"),
    "Grand Library - Boss Key Chest": ID2LocationData(rname.d8_e.value, 1510, "Dungeons"),
    "Grand Library - Boss Reward Chest": ID2LocationData(rname.d8_rewards.value, 1511, "Dungeons"),
    "Grand Library - Extra Boss Reward Chest": ID2LocationData(rname.d8_rewards.value, 1512, "Dungeons"),
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
    "Autumn Climb - Chest": ID2LocationData(rname.autumn_climb.value, 2500, "Portal Worlds"),
    "The Vault - Chest": ID2LocationData(rname.the_vault_b_center.value, 2501, "Portal Worlds"),
    "Painful Plain - Chest": ID2LocationData(rname.painful_plain.value, 2502, "Portal Worlds"),
    "Farthest Shore - Chest": ID2LocationData(rname.farthest_shore.value, 2503, "Portal Worlds"),
    "Scrap Yard - Chest": ID2LocationData(rname.scrap_yard_a.value, 2504, "Portal Worlds"),
    "Brutal Oasis - Chest": ID2LocationData(rname.brutal_oasis.value, 2505, "Portal Worlds"),
    "Former Colossus - Chest": ID2LocationData(rname.former_colossus_end.value, 2506, "Portal Worlds"),
    "Sand Crucible - Chest": ID2LocationData(rname.sand_crucible_a.value, 2507, "Portal Worlds"),
    "Ocean Castle - Chest": ID2LocationData(rname.ocean_castle.value, 2508, "Portal Worlds"),
    "Promenade Path - Chest": ID2LocationData(rname.promenade_path.value, 2509, "Portal Worlds"),
    "Maze of Steel - Chest": ID2LocationData(rname.maze_of_steel_a_left.value, 2510, "Portal Worlds"),
    "Wall of Text - Chest": ID2LocationData(rname.wall_of_text_b.value, 2511, "Portal Worlds"),
    "Lost City of Avlopp - Chest": ID2LocationData(rname.lost_city_c.value, 2512, "Portal Worlds"),
    "Northern End - Chest": ID2LocationData(rname.northern_end_f.value, 2513, "Portal Worlds"),
    "Moon Garden - Chest": ID2LocationData(rname.moon_garden_north.value, 2514, "Portal Worlds"),
    
    # 2600+: Misc Locations
    "Ludo City - Chest": ID2LocationData(rname.ludo_city.value, 2600, "Super Secrets"),
    "Bad Dream - Card": ID2LocationData(rname.bad_dream.value, 2602, "Super Secrets")
}

location_name_to_id: Dict[str, int] = {name: location_base_id + data.location_id_offset for name, data in location_table.items()}

location_name_groups: Dict[str, Set[str]] = {}
for loc_name, loc_data in location_table.items():
    loc_group_name = loc_name.split(" - ", 1)[0]
    location_name_groups.setdefault(loc_group_name, set()).add(loc_name)
    if loc_data.location_group:
        location_name_groups.setdefault(loc_data.location_group, set()).add(loc_name)
