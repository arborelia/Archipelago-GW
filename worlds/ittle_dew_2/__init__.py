from typing import Dict, List, Any, Tuple, TypedDict
from logging import warning
from BaseClasses import Region, Location, Item, Tutorial, ItemClassification, MultiWorld
from .items import item_name_to_id, item_table, item_name_groups, fool_tiers, filler_items, slot_data_item_names
from .locations import location_table, location_name_groups, location_name_to_id, hexagon_locations
from .rules import set_location_rules, set_region_rules, randomize_ability_unlocks, gold_hexagon
from .er_rules import set_er_location_rules
from .regions import tunic_regions
from .options import ID2Options
from worlds.AutoWorld import WebWorld, World
from decimal import Decimal, ROUND_HALF_UP


class ID2Web(WebWorld):
    tutorials = [
        Tutorial(
            tutorial_name="Multiworld Setup Guide",
            description="A guide to setting up the Ittle Dew 2 Randomizer for Archipelago multiworld games.",
            language="English",
            file_name="setup_en.md",
            link="setup/en",
            authors=["SilentDestroyer"] # TODO write a guide and update author
        )
    ]
    theme = "ocean"
    game = "Ittle Dew 2"
    option_groups = tunic_option_groups
    options_presets = tunic_option_presets


class ID2Item(Item):
    game: str = "Ittle Dew 2"


class ID2Location(Location):
    game: str = "Ittle Dew 2"


class SeedGroup(TypedDict):
    logic_rules: int  # logic rules value
    laurels_at_10_fairies: bool  # laurels location value
    fixed_shop: bool  # fixed shop value
    plando: TunicPlandoConnections  # consolidated of plando connections for the seed group


class ID2World(World):
    """
    Hunting for adventure, Ittle and her magical sidekick fox Tippsie have crashed on a mysterious island.
    Explore the island and tackle its eight dungeons on a search for Raft Pieces to escape!
    However, dark secrets and ancient dreams reside within. Will Ittle get the adventure she bargained for?
    Or will she succumb to the machinations of the Queen of Adventure?
    """
    game = "Ittle Dew 2"
    web = ID2Web()

    options: ID2Options
    options_dataclass = ID2Options
    item_name_groups = item_name_groups
    location_name_groups = location_name_groups

    item_name_to_id = item_name_to_id
    location_name_to_id = location_name_to_id

    ability_unlocks: Dict[str, int]
    slot_data_items: List[ID2Item]
    tunic_portal_pairs: Dict[str, str]
    er_portal_hints: Dict[int, str]
    seed_groups: Dict[str, SeedGroup] = {}

    