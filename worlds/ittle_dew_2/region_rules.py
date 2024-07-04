from typing import List, Dict, TYPE_CHECKING, cast
from BaseClasses import Region, Location, ItemClassification
from worlds.generic.Rules import CollectionRule
from .region_data import ID2Type
from .names_regions import RegionNames as rname
from .names_locations import LocationNames as lname
from .names_items import ItemNames as iname
from .items import ID2Item
from .options import KeySettings

if TYPE_CHECKING:
    from . import ID2World


class ID2Location(Location):
    game: str = "Ittle Dew 2"


# group requirements and their individual requirements
helper_reference: Dict[str, List[str]] = {
    iname.weapon_any.value: [iname.melee.value, iname.force.value, iname.dynamite.value, iname.ice.value],
    iname.weapon_no_dynamite.value: [iname.melee.value, iname.force.value, iname.ice.value],
    iname.weapon_no_force.value: [iname.melee.value, iname.dynamite.value, iname.ice.value],
    iname.weapon_projectile.value: [iname.fire_mace.value, iname.force.value],
    iname.basic_combat.value: [iname.melee.value, iname.force.value, iname.dynamite.value, iname.ice.value]
}

# number of keys in each dungeon
key_count_requirements: Dict[lname, int] = {
    lname.event_all_d1_keys: 2,
    lname.event_all_d2_keys: 2,
    lname.event_all_d3_keys: 4,
    lname.event_all_d4_keys: 4,
    lname.event_all_d5_keys: 5,
    lname.event_all_d6_keys: 5,
    lname.event_all_d7_keys: 5,
    lname.event_all_d8_keys: 8,
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
def convert_helper_reqs(helper_name: str, reqs: List[List[str]]) -> List[List[str]]:
    new_list_storage: List[List[str]] = []
    for i, sublist in enumerate(reqs):
        for j, req in enumerate(sublist):
            if req == helper_name:
                for replacement in helper_reference[helper_name]:
                    new_list = sublist.copy()
                    new_list[j] = replacement
                    print("REPLACEMENT LIST: ")
                    print(new_list)
                    new_list_storage.append(new_list)
                # replace the starter list with one of the storage lists to keep it from skipping an entry
                reqs[i] = new_list_storage.pop()
                break

    for sublist in new_list_storage:
        # newlist: List[str] = []
        # for list_item in sublist:
        #     print("LIST ITEM: " + list_item)
        #     # item: iname = cast(iname, list_item)
        #     check_item_type = copy(item)
        #     is_an_iname = isinstance(check_item_type, iname)
        #     print(is_an_iname)
        #     print("ACTUAL ITEM (the enum): " + item)
        #     if is_an_iname:
        #         newlist.append(item.value)
        #     else:
        #         newlist.append(item)
        # print("NEW LIST:")
        # print(newlist)
        reqs.append(sublist)

    # TODO remove empty lists from the reqs

    return reqs


# create a bunch of empty regions
def create_id2_regions(world: "ID2World") -> Dict[str, Region]:
    id2_regions: Dict[str, Region] = {}
    # TODO exclude regions based on options
    for region_name in rname:
        print(f"CREATING REGION: {region_name}")
        id2_regions[region_name] = Region(region_name, world.player, world.multiworld)
    return id2_regions


# break down and convert requirements
def interpret_rule(reqs: List[List[str]], world: "ID2World") -> CollectionRule:
    for helper_name in helper_reference.keys():
        reqs = convert_helper_reqs(helper_name, reqs)
    print("REQUIREMENTS INTERPRETED: ")
    print(reqs)
    return lambda state: any(state.has_all(sublist, world.player) for sublist in reqs)


# create the regions, fill them with exits and locations, and assign logic
def create_regions_with_rules(world: "ID2World") -> None:
    player = world.player
    options = world.options
    id2_regions = create_id2_regions(world)

    for origin_name, destinations in world.traversal_requirements.items():
        origin_name = cast(str, origin_name.value)
        # TODO exclude regions based on pool settings

        print("ADDING REGION: " + origin_name)
        for destination_name, data in destinations.items():
            destination_name = cast(str, destination_name.value)
            if data.type == ID2Type.location:
                print(f"ADDING LOCATION: {destination_name}")
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
                print(f"ADDING REGION CONNECTION: {destination_name}")
                # TODO add shard requirements for shard dungeons (maybe make that an item?)
                id2_regions[origin_name].connect(connecting_region=id2_regions[destination_name],
                                                 rule=interpret_rule(data.rules, world))
            print("DATA RULES:")
            print(data.rules)

    # "give" the player permission to use their keys once they've obained them all
    keys_location_list = [name for name in lname if name.endswith(" Keys")]
    for key_location in keys_location_list:
        print(f"PLACING KEY LOCATION {key_location}")
        key_access_location = ID2Location(player, key_location, None, id2_regions[rname.menu])
        key_name = key_location.value.replace("Received", "Can Use")
        key_item = key_location.value.removeprefix("Received ")
        key_item = key_item.removesuffix("s")
        if options.key_settings == KeySettings.option_keyrings:
            key_item += " Ring"

        key_access_location.place_locked_item(ID2Item(key_name, ItemClassification.progression, None, player))
        print("KEY ITEM NAME: " + key_item)
        print("KEY EVENT NAME: " + key_name)
        if options.key_settings.value == KeySettings.option_default:
            key_access_location.access_rule = lambda state, item=key_item, quantity=key_count_requirements[key_location]: state.has(item, player, quantity)
            print(f"KEY REQUIREMENTS: {key_item} x {key_count_requirements[key_location]}")
        elif options.key_settings.value == KeySettings.option_keyrings:
            key_access_location.access_rule = lambda state, item=key_item: state.has(item, player)
        else:  # keysey we can just assume we always have access to locked doors
            key_access_location.access_rule = lambda _: True
        id2_regions[rname.menu].locations.append(key_access_location)

    # give the player access to fire sword and mace once they've obtained 2 and 3 progressive melees
    fire_sword_event = ID2Location(player, lname.event_fire_sword, None, id2_regions[rname.menu])
    fire_sword_event.place_locked_item(ID2Item(iname.fire_sword.value, ItemClassification.progression, None, player))
    fire_sword_event.access_rule = lambda state: state.has(iname.melee.value, player, 2)
    id2_regions[rname.menu].locations.append(fire_sword_event)

    fire_mace_event = ID2Location(player, lname.event_fire_mace, None, id2_regions[rname.menu])
    fire_mace_event.place_locked_item(ID2Item(iname.fire_mace.value, ItemClassification.progression, None, player))
    fire_mace_event.access_rule = lambda state: state.has(iname.melee.value, player, 3)
    id2_regions[rname.menu].locations.append(fire_mace_event)

    # Force Jump
    force_jump_event = ID2Location(player, lname.event_force_jump, None, id2_regions[rname.menu])
    force_jump_event.place_locked_item(ID2Item(iname.force_jump.value, ItemClassification.progression, None, player))
    force_jump_event.access_rule = lambda state: state.has_all({iname.force.value, iname.ice.value}, player)
    id2_regions[rname.menu].locations.append(force_jump_event)

    # dreamworld dungeon complete events
    if not options.open_dreamworld:
        dw2_event = ID2Location(player, lname.event_dreamworld_2, None, id2_regions[rname.menu])
        dw2_event.place_locked_item(ID2Item(iname.dw_2.value, ItemClassification.progression, None, player))
        dw2_event.access_rule = lambda state: state.has(iname.dw_dungeon_complete.value, player, 2)
        id2_regions[rname.menu].locations.append(dw2_event)

        dw3_event = ID2Location(player, lname.event_dreamworld_3, None, id2_regions[rname.menu])
        dw3_event.place_locked_item(ID2Item(iname.dw_3.value, ItemClassification.progression, None, player))
        dw3_event.access_rule = lambda state: state.has(iname.dw_dungeon_complete.value, player, 3)
        id2_regions[rname.menu].locations.append(dw3_event)

        dw4_event = ID2Location(player, lname.event_dreamworld_4, None, id2_regions[rname.menu])
        dw4_event.place_locked_item(ID2Item(iname.dw_4.value, ItemClassification.progression, None, player))
        dw4_event.access_rule = lambda state: state.has(iname.dw_dungeon_complete.value, player, 4)
        id2_regions[rname.menu].locations.append(dw4_event)

    # open dungeons settings
    d8_event = ID2Location(player, lname.event_d8, None, id2_regions[rname.menu])
    d8_event.place_locked_item(ID2Item(iname.has_opened_d8.value, ItemClassification.progression, None, player))
    if not options.open_d8:
        d8_event.access_rule = lambda state: state.has(iname.raft.value, player, 7)
    id2_regions[rname.menu].locations.append(d8_event)

    s1_event = ID2Location(player, lname.event_s1, None, id2_regions[rname.menu])
    s1_event.place_locked_item(ID2Item(iname.has_opened_s1.value, ItemClassification.progression, None, player))
    s1_event.access_rule = lambda state: state.has(iname.shard.value, player, options.shard_settings.value * 4)
    id2_regions[rname.menu].locations.append(s1_event)

    s2_event = ID2Location(player, lname.event_s2, None, id2_regions[rname.menu])
    s2_event.place_locked_item(ID2Item(iname.has_opened_s2.value, ItemClassification.progression, None, player))
    s2_event.access_rule = lambda state: state.has(iname.shard.value, player, options.shard_settings.value * 8)
    id2_regions[rname.menu].locations.append(s2_event)

    s3_event = ID2Location(player, lname.event_s3, None, id2_regions[rname.menu])
    s3_event.place_locked_item(ID2Item(iname.has_opened_s3.value, ItemClassification.progression, None, player))
    s3_event.access_rule = lambda state: state.has(iname.shard.value, player, options.shard_settings.value * 12)
    id2_regions[rname.menu].locations.append(s3_event)

    s4_event = ID2Location(player, lname.event_s4, None, id2_regions[rname.menu])
    s4_event.place_locked_item(ID2Item(iname.has_opened_s4.value, ItemClassification.progression, None, player))
    if not options.open_s4:
        s4_event.access_rule = lambda state: state.has(iname.f_key.value, player, 4)
    id2_regions[rname.menu].locations.append(s4_event)

    dw_event = ID2Location(player, lname.event_dw, None, id2_regions[rname.menu])
    dw_event.place_locked_item(ID2Item(iname.has_opened_dw.value, ItemClassification.progression, None, player))
    if not options.open_dreamworld:
        dw_event.access_rule = lambda state: state.has(iname.raft.value, player, 1)
    id2_regions[rname.menu].locations.append(dw_event)

    # conditional can_open_chests
    chest_opener_event = ID2Location(player, lname.event_chest_opener, None, id2_regions[rname.menu])
    chest_opener_event.place_locked_item(ID2Item(iname.can_open_chests.value, ItemClassification.progression,
                                                 None, player))
    if options.roll_opens_chests:
        chest_opener_event.access_rule = lambda state: state.has_any({iname.melee.value, iname.force.value,
                                                                      iname.dynamite.value, iname.ice.value,
                                                                      iname.roll.value}, player)
    else:
        chest_opener_event.access_rule = lambda state: state.has_any({iname.melee.value, iname.force.value,
                                                                      iname.dynamite.value, iname.ice.value}, player)
    id2_regions[rname.menu].locations.append(chest_opener_event)

    # phasing
    if options.phasing_itemless:
        phase_itemless_event = ID2Location(player, lname.event_phase_itemless, None, id2_regions[rname.menu])
        phase_itemless_event.place_locked_item(ID2Item(iname.can_phase_itemless, ItemClassification.progression,
                                                       None, player))
        phase_itemless_event.access_rule = lambda state: state.has(iname.option_phasing, player)
        id2_regions[rname.menu].locations.append(phase_itemless_event)

        if options.phasing_difficult:
            phase_itemless_difficult_event = ID2Location(player, lname.event_phase_itemless_difficult,
                                                         None, id2_regions[rname.menu])
            phase_itemless_difficult_event.place_locked_item(ID2Item(iname.can_phase_itemless_difficult,
                                                                     ItemClassification.progression, None, player))
            phase_itemless_difficult_event.access_rule = lambda state: state.has_all({iname.option_phasing,
                                                                                      iname.option_phasing_difficult},
                                                                                     player)
            id2_regions[rname.menu].locations.append(phase_itemless_difficult_event)

    if options.phasing_ice:
        phase_ice_event = ID2Location(player, lname.event_phase_ice, None, id2_regions[rname.menu])
        phase_ice_event.place_locked_item(ID2Item(iname.can_phase_ice, ItemClassification.progression, None, player))
        phase_ice_event.access_rule = lambda state: state.has_all({iname.option_phasing_ice, iname.ice}, player)
        id2_regions[rname.menu].locations.append(phase_ice_event)

        phase_ice_itemless_event = ID2Location(player, lname.event_phase_ice_itemless, None, id2_regions[rname.menu])
        phase_ice_itemless_event.place_locked_item(ID2Item(iname.can_phase_ice_itemless, ItemClassification.progression,
                                                           None, player))
        phase_ice_itemless_event.access_rule = lambda state: state.has(iname.option_phasing_ice, player)
        id2_regions[rname.menu].locations.append(phase_ice_itemless_event)

        if options.phasing_difficult:
            phase_ice_difficult_event = ID2Location(player, lname.event_phase_ice_difficult,
                                                    None, id2_regions[rname.menu])
            phase_ice_difficult_event.place_locked_item(ID2Item(iname.can_phase_ice_difficult,
                                                                ItemClassification.progression, None, player))
            phase_ice_difficult_event.access_rule = lambda state: state.has_all({iname.option_phasing_ice,
                                                                                 iname.option_phasing_difficult,
                                                                                 iname.ice}, player)
            id2_regions[rname.menu].locations.append(phase_ice_difficult_event)

            phase_ice_itemless_difficult_event = ID2Location(player, lname.event_phase_ice_itemless_difficult,
                                                             None, id2_regions[rname.menu])
            phase_ice_itemless_difficult_event.place_locked_item(ID2Item(iname.can_phase_ice_itemless_difficult,
                                                                         ItemClassification.progression, None, player))
            phase_ice_itemless_difficult_event.access_rule = lambda state: state.has_all({iname.option_phasing_ice,
                                                                                          iname.option_phasing_difficult
                                                                                          }, player)
            id2_regions[rname.menu].locations.append(phase_ice_itemless_difficult_event)

    if options.phasing_dynamite:
        phase_dynamite_event = ID2Location(player, lname.event_phase_dynamite, None, id2_regions[rname.menu])
        phase_dynamite_event.place_locked_item(ID2Item(iname.can_phase_dynamite, ItemClassification.progression,
                                                       None, player))
        phase_dynamite_event.access_rule = lambda state: state.has_all({iname.option_phasing_dynamite, iname.dynamite,
                                                                        iname.ice}, player)
        id2_regions[rname.menu].locations.append(phase_dynamite_event)

        if options.phasing_difficult:
            phase_dynamite_difficult_event = ID2Location(player, lname.event_phase_dynamite_difficult,
                                                         None, id2_regions[rname.menu])
            phase_dynamite_difficult_event.place_locked_item(ID2Item(iname.can_phase_dynamite_difficult,
                                                                     ItemClassification.progression, None, player))
            phase_dynamite_difficult_event.access_rule = lambda state: state.has_all({iname.option_phasing_dynamite,
                                                                                      iname.option_phasing_difficult,
                                                                                      iname.dynamite, iname.ice},
                                                                                     player)
            id2_regions[rname.menu].locations.append(phase_dynamite_difficult_event)

    if options.phasing_enemies:
        phase_enemy_event = ID2Location(player, lname.event_phase_enemy, None, id2_regions[rname.menu])
        phase_enemy_event.place_locked_item(ID2Item(iname.can_phase_enemy, ItemClassification.progression,
                                                    None, player))
        phase_enemy_event.access_rule = lambda state: state.has_all({iname.option_phasing_enemy, iname.roll}, player)
        id2_regions[rname.menu].locations.append(phase_enemy_event)

        if options.phasing_difficult:
            phase_enemy_difficult_event = ID2Location(player, lname.event_phase_itemless_difficult,
                                                      None, id2_regions[rname.menu])
            phase_enemy_difficult_event.place_locked_item(ID2Item(iname.can_phase_itemless_difficult,
                                                                  ItemClassification.progression, None, player))
            phase_enemy_difficult_event.access_rule = lambda state: state.has_all({iname.option_phasing_enemy,
                                                                                   iname.option_phasing_difficult,
                                                                                   iname.roll}, player)
            id2_regions[rname.menu].locations.append(phase_enemy_difficult_event)

    for region in id2_regions.values():
        world.multiworld.regions.append(region)

    # TODO special entrances conditions

    world.multiworld.completion_condition[world.player] = lambda state: state.has(iname.victory.value, world.player)
