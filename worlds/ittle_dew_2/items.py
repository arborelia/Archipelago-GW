from itertools import groupby
from typing import Dict, List, Set, NamedTuple
from BaseClasses import ItemClassification, Item
from names_items import ItemNames as iname

class ID2Item(Item):
    game: str = "Ittle Dew 2"

class ID2ItemData(NamedTuple):
    classification: ItemClassification
    quantity_in_item_pool: int
    item_id_offset: int
    item_group: str = ""


item_base_id = 238492834

item_table: Dict[str, ID2ItemData] = {
    iname.melee: ID2ItemData(ItemClassification.progression, 3, 0, "Major Items"),
    iname.force: ID2ItemData(ItemClassification.progression, 3, 1, "Major Items"),
    iname.dynamite: ID2ItemData(ItemClassification.progression, 3, 2, "Major Items"),
    iname.ice: ID2ItemData(ItemClassification.progression, 3, 3, "Major Items"),
    iname.chain: ID2ItemData(ItemClassification.progression, 3, 4, "Major Items"),
    # Upgrades can substitute for two progressive weapons of the same type to prevent dupes
    iname.force_upgrade: ID2ItemData(ItemClassification.useful, 2, 5, "Upgrades"),
    iname.dynamite_upgrade: ID2ItemData(ItemClassification.useful, 2, 6, "Upgrades"),
    iname.ice_upgrade: ID2ItemData(ItemClassification.useful, 2, 7, "Upgrades"),
    iname.chain_upgrade: ID2ItemData(ItemClassification.useful, 2, 8, "Upgrades"),
    iname.roll: ID2ItemData(ItemClassification.progression, 1, 9, "Major Items"),
    iname.tracker: ID2ItemData(ItemClassification.useful, 3, 10, "Minor Items"),
    iname.headband: ID2ItemData(ItemClassification.useful, 3, 11, "Minor Items"),
    iname.amulet: ID2ItemData(ItemClassification.useful, 3, 12, "Minor Items"),
    iname.tome: ID2ItemData(ItemClassification.useful, 3, 13, "Minor Items"),
    iname.shard: ID2ItemData(ItemClassification.progression, 36, 14, "Collectables"),
    iname.f_key: ID2ItemData(ItemClassification.progression, 4, 15, "Collectables"),
    iname.lockpick: ID2ItemData(ItemClassification.useful, 12, 16, "Minor Items"),
    iname.crayon: ID2ItemData(ItemClassification.useful, 20, 17, "Minor Items"),
    iname.scroll_cave: ID2ItemData(ItemClassification.filler, 10, 18, "Bonus Items"),
    iname.scroll_portal: ID2ItemData(ItemClassification.filler, 10, 19, "Bonus Items"),
    iname.heart_yellow: ID2ItemData(ItemClassification.filler, 10, 20, "Bonus Items"),
    iname.d1_key: ID2ItemData(ItemClassification.progression, 2, 22, "Keys"),
    iname.d1_keyring: ID2ItemData(ItemClassification.progression, 1, 23, "Key Rings"),
    iname.d2_key: ID2ItemData(ItemClassification.progression, 2, 24, "Keys"),
    iname.d2_keyring: ID2ItemData(ItemClassification.progression, 1, 25, "Key Rings"),
    iname.d3_key: ID2ItemData(ItemClassification.progression, 4, 26, "Keys"),
    iname.d3_keyring: ID2ItemData(ItemClassification.progression, 1, 27, "Key Rings"),
    iname.d4_key: ID2ItemData(ItemClassification.progression, 4, 28, "Keys"),
    iname.d4_keyring: ID2ItemData(ItemClassification.progression, 1, 29, "Key Rings"),
    iname.d5_key: ID2ItemData(ItemClassification.progression, 5, 30, "Keys"),
    iname.d5_keyring: ID2ItemData(ItemClassification.progression, 1, 31, "Key Rings"),
    iname.d6_key: ID2ItemData(ItemClassification.progression, 5, 32, "Keys"),
    iname.d6_keyring: ID2ItemData(ItemClassification.progression, 1, 33, "Key Rings"),
    iname.d7_key: ID2ItemData(ItemClassification.progression, 5, 34, "Keys"),
    iname.d7_keyring: ID2ItemData(ItemClassification.progression, 1, 35, "Key Rings"),
    iname.d8_key: ID2ItemData(ItemClassification.progression, 8, 36, "Keys"),
    iname.d8_keyring: ID2ItemData(ItemClassification.progression, 1, 37, "Key Rings"),
    iname.s1_key: ID2ItemData(ItemClassification.progression, 3, 38, "Keys"),
    iname.s1_keyring: ID2ItemData(ItemClassification.progression, 1, 39, "Key Rings"),
    iname.s2_key: ID2ItemData(ItemClassification.progression, 5, 40, "Keys"),
    iname.s2_keyring: ID2ItemData(ItemClassification.progression, 1, 41, "Key Rings"),
    iname.s3_key: ID2ItemData(ItemClassification.progression, 5, 42, "Keys"),
    iname.s3_keyring: ID2ItemData(ItemClassification.progression, 1, 43, "Key Rings"),
    iname.s4_key: ID2ItemData(ItemClassification.progression, 10, 44, "Keys"),
    iname.s4_keyring: ID2ItemData(ItemClassification.progression, 1, 45, "Key Rings"),
    iname.dd_key: ID2ItemData(ItemClassification.progression, 3, 46, "Keys"),
    iname.dd_keyring: ID2ItemData(ItemClassification.progression, 1, 47, "Key Rings"),
    iname.di_key: ID2ItemData(ItemClassification.progression, 4, 48, "Keys"),
    iname.di_keyring: ID2ItemData(ItemClassification.progression, 1, 49, "Key Rings"),
    iname.dfc_key: ID2ItemData(ItemClassification.progression, 4, 50, "Keys"),
    iname.dfc_keyring: ID2ItemData(ItemClassification.progression, 1, 51, "Key Rings"),
    iname.da_key: ID2ItemData(ItemClassification.progression, 4, 52, "Keys"),
    iname.da_keyring: ID2ItemData(ItemClassification.progression, 1, 53, "Key Rings"),
    iname.outfit_jenny: ID2ItemData(ItemClassification.filler, 1, 54, "Outfits"),
    iname.outfit_swimsuit: ID2ItemData(ItemClassification.filler, 1, 55, "Outfits"),
    iname.outfit_tippsie: ID2ItemData(ItemClassification.filler, 1, 56, "Outfits"),
    iname.outfit_dude: ID2ItemData(ItemClassification.filler, 1, 57, "Outfits"),
    iname.outfit_tiger: ID2ItemData(ItemClassification.filler, 1, 58, "Outfits"),
    iname.outfit_id: ID2ItemData(ItemClassification.filler, 1, 59, "Outfits"),
    iname.outfit_delinquint: ID2ItemData(ItemClassification.filler, 1, 60, "Outfits"),
    iname.outfit_berry: ID2ItemData(ItemClassification.filler, 1, 61, "Outfits"),
    iname.outfit_apa: ID2ItemData(ItemClassification.filler, 1, 62, "Outfits"),
    iname.outfit_that_guy: ID2ItemData(ItemClassification.filler, 1, 63, "Outfits"),
    iname.loot: ID2ItemData(ItemClassification.filler, 1 , 64, "Major Items"),
    iname.fake_efcs: ID2ItemData(ItemClassification.progression, 1, 65, "Major Items"),
    iname.card_fishbun: ID2ItemData(ItemClassification.filler, 1, 100, "Cards"),
    iname.card_bee: ID2ItemData(ItemClassification.filler, 1, 101, "Cards"),
    iname.card_safety: ID2ItemData(ItemClassification.filler, 1, 102, "Cards"),
    iname.card_shellbun: ID2ItemData(ItemClassification.filler, 1, 103, "Cards"),
    iname.card_spikebun: ID2ItemData(ItemClassification.filler, 1, 104, "Cards"),
    iname.card_gate: ID2ItemData(ItemClassification.filler, 1, 105, "Cards"),
    iname.card_snake: ID2ItemData(ItemClassification.filler, 1, 106, "Cards"),
    iname.card_mimic: ID2ItemData(ItemClassification.filler, 1, 107, "Cards"),
    iname.card_ogler: ID2ItemData(ItemClassification.filler, 1, 108, "Cards"),
    iname.card_hyperdusa: ID2ItemData(ItemClassification.filler, 1, 109, "Cards"),
    iname.card_easel: ID2ItemData(ItemClassification.filler, 1, 110, "Cards"),
    iname.card_warnip: ID2ItemData(ItemClassification.filler, 1, 111, "Cards"),
    iname.card_octacle: ID2ItemData(ItemClassification.filler, 1, 112, "Cards"),
    iname.card_rotnip: ID2ItemData(ItemClassification.filler, 1, 113, "Cards"),
    iname.card_bees: ID2ItemData(ItemClassification.filler, 1, 114, "Cards"),
    iname.card_volcano: ID2ItemData(ItemClassification.filler, 1, 115, "Cards"),
    iname.card_shark: ID2ItemData(ItemClassification.filler, 1, 116, "Cards"),
    iname.card_swimmy: ID2ItemData(ItemClassification.filler, 1, 117, "Cards"),
    iname.card_bunboy: ID2ItemData(ItemClassification.filler, 1, 118, "Cards"),
    iname.card_spectre: ID2ItemData(ItemClassification.filler, 1, 119, "Cards"),
    iname.card_brutus: ID2ItemData(ItemClassification.filler, 1, 120, "Cards"),
    iname.card_jelly: ID2ItemData(ItemClassification.filler, 1, 121, "Cards"),
    iname.card_skullnip: ID2ItemData(ItemClassification.filler, 1, 122, "Cards"),
    iname.card_slayer: ID2ItemData(ItemClassification.filler, 1, 123, "Cards"),
    iname.card_titan: ID2ItemData(ItemClassification.filler, 1, 124, "Cards"),
    iname.card_chilly: ID2ItemData(ItemClassification.filler, 1, 125, "Cards"),
    iname.card_flower: ID2ItemData(ItemClassification.filler, 1, 126, "Cards"),
    iname.card_hexrot: ID2ItemData(ItemClassification.filler, 1, 127, "Cards"),
    iname.card_mole: ID2ItemData(ItemClassification.filler, 1, 128, "Cards"),
    iname.card_bun: ID2ItemData(ItemClassification.filler, 1, 129, "Cards"),
    iname.card_cat: ID2ItemData(ItemClassification.filler, 1, 130, "Cards"),
    iname.card_mermaid: ID2ItemData(ItemClassification.filler, 1, 131, "Cards"),
    iname.card_berry: ID2ItemData(ItemClassification.filler, 1, 132, "Cards"),
    iname.card_mapman: ID2ItemData(ItemClassification.filler, 1, 133, "Cards"),
    iname.card_cyber: ID2ItemData(ItemClassification.filler, 1, 134, "Cards"),
    iname.card_biadlo: ID2ItemData(ItemClassification.filler, 1, 135, "Cards"),
    iname.card_lenny: ID2ItemData(ItemClassification.filler, 1, 136, "Cards"),
    iname.card_passel: ID2ItemData(ItemClassification.filler, 1, 137, "Cards"),
    iname.card_tippsie: ID2ItemData(ItemClassification.filler, 1, 138, "Cards"),
    iname.card_ittle: ID2ItemData(ItemClassification.filler, 1, 139, "Cards"),
    iname.card_fly: ID2ItemData(ItemClassification.filler, 1, 140, "Cards")
}

item_name_to_id: Dict[str, int] = {name: item_base_id + data.item_id_offset for name, data in item_table.items()}

filler_items: List[str] = [name for name, data in item_table.items() if data.classification == ItemClassification.filler]


def get_item_group(item_name: str) -> str:
    return item_table[item_name].item_group


item_name_groups: Dict[str, Set[str]] = {
    group: set(item_names) for group, item_names in groupby(sorted(item_table, key=get_item_group), get_item_group) if group != ""
}

# extra groups for the purpose of aliasing items
extra_groups: Dict[str, Set[str]] = {
    "Melee": {"Progressive Melee"},
    "Stick": {"Progressive Melee"},
    "Fire Sword": {"Progressive Melee"},
    "Sword": {"Progressive Melee"},
    "Fire Mace": {"Progressive Melee"},
    "Mace": {"Progressive Melee"},
    "Force": {"Progressive Force Wand", "Force Wand Upgrade"},
    "Wand": {"Progressive Force Wand", "Force Wand Upgrade"},
    "Force Wand": {"Progressive Force Wand", "Force Wand Upgrade"},
    "Dynamite": {"Progressive Dynamite", "Dynamite Upgrade"},
    "Ice": {"Progressive Ice Ring", "Ice Ring Upgrade"},
    "Ring": {"Progressive Ice Ring", "Ice Ring Upgrade"},
    "Ice Ring": {"Progressive Ice Ring", "Ice Ring Upgrade"},
    "Chain": {"Progressive Chain", "Chain Upgrade"},
    "Tracker": {"Progressive Tracker"},
    "Headband": {"Progressive Headband"},
    "Amulet": {"Progressive Amulet"},
    "Tome": {"Progressive Tome"},
    "Shard": {"Secret Shard"},
    "Loot": {"Big Old Pile of Loot"}
}

item_name_groups.update(extra_groups)
