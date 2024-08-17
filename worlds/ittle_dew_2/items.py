from itertools import groupby
from typing import Dict, List, Set, NamedTuple, Union
from BaseClasses import ItemClassification, Item
from .names_items import ItemNames as iname


class ID2Item(Item):
    game: str = "Ittle Dew 2"


class ID2ItemData(NamedTuple):
    classification: ItemClassification
    quantity_in_item_pool: int  # 0 should be used for items not in pool by default and keys
    item_id_offset: Union[int, None]
    item_group: str = ""


item_base_id = 238492834

item_table: Dict[str, ID2ItemData] = {
    iname.melee.value: ID2ItemData(ItemClassification.progression, 3, 0, "Major Items"),
    iname.force.value: ID2ItemData(ItemClassification.progression, 3, 1, "Major Items"),
    iname.dynamite.value: ID2ItemData(ItemClassification.progression, 3, 2, "Major Items"),
    iname.ice.value: ID2ItemData(ItemClassification.progression, 3, 3, "Major Items"),
    iname.chain.value: ID2ItemData(ItemClassification.progression, 3, 4, "Major Items"),
    # Upgrades can substitute for two progressive weapons of the same type to prevent dupes
    iname.force_upgrade.value: ID2ItemData(ItemClassification.useful, 0, 5, "Upgrades"),
    iname.dynamite_upgrade.value: ID2ItemData(ItemClassification.useful, 0, 6, "Upgrades"),
    iname.ice_upgrade.value: ID2ItemData(ItemClassification.useful, 0, 7, "Upgrades"),
    iname.chain_upgrade.value: ID2ItemData(ItemClassification.useful, 0, 8, "Upgrades"),
    iname.roll.value: ID2ItemData(ItemClassification.progression, 1, 9, "Major Items"),
    iname.tracker.value: ID2ItemData(ItemClassification.useful, 3, 10, "Minor Items"),
    iname.headband.value: ID2ItemData(ItemClassification.useful, 3, 11, "Minor Items"),
    iname.amulet.value: ID2ItemData(ItemClassification.useful, 3, 12, "Minor Items"),
    iname.tome.value: ID2ItemData(ItemClassification.useful, 3, 13, "Minor Items"),
    iname.shard.value: ID2ItemData(ItemClassification.progression | ItemClassification.useful, 36, 14, "Major Items"),
    iname.f_key.value: ID2ItemData(ItemClassification.progression, 4, 15, "Major Items"),
    iname.lockpick.value: ID2ItemData(ItemClassification.useful, 12, 16, "Minor Items"),
    iname.crayon.value: ID2ItemData(ItemClassification.useful, 20, 17, "Minor Items"),
    # iname.scroll_cave.value: ID2ItemData(ItemClassification.filler, 0, 18, "Bonus Items"),
    # iname.scroll_portal.value: ID2ItemData(ItemClassification.filler, 0, 19, "Bonus Items"),
    iname.heart_yellow.value: ID2ItemData(ItemClassification.filler, 0, 20, "Bonus Items"),
    iname.raft.value: ID2ItemData(ItemClassification.progression, 8, 21, "Major Items"),
    iname.d1_key.value: ID2ItemData(ItemClassification.progression, 0, 22, "Keys"),
    iname.d1_keyring.value: ID2ItemData(ItemClassification.progression, 0, 23, "Key Rings"),
    iname.d2_key.value: ID2ItemData(ItemClassification.progression, 0, 24, "Keys"),
    iname.d2_keyring.value: ID2ItemData(ItemClassification.progression, 0, 25, "Key Rings"),
    iname.d3_key.value: ID2ItemData(ItemClassification.progression, 0, 26, "Keys"),
    iname.d3_keyring.value: ID2ItemData(ItemClassification.progression, 0, 27, "Key Rings"),
    iname.d4_key.value: ID2ItemData(ItemClassification.progression, 0, 28, "Keys"),
    iname.d4_keyring.value: ID2ItemData(ItemClassification.progression, 0, 29, "Key Rings"),
    iname.d5_key.value: ID2ItemData(ItemClassification.progression, 0, 30, "Keys"),
    iname.d5_keyring.value: ID2ItemData(ItemClassification.progression, 0, 31, "Key Rings"),
    iname.d6_key.value: ID2ItemData(ItemClassification.progression, 0, 32, "Keys"),
    iname.d6_keyring.value: ID2ItemData(ItemClassification.progression, 0, 33, "Key Rings"),
    iname.d7_key.value: ID2ItemData(ItemClassification.progression, 0, 34, "Keys"),
    iname.d7_keyring.value: ID2ItemData(ItemClassification.progression, 0, 35, "Key Rings"),
    iname.d8_key.value: ID2ItemData(ItemClassification.progression, 0, 36, "Keys"),
    iname.d8_keyring.value: ID2ItemData(ItemClassification.progression, 0, 37, "Key Rings"),
    iname.s1_key.value: ID2ItemData(ItemClassification.progression, 0, 38, "Keys"),
    iname.s1_keyring.value: ID2ItemData(ItemClassification.progression, 0, 39, "Key Rings"),
    iname.s2_key.value: ID2ItemData(ItemClassification.progression, 0, 40, "Keys"),
    iname.s2_keyring.value: ID2ItemData(ItemClassification.progression, 0, 41, "Key Rings"),
    iname.s3_key.value: ID2ItemData(ItemClassification.progression, 0, 42, "Keys"),
    iname.s3_keyring.value: ID2ItemData(ItemClassification.progression, 0, 43, "Key Rings"),
    iname.s4_key.value: ID2ItemData(ItemClassification.progression, 0, 44, "Keys"),
    iname.s4_keyring.value: ID2ItemData(ItemClassification.progression, 0, 45, "Key Rings"),
    iname.dd_key.value: ID2ItemData(ItemClassification.progression, 0, 46, "Keys"),
    iname.dd_keyring.value: ID2ItemData(ItemClassification.progression, 0, 47, "Key Rings"),
    iname.di_key.value: ID2ItemData(ItemClassification.progression, 0, 48, "Keys"),
    iname.di_keyring.value: ID2ItemData(ItemClassification.progression, 0, 49, "Key Rings"),
    iname.dfc_key.value: ID2ItemData(ItemClassification.progression, 0, 50, "Keys"),
    iname.dfc_keyring.value: ID2ItemData(ItemClassification.progression, 0, 51, "Key Rings"),
    iname.da_key.value: ID2ItemData(ItemClassification.progression, 0, 52, "Keys"),
    iname.da_keyring.value: ID2ItemData(ItemClassification.progression, 0, 53, "Key Rings"),
    iname.outfit_jenny.value: ID2ItemData(ItemClassification.useful, 1, 54, "Outfits"),
    iname.outfit_swimsuit.value: ID2ItemData(ItemClassification.useful, 1, 55, "Outfits"),
    iname.outfit_tippsie.value: ID2ItemData(ItemClassification.useful, 1, 56, "Outfits"),
    iname.outfit_dude.value: ID2ItemData(ItemClassification.useful, 1, 57, "Outfits"),
    iname.outfit_tiger.value: ID2ItemData(ItemClassification.useful, 1, 58, "Outfits"),
    iname.outfit_id.value: ID2ItemData(ItemClassification.useful, 1, 59, "Outfits"),
    iname.outfit_delinquint.value: ID2ItemData(ItemClassification.useful, 1, 60, "Outfits"),
    iname.outfit_berry.value: ID2ItemData(ItemClassification.useful, 0, 61, "Outfits"),
    iname.outfit_apa.value: ID2ItemData(ItemClassification.useful, 0, 62, "Outfits"),
    iname.outfit_that_guy.value: ID2ItemData(ItemClassification.useful, 0, 63, "Outfits"),
    iname.loot.value: ID2ItemData(ItemClassification.useful, 0, 64, "Major Items"),
    iname.fake_efcs.value: ID2ItemData(ItemClassification.progression, 1, 65, "Major Items"),
    iname.card_fishbun.value: ID2ItemData(ItemClassification.filler, 1, 100, "Cards"),
    iname.card_bee.value: ID2ItemData(ItemClassification.filler, 1, 101, "Cards"),
    iname.card_safety.value: ID2ItemData(ItemClassification.filler, 1, 102, "Cards"),
    iname.card_shellbun.value: ID2ItemData(ItemClassification.filler, 1, 103, "Cards"),
    iname.card_spikebun.value: ID2ItemData(ItemClassification.filler, 1, 104, "Cards"),
    iname.card_gate.value: ID2ItemData(ItemClassification.filler, 1, 105, "Cards"),
    iname.card_snake.value: ID2ItemData(ItemClassification.filler, 1, 106, "Cards"),
    iname.card_mimic.value: ID2ItemData(ItemClassification.filler, 1, 107, "Cards"),
    iname.card_ogler.value: ID2ItemData(ItemClassification.filler, 1, 108, "Cards"),
    iname.card_hyperdusa.value: ID2ItemData(ItemClassification.filler, 1, 109, "Cards"),
    iname.card_easel.value: ID2ItemData(ItemClassification.filler, 1, 110, "Cards"),
    iname.card_warnip.value: ID2ItemData(ItemClassification.filler, 1, 111, "Cards"),
    iname.card_octacle.value: ID2ItemData(ItemClassification.filler, 1, 112, "Cards"),
    iname.card_rotnip.value: ID2ItemData(ItemClassification.filler, 1, 113, "Cards"),
    iname.card_bees.value: ID2ItemData(ItemClassification.filler, 1, 114, "Cards"),
    iname.card_volcano.value: ID2ItemData(ItemClassification.filler, 1, 115, "Cards"),
    iname.card_shark.value: ID2ItemData(ItemClassification.filler, 1, 116, "Cards"),
    iname.card_swimmy.value: ID2ItemData(ItemClassification.filler, 1, 117, "Cards"),
    iname.card_bunboy.value: ID2ItemData(ItemClassification.filler, 1, 118, "Cards"),
    iname.card_spectre.value: ID2ItemData(ItemClassification.filler, 1, 119, "Cards"),
    iname.card_brutus.value: ID2ItemData(ItemClassification.filler, 1, 120, "Cards"),
    iname.card_jelly.value: ID2ItemData(ItemClassification.filler, 1, 121, "Cards"),
    iname.card_skullnip.value: ID2ItemData(ItemClassification.filler, 1, 122, "Cards"),
    iname.card_slayer.value: ID2ItemData(ItemClassification.filler, 1, 123, "Cards"),
    iname.card_titan.value: ID2ItemData(ItemClassification.filler, 1, 124, "Cards"),
    iname.card_chilly.value: ID2ItemData(ItemClassification.filler, 1, 125, "Cards"),
    iname.card_flower.value: ID2ItemData(ItemClassification.filler, 1, 126, "Cards"),
    iname.card_hexrot.value: ID2ItemData(ItemClassification.filler, 1, 127, "Cards"),
    iname.card_mole.value: ID2ItemData(ItemClassification.filler, 1, 128, "Cards"),
    iname.card_bun.value: ID2ItemData(ItemClassification.filler, 1, 129, "Cards"),
    iname.card_cat.value: ID2ItemData(ItemClassification.filler, 1, 130, "Cards"),
    iname.card_mermaid.value: ID2ItemData(ItemClassification.filler, 1, 131, "Cards"),
    iname.card_berry.value: ID2ItemData(ItemClassification.filler, 1, 132, "Cards"),
    iname.card_mapman.value: ID2ItemData(ItemClassification.filler, 1, 133, "Cards"),
    iname.card_cyber.value: ID2ItemData(ItemClassification.filler, 1, 134, "Cards"),
    iname.card_biadlo.value: ID2ItemData(ItemClassification.filler, 1, 135, "Cards"),
    iname.card_lenny.value: ID2ItemData(ItemClassification.filler, 1, 136, "Cards"),
    iname.card_passel.value: ID2ItemData(ItemClassification.filler, 1, 137, "Cards"),
    iname.card_tippsie.value: ID2ItemData(ItemClassification.filler, 1, 138, "Cards"),
    iname.card_ittle.value: ID2ItemData(ItemClassification.filler, 1, 139, "Cards"),
    iname.card_fly.value: ID2ItemData(ItemClassification.filler, 1, 140, "Cards"),
    iname.buff.value: ID2ItemData(ItemClassification.filler, 0, 141, "Bonus Items"),
    iname.debuff.value: ID2ItemData(ItemClassification.trap, 0, 142, "Traps"),
    iname.bee.value: ID2ItemData(ItemClassification.trap, 0, 143, "Traps")
}

none_item_table: Dict[str, ID2ItemData] = {
    iname.keysey.value: ID2ItemData(ItemClassification.progression, 0, None, "Options"),
    iname.glitchless.value: ID2ItemData(ItemClassification.progression, 0, None, "Options"),
    iname.dw_vanilla.value: ID2ItemData(ItemClassification.progression, 0, None, "Options"),
    iname.dw_fun.value: ID2ItemData(ItemClassification.progression, 0, None, "Options"),
    iname.open_d8.value: ID2ItemData(ItemClassification.progression, 0, None, "Options"),
    iname.open_s4.value: ID2ItemData(ItemClassification.progression, 0, None, "Options"),
    iname.open_dw.value: ID2ItemData(ItemClassification.progression, 0, None, "Options"),
    iname.major_skips.value: ID2ItemData(ItemClassification.progression, 0, None, "Options"),
    iname.option_phasing.value: ID2ItemData(ItemClassification.progression, 0, None, "Options"),
    iname.option_phasing_objects.value: ID2ItemData(ItemClassification.progression, 0, None, "Options"),
    iname.option_phasing_dynamite.value: ID2ItemData(ItemClassification.progression, 0, None, "Options"),
    iname.option_phasing_enemy.value: ID2ItemData(ItemClassification.progression, 0, None, "Options"),
    iname.option_phasing_difficult.value: ID2ItemData(ItemClassification.progression, 0, None, "Options")
}

item_name_to_id: Dict[str, int] = {name: item_base_id + data.item_id_offset for name, data in item_table.items()}

filler_items: List[str] = [name for name, data in item_table.items() if data.classification in [ItemClassification.filler | ItemClassification.trap] and data.quantity_in_item_pool == 0]


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
    "Progressive Sword": {"Progressive Melee"},
    "Progressive Mace": {"Progressive Melee"},
    "EFCS": {"Impossible Gates Pass"},
    "Force": {"Progressive Force Wand"},
    "Wand": {"Progressive Force Wand"},
    "Force Wand": {"Progressive Force Wand"},
    "Dynamite": {"Progressive Dynamite"},
    "Ice": {"Progressive Ice Ring"},
    "Ring": {"Progressive Ice Ring"},
    "Ice Ring": {"Progressive Ice Ring"},
    "Chain": {"Progressive Chain"},
    "Tracker": {"Progressive Tracker"},
    "Headband": {"Progressive Headband"},
    "Amulet": {"Progressive Amulet"},
    "Tome": {"Progressive Tome"},
    "Shard": {"Secret Shard"},
    "Loot": {"Big Old Pile of Loot"}
}

item_name_groups.update(extra_groups)
