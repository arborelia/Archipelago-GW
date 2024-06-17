from typing import Dict, List, Any, Tuple, TypedDict
from logging import warning
from BaseClasses import Region, Location, Item, Tutorial, ItemClassification, MultiWorld
from .items import item_name_to_id, item_table, item_name_groups
from .locations import location_table, location_name_groups, location_name_to_id
from .region_data import traversal_requirements as reqs, ID2Data, ID2Type
from .options import ID2Options, id2_options_groups, id2_options_presets
from .names_regions import RegionNames as rname
from .names_locations import LocationNames as lname
from .names_items import ItemNames as iname
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
    bug_report_page = "https://github.com/Extra-2-Dew/ArchipelagoRandomizer/issues"
    option_groups = id2_options_groups
    options_presets = id2_options_presets


class ID2Item(Item):
    game: str = "Ittle Dew 2"


class ID2Location(Location):
    game: str = "Ittle Dew 2"

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

    def create_regions(self) -> None:
        for region in reqs:
            id2_regions[region] = Region(region, self.player, self.multiworld)
            for location in reqs[region]:
                if location == ID2Type.location:
                    id2_regions[region].add_locations(location)
            self.multiworld.regions.append(id2_regions[region])

id2_regions: Dict[str, Region]