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
    "Roll": ID2ItemData(ItemClassification.progression, 1, 9),
    "Progressive Tracker": ID2ItemData(ItemClassification.useful, 3, 10, "Auxillery Items"),
    "Progressive Headband": ID2ItemData(ItemClassification.useful, 3, 11, "Auxillery Items"),
    "Progressive Amulet": ID2ItemData(ItemClassification.useful, 3, 12, "Auxillery Items"),
    "Progressive Tome": ID2ItemData(ItemClassification.useful, 3, 13, "Auxillery Items"),
    "Secret Shard": ID2ItemData(ItemClassification.progression, 36, 14),
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
    "Jenny Dew Outfit": ID2ItemData(ItemClassification.filler, 1, 54, "Outfits"),
    "Swimsuit Outfit": ID2ItemData(ItemClassification.filler, 1, 55, "Outfits"),
    "Tippsie Outfit": ID2ItemData(ItemClassification.filler, 1, 56, "Outfits"),
    "Little Dude Outfit": ID2ItemData(ItemClassification.filler, 1, 57, "Outfits"),
    "Tiger Jenny Outfit": ID2ItemData(ItemClassification.filler, 1, 58, "Outfits"),
    "ID1 Outfit": ID2ItemData(ItemClassification.filler, 1, 59, "Outfits"),
    "Delinquint Outfit": ID2ItemData(ItemClassification.filler, 1, 60, "Outfits"),
    "Jenny Berry Outfit": ID2ItemData(ItemClassification.filler, 1, 61, "Outfits"),
    "Apathetic Frog Outfit": ID2ItemData(ItemClassification.filler, 1, 62, "Outfits"),
    "That Guy Outfit": ID2ItemData(ItemClassification.filler, 1, 63, "Outfits"),
    "Big Old Pile of Loot": ID2ItemData(ItemClassification.filler, 1 , 64)
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
