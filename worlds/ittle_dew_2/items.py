from itertools import groupby
from typing import Dict, List, Set, NamedTuple
from BaseClasses import ItemClassification


class ID2ItemData(NamedTuple):
    classification: ItemClassification
    quantity_in_item_pool: int
    item_id_offset: int
    item_group: str = ""


item_base_id = 238492834

item_table: Dict[str, ID2ItemData] = {
    "Progressive Melee": ID2ItemData(ItemClassification.progression, 3, 0, "Weapons"),
    "Progressive Force Wand": ID2ItemData(ItemClassification.progression, 3, 1, "Weapons"),
    "Progressive Dynamite": ID2ItemData(ItemClassification.progression, 3, 2, "Weapons"),
    "Progressive Ice Ring": ID2ItemData(ItemClassification.progression, 3, 3, "Weapons"),
    "Progressive Chain": ID2ItemData(ItemClassification.progression, 3, 4, "Auxillery Items"),
    # Upgrades can substitute for two progressive weapons of the same type to prevent dupes
    "Force Wand Upgrade": ID2ItemData(ItemClassification.useful, 2, 5, "Upgrades"),
    "Dynamite Upgrade": ID2ItemData(ItemClassification.useful, 2, 6, "Upgrades"),
    "Ice Ring Upgrade": ID2ItemData(ItemClassification.useful, 2, 7, "Upgrades"),
    "Chain Upgrade": ID2ItemData(ItemClassification.useful, 2, 8, "Upgrades"),
    "Roll": ID2ItemData(ItemClassification.progression, 1, 9, "Roll"),
    "Progressive Tracker": ID2ItemData(ItemClassification.useful, 3, 10, "Auxillery Items"),
    "Progressive Headband": ID2ItemData(ItemClassification.useful, 3, 11, "Auxillery Items"),
    "Progressive Amulet": ID2ItemData(ItemClassification.useful, 3, 12, "Auxillery Items"),
    "Progressive Tome": ID2ItemData(ItemClassification.useful, 3, 13, "Auxillery Items"),
    "Secret Shard": ID2ItemData(ItemClassification.progression, 36, 14, "Shards"),
    "Forbidden Key": ID2ItemData(ItemClassification.progression, 4, 15, "Auxillery Items"),
    "Lockpick": ID2ItemData(ItemClassification.useful, 12, 16, "Auxillery Items"),
    "Crayon": ID2ItemData(ItemClassification.useful, 20, 17, "Auxillery Items"),
    "Cave Scroll": ID2ItemData(ItemClassification.filler, 10, 18, "Bonus Items"),
    "Portal World Scroll": ID2ItemData(ItemClassification.filler, 10, 19, "Bonus Items"),
    "Yellow Heart": ID2ItemData(ItemClassification.filler, 10, 20, "Bonus Items"),
    "Card": ID2ItemData(ItemClassification.filler, 41, 21, "Bonus Items"),
    "Pillow Fort Key": ID2ItemData(ItemClassification.progression, 2, 22, "Keys"),
    "Pillow Fort Key Ring": ID2ItemData(ItemClassification.progression, 1, 23, "Key Rings"),
    "Sand Castle Key": ID2ItemData(ItemClassification.progression, 2, 24, "Keys"),
    "Sand Castle Key Ring": ID2ItemData(ItemClassification.progression, 1, 25, "Key Rings"),
    "Art Gallery Key": ID2ItemData(ItemClassification.progression, 4, 26, "Keys"),
    "Art Gallery Key Ring": ID2ItemData(ItemClassification.progression, 1, 27, "Key Rings"),
    "Trash Cave Key": ID2ItemData(ItemClassification.progression, 4, 28, "Keys"),
    "Trash Cave Key Ring": ID2ItemData(ItemClassification.progression, 1, 29, "Key Rings"),
    "Flooded Basement Key": ID2ItemData(ItemClassification.progression, 5, 30, "Keys"),
    "Flooded Basement Key Ring": ID2ItemData(ItemClassification.progression, 1, 31, "Key Rings"),
    "Potassium Mines Key": ID2ItemData(ItemClassification.progression, 5, 32, "Keys"),
    "Potassium Mines Key Ring": ID2ItemData(ItemClassification.progression, 1, 33, "Key Rings"),
    "Boiling Grave Key": ID2ItemData(ItemClassification.progression, 5, 34, "Keys"),
    "Boiling Grave Key Ring": ID2ItemData(ItemClassification.progression, 1, 35, "Key Rings"),
    "Grand Library Key": ID2ItemData(ItemClassification.progression, 8, 36, "Keys"),
    "Grand Library Key Ring": ID2ItemData(ItemClassification.progression, 1, 37, "Key Rings"),
    "Sunken Labyrinth Key": ID2ItemData(ItemClassification.progression, 3, 38, "Keys"),
    "Sunken Labyrinth Key Ring": ID2ItemData(ItemClassification.progression, 1, 39, "Key Rings"),
    "Machine Fortress Key": ID2ItemData(ItemClassification.progression, 5, 40, "Keys"),
    "Machine Fortress Key Ring": ID2ItemData(ItemClassification.progression, 1, 41, "Key Rings"),
    "Dark Hypostyle Key": ID2ItemData(ItemClassification.progression, 5, 42, "Keys"),
    "Dark Hypostyle Key Ring": ID2ItemData(ItemClassification.progression, 1, 43, "Key Rings"),
    "Tomb of Simulacrum Key": ID2ItemData(ItemClassification.progression, 10, 44, "Keys"),
    "Tomb of Simulacrum Key Ring": ID2ItemData(ItemClassification.progression, 1, 45, "Key Rings"),
    "Syncope Key": ID2ItemData(ItemClassification.progression, 3, 46, "Keys"),
    "Syncope Key Ring": ID2ItemData(ItemClassification.progression, 1, 47, "Key Rings"),
    "Bottomless Tower Key": ID2ItemData(ItemClassification.progression, 4, 48, "Keys"),
    "Bottomless Tower Key Ring": ID2ItemData(ItemClassification.progression, 1, 49, "Key Rings"),
    "Antigram Key": ID2ItemData(ItemClassification.progression, 4, 50, "Keys"),
    "Antigram Key Ring": ID2ItemData(ItemClassification.progression, 1, 51, "Key Rings"),
    "Quietus Key": ID2ItemData(ItemClassification.progression, 4, 52, "Keys"),
    "Quietus Key Ring": ID2ItemData(ItemClassification.progression, 1, 53, "Key Rings"),
}

fool_tiers: List[List[str]] = [
    [],
    ["Money x1", "Money x10", "Money x15", "Money x16"],
    ["Money x1", "Money x10", "Money x15", "Money x16", "Money x20"],
    ["Money x1", "Money x10", "Money x15", "Money x16", "Money x20", "Money x25", "Money x30"],
]

slot_data_item_names = [
    "Stick",
    "Sword",
    "Sword Upgrade",
    "Magic Dagger",
    "Magic Wand",
    "Magic Orb",
    "Hero's Laurels",
    "Lantern",
    "Gun",
    "Scavenger Mask",
    "Shield",
    "Dath Stone",
    "Hourglass",
    "Old House Key",
    "Fortress Vault Key",
    "Hero Relic - ATT",
    "Hero Relic - DEF",
    "Hero Relic - POTION",
    "Hero Relic - HP",
    "Hero Relic - SP",
    "Hero Relic - MP",
    "Pages 24-25 (Prayer)",
    "Pages 42-43 (Holy Cross)",
    "Pages 52-53 (Icebolt)",
    "Red Questagon",
    "Green Questagon",
    "Blue Questagon",
    "Gold Questagon",
]

item_name_to_id: Dict[str, int] = {name: item_base_id + data.item_id_offset for name, data in item_table.items()}

filler_items: List[str] = [name for name, data in item_table.items() if data.classification == ItemClassification.filler]


def get_item_group(item_name: str) -> str:
    return item_table[item_name].item_group


item_name_groups: Dict[str, Set[str]] = {
    group: set(item_names) for group, item_names in groupby(sorted(item_table, key=get_item_group), get_item_group) if group != ""
}

# extra groups for the purpose of aliasing items
extra_groups: Dict[str, Set[str]] = {
    "Laurels": {"Hero's Laurels"},
    "Orb": {"Magic Orb"},
    "Dagger": {"Magic Dagger"},
    "Wand": {"Magic Wand"},
    "Magic Rod": {"Magic Wand"},
    "Fire Rod": {"Magic Wand"},
    "Holy Cross": {"Pages 42-43 (Holy Cross)"},
    "Prayer": {"Pages 24-25 (Prayer)"},
    "Icebolt": {"Pages 52-53 (Icebolt)"},
    "Ice Rod": {"Pages 52-53 (Icebolt)"},
    "Melee Weapons": {"Stick", "Sword", "Sword Upgrade"},
    "Progressive Sword": {"Sword Upgrade"},
    "Abilities": {"Pages 24-25 (Prayer)", "Pages 42-43 (Holy Cross)", "Pages 52-53 (Icebolt)"},
    "Questagons": {"Red Questagon", "Green Questagon", "Blue Questagon", "Gold Questagon"},
    "Ladder to Atoll": {"Ladder to Ruined Atoll"},  # fuzzy matching made it hint Ladders in Well, now it won't
    "Ladders to Bell": {"Ladders to West Bell"},
    "Ladders to Well": {"Ladders in Well"},  # fuzzy matching decided ladders in well was ladders to west bell
    "Ladders in Atoll": {"Ladders in South Atoll"},
    "Ladders in Ruined Atoll": {"Ladders in South Atoll"},
}

item_name_groups.update(extra_groups)
