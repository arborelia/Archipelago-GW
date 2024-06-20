from typing import List, Dict, TYPE_CHECKING, cast
from BaseClasses import Region, Location, ItemClassification
from worlds.generic.Rules import CollectionRule
from .region_data import ID2Type
from .names_regions import RegionNames as rname
from .names_locations import LocationNames as lname
from .names_items import ItemNames as iname
from .items import ID2Item
from .options import ID2Options, KeySettings

if TYPE_CHECKING:
    from . import ID2World

class ID2Location(Location):
    game: str = "Ittle Dew 2"

# group requirements and their individual requirements
helper_reference: Dict[str, List[str]] = {
    iname.can_break_weak_objects: [iname.melee, iname.force, iname.dynamite, iname.ice],
    iname.can_break_strong_objects: [iname.melee, iname.dynamite, iname.ice],
    iname.can_phase_itemless: [iname.option_phasing],
    iname.can_phase_itemless_difficult: [iname.option_phasing, iname.option_phasing_difficult],
    iname.can_phase_ice: [iname.ice, iname.option_phasing_ice],
    iname.can_phase_ice_difficult: [iname.ice, iname.option_phasing_ice, iname.option_phasing_difficult],
    iname.can_phase_ice_itemless: [iname.option_phasing_ice],
    iname.can_phase_ice_itemless_difficult: [iname.option_phasing_ice, iname.option_phasing_difficult],
    iname.can_phase_dynamite: [iname.ice, iname.dynamite, iname.option_phasing_dynamite],
    iname.can_phase_dynamite_difficult: [iname.ice, iname.dynamite, 
                                         iname.option_phasing_dynamite, iname.option_phasing_difficult],
    iname.can_phase_enemy: [iname.roll, iname.option_phasing_enemy],
    iname.can_phase_enemy_difficult: [iname.roll, iname.option_phasing_enemy, iname.option_phasing_difficult]
}

# if keyrings are active, convert keyrings to permission to use keys
keyring_helper_reference: Dict[str, List[str]] = {
    iname.can_use_d1_keys: [iname.d1_keyring],
    iname.can_use_d2_keys: [iname.d2_keyring],
    iname.can_use_d3_keys: [iname.d3_keyring],
    iname.can_use_d4_keys: [iname.d4_keyring],
    iname.can_use_d5_keys: [iname.d5_keyring],
    iname.can_use_d6_keys: [iname.d6_keyring],
    iname.can_use_d7_keys: [iname.d7_keyring],
    iname.can_use_d8_keys: [iname.d8_keyring],
    iname.can_use_s1_keys: [iname.s1_keyring],
    iname.can_use_s2_keys: [iname.s2_keyring],
    iname.can_use_s3_keys: [iname.s3_keyring],
    iname.can_use_s4_keys: [iname.s4_keyring],
    iname.can_use_dd_keys: [iname.dd_keyring],
    iname.can_use_dfc_keys: [iname.dfc_keyring],
    iname.can_use_di_keys: [iname.di_keyring],
    iname.can_use_da_keys: [iname.da_keyring]
}

# number of keys in each dungeon
key_count_requirements: Dict[lname, int] = {
    # lname.got_all_d1_keys: 2,
    lname.got_all_d2_keys: 2,
    # lname.got_all_d3_keys: 4,
    # lname.got_all_d4_keys: 4,
    # lname.got_all_d5_keys: 5,
    # lname.got_all_d6_keys: 5,
    # lname.got_all_d7_keys: 5,
    # lname.got_all_d8_keys: 8,
    # lname.got_all_s1_keys: 3,
    # lname.got_all_s2_keys: 5,
    # lname.got_all_s3_keys: 5,
    # lname.got_all_s4_keys: 10,
    # lname.got_all_dd_keys: 3,
    # lname.got_all_di_keys: 4,
    # lname.got_all_dfc_keys: 4,
    # lname.got_all_da_keys: 4,
}

# cut grouped requirements into their individual requirements
def convert_helper_reqs(helper_name: str, reqs: List[List[str]], options: ID2Options) -> List[List[str]]:
    new_list_storage: List[List[str]] = []
    for i, sublist in enumerate(reqs):
        for j, req in enumerate(sublist):
            if req == helper_name:
                for replacement in helper_reference[helper_name]:
                    new_list = sublist.copy()
                    new_list[j] = replacement
                    new_list_storage.append(new_list)
                # if we're running with keyrings, convert keyrings to the ability to use locks
                if options.key_settings == KeySettings.option_keyrings:
                    for key_replacement in keyring_helper_reference[helper_name]:
                        key_new_list = sublist.copy()
                        key_new_list[j] = key_replacement
                        new_list_storage.append(key_new_list)
                # replace the starter list with one of the storage lists to keep it from skipping an entry
                reqs[i] = new_list_storage.pop()
                break

    for sublist in new_list_storage:
        reqs.append(sublist)

    # TODO remove empty lists from the reqs
        
    return reqs

# create a bunch of empty regions
def create_id2_regions(world: "ID2World") -> Dict[str, Region]:
    id2_regions: Dict[str, Region] = {}
    # TODO exclude regions based on options
    for region_name in rname:
        id2_regions[region_name] = Region(region_name, world.player, world.multiworld)
    return id2_regions

# break down and convert requirements
def interpret_rule(reqs: List[List[str]], world: "ID2World") -> CollectionRule:
    for helper_name in helper_reference.keys():
        reqs = convert_helper_reqs(helper_name, reqs, world.options)
    return lambda state: any(state.has_all(sublist, world.player) for sublist in reqs)

# create the regions, fill them with exits and locations, and assign logic
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
                id2_regions[origin_name].connect(connecting_region = id2_regions[destination_name],
                                                            rule = interpret_rule(data.rules, world))

    # "give" the player permission to use their keys once they've obained them all
    if options.key_settings == KeySettings.option_default:
        keys_location_list = [name for name in lname if name.value.endswith(" Keys")]
        for key_location in keys_location_list:
            location = ID2Location(player, key_location, None, id2_regions[rname.menu])
            key_name = key_location.value.replace("Received", "Can Use")
            key_item = key_location.value.removeprefix("Received ")
            key_item = key_item.removesuffix("s")
            location.place_locked_item(ID2Item(key_name, ItemClassification.progression, None, player))
            location.access_rule = lambda state: state.has(key_item, player, key_count_requirements[key_location])
            id2_regions[rname.menu].locations.append(location)

    # give the player access to fire sword and mace once they've obtained 2 and 3 progressive melees
    fire_sword_event = ID2Location(player, lname.got_fire_sword, None, id2_regions[rname.menu])
    fire_sword_event.place_locked_item(ID2Item(iname.fire_sword, ItemClassification.progression, None, player))
    fire_sword_event.access_rule = lambda state: state.has(iname.melee, player, 2)
    id2_regions[rname.menu].locations.append(fire_sword_event)

    fire_mace_event = ID2Location(player, lname.got_fire_mace, None, id2_regions[rname.menu])
    fire_mace_event.place_locked_item(ID2Item(iname.fire_mace, ItemClassification.progression, None, player))
    fire_mace_event.access_rule = lambda state: state.has(iname.melee, player, 3)
    id2_regions[rname.menu].locations.append(fire_mace_event)

    for region in id2_regions.values():
        world.multiworld.regions.append(region)

    # TODO special entrances conditions

    world.multiworld.completion_condition[world.player] = lambda state: state.has(iname.victory, world.player)