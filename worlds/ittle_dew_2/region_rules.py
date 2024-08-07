from typing import List, Dict, TYPE_CHECKING, cast, Tuple
from random import randint
from BaseClasses import Region, Location, ItemClassification, LocationProgressType
from worlds.generic.Rules import CollectionRule, forbid_item
from .locations import location_name_groups
from .region_data import ID2Type
from .names_regions import RegionNames as rname
from .names_locations import LocationNames as lname
from .names_items import ItemNames as iname
from .items import ID2Item, item_name_to_id
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


# cut grouped requirements into their individual requirements
def convert_helper_reqs(helper_name: str, reqs: List[List[str]]) -> List[List[str]]:
    new_list_storage: List[List[str]] = []
    for i, sublist in enumerate(reqs):
        for j, req in enumerate(sublist):
            if req == helper_name:
                for replacement in helper_reference[helper_name]:
                    # replaces requirements that can be one of multiple items with duplicates that have one of the items
                    new_list = sublist.copy()
                    new_list[j] = replacement
                    # print("REPLACEMENT LIST: ")
                    # print(new_list)
                    new_list_storage.append(new_list)
                # replace the starter list with one of the storage lists to keep it from skipping an entry
                reqs[i] = new_list_storage.pop()
                break

    for sublist in new_list_storage:
        reqs.append(sublist)

    return reqs


def get_requirement_quantities(reqs: List[List[str]], world: "ID2World") -> List[Dict[str, int]]:
    new_list: List[Dict[str, int]] = []
    for sublist in reqs:
        item_reqs: Dict[str, int] = {}
        print("LOGICAL REQUIREMENTS:")
        for item in sublist:
            if "*" in item:
                if "Key" in item and "Forbidden" not in item:
                    key_req = convert_key_requirements(item, world)
                    item_reqs[key_req[0]] = key_req[1]
                else:
                    components = item.split("*")
                    item_reqs[components[0]] = int(components[1])
            else:
                item_reqs[item] = 1
                print(f"Adding a single {item}")

            print(f"DICTIONARY LENGTH: {len(item_reqs)}")

        new_list.append(item_reqs)

    return new_list


def convert_key_requirements(key_name: str, world: "ID2World") -> Tuple[str, int]:
    options = world.options
    key_setting = options.key_settings
    converted_item: Tuple[str, int]
    components = key_name.split("*")
    item = components[0]
    quantity = int(components[1])
    print(f"Converting key requirements for {quantity} {item}s")
    if key_setting.value == KeySettings.option_keyrings:
        item += " Ring"
        quantity = 1
    elif key_setting.value == KeySettings.option_keysey:
        item = iname.keysey.value
        quantity = 1

    converted_item = item, quantity
    print(converted_item)

    return converted_item


# create a bunch of empty regions
def create_id2_regions(world: "ID2World") -> Dict[str, Region]:
    id2_regions: Dict[str, Region] = {}
    for region_name in rname:
        # print(f"CREATING REGION: {region_name}")
        id2_regions[region_name] = Region(region_name, world.player, world.multiworld)
    return id2_regions


# break down and convert requirements
def interpret_rule(reqs: List[List[str]], world: "ID2World") -> CollectionRule:
    item_reqs: List[Dict[str, int]] = []
    for helper_name in helper_reference.keys():
        reqs = convert_helper_reqs(helper_name, reqs)

    item_reqs = get_requirement_quantities(reqs, world)
    print("REQUIREMENTS INTERPRETED: ")
    print(item_reqs)
    return lambda state: any(state.has_all_counts(sublist, world.player) for sublist in item_reqs)


def determine_required_dungeons(world: "ID2World") -> List[str]:
    options = world.options
    if options.dungeon_rewards_setting.value != options.dungeon_rewards_setting.option_anything:
        main_dungeons: List[lname] = [
            lname.d1_boss_reward,
            lname.d2_boss_reward,
            lname.d3_boss_reward,
            lname.d4_boss_reward,
            lname.d5_boss_reward,
            lname.d6_boss_reward,
            lname.d7_boss_reward,
            lname.d8_boss_reward
        ]
        secret_dungeons: List[lname] = [
            lname.s1_boss_reward,
            lname.s2_boss_reward,
            lname.s3_boss_reward
        ]
        dream_dungeons: List[lname] = [
            lname.dfc_reward_b,
            lname.df_reward_b,
            lname.dd_reward_b,
            lname.di_reward_b
        ]
        world.required_dungeons = []
        all_dungeons: List[lname] = []
        all_dungeons += main_dungeons
        if options.include_secret_dungeons:
            all_dungeons += secret_dungeons
        if options.include_dream_dungeons:
            all_dungeons += dream_dungeons
        selected_dungeons: List[str] = []
        while len(selected_dungeons) < options.dungeon_rewards_count.value:
            if len(all_dungeons) == 0:
                raise ValueError("Not enough dungeons to place rewards in!")
            rnd = randint(0, len(all_dungeons) - 1)
            dungeon = all_dungeons[rnd]
            selected_dungeons.append(dungeon)
            world.required_dungeons.append(dungeon.value.split(" - ", 1)[0])
            all_dungeons.remove(dungeon)

        return selected_dungeons


# create the regions, fill them with exits and locations, and assign logic
def create_regions_with_rules(world: "ID2World") -> None:
    player = world.player
    options = world.options
    id2_regions = create_id2_regions(world)
    required_dungeons: List[str] = []
    rafts_to_place = 0
    fkeys_to_place = 0
    if options.dungeon_rewards_setting.value != options.dungeon_rewards_setting.option_anything:
        required_dungeons = determine_required_dungeons(world)
        if options.dungeon_rewards_setting.value == options.dungeon_rewards_setting.option_rewards:
            rafts_to_place = 8
            if not options.open_s4:
                fkeys_to_place = 4

    for origin_name, destinations in world.traversal_requirements.items():
        origin_name = cast(str, origin_name.value)

        print("ADDING REGION: " + origin_name)
        for destination_name, data in destinations.items():
            destination_name = cast(str, destination_name.value)
            if data.type == ID2Type.location:
                print(f"ADDING LOCATION: {destination_name}")
                if not options.include_portal_worlds:
                    if destination_name in location_name_groups["Portal Worlds"]:
                        # print("Portal Worlds are off, excluding this location.")
                        continue
                if not options.include_secret_dungeons:
                    if destination_name in location_name_groups["Secret Dungeons"]:
                        print("Secret Dungeons are off, excluding this location.")
                        continue
                if not options.include_dream_dungeons:
                    if destination_name in location_name_groups["Dreamworld"]:
                        print("Dream Dungeons are off, excluding this location.")
                        continue
                if not options.include_super_secrets:
                    if destination_name in location_name_groups["Super Secrets"]:
                        # print("Super Secrets are off, excluding this location.")
                        continue
                if data.grant_event:
                    location = ID2Location(player, destination_name, None, id2_regions[origin_name])
                    location.place_locked_item(ID2Item(data.grant_event, ItemClassification.progression, None, player))
                else:
                    location = ID2Location(player, destination_name, world.location_name_to_id[destination_name],
                                           id2_regions[origin_name])
                    if destination_name in required_dungeons:
                        # print(f"SETTING {destination_name} AS A REQUIRED LOCATION")
                        if rafts_to_place > 0:
                            location.place_locked_item(ID2Item(iname.raft.value, ItemClassification.progression,
                                                               item_name_to_id[iname.raft.value], player))
                            rafts_to_place -= 1
                        elif fkeys_to_place > 0:
                            location.place_locked_item(ID2Item(iname.f_key.value, ItemClassification.progression,
                                                               item_name_to_id[iname.f_key.value], player))
                            fkeys_to_place -= 1
                        else:
                            location.progress_type = LocationProgressType.PRIORITY
                    elif destination_name == lname.s4_boss_reward:
                        quality = ItemClassification.filler
                        if options.goal.value == options.goal.option_queen_of_adventure:
                            quality = ItemClassification.progression
                        location.place_locked_item(ID2Item(iname.loot.value, quality, item_name_to_id[iname.loot.value], player))
                    if destination_name in location_name_groups["Secret Dungeons"]:
                        forbid_item(location, iname.shard.value, player)
                location.access_rule = interpret_rule(data.rules, world)
                id2_regions[origin_name].locations.append(location)
            elif data.type == ID2Type.region:
                print(f"ADDING REGION CONNECTION: {destination_name}")
                # TODO add shard requirements for shard dungeons (maybe make that an item?)
                id2_regions[origin_name].connect(connecting_region=id2_regions[destination_name],
                                                 rule=interpret_rule(data.rules, world))
            # print("DATA RULES:")
            # print(data.rules)

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
    if options.phasing_setting.value >= options.phasing_setting.option_gap_phases:
        phase_gap_event = ID2Location(player, lname.event_phase_gap, None, id2_regions[rname.menu])
        phase_gap_event.place_locked_item(ID2Item(iname.can_phase_gap.value, ItemClassification.progression,
                                                  None, player))
        phase_gap_event.access_rule = lambda state: state.has(iname.option_phasing.value, player)
        id2_regions[rname.menu].locations.append(phase_gap_event)

        phase_door_event = ID2Location(player, lname.event_phase_door, None, id2_regions[rname.menu])
        phase_door_event.place_locked_item(
            ID2Item(iname.can_phase_doors.value, ItemClassification.progression, None, player))
        phase_gap_event.access_rule = lambda state: state.has_all({iname.option_phasing.value, iname.roll.value},
                                                                  player)

        if options.phasing_difficult:
            phase_gap_difficult_event = ID2Location(player, lname.event_phase_gap_difficult,
                                                    None, id2_regions[rname.menu])
            phase_gap_difficult_event.place_locked_item(ID2Item(iname.can_phase_gap_difficult.value,
                                                                ItemClassification.progression, None, player))
            phase_gap_difficult_event.access_rule = lambda state: state.has_all({iname.option_phasing.value,
                                                                                 iname.option_phasing_difficult.value},
                                                                                player)
            id2_regions[rname.menu].locations.append(phase_gap_difficult_event)

            phase_gap_event.access_rule = lambda state: state.has(iname.option_phasing.value, player)

        id2_regions[rname.menu].locations.append(phase_door_event)

    if options.phasing_setting.value >= options.phasing_setting.option_object_phases:
        phase_object_event = ID2Location(player, lname.event_phase_object, None, id2_regions[rname.menu])
        phase_object_event.place_locked_item(
            ID2Item(iname.can_phase_object.value, ItemClassification.progression, None, player))
        phase_object_event.access_rule = lambda state: state.has(iname.option_phasing_objects.value, player)
        id2_regions[rname.menu].locations.append(phase_object_event)

        if options.phasing_difficult:
            phase_object_difficult_event = ID2Location(player, lname.event_phase_object_difficult,
                                                       None, id2_regions[rname.menu])
            phase_object_difficult_event.place_locked_item(ID2Item(iname.can_phase_object_difficult.value,
                                                                   ItemClassification.progression, None, player))
            phase_object_difficult_event.access_rule = lambda state: state.has_all({iname.option_phasing_objects.value,
                                                                                    iname.option_phasing_difficult.value},
                                                                                   player)
            id2_regions[rname.menu].locations.append(phase_object_difficult_event)

    if options.phasing_setting.value >= options.phasing_setting.option_ice_dynamite_clips:
        phase_dynamite_event = ID2Location(player, lname.event_phase_dynamite, None, id2_regions[rname.menu])
        phase_dynamite_event.place_locked_item(ID2Item(iname.can_phase_dynamite.value, ItemClassification.progression,
                                                       None, player))
        phase_dynamite_event.access_rule = lambda state: state.has_all(
            {iname.option_phasing_dynamite.value, iname.dynamite.value,
             iname.ice.value}, player)
        id2_regions[rname.menu].locations.append(phase_dynamite_event)

        if options.phasing_difficult:
            phase_dynamite_difficult_event = ID2Location(player, lname.event_phase_dynamite_difficult,
                                                         None, id2_regions[rname.menu])
            phase_dynamite_difficult_event.place_locked_item(ID2Item(iname.can_phase_dynamite_difficult.value,
                                                                     ItemClassification.progression, None, player))
            phase_dynamite_difficult_event.access_rule = lambda state: state.has_all(
                {iname.option_phasing_dynamite.value,
                 iname.option_phasing_difficult.value,
                 iname.dynamite.value, iname.ice.value},
                player)
            id2_regions[rname.menu].locations.append(phase_dynamite_difficult_event)

    if options.phasing_enemies:
        phase_enemy_event = ID2Location(player, lname.event_phase_enemy, None, id2_regions[rname.menu])
        phase_enemy_event.place_locked_item(ID2Item(iname.can_phase_enemy.value, ItemClassification.progression,
                                                    None, player))
        phase_enemy_event.access_rule = lambda state: state.has_all(
            {iname.option_phasing_enemy.value, iname.roll.value}, player)
        id2_regions[rname.menu].locations.append(phase_enemy_event)

        if options.phasing_difficult:
            phase_enemy_difficult_event = ID2Location(player, lname.event_phase_enemy_difficult,
                                                      None, id2_regions[rname.menu])
            phase_enemy_difficult_event.place_locked_item(ID2Item(iname.can_phase_enemy_difficult.value,
                                                                  ItemClassification.progression, None, player))
            phase_enemy_difficult_event.access_rule = lambda state: state.has_all({iname.option_phasing_enemy.value,
                                                                                   iname.option_phasing_difficult.value,
                                                                                   iname.roll.value}, player)
            id2_regions[rname.menu].locations.append(phase_enemy_difficult_event)

    # Victory
    if options.goal.value != options.goal.option_queen_of_dreams:
        victory_event = ID2Location(player, lname.victory_location, None, id2_regions[rname.fluffy_fields])
        victory_event.place_locked_item(ID2Item(iname.victory, ItemClassification.progression, None, player))
        if options.goal.value == options.goal.option_raft_quest:
            victory_event.access_rule = lambda state: state.has(iname.raft.value, player, 8)
        else:
            victory_event.access_rule = lambda state: state.has(iname.raft.value, player, 8) and state.has(iname.loot.value, player)
        id2_regions[rname.fluffy_fields].locations.append(victory_event)
    else:
        victory_event = ID2Location(player, lname.victory_location, None, id2_regions[rname.da_ab])
        victory_event.place_locked_item(ID2Item(iname.victory, ItemClassification.progression, None, player))
        victory_event.access_rule = lambda state: state.has(iname.dw_finished_dungeon.value, player, 4)
        id2_regions[rname.da_ab].locations.append(victory_event)

    if options.include_super_secrets:
        efcs_event = ID2Location(player, lname.event_efcs, None, id2_regions[rname.menu])
        efcs_event.place_locked_item(ID2Item(iname.efcs, ItemClassification.progression, None, player))
        efcs_event.access_rule = lambda state: state.has_all({iname.fire_mace.value, iname.fake_efcs.value}, player)
        id2_regions[rname.menu].locations.append(efcs_event)

    for region in id2_regions.values():
        world.multiworld.regions.append(region)

    world.multiworld.completion_condition[world.player] = lambda state: state.has(iname.victory.value, world.player)
