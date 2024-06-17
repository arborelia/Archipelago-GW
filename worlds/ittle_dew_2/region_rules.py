from typing import List, Dict, TYPE_CHECKING, cast
from BaseClasses import Region, Location, ItemClassification
from worlds.generic.Rules import CollectionRule, add_rule
from .region_data import ID2Type
from names_regions import RegionNames as rname
from names_locations import LocationNames as lname
from names_items import ItemNames as iname
from .items import ID2Item
from .options import ID2Options

if TYPE_CHECKING:
    from . import ID2World

class ID2Location(Location):
    game: str = "Ittle Dew 2"

requirements: Dict[iname, bool]

def populate_requirements() -> None:
    for itm in iname._member_names_:
        


helper_reference: Dict[str, List[str]] = {
    iname.can_break_weak_objects: [iname.melee, iname.force, iname.dynamite, iname.ice],
    iname.can_break_stong_objects: [iname.melee, iname.dynamite, iname.ice]
}

def convert_helper_reqs(helper_name: str, reqs: List[List[str]]) -> List[List[str]]:
    new_list_storage: List[List[str]] = []
    for i, sublist in enumerate(reqs):
        for j, req in enumerate(sublist):
            if req == helper_name:
                for replacement in helper_reference[helper_name]:
                    new_list = sublist.copy()
                    new_list[j] = replacement
                    new_list_storage.append(new_list)
                # replace the starter list with one of the storage lists to keep it from skipping an entry
                reqs[i] = new_list_storage.pop()
                break

    for sublist in new_list_storage:
        reqs.append(sublist)

    # remove empty lists from the reqs
    return reqs

def convert_key_reqs(reqs: List[List[str]], options: ID2Options) -> List[List[str]]:
    if options.key_settings.option_default