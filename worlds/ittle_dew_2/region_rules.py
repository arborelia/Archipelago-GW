from typing import List, Dict, TYPE_CHECKING, cast, Callable
from BaseClasses import Region, Location, ItemClassification, CollectionState
from worlds.generic.Rules import CollectionRule, add_rule
from .region_data import ID2Type, ID2Data
from names_regions import RegionNames as rname
from names_locations import LocationNames as lname
from names_items import ItemNames as iname
from .items import ID2Item
from .options import ID2Options

if TYPE_CHECKING:
    from . import ID2World

class ID2Location(Location):
    game: str = "Ittle Dew 2"

helper_reference: Dict[str, List[str]] = {
    iname.can_break_weak_objects: [iname.melee, iname.force, iname.dynamite, iname.ice],
    iname.can_break_stong_objects: [iname.melee, iname.dynamite, iname.ice],
    iname.can_phase_itemless: [iname.option_phasing],
    iname.can_phase_itemless_difficult: [iname.option_phasing, iname.option_phasing_difficult],
    iname.can_phase_ice: [iname.ice, iname.option_phasing_ice],
    iname.can_phase_ice_difficult: [iname.ice, iname.option_phasing_ice, iname.option_phasing_difficult],
    iname.can_phase_dynamite: [iname.ice, iname.dynamite, iname.option_phasing_dynamite],
    iname.can_phase_dynamite_difficult: [iname.ice, iname.dynamite, 
                                         iname.option_phasing_dynamite, iname.option_phasing_difficult],
    iname.can_phase_enemy: [iname.roll, iname.option_phasing_enemy],
    iname.can_phase_enemy_difficult: [iname.roll, iname.option_phasing_enemy, iname.option_phasing_difficult]
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

def create_id2_regions(world: "ID2World") -> Dict[str, Region]:
    id2_regions: Dict[str, Region] = {}
    for region_name in rname:
        id2_regions[region_name] = Region(region_name, world.player, world.multiworld)

# break down and convert requirements
def interpret_rule(reqs: List[List[str]], world: "ID2World", options: ID2Options) -> CollectionRule:
    for helper_name in helper_reference.keys():
        reqs = convert_helper_reqs(helper_name, reqs)
    return lambda state: any(state.has_all(sublist, world.player) for sublist in reqs)

def create_regions_with_rules(world: "ID2World") -> None:
    player = world.player
    options = world.options
    id2_regions = create_id2_regions(world)

    for origin_name, destinations in world.traversal_requirements.items():
        origin_name = cast(str, origin_name.value)
        # TODO exclude regions based on pool settings

        for destination_name, data in destinations.items():
            destination_name = cast(str, destination_name.value)
            if data.type == ID2Type.location:
                # TODO exclude locations based on sanities, I don't think we have any of those but just in case
                if data.grant_event:
                    location = ID2Location(player, destination_name, None, id2_regions[origin_name])
                    location.place_locked_item(ID2Item(data.grant_event, ItemClassification.progression, None, player))
                else:
                    location = ID2Location(player, destination_name, world.location_name_to_id[destination_name],
                                           id2_regions[origin_name])
                location.access_rule = interpret_rule(data.rules, world)
                id2_regions[origin_name].locations.append(location)
            elif data.type == ID2Type.region:
                # TODO add shard requirements for shard dungeons (maybe make that an item?)
                entrance = id2_regions[origin_name].connect(connecting_region=id2_regions[destination_name],
                                                            rule=interpret_rule(data.rules, world))
                
                