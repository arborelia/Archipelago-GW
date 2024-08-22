from typing import Dict, List, NamedTuple, Optional, Union
from enum import IntEnum
from .names_regions import RegionNames as rname
from .names_locations import LocationNames as lname
from .names_items import ItemNames as iname


class ID2Type(IntEnum):
    location = 1
    region = 2


class ID2Data(NamedTuple):
    type: ID2Type  # Either Location or Region
    rules: List[List[str]] = [[]]  # List of rules for access requirements
    # for rules to be satisfied, you need to have at least one set of the rules items
    grant_event: Optional[str] = None  # grants the specified event item when the location is collected


# First Union is the source region
# Second Union is the destination region or location
# The ID2Data is a list of requirements
traversal_requirements: Dict[rname, Dict[Union[lname, rname], ID2Data]] = {
    # Currently vanilla start will be the only available starting location
    # For now MVP is going to move starting logical location to be Sweetwater Coast
    rname.menu: {
        rname.fluffy_fields:
            ID2Data(ID2Type.region)
    },
    # Overworld regions
    rname.fluffy_fields: {
        rname.pepperpain_prairie:
            ID2Data(ID2Type.region, [[iname.access_prairie.value]]),
        rname.sweetwater_coast:
            ID2Data(ID2Type.region, [[iname.access_coast.value]]),
        rname.fancy_ruins:
            ID2Data(ID2Type.region, [[iname.access_ruins.value]]),
        rname.star_woods:
            ID2Data(ID2Type.region, [[iname.access_woods.value]]),
        rname.slippery_slope:
            ID2Data(ID2Type.region, [[iname.access_slope.value]]),
        rname.dreamworld_hub:
            ID2Data(ID2Type.region, [[iname.raft.value]]),
        rname.ffc_a:
        # Only melee can hit the musical pillars
            ID2Data(ID2Type.region, [[iname.melee.value]]),
        rname.ffc_b:
            ID2Data(ID2Type.region),
        rname.ffc_c:
            ID2Data(ID2Type.region),
        rname.ffc_d:
            ID2Data(ID2Type.region),
        rname.ffc_e:
            ID2Data(ID2Type.region, [[iname.weapon_any.value]]),
        rname.ffc_f:
            ID2Data(ID2Type.region),
        rname.ffc_g:
            ID2Data(ID2Type.region, [[iname.weapon_any.value]]),
        rname.ffc_h:
            ID2Data(ID2Type.region),
        rname.ffc_i:
            ID2Data(ID2Type.region),
        rname.ffc_j:
            ID2Data(ID2Type.region),
        rname.ffc_k:
            ID2Data(ID2Type.region, [[iname.weapon_any.value]]),
        rname.ffc_l:
            ID2Data(ID2Type.region),
        rname.ffc_m:
            ID2Data(ID2Type.region),
        rname.ffc_n:
            ID2Data(ID2Type.region),
        rname.ffc_o:
            ID2Data(ID2Type.region, [[iname.weapon_any.value]]),
        rname.ffc_p:
            ID2Data(ID2Type.region),
        rname.ffc_q:
            ID2Data(ID2Type.region, [[iname.weapon_any.value]]),
        rname.ffc_r:
            ID2Data(ID2Type.region),
        rname.ffc_s:
            ID2Data(ID2Type.region),
        rname.ffc_s2:
            ID2Data(ID2Type.region),
        rname.ffc_u:
        # only requires waiting in the corner of warp garden,
        # but otherwise should be considered a Super Secret location
            ID2Data(ID2Type.region),
        rname.ffc_w:
            ID2Data(ID2Type.region),
        rname.ffc_x:
            ID2Data(ID2Type.region),
        rname.ffc_y:
            ID2Data(ID2Type.region),
        rname.d1_h:
            ID2Data(ID2Type.region),
        rname.s1_m:
            ID2Data(ID2Type.region, [[iname.has_opened_s1.value]])
    },
    rname.sweetwater_coast: {
        rname.fluffy_fields:
            ID2Data(ID2Type.region),
        rname.star_woods:
            ID2Data(ID2Type.region, [[iname.access_woods.value]]),
        rname.slippery_slope:
            ID2Data(ID2Type.region, [[iname.access_slope.value]]),
        rname.scc_a:
            ID2Data(ID2Type.region),
        rname.scc_b:
            ID2Data(ID2Type.region, [[iname.weapon_no_force.value]]),
        rname.scc_c:
            ID2Data(ID2Type.region),
        rname.scc_f:
        # transitional cave, gives access to d and e
            ID2Data(ID2Type.region),
        rname.sweetwater_hill:
            ID2Data(ID2Type.region, [[iname.can_phase_dynamite_difficult.value],
                                     [iname.can_phase_object.value, iname.ice.value, iname.roll.value],
                                     [iname.can_phase_enemy_difficult.value, iname.roll.value]]),
        rname.scc_g:
            ID2Data(ID2Type.region, [[iname.weapon_no_force.value]]),
        rname.scc_h:
            ID2Data(ID2Type.region),
        rname.scc_i:
            ID2Data(ID2Type.region),
        rname.scc_j:
            ID2Data(ID2Type.region, [[iname.roll.value]]),
        rname.scc_k:
            ID2Data(ID2Type.region),
        rname.scc_l:
            ID2Data(ID2Type.region, [[iname.weapon_any.value]]),
        rname.scc_m:
            ID2Data(ID2Type.region),
        rname.scc_n:
            ID2Data(ID2Type.region),
        rname.scc_o:
            ID2Data(ID2Type.region, [[iname.weapon_any.value]]),
        rname.scc_p:
            ID2Data(ID2Type.region, [[iname.access_ruins.value, iname.access_coast.value]]),
        rname.scc_q:
            ID2Data(ID2Type.region),
        rname.d2_g:
            ID2Data(ID2Type.region)
    },
    rname.sweetwater_hill: {
        rname.scc_d:
            ID2Data(ID2Type.region),
        rname.scc_e:
            ID2Data(ID2Type.region, [[iname.weapon_any.value]]),
    },
    rname.fancy_ruins: {
        rname.fluffy_fields:
            ID2Data(ID2Type.region),
        rname.star_woods:
            ID2Data(ID2Type.region, [[iname.access_woods.value]]),
        rname.pepperpain_prairie:
            ID2Data(ID2Type.region, [[iname.access_prairie.value]]),
        rname.frozen_court:
            ID2Data(ID2Type.region, [[iname.access_court.value]]),
        rname.frc_a:
            ID2Data(ID2Type.region, [[iname.weapon_any.value]]),
        rname.frc_b:
            ID2Data(ID2Type.region, [[iname.weapon_any.value]]),
        rname.frc_c:
            ID2Data(ID2Type.region),
        rname.frc_d:
            ID2Data(ID2Type.region),
        # There is no E cave
        rname.frc_f:
            ID2Data(ID2Type.region),
        rname.frc_g:
            ID2Data(ID2Type.region),
        rname.frc_h:
            ID2Data(ID2Type.region),
        rname.frc_i:
            ID2Data(ID2Type.region),
        rname.frc_j:
            ID2Data(ID2Type.region, [[iname.weapon_no_force.value]]),
        rname.frc_k:
            ID2Data(ID2Type.region, [[iname.weapon_any.value]]),
        rname.frc_l:
            ID2Data(ID2Type.region),
        rname.frc_m:
            ID2Data(ID2Type.region, [[iname.basic_combat.value]]),
        # N's entrance is one-way and requires entering from FC first
        # There is no O or P cave
        rname.frc_q:
            ID2Data(ID2Type.region),
        rname.frc_r:
            ID2Data(ID2Type.region),
        # S must be reached from N
        rname.scc_p:
            ID2Data(ID2Type.region, [[iname.access_ruins.value, iname.access_coast.value]]),
        rname.s2_p:
            ID2Data(ID2Type.region, [[iname.has_opened_s2.value]]),  # TODO make event item
    },
    rname.fancy_hilltop: {
        rname.frc_q:
            ID2Data(ID2Type.region),
        rname.d3_q:
            ID2Data(ID2Type.region),
    },
    rname.star_woods: {
        rname.fluffy_fields:
            ID2Data(ID2Type.region),
        rname.sweetwater_coast:
            ID2Data(ID2Type.region, [[iname.access_coast.value]]),
        rname.swc_a:
            ID2Data(ID2Type.region, [[iname.weapon_any.value]]),
        rname.swc_b:
            ID2Data(ID2Type.region, [[iname.weapon_no_force.value]]),
        rname.swc_c:
            ID2Data(ID2Type.region, [[iname.weapon_any.value]]),
        rname.swc_d:
            ID2Data(ID2Type.region),
        rname.swc_e:
            ID2Data(ID2Type.region),
        rname.swc_f:
            ID2Data(ID2Type.region, [[iname.weapon_no_force.value]]),
        rname.swc_g:
            ID2Data(ID2Type.region),
        rname.swc_h:
            ID2Data(ID2Type.region, [[iname.weapon_no_force.value]]),
        rname.swc_i:
            ID2Data(ID2Type.region),
        rname.swc_k:
            ID2Data(ID2Type.region),
        rname.swc_n:
            ID2Data(ID2Type.region, [[iname.weapon_any.value]]),
        rname.swc_q:
            ID2Data(ID2Type.region),
        rname.swc_r:
            ID2Data(ID2Type.region),
        rname.swc_s:
            ID2Data(ID2Type.region),
        rname.d4_r:
            ID2Data(ID2Type.region),
    },
    rname.star_east: {
        rname.swc_j:
            ID2Data(ID2Type.region),
        rname.swc_p:
        # The star responds to all weapons, but only melee and ice can hit it rapidly enough
            ID2Data(ID2Type.region, [[iname.melee.value],
                                     [iname.ice.value]]),
        rname.swc_q:
            ID2Data(ID2Type.region),
        rname.swc_r:
            ID2Data(ID2Type.region),
        rname.s3_s:
            ID2Data(ID2Type.region, [[iname.has_opened_s3.value]]),  # TODO turn into event item
        rname.star_woods:
        # clip by the artist's hous OoB, then navigate to the Fancy Ruins entrance
        # other way is technically possible but unfeasible without freecam
            ID2Data(ID2Type.region, [[iname.can_phase_dynamite_difficult.value, iname.roll.value],
                                     # it can also be done with just ice and roll
                                     [iname.can_phase_object_difficult.value, iname.ice.value, iname.melee.value,
                                      iname.roll.value]])
        # TODO honestly not that bad, maybe consider making them normal instead of difficult after feedback?
    },
    rname.star_coast: {
        rname.swc_l:
            ID2Data(ID2Type.region),
        rname.swc_m:
            ID2Data(ID2Type.region, [[iname.weapon_no_force.value]]),
        rname.swc_s:
            ID2Data(ID2Type.region),
        rname.swc_t:
        # You need to be able to kill the Octocles blocking the path
            ID2Data(ID2Type.region, [[iname.basic_combat.value]]),
    },
    rname.slippery_slope: {
        rname.fluffy_fields:
            ID2Data(ID2Type.region),
        rname.sweetwater_coast:
            ID2Data(ID2Type.region, [[iname.access_coast.value]]),
        rname.pepperpain_prairie:
            ID2Data(ID2Type.region, [[iname.access_prairie.value]]),
        rname.lonely_road_c_entrance:
            ID2Data(ID2Type.region, [[iname.access_road.value]]),
        rname.ssc_a:
            ID2Data(ID2Type.region, [[iname.weapon_any.value]]),
        rname.ssc_b:
            ID2Data(ID2Type.region),
        rname.ssc_c:
            ID2Data(ID2Type.region),
        rname.ssc_d:
            ID2Data(ID2Type.region),
        rname.ssc_e:
            ID2Data(ID2Type.region),
        rname.ssc_f:
            ID2Data(ID2Type.region, [[iname.weapon_any.value]]),
        rname.ssc_g:
            ID2Data(ID2Type.region),
        rname.ssc_h:
        # any weapon can hit the mushroom
            ID2Data(ID2Type.region, [[iname.weapon_any.value]]),
        rname.ssc_i:
            ID2Data(ID2Type.region, [[iname.weapon_any.value]]),
        rname.ssc_j:
            ID2Data(ID2Type.region),
        rname.ssc_k:
            ID2Data(ID2Type.region, [[iname.weapon_any.value]]),
        rname.ssc_l:
            ID2Data(ID2Type.region),
        rname.ssc_m:
        # shortcut from house on the hill to warp, technically has two entrances
            ID2Data(ID2Type.region),
        rname.ssc_n:
            ID2Data(ID2Type.region),
        rname.ssc_o:
            ID2Data(ID2Type.region),
    },
    rname.pepperpain_prairie: {
        rname.fluffy_fields:
            ID2Data(ID2Type.region),
        rname.fancy_ruins:
            ID2Data(ID2Type.region, [[iname.access_ruins.value]]),
        rname.slippery_slope:
            ID2Data(ID2Type.region, [[iname.access_slope.value]]),
        rname.ppc_a:
            ID2Data(ID2Type.region, [[iname.weapon_no_force.value]]),
        rname.ppc_b:
            ID2Data(ID2Type.region, [[iname.weapon_any.value]]),
        rname.ppc_c:
            ID2Data(ID2Type.region),
        rname.ppc_d:
            ID2Data(ID2Type.region, [[iname.weapon_any.value]]),
        rname.ppc_e:
            ID2Data(ID2Type.region),
        rname.ppc_f:
        # This cave can be opened itemless by utilizing a bunboy's homing bullet
        # TODO make require a non-force weapon if enemy rando is on
            ID2Data(ID2Type.region),
        rname.ppc_g:
            ID2Data(ID2Type.region),
        rname.ppc_h:
            ID2Data(ID2Type.region, [[iname.weapon_any.value]]),
        rname.ppc_i:
            ID2Data(ID2Type.region),
        rname.ppc_j:
            ID2Data(ID2Type.region, [[iname.weapon_any.value]]),
        rname.ppc_k:
            ID2Data(ID2Type.region),
        rname.ppc_l:
            ID2Data(ID2Type.region, [[iname.weapon_any.value]]),
        rname.ppc_m:
            ID2Data(ID2Type.region),
        rname.ssc_n:
            ID2Data(ID2Type.region),
    },
    rname.pepperpain_trail: {
        rname.ppc_c:
            ID2Data(ID2Type.region),
        rname.ppc_r:
            ID2Data(ID2Type.region),
        rname.ppc_u:
            ID2Data(ID2Type.region),
    },
    rname.pepperpain_mountain: {
        rname.fluffy_fields:
            ID2Data(ID2Type.region),
        rname.ppc_o:
            ID2Data(ID2Type.region, [[iname.roll.value, iname.weapon_any.value]]),
        rname.ppc_p:
            ID2Data(ID2Type.region, [[iname.weapon_any.value]]),
        rname.ppc_q:
            ID2Data(ID2Type.region),
        rname.ppc_r:
            ID2Data(ID2Type.region),
        rname.ppc_s:
            ID2Data(ID2Type.region),
        rname.ppc_t:
            ID2Data(ID2Type.region),
        rname.d6_q:
            ID2Data(ID2Type.region),
    },
    rname.frozen_court: {
        rname.fluffy_fields:
            ID2Data(ID2Type.region),
        rname.fancy_ruins:
            ID2Data(ID2Type.region, [[iname.access_ruins.value]]),
        rname.fcc_a:
            ID2Data(ID2Type.region, [[iname.melee.value]]),
        rname.fcc_b:
            ID2Data(ID2Type.region),
        rname.fcc_c:
            ID2Data(ID2Type.region, [[iname.melee.value]]),
        rname.fcc_d:
            ID2Data(ID2Type.region, [[iname.melee.value]]),
        rname.fcc_e:
            ID2Data(ID2Type.region),
        rname.fcc_f:
            ID2Data(ID2Type.region, [[iname.weapon_any.value]]),
        rname.fcc_g:
            ID2Data(ID2Type.region),
        rname.fcc_h:
            ID2Data(ID2Type.region),
        rname.fcc_i:
            ID2Data(ID2Type.region),
        rname.fcc_j:
            ID2Data(ID2Type.region),
        rname.fcc_k:
            ID2Data(ID2Type.region, [[iname.weapon_any.value]]),
        rname.fcc_l:
            ID2Data(ID2Type.region),
        rname.fcc_m:
            ID2Data(ID2Type.region),
        rname.frc_n:
            ID2Data(ID2Type.region),
        rname.swc_t:
            ID2Data(ID2Type.region),
        rname.d7_y:
            ID2Data(ID2Type.region),
    },
    rname.frozen_island: {
        rname.fcc_m:
            ID2Data(ID2Type.region),
        rname.fcc_o:
            ID2Data(ID2Type.region, [[iname.weapon_any.value]]),
    },
    # TODO determine phasability between LR regions
    rname.lonely_road_a: {
        rname.fluffy_fields:
            ID2Data(ID2Type.region),
        rname.lonely_road_b:
            ID2Data(ID2Type.region),
        rname.lrc_a:
            ID2Data(ID2Type.region, [[iname.weapon_any.value]]),
        rname.lrc_b:
            ID2Data(ID2Type.region),
        rname.lrc_c:
            ID2Data(ID2Type.region),
        rname.d8_y:
            ID2Data(ID2Type.region, [[iname.has_opened_d8.value],
                                     [iname.major_skips.value, iname.can_phase_dynamite_difficult.value,
                                      iname.roll.value]]),
    },
    rname.lonely_road_b: {
        rname.lonely_road_a:
            ID2Data(ID2Type.region),
        rname.lrc_d:
            ID2Data(ID2Type.region),
        rname.lrc_e_upper:
            ID2Data(ID2Type.region),
    },
    rname.lonely_road_c_garden: {
        rname.lrc_e_upper:
            ID2Data(ID2Type.region),
        rname.lrc_f:
            ID2Data(ID2Type.region),
        rname.lrc_k:
            ID2Data(ID2Type.region, [[iname.roll.value, iname.weapon_no_force.value]])
    },
    rname.lonely_road_c_entrance: {
        rname.slippery_slope:
            ID2Data(ID2Type.region),
        rname.lrc_e_lower:
            ID2Data(ID2Type.region),
        rname.lrc_g:
            ID2Data(ID2Type.region),
        rname.lrc_p:
            ID2Data(ID2Type.region),
        rname.lrc_q:
            ID2Data(ID2Type.region)
    },
    rname.lonely_road_c_pond_trail: {
        rname.lrc_f:
            ID2Data(ID2Type.region),
        rname.lrc_h:
            ID2Data(ID2Type.region),
        rname.lrc_l:
            ID2Data(ID2Type.region),
        rname.lrc_o:
            ID2Data(ID2Type.region, [[iname.roll.value]]),
    },
    rname.lonely_road_c_lightning_rock_trail: {
        rname.lrc_g:
            ID2Data(ID2Type.region),
        rname.lrc_h:
            ID2Data(ID2Type.region),
        rname.lrc_r:
            ID2Data(ID2Type.region)
    },
    rname.lonely_road_c_lake: {
        rname.lonely_road_d:
            ID2Data(ID2Type.region),
        rname.lonely_road_e:
            ID2Data(ID2Type.region),
        rname.lrc_h:
            ID2Data(ID2Type.region),
        rname.lrc_i_left:
            ID2Data(ID2Type.region),
        rname.lrc_m:
            ID2Data(ID2Type.region, [[iname.melee.value]]),
        rname.lrc_n:
            ID2Data(ID2Type.region),
        rname.lrc_s:
            ID2Data(ID2Type.region, [[iname.melee.value]]),
        rname.lrc_t:
            ID2Data(ID2Type.region, [[iname.melee.value]])
    },
    rname.lonely_road_d: {
        rname.lonely_road_c_lake:
            ID2Data(ID2Type.region),
        rname.lrc_u:
            ID2Data(ID2Type.region, [[iname.melee.value]])
    },
    rname.lonely_road_e: {
        rname.lonely_road_c_lake:
            ID2Data(ID2Type.region),
        rname.lrc_j:
            ID2Data(ID2Type.region, [[iname.basic_combat.value]])
    },
    rname.forbidden_area_south: {
        rname.fluffy_fields:
            ID2Data(ID2Type.region),
        rname.forbidden_area_north:
            ID2Data(ID2Type.region, [[iname.has_opened_s4.value],
                                     [iname.major_skips.value, iname.can_phase_dynamite.value, iname.roll.value],
                                     [iname.major_skips.value, iname.can_phase_object_difficult.value, iname.ice.value, iname.roll.value]]),
        rname.lrc_i_right:
            ID2Data(ID2Type.region),
        rname.lrc_j:
            ID2Data(ID2Type.region),
    },
    rname.forbidden_area_north: {
        rname.forbidden_area_south:
            ID2Data(ID2Type.region, [[iname.has_opened_s4.value],
                                     [iname.can_phase_dynamite.value, iname.roll.value]]),
        rname.s4_an:
            ID2Data(ID2Type.region)
    },

    # Caves
    # Fluffy Fields Caves
    rname.ffc_a: {
        rname.autumn_climb:
            ID2Data(ID2Type.region, [[iname.basic_combat.value],
                                     [iname.can_phase_gap.value]]),
    },
    rname.ffc_b: {
        lname.ffc_goldbun_combat:
            ID2Data(ID2Type.location, [[iname.basic_combat.value]]),
    },
    rname.ffc_c: {
        lname.ffc_portal_room:
            ID2Data(ID2Type.location, [[iname.can_open_chests.value]]),
    },
    rname.ffc_d: {
        # clockwise tree house turnip
    },
    rname.ffc_e: {
        lname.ffc_timed_bridge:
            ID2Data(ID2Type.location, [[iname.weapon_any.value]]),
    },
    rname.ffc_f: {
        lname.ffc_hermit_hint:
            ID2Data(ID2Type.location, [[iname.can_open_chests.value]]),
    },
    rname.ffc_g: {
        lname.ffc_laser:
            ID2Data(ID2Type.location, [[iname.can_open_chests.value]]),
    },
    rname.ffc_h: {
        # transitional cave from one side of Fluffy to the other
        # ...SPRUCE THAT IS...
    },
    rname.ffc_i: {
        # lazy turnip cave
    },
    rname.ffc_j: {
        lname.ffc_number_blocks:
            ID2Data(ID2Type.location, [[iname.can_open_chests.value]]),
    },
    rname.ffc_k: {
        lname.ffc_ice_blockade:
            ID2Data(ID2Type.location, [[iname.melee.value],
                                       # itemless ice phasing isn't possible due to some weird properties of the
                                       # natural ice blocks, still unknown why
                                       [iname.can_phase_object.value, iname.ice.value]]),
    },
    rname.ffc_l: {
        # West Safety Jenny hint house
    },
    rname.ffc_m: {
        lname.ffc_double_spikebun_combat:
            ID2Data(ID2Type.location, [[iname.basic_combat.value]])
    },
    rname.ffc_n: {
        # East Safety Jenny hint house
    },
    rname.ffc_o: {
        rname.ffc_t:
            ID2Data(ID2Type.region, [[iname.weapon_any.value]]),
    },
    rname.ffc_p: {
        lname.ffc_potion_bar:
            ID2Data(ID2Type.location, [[iname.weapon_any.value]]),
    },
    rname.ffc_q: {
        lname.ffc_six_buns_combat:
            ID2Data(ID2Type.location, [[iname.basic_combat.value]])
    },
    rname.ffc_r: {
        # Lenny's house
    },
    rname.ffc_s: {
        # Tutorial house
    },
    rname.ffc_s2: {
        rname.ffc_s:
            ID2Data(ID2Type.region, [[iname.weapon_any.value]]),
    },
    rname.ffc_t: {
        # Barrel room
    },
    rname.ffc_u: {
        lname.ffc_jenny_berry_house:
            ID2Data(ID2Type.location, [[iname.weapon_any.value]]),
        rname.ffc_u2:
            ID2Data(ID2Type.region, [[iname.weapon_any.value]]),
    },
    rname.ffc_u2: {
        # Jenny Berry PR hint sign
    },
    rname.ffc_w: {
        # Laundry
    },
    rname.ffc_x: {
        rname.ffc_x2:
            ID2Data(ID2Type.region, [[iname.weapon_any.value]]),
    },
    rname.ffc_x2: {
        lname.ffc_artist_backroom:
            ID2Data(ID2Type.location, [[iname.can_open_chests.value]]),
        rname.ffc_x:
            ID2Data(ID2Type.region, [[iname.weapon_any.value]]),
    },
    rname.ffc_y: {
        # Raft storage
    },
    # Sweetwater Caves
    rname.scc_a: {
        # rock performance
    },
    rname.scc_b: {
        lname.scc_white_gates_combat:
            ID2Data(ID2Type.location, [[iname.basic_combat.value]])
    },
    rname.scc_c: {
        # pink friendly ogler
    },
    rname.scc_d: {
        # transitional cave from e to main coast
    },
    rname.scc_e: {
        rname.the_vault_d:
            ID2Data(ID2Type.region)
    },
    rname.scc_f: {
        rname.sweetwater_hill:
            ID2Data(ID2Type.region)
    },
    rname.scc_g: {
        lname.scc_feral_gates_combat:
            ID2Data(ID2Type.location, [[iname.basic_combat.value]])
    },
    rname.scc_h: {
        lname.scc_three_teleporters:
            ID2Data(ID2Type.location, [[iname.can_open_chests.value]])
    },
    rname.scc_i: {
        lname.scc_four_candy_snakes_combat:
            ID2Data(ID2Type.location, [[iname.basic_combat.value]])
    },
    rname.scc_j: {
        lname.scc_portal_spikes_chest:
            ID2Data(ID2Type.location, [[iname.weapon_any.value],
                                       [iname.can_phase_object.value, iname.can_open_chests.value]])
    },
    rname.scc_k: {
        lname.scc_hint_hermit:
            ID2Data(ID2Type.location, [[iname.can_open_chests.value]])
    },
    rname.scc_l: {
        lname.scc_fake_chest_cave:
            ID2Data(ID2Type.location, [[iname.melee.value],
                                       [iname.force.value],
                                       [iname.ice.value]])
    },
    rname.scc_m: {
        lname.scc_wooden_balls_spike_floor:
            ID2Data(ID2Type.location, [[iname.can_open_chests.value]])
    },
    rname.scc_n: {
        lname.scc_kung_fu_jenny:
            ID2Data(ID2Type.location, [[iname.can_open_chests.value]])
    },
    rname.scc_o: {
        rname.painful_plain:
            ID2Data(ID2Type.region, [[iname.weapon_any.value]])
    },
    rname.scc_p: {
        # Transition cave to Fancy
    },
    rname.scc_q: {
        # Changing Tent
    },
    # Fancy Ruins Caves
    rname.frc_a: {
        lname.frc_two_torches:
            ID2Data(ID2Type.location, [[iname.melee.value]]),
    },
    rname.frc_b: {
        lname.frc_numbered_torches:
            ID2Data(ID2Type.location, [[iname.melee.value]]),
    },
    rname.frc_c: {
        lname.frc_two_crystals:
            ID2Data(ID2Type.location, [[iname.weapon_any.value],
                                       [iname.can_phase_gap.value, iname.roll.value, iname.can_open_chests.value]]),
    },
    rname.frc_d: {
        lname.frc_big_ogler_combat:
            ID2Data(ID2Type.location, [[iname.basic_combat.value, iname.roll.value]]),
    },
    rname.frc_f: {
        rname.farthest_shore:
            ID2Data(ID2Type.region),
    },
    rname.frc_g: {
        lname.frc_hint_turnip:
            ID2Data(ID2Type.location, [[iname.can_open_chests.value]]),
    },
    rname.frc_h: {
        lname.frc_rhythm_pillars:
            ID2Data(ID2Type.location, [[iname.melee.value]]),
    },
    rname.frc_i: {
        lname.frc_teleporter_puzzle:
            ID2Data(ID2Type.location, [[iname.weapon_any.value]]),
    },
    rname.frc_j: {
        lname.frc_four_oglers_combat:
            ID2Data(ID2Type.location, [[iname.basic_combat.value]]),
    },
    rname.frc_k: {
        lname.frc_spike_path:
            ID2Data(ID2Type.location, [[iname.weapon_any.value]]),
    },
    rname.frc_l: {
        lname.frc_hiding_hermit:
            ID2Data(ID2Type.location, [[iname.can_open_chests.value]]),
    },
    rname.frc_m: {
        lname.frc_ice_and_torch:
            ID2Data(ID2Type.location, [[iname.melee.value]]),
    },
    rname.frc_n: {
        rname.fancy_ruins:
            ID2Data(ID2Type.region, [[iname.access_ruins.value]]),
        rname.frozen_court:
            ID2Data(ID2Type.region),
        rname.frc_s:
            ID2Data(ID2Type.region),
    },
    rname.frc_q: {
        rname.fancy_ruins:
            ID2Data(ID2Type.region),
        rname.fancy_hilltop:
            ID2Data(ID2Type.region),
    },
    rname.frc_r: {
        rname.scrap_yard_f:
            ID2Data(ID2Type.region),
    },
    rname.frc_s: {
        rname.frc_n:
            ID2Data(ID2Type.region),
    },
    # Star Woods Caves
    rname.swc_a: {
        lname.swc_turnip_combat:
            ID2Data(ID2Type.location, [[iname.basic_combat.value]]),
    },
    rname.swc_b: {
        lname.swc_barrel_blast:
            ID2Data(ID2Type.location, [[iname.melee.value],
                                       # put the dynamite on the bridge, then press the button right before
                                       # the dynamite explodes
                                       [iname.dynamite.value]]),
    },
    rname.swc_c: {
        lname.swc_four_crystals:
            ID2Data(ID2Type.location, [[iname.melee.value],
                                       [iname.ice.value]])
    },
    rname.swc_d: {
        lname.swc_sleeping_jenny:
            ID2Data(ID2Type.location, [[iname.weapon_any.value]])
    },
    rname.swc_e: {
        # green star hint ogler
    },
    rname.swc_f: {
        lname.swc_rotating_spikes:
            ID2Data(ID2Type.location, [[iname.can_open_chests.value]])
    },
    rname.swc_g: {
        lname.swc_number_tiles:
            ID2Data(ID2Type.location, [[iname.can_open_chests.value]])
    },
    rname.swc_h: {
        lname.swc_whirlwind:
            ID2Data(ID2Type.location, [[iname.can_open_chests.value]])
    },
    rname.swc_i: {
        lname.swc_magic_crystal:
            ID2Data(ID2Type.location, [[iname.can_open_chests.value]])
    },
    rname.swc_j: {
        lname.swc_artist_turnip:
            ID2Data(ID2Type.location, [[iname.can_open_chests.value]])
    },
    rname.swc_k: {
        lname.swc_hint_bee:
            ID2Data(ID2Type.location, [[iname.can_open_chests.value]])
    },
    rname.swc_l: {
        # Dancing Turnip
    },
    rname.swc_m: {
        rname.swc_o:
            ID2Data(ID2Type.region, [[iname.weapon_any.value]])
    },
    rname.swc_n: {
        rname.brutal_oasis:
            ID2Data(ID2Type.region, [[iname.weapon_any.value],
                                     [iname.can_phase_gap.value]])
    },
    rname.swc_o: {
        lname.swc_extinguish_flames:
            ID2Data(ID2Type.location, [[iname.can_open_chests.value]]),
        rname.swc_m:
            ID2Data(ID2Type.region, [[iname.weapon_any.value]])
    },
    rname.swc_p: {
        rname.former_colossus:
            ID2Data(ID2Type.region)
    },
    rname.swc_q: {
        rname.star_woods:
            ID2Data(ID2Type.region),
        rname.star_east:
            ID2Data(ID2Type.region)
    },
    rname.swc_r: {
        rname.star_woods:
            ID2Data(ID2Type.region),
        rname.star_east:
            ID2Data(ID2Type.region)
    },
    rname.swc_s: {
        rname.star_woods:
            ID2Data(ID2Type.region),
        rname.star_coast:
            ID2Data(ID2Type.region)
    },
    rname.swc_t: {
        rname.star_coast:
            ID2Data(ID2Type.region, [[iname.access_woods.value]]),
        rname.frozen_court:
            ID2Data(ID2Type.region, [[iname.access_court.value]])
    },
    # Slippery Slope Caves
    rname.ssc_a: {
        lname.ssc_volcanic_path:
            ID2Data(ID2Type.location, [[iname.can_open_chests.value]])
    },
    rname.ssc_b: {
        lname.ssc_ice_and_barrels:
        # This room is weird and you can't phase to any of the natural entities in this room.
            ID2Data(ID2Type.location, [[iname.weapon_any.value]])
    },
    rname.ssc_c: {
        rname.ocean_castle:
            ID2Data(ID2Type.region, [[iname.basic_combat.value]])
    },
    rname.ssc_d: {
        lname.ssc_eight_crystals:
            ID2Data(ID2Type.location, [[iname.melee.value],
                                       # push the crystals using phasing to more conveniently hit them
                                       [iname.can_phase_object.value, iname.ice.value]
                                       # TODO this might be possible with dynamite and weapon_no_dynamite
                                       ])
    },
    rname.ssc_e: {
        lname.ssc_forgetful_jennies:
            ID2Data(ID2Type.location, [[iname.can_open_chests.value]])
    },
    rname.ssc_f: {
        lname.ssc_push_the_crystals:
            ID2Data(ID2Type.location, [[iname.weapon_any.value]])
    },
    rname.ssc_g: {
        lname.ssc_exhausted_turnip:
            ID2Data(ID2Type.location, [[iname.can_open_chests.value]])
    },
    rname.ssc_h: {
        rname.sand_crucible_c:
            ID2Data(ID2Type.region)
    },
    rname.ssc_i: {
        lname.ssc_bee_nest_combat:
            ID2Data(ID2Type.location, [[iname.basic_combat.value]])
    },
    rname.ssc_j: {
        lname.ssc_pushable_fan:
            ID2Data(ID2Type.location, [[iname.weapon_any.value],
                                       [iname.can_phase_gap.value, iname.roll.value]])
    },
    rname.ssc_k: {
        lname.ssc_moving_crystals:
            ID2Data(ID2Type.location, [[iname.melee.value],
                                       [iname.ice.value],
                                       [iname.dynamite.value, iname.weapon_no_dynamite.value]])
    },
    rname.ssc_l: {
        lname.ssc_shark_house:
            ID2Data(ID2Type.location, [[iname.can_open_chests.value]])
    },
    rname.ssc_m: {
        rname.slippery_slope:
            ID2Data(ID2Type.region)
    },
    rname.ssc_n: {
        rname.slippery_slope:
            ID2Data(ID2Type.region, [[iname.access_slope.value]]),
        rname.pepperpain_prairie:
            ID2Data(ID2Type.region, [[iname.access_prairie.value]])
    },
    rname.ssc_o: {
        rname.slippery_slope:
            ID2Data(ID2Type.region),
        rname.d5_s:
            ID2Data(ID2Type.region)
    },
    # Pepperpain Caves
    rname.ppc_a: {
        lname.ppc_cowbun_combat:
            ID2Data(ID2Type.location, [[iname.basic_combat.value]])
    },
    rname.ppc_b: {
        lname.ppc_brutus_combat:
            ID2Data(ID2Type.location, [[iname.basic_combat.value, iname.roll.value]])
    },
    rname.ppc_c: {
        rname.pepperpain_prairie:
            ID2Data(ID2Type.region),
        rname.pepperpain_trail:
            ID2Data(ID2Type.region)
    },
    rname.ppc_d: {
        rname.pepperpain_prairie:
            ID2Data(ID2Type.region),
        rname.promenade_path:
            ID2Data(ID2Type.region)
    },
    rname.ppc_e: {
        # hint bee ...NEXT TO...
    },
    rname.ppc_f: {
        lname.ppc_torch_disappearing_path:
            ID2Data(ID2Type.location, [[iname.melee.value],
                                       [iname.weapon_projectile.value],
                                       [iname.can_phase_object.value, iname.ice.value, iname.roll.value],
                                       [iname.can_phase_gap.value, iname.roll.value, iname.can_open_chests.value]])
    },
    rname.ppc_g: {
        lname.ppc_spiky_hint_bee:
            ID2Data(ID2Type.location, [[iname.can_open_chests.value]])
    },
    rname.ppc_h: {
        lname.ppc_cannon_path:
            ID2Data(ID2Type.location, [[iname.can_open_chests.value]])
    },
    rname.ppc_i: {
        # hint volcano
    },
    rname.ppc_j: {
        lname.ppc_volcano_trail:
            ID2Data(ID2Type.location, [[iname.basic_combat.value]])
    },
    rname.ppc_k: {
        lname.ppc_barrel_hint_bee:
            ID2Data(ID2Type.location, [[iname.can_open_chests.value]])
    },
    rname.ppc_l: {
        lname.ppc_haunted_guns:
            ID2Data(ID2Type.location, [[iname.can_open_chests.value]])
    },
    rname.ppc_m: {
        # abandoned house
    },
    rname.ppc_o: {
        lname.ppc_buzzsaw_path:
            ID2Data(ID2Type.location, [[iname.can_open_chests.value]])
    },
    rname.ppc_p: {
        lname.ppc_number_tiles:
            ID2Data(ID2Type.location, [[iname.can_open_chests.value]])
    },
    rname.ppc_q: {
        # gardener jenny
    },
    rname.ppc_r: {
        rname.pepperpain_trail:
            ID2Data(ID2Type.region),
        rname.pepperpain_mountain:
            ID2Data(ID2Type.region)
    },
    rname.ppc_s: {
        # Bunboy house
    },
    rname.ppc_t: {
        rname.maze_of_steel_d:
            ID2Data(ID2Type.region)
    },
    rname.ppc_u: {
        lname.ppc_pacifist_brute:
            ID2Data(ID2Type.location, [[iname.can_open_chests.value]])
    },
    # Frozen Court Caves
    rname.fcc_a: {
        lname.fcc_bushfire:
            ID2Data(ID2Type.location, [[iname.melee.value]]),
    },
    rname.fcc_b: {
        lname.fcc_cannon_spinner:
            ID2Data(ID2Type.location, [[iname.can_open_chests.value]]),
    },
    rname.fcc_c: {
        lname.fcc_mimicbuns:
            ID2Data(ID2Type.location, [[iname.basic_combat.value]])
    },
    rname.fcc_d: {
        rname.frozen_court:
            ID2Data(ID2Type.region),
        rname.wall_of_text_a:
            ID2Data(ID2Type.region)
    },
    rname.fcc_e: {
        lname.fcc_teleporter_maze:
            ID2Data(ID2Type.location, [[iname.can_open_chests.value]])
    },
    rname.fcc_f: {
        lname.fcc_chilly_roger_combat:
            ID2Data(ID2Type.location, [[iname.basic_combat.value, iname.roll.value]])
    },
    rname.fcc_g: {
        rname.frozen_court:
            ID2Data(ID2Type.region)
    },
    rname.fcc_h: {
        lname.fcc_rickety_bridge:
            ID2Data(ID2Type.location, [[iname.can_open_chests.value]])
    },
    rname.fcc_i: {
        lname.fcc_titans_combat:
        # Force can't knock back titans for some reason
            ID2Data(ID2Type.location, [[iname.weapon_no_force.value],
                                       # Just wait for the titans to fall into the pit on their own
                                       [iname.can_phase_gap.value, iname.can_open_chests.value]]),
        rname.fcc_p:
            ID2Data(ID2Type.region, [[iname.force_jump.value],
                                     [iname.can_phase_gap.value, iname.weapon_no_force.value]])
    },
    rname.fcc_j: {
        lname.fcc_crystal_path:
            ID2Data(ID2Type.location, [[iname.weapon_any.value],
                                       [iname.can_phase_gap.value, iname.can_open_chests.value]])
    },
    rname.fcc_k: {
        lname.fcc_teleporter_grate:
            ID2Data(ID2Type.location, [[iname.can_open_chests.value]])
    },
    rname.fcc_l: {
        lname.fcc_hint_hermit:
            ID2Data(ID2Type.location, [[iname.can_open_chests.value]])
    },
    rname.fcc_m: {
        rname.frozen_court:
            ID2Data(ID2Type.region),
        rname.frozen_island:
            ID2Data(ID2Type.region, [[iname.roll.value]])
    },
    rname.fcc_o: {
        rname.frozen_island:
            ID2Data(ID2Type.region),
        rname.lost_city_d:
            ID2Data(ID2Type.region)
    },
    rname.fcc_p: {
        rname.frozen_court:
            ID2Data(ID2Type.region),
        rname.fcc_i:
        # interestingly, you can open it this way with any weapon, but other way can't be done with force
            ID2Data(ID2Type.region, [[iname.weapon_any.value]])
    },
    # Lonely Road Caves
    rname.lrc_a: {
        rname.lonely_road_a:
            ID2Data(ID2Type.region),
        rname.moon_garden_south:
            ID2Data(ID2Type.region),
    },
    rname.lrc_b: {
        lname.lrc_timed_platforms:
            ID2Data(ID2Type.location, [[iname.weapon_any.value]]),
    },
    rname.lrc_c: {
        lname.lrc_timed_number_tiles:
            ID2Data(ID2Type.location, [[iname.weapon_any.value]]),
    },
    rname.lrc_d: {
        lname.lrc_volcano:
            ID2Data(ID2Type.location, [[iname.can_open_chests.value]]),
    },
    rname.lrc_e_upper: {
        rname.lonely_road_b:
            ID2Data(ID2Type.region),
        rname.lonely_road_c_garden:
            ID2Data(ID2Type.region),
        rname.lrc_e_lower:
        # one-way path
            ID2Data(ID2Type.region),
    },
    rname.lrc_e_lower: {
        rname.lonely_road_c_entrance:
            ID2Data(ID2Type.region),
        rname.lrc_e_upper:
            ID2Data(ID2Type.region, [[iname.can_phase_gap.value, iname.roll.value],
                                     [iname.can_phase_gap_difficult.value]]),
    },
    rname.lrc_f: {
        rname.lonely_road_c_garden:
            ID2Data(ID2Type.region, [[iname.roll.value]]),
        rname.lonely_road_c_pond_trail:
            ID2Data(ID2Type.region, [[iname.roll.value]])
    },
    rname.lrc_g: {
        rname.lonely_road_c_entrance:
            ID2Data(ID2Type.region),
        rname.lonely_road_c_lightning_rock_trail:
            ID2Data(ID2Type.region, [[iname.weapon_any.value],
                                     [iname.can_phase_gap.value, iname.roll],
                                     [iname.can_phase_gap_difficult.value]]),
    },
    rname.lrc_h: {
        rname.lonely_road_c_lightning_rock_trail:
            ID2Data(ID2Type.region),
        rname.lonely_road_c_lake:
            ID2Data(ID2Type.region),
        rname.lonely_road_c_pond_trail:
            ID2Data(ID2Type.region)
    },
    rname.lrc_i_left: {
        rname.lonely_road_c_lake:
            ID2Data(ID2Type.region),
        rname.lrc_i_right:
            ID2Data(ID2Type.region, [[iname.can_phase_gap_difficult.value]])
    },
    rname.lrc_i_right: {
        rname.forbidden_area_south:
            ID2Data(ID2Type.region),
        rname.lrc_i_left:
            ID2Data(ID2Type.region, [[iname.roll.value],
                                     [iname.can_phase_gap_difficult.value]]),
    },
    rname.lrc_j: {
        rname.lonely_road_e:
            ID2Data(ID2Type.region, [[iname.roll.value]]),
        rname.forbidden_area_south:
            ID2Data(ID2Type.region, [[iname.roll.value]]),
    },
    rname.lrc_k: {
        lname.lrc_lava_fans:
            ID2Data(ID2Type.location, [[iname.can_open_chests.value]]),
    },
    rname.lrc_l: {
        # Carrot cave
    },
    rname.lrc_m: {
        lname.lrc_force_turrets:
            ID2Data(ID2Type.location, [[iname.can_open_chests.value]]),
    },
    rname.lrc_n: {
        # Flower Jenny Cave
    },
    rname.lrc_o: {
        # Jenny Cat Cave, Mjau
    },
    rname.lrc_p: {
        lname.lrc_hint_shark:
            ID2Data(ID2Type.location, [[iname.can_open_chests.value]]),
    },
    rname.lrc_q: {
        # Flower Jenny house
    },
    rname.lrc_r: {
        lname.lrc_teleporter_cube:
            ID2Data(ID2Type.location, [[iname.can_open_chests.value]]),
    },
    rname.lrc_s: {
        lname.lrc_dark_maze:
            ID2Data(ID2Type.location, [[iname.weapon_no_dynamite.value]]),
    },
    rname.lrc_t: {
        lname.lrc_block_factory:
            ID2Data(ID2Type.location, [[iname.melee.value],
                                       [iname.can_phase_gap.value, iname.roll.value],
                                       [iname.can_phase_dynamite.value]]),
    },
    rname.lrc_u: {
        rname.lonely_road_d:
            ID2Data(ID2Type.region),
        rname.northern_end_e:
            ID2Data(ID2Type.region, [[iname.melee.value],
                                     [iname.dynamite.value],
                                     [iname.can_phase_object.value, iname.ice.value, iname.roll.value]]),
    },
    rname.dreamworld_hub: {
        rname.fluffy_fields:
            ID2Data(ID2Type.region),
        # to simplify logic, we're going to assume we can make the block in the hub always phasable
        rname.dreamworld_force:
            ID2Data(ID2Type.region, [[iname.force.value],
                                     [iname.can_phase_gap.value, iname.roll.value],
                                     [iname.open_dw.value]]),
        rname.dreamworld_dynamite:
            ID2Data(ID2Type.region, [[iname.dynamite.value],
                                     [iname.can_phase_object_difficult.value, iname.ice.value, iname.roll.value],
                                     [iname.open_dw.value]]),
        rname.dreamworld_ice:
            ID2Data(ID2Type.region, [[iname.ice.value],
                                     [iname.force.value, iname.can_phase_object.value, iname.roll.value],
                                     [iname.open_dw.value]]),
        rname.dreamworld_fire_chain:
            ID2Data(ID2Type.region, [[iname.fire_sword.value, iname.chain.value],
                                     [iname.fire_sword.value, iname.can_phase_object.value, iname.ice.value,
                                      iname.roll.value],
                                     [iname.can_phase_dynamite.value, iname.roll.value],
                                     [iname.open_dw.value]]),
        rname.dreamworld_end:
            ID2Data(ID2Type.region, [[iname.dw_finished_dungeon.value + "*4", iname.ice.value, iname.fire_mace.value],
                                     [iname.can_phase_object.value, iname.ice.value, iname.roll.value],
                                     [iname.can_phase_gap.value, iname.dw_finished_dungeon.value + "*4", iname.fire_mace.value],
                                     [iname.can_phase_gap.value, iname.dw_finished_dungeon.value + "*3", iname.ice.value,
                                      iname.fire_mace.value],
                                     [iname.can_phase_object.value, iname.dw_finished_dungeon.value + "*3", iname.force.value,
                                      iname.fire_mace.value, iname.roll.value],
                                     [iname.can_phase_object.value, iname.dw_finished_dungeon.value + "*2", iname.ice.value,
                                      iname.force.value, iname.fire_mace.value]]),
        rname.house_of_secrets:
            ID2Data(ID2Type.region, [[iname.force_jump.value],
                                     [iname.can_phase_object.value, iname.ice.value, iname.roll.value],
                                     [iname.can_phase_dynamite.value, iname.roll.value]]),
    },
    # You can always warp to the DW hub
    rname.dreamworld_force: {
        rname.dreamworld_hub:
            ID2Data(ID2Type.region),
        rname.df_ad:
            ID2Data(ID2Type.region),
    },
    rname.dreamworld_dynamite: {
        rname.dreamworld_hub:
            ID2Data(ID2Type.region),
        rname.dd_au:
            ID2Data(ID2Type.region),
    },
    rname.dreamworld_ice: {
        rname.dreamworld_hub:
            ID2Data(ID2Type.region),
        rname.di_h:
            ID2Data(ID2Type.region),
    },
    rname.dreamworld_fire_chain: {
        rname.dreamworld_hub:
            ID2Data(ID2Type.region),
        rname.dfc_q:
            ID2Data(ID2Type.region),
    },
    rname.dreamworld_end: {
        rname.dreamworld_hub:
            ID2Data(ID2Type.region),
        rname.da_b:
            ID2Data(ID2Type.region),
    },

    # Dungeons
    # Pillow Fort
    rname.d1_a: {
        rname.d1_b:
            ID2Data(ID2Type.region, [[iname.basic_combat.value]])
    },
    rname.d1_b: {
        rname.d1_c:
            ID2Data(ID2Type.region)
    },
    rname.d1_c: {
        lname.d1_boss_reward:
            ID2Data(ID2Type.location, [[iname.basic_combat.value, iname.roll.value]]),
        rname.d1_b:
            ID2Data(ID2Type.region, [[iname.basic_combat.value, iname.roll.value]])
    },
    rname.d1_d: {
        rname.d1_g:
            ID2Data(ID2Type.region, [[iname.d1_key.value + "*2"]]),
        rname.d1_a:
            ID2Data(ID2Type.region, [[iname.weapon_any.value],
                                     [iname.can_phase_object.value]])
    },
    rname.d1_e: {
        lname.d1_safety_jenny_gate:
            ID2Data(ID2Type.location, [[iname.basic_combat.value],
                                       [iname.can_phase_enemy_difficult.value]]),
        rname.d1_f:
            ID2Data(ID2Type.region, [[iname.weapon_any.value]]),
        rname.d1_h:
            ID2Data(ID2Type.region)
    },
    rname.d1_f: {
        rname.d1_e:
            ID2Data(ID2Type.region, [[iname.weapon_any.value]])
    },
    rname.d1_g: {
        lname.d1_crayon:
            ID2Data(ID2Type.location, [[iname.basic_combat.value]]),
        rname.d1_d:
            ID2Data(ID2Type.region, [[iname.d1_key.value + "*2"]]),
        rname.d1_h:
            ID2Data(ID2Type.region),
        rname.d1_j:
            ID2Data(ID2Type.region),
    },
    rname.d1_h: {
        rname.d1_e:
            ID2Data(ID2Type.region),
        rname.d1_g:
            ID2Data(ID2Type.region),
        rname.d1_j:
            ID2Data(ID2Type.region),
        rname.d1_k:
            ID2Data(ID2Type.region, [[iname.d1_key.value + "*2"]]),
    },
    rname.d1_i: {
        lname.d1_treasure:
            ID2Data(ID2Type.location, [[iname.can_open_chests.value]]),
        rname.d1_h:
            ID2Data(ID2Type.region),
        rname.d1_k:
            ID2Data(ID2Type.region),
    },
    rname.d1_j: {
        lname.d1_shellbun_nest:
            ID2Data(ID2Type.location),
        rname.d1_g:
            ID2Data(ID2Type.region),
        rname.d1_h:
            ID2Data(ID2Type.region),
    },
    rname.d1_k: {
        rname.d1_h:
            ID2Data(ID2Type.region, [[iname.d1_key.value + "*2"]]),
        rname.d1_i:
            ID2Data(ID2Type.region),
    },
    # Sand Castle
    rname.d2_a: {
        lname.d2_boss_reward:
            ID2Data(ID2Type.location, [[iname.basic_combat.value, iname.roll.value]]),
        rname.d2_b:
            ID2Data(ID2Type.region, [[iname.basic_combat.value, iname.roll.value]])
    },
    rname.d2_b: {
        rname.d2_a:
            ID2Data(ID2Type.region),
        rname.d2_f:
            ID2Data(ID2Type.region)
    },
    rname.d2_c: {
        rname.d2_d:
            ID2Data(ID2Type.region, [[iname.weapon_any.value]]),
        rname.d2_h:
            ID2Data(ID2Type.region, [[iname.weapon_any.value]])
    },
    rname.d2_d: {
        lname.d2_spikebun_dunes:
            ID2Data(ID2Type.location, [[iname.weapon_any.value]]),
        rname.d2_c:
            ID2Data(ID2Type.region, [[iname.weapon_any.value]]),
        rname.d2_h:
            ID2Data(ID2Type.region)
    },
    rname.d2_e: {
        rname.d2_f:
            ID2Data(ID2Type.region, [[iname.basic_combat.value]]),
        rname.d2_i:
            ID2Data(ID2Type.region, [[iname.d2_key.value + "*2"]])
    },
    rname.d2_f: {
        rname.d2_b:
            ID2Data(ID2Type.region, [[iname.force.value],
                                     [iname.can_phase_object.value, iname.ice.value, iname.roll.value]]),
        rname.d2_g:
            ID2Data(ID2Type.region)
    },
    rname.d2_g: {
        lname.d2_crayon:
            ID2Data(ID2Type.location, [[iname.force.value],
                                       [iname.melee.value, iname.chain.value],
                                       [iname.dynamite.value],
                                       [iname.fire_mace.value],
                                       [iname.can_phase_object.value, iname.ice.value],
                                       [iname.can_open_chests.value, iname.can_phase_enemy.value]]),
        rname.d2_h:
            ID2Data(ID2Type.region),
        rname.d2_i:
            ID2Data(ID2Type.region),
        rname.d2_f:
            ID2Data(ID2Type.region, [[iname.fire_sword.value]]),
        rname.sweetwater_coast:
            ID2Data(ID2Type.region)
    },
    rname.d2_h: {
        rname.d2_c:
            ID2Data(ID2Type.region, [[iname.weapon_any.value]]),
        rname.d2_d:
            ID2Data(ID2Type.region),
        rname.d2_g:
            ID2Data(ID2Type.region),
        rname.d2_j:
            ID2Data(ID2Type.region, [[iname.dynamite.value],
                                     [iname.can_phase_object.value, iname.ice.value],
                                     [iname.can_phase_enemy.value]]),
        rname.d2_k:
            ID2Data(ID2Type.region, [[iname.d2_key.value + "*2"]])
    },
    rname.d2_i: {
        lname.d2_orbiting_balls:
            ID2Data(ID2Type.location, [[iname.melee.value],
                                       [iname.can_phase_doors.value, iname.d2_key.value + "*2"],
                                       [iname.can_phase_dynamite.value]]),
        rname.d2_e:
            ID2Data(ID2Type.region, [[iname.d2_key.value + "*2", iname.melee.value],
                                     [iname.d2_key.value + "*2", iname.can_phase_doors.value],
                                     [iname.d2_key.value + "*2", iname.can_phase_dynamite.value]]),
        rname.d2_g:
            ID2Data(ID2Type.region)
    },
    rname.d2_j: {
        lname.d2_treasure:
            ID2Data(ID2Type.location, [[iname.can_open_chests.value]]),
        rname.d2_h:
            ID2Data(ID2Type.region, [[iname.force.value],
                                     [iname.can_phase_object.value, iname.ice.value]])
    },
    rname.d2_k: {
        rname.d2_h:
            ID2Data(ID2Type.region, [[iname.d2_key.value + "*2"]]),
        rname.d2_j:
            ID2Data(ID2Type.region, [[iname.basic_combat.value]])
    },
    # Art Exhibit
    rname.d3_a: {
        lname.d3_business_casual_man:
            ID2Data(ID2Type.location),
    },
    rname.d3_b: {
        rname.d3_a:
            ID2Data(ID2Type.region, [[iname.basic_combat.value]]),
        rname.d3_c:
            ID2Data(ID2Type.region, [[iname.d3_key.value + "*4"]]),
        rname.d3_e:
            ID2Data(ID2Type.region, [[iname.d3_key.value + "*4"]]),
    },
    rname.d3_c: {
        rname.d3_b:
            ID2Data(ID2Type.region, [[iname.d3_key.value + "*3"]]),
        rname.d3_d:
            ID2Data(ID2Type.region),
    },
    rname.d3_d: {
        lname.d3_boss_reward:
            ID2Data(ID2Type.location, [[iname.basic_combat.value, iname.roll.value]]),
        rname.d3_c:
            ID2Data(ID2Type.region, [[iname.basic_combat.value, iname.roll.value]]),
    },
    rname.d3_e: {
        lname.d3_spike_floor:
            ID2Data(ID2Type.location),
        rname.d3_b:
            ID2Data(ID2Type.region, [[iname.d3_key.value + "*3"]]),
        rname.d3_c:
            ID2Data(ID2Type.region, [[iname.fire_sword.value]]),
        rname.d3_h:
            ID2Data(ID2Type.region),
    },
    rname.d3_f: {
        lname.d3_crayon:
            ID2Data(ID2Type.location, [[iname.weapon_no_dynamite.value, iname.dynamite.value],
                                       [iname.melee.value, iname.chain.value],
                                       [iname.can_phase_object.value, iname.ice.value]]),
        rname.d3_g:
            ID2Data(ID2Type.region),
    },
    rname.d3_g: {
        rname.d3_f:
            ID2Data(ID2Type.region),
        rname.d3_j:
            ID2Data(ID2Type.region, [[iname.weapon_any.value]]),
        rname.d3_s:
            ID2Data(ID2Type.region),
    },
    rname.d3_h: {
        rname.d3_e:
            ID2Data(ID2Type.region),
        rname.d3_g:
            ID2Data(ID2Type.region, [[iname.basic_combat.value]]),
        rname.d3_i:
            ID2Data(ID2Type.region, [[iname.weapon_any.value]]),
        rname.d3_k:
        # odd, since you'd never come this way normally
            ID2Data(ID2Type.region, [[iname.basic_combat.value]]),
    },
    rname.d3_i: {
        rname.d3_h:
            ID2Data(ID2Type.region, [[iname.weapon_any.value]]),
    },
    rname.d3_j: {
        rname.d3_k:
            ID2Data(ID2Type.region),
        rname.d3_l:
            ID2Data(ID2Type.region, [[iname.d3_key.value + "*4"]]),
    },
    rname.d3_k: {
        rname.d3_h:
            ID2Data(ID2Type.region, [[iname.dynamite.value],
                                     [iname.can_phase_object.value, iname.ice.value],
                                     [iname.can_phase_gap_difficult.value, iname.roll.value]]),
        rname.d3_j:
            ID2Data(ID2Type.region),
        rname.d3_m:
            ID2Data(ID2Type.region),
    },
    rname.d3_l: {
        lname.d3_treasure:
            ID2Data(ID2Type.location, [[iname.can_open_chests.value]]),
        rname.d3_j:
            ID2Data(ID2Type.region, [[iname.d3_key.value + "*4"]]),
    },
    rname.d3_m: {
        rname.d3_j:
            ID2Data(ID2Type.region, [[iname.weapon_projectile.value],
                                     [iname.melee.value, iname.chain.value],
                                     [iname.can_phase_object.value, iname.ice.value]]),
        rname.d3_k:
            ID2Data(ID2Type.region),
        rname.d3_n:
            ID2Data(ID2Type.region),
    },
    rname.d3_n: {
        lname.d3_evil_easels:
            ID2Data(ID2Type.location),
    },
    rname.d3_o: {
        rname.d3_j:
            ID2Data(ID2Type.region, [[iname.basic_combat.value]]),
    },
    rname.d3_p: {
        rname.d3_m:
            ID2Data(ID2Type.region, [[iname.weapon_any.value]]),
        rname.d3_o:
            ID2Data(ID2Type.region, [[iname.force.value],
                                     [iname.ice.value],
                                     [iname.can_phase_object.value]]),
        rname.d3_r:
            ID2Data(ID2Type.region, [[iname.d3_key.value + "*1"]]),
    },
    rname.d3_q: {
        rname.d3_r:
            ID2Data(ID2Type.region),
        rname.fancy_hilltop:
            ID2Data(ID2Type.region)
    },
    rname.d3_r: {
        lname.d3_entry_combat:
            ID2Data(ID2Type.location, [[iname.basic_combat.value],
                                       [iname.can_phase_object.value, iname.ice.value, iname.roll.value]]),
        rname.d3_p:
            ID2Data(ID2Type.region, [[iname.d3_key.value + "*1"]]),
        rname.d3_q:
            ID2Data(ID2Type.region),
        rname.d3_s:
            ID2Data(ID2Type.region, [[iname.dynamite.value, iname.weapon_no_dynamite.value],
                                     [iname.melee.value, iname.chain.value, iname.can_phase_gap_difficult.value,
                                      iname.roll.value]])
    },
    rname.d3_s: {
        rname.d3_g:
            ID2Data(ID2Type.region),
        rname.d3_r:
            ID2Data(ID2Type.region),
    },
    # Trash Cave
    rname.d4_a: {
        rname.d4_b:
            ID2Data(ID2Type.region),
        rname.d4_e:
            ID2Data(ID2Type.region, [[iname.d4_key.value + "*4"]]),
    },
    rname.d4_b: {
        lname.d4_boss_reward:
            ID2Data(ID2Type.location, [[iname.basic_combat.value, iname.roll.value]]),
        rname.d4_a:
            ID2Data(ID2Type.region, [[iname.basic_combat.value, iname.roll.value]]),
    },
    rname.d4_c: {
        rname.d4_d:
            ID2Data(ID2Type.region),
        rname.d4_p:
            ID2Data(ID2Type.region),
    },
    rname.d4_d: {
        lname.d4_treasure:
            ID2Data(ID2Type.location, [[iname.can_open_chests.value]]),
        rname.d4_c:
            ID2Data(ID2Type.region),
        rname.d4_f:
            ID2Data(ID2Type.region, [[iname.d4_key.value + "*4", iname.weapon_any.value],
                                     [iname.can_phase_gap.value, iname.d4_key.value + "*4"]]),
    },
    rname.d4_e: {
        lname.d4_block_maze:
            ID2Data(ID2Type.location, [[iname.basic_combat.value]]),
        rname.d4_a:
            ID2Data(ID2Type.region, [[iname.d4_key.value + "*4"]]),
        rname.d4_h:
            ID2Data(ID2Type.region, [[iname.d4_key.value + "*3"]]),
    },
    rname.d4_f: {
        rname.d4_d:
            ID2Data(ID2Type.region, [[iname.d4_key.value + "*4"]]),
        rname.d4_g_left:
            ID2Data(ID2Type.region, [[iname.force.value],
                                     [iname.can_phase_gap.value]]),
        rname.d4_j:
            ID2Data(ID2Type.region),
    },
    rname.d4_g_left: {
        lname.d4_rotnip_combat:
            ID2Data(ID2Type.location),
        rname.d4_f:
            ID2Data(ID2Type.region),
        rname.d4_g_right:
            ID2Data(ID2Type.region, [[iname.can_phase_dynamite.value],
                                     [iname.can_phase_enemy.value]]),
    },
    rname.d4_g_right: {
        rname.d4_g_left:
            ID2Data(ID2Type.region, [[iname.basic_combat.value]]),
    },
    rname.d4_h: {
        lname.d4_mimic_combat:
            ID2Data(ID2Type.location),
        rname.d4_e:
            ID2Data(ID2Type.region, [[iname.d4_key.value + "*3"]]),
    },
    rname.d4_i: {
        rname.d4_f:
            ID2Data(ID2Type.region),
        rname.d4_l:
            ID2Data(ID2Type.region, [[iname.d4_key.value + "*3"]]),
    },
    rname.d4_j: {
        rname.d4_f:
            ID2Data(ID2Type.region),
        rname.d4_g_right:
            ID2Data(ID2Type.region, [[iname.basic_combat.value]]),
    },
    rname.d4_k: {
        rname.d4_h:
            ID2Data(ID2Type.region, [[iname.melee.value],
                                     [iname.force.value],
                                     [iname.ice.value]]),
        rname.d4_n_upper:
            ID2Data(ID2Type.region),
        rname.d4_s:
            ID2Data(ID2Type.region, [[iname.weapon_any.value]]),
    },
    rname.d4_l: {
        rname.d4_i:
            ID2Data(ID2Type.region, [[iname.d4_key.value + "*3"]]),
        rname.d4_m:
            ID2Data(ID2Type.region, [[iname.melee.value, iname.chain.value],
                                     [iname.can_phase_object.value, iname.ice.value, iname.weapon_projectile.value]]),
        rname.d4_n_lower:
            ID2Data(ID2Type.region),
        rname.d4_q:
            ID2Data(ID2Type.region),
    },
    rname.d4_m: {
        lname.d4_crayon:
            ID2Data(ID2Type.location, [[iname.melee.value],
                                       [iname.ice.value, iname.force.value],
                                       [iname.can_phase_object.value]]),
        rname.d4_l:
            ID2Data(ID2Type.region, [[iname.weapon_any.value]]),
        rname.d4_t:
            ID2Data(ID2Type.region, [[iname.weapon_any.value]]),
    },
    rname.d4_n_lower: {
        lname.d4_ice_barricade:
            ID2Data(ID2Type.location, [[iname.weapon_any.value],
                                       [iname.can_phase_object.value]]),
        rname.d4_l:
            ID2Data(ID2Type.region),
        rname.d4_n_upper:
            ID2Data(ID2Type.region, [[iname.fire_sword.value],
                                     [iname.can_phase_doors.value],
                                     [iname.can_phase_object.value]]),
    },
    rname.d4_n_upper: {
        rname.d4_k:
            ID2Data(ID2Type.region),
        rname.d4_n_lower:
            ID2Data(ID2Type.region, [[iname.fire_sword.value],
                                     [iname.can_phase_doors.value],
                                     [iname.can_phase_object.value]]),
    },
    rname.d4_o: {
        rname.d4_m:
            ID2Data(ID2Type.region, [[iname.basic_combat.value]]),
    },
    rname.d4_p: {
        rname.d4_c:
            ID2Data(ID2Type.region),
        rname.d4_n_lower:
            ID2Data(ID2Type.region),
        rname.d4_q:
            ID2Data(ID2Type.region),
    },
    rname.d4_q: {
        rname.d4_l:
            ID2Data(ID2Type.region, [[iname.dynamite.value, iname.force.value],
                                     [iname.can_phase_object.value, iname.ice.value]]),
        rname.d4_o:
            ID2Data(ID2Type.region),
        rname.d4_p:
            ID2Data(ID2Type.region, [[iname.force.value],
                                     [iname.can_phase_object.value]]),
    },
    rname.d4_r: {
        rname.d4_q:
            ID2Data(ID2Type.region, [[iname.melee.value]]),
        rname.star_woods:
            ID2Data(ID2Type.region),
    },
    rname.d4_s: {
        rname.d4_k:
            ID2Data(ID2Type.region, [[iname.weapon_any.value]]),
    },
    rname.d4_t: {
        rname.d4_m:
            ID2Data(ID2Type.region, [[iname.weapon_any.value]]),
    },
    # Flooded Basement
    rname.d5_a: {
        lname.d5_portal_cube:
            ID2Data(ID2Type.location),
        rname.d5_f:
            ID2Data(ID2Type.region, [[iname.weapon_any.value]]),
    },
    rname.d5_b: {
        rname.d5_a:
            ID2Data(ID2Type.region, [[iname.melee.value],
                                     [iname.force.value, iname.dynamite.value],
                                     # kind of precise?
                                     [iname.ice.value]]),
        rname.d5_e:
            ID2Data(ID2Type.region),
    },
    rname.d5_c: {
        lname.d5_boss_reward:
            ID2Data(ID2Type.location, [[iname.basic_combat.value, iname.roll.value]]),
        rname.d5_d:
            ID2Data(ID2Type.region),
    },
    rname.d5_d: {
        rname.d5_c:
            ID2Data(ID2Type.region),
        rname.d5_h:
            ID2Data(ID2Type.region, [[iname.d5_key.value + "*5"]]),
    },
    rname.d5_e: {
        rname.d5_b:
            ID2Data(ID2Type.region),
    },
    rname.d5_f: {
        rname.d5_g:
            ID2Data(ID2Type.region, [[iname.weapon_projectile.value, iname.ice.value, iname.melee.value],
                                     [iname.can_phase_doors.value, iname.melee.value, iname.chain.value],
                                     [iname.can_phase_object.value, iname.ice.value, iname.roll.value],
                                     [iname.can_phase_dynamite.value],
                                     [iname.can_phase_enemy.value, iname.roll.value, iname.weapon_any.value]]),
        rname.d5_j:
            ID2Data(ID2Type.region),
        rname.d5_k_top:
            ID2Data(ID2Type.region, [[iname.d5_key.value + "*5"]]),
    },
    rname.d5_g: {
        lname.d5_crayon:
            ID2Data(ID2Type.location, [[iname.can_open_chests.value]]),
        rname.d5_f:
            ID2Data(ID2Type.region),
        rname.d5_h:
            ID2Data(ID2Type.region, [[iname.d5_key.value + "*5"]]),
    },
    rname.d5_h: {
        lname.d5_treasure:
            ID2Data(ID2Type.location, [[iname.can_open_chests.value]]),
        rname.d5_d:
            ID2Data(ID2Type.region, [[iname.d5_key.value + "*5"]]),
        rname.d5_g:
            ID2Data(ID2Type.region, [[iname.d5_key.value + "*5"]]),
        rname.d5_i:
            ID2Data(ID2Type.region, [[iname.weapon_any.value]]),
        rname.d5_m:
            ID2Data(ID2Type.region),
        rname.d5_r:
            ID2Data(ID2Type.region),
    },
    rname.d5_i: {
        rname.d5_h:
            ID2Data(ID2Type.region, [[iname.weapon_any.value]]),
        rname.d5_m:
            ID2Data(ID2Type.region, [[iname.weapon_any.value]]),
    },
    rname.d5_j: {
        rname.d5_e:
            ID2Data(ID2Type.region, [[iname.weapon_any.value]]),
        rname.d5_f:
            ID2Data(ID2Type.region),
        rname.d5_k_top:
            ID2Data(ID2Type.region, [[iname.melee.value, iname.chain.value],
                                     [iname.can_phase_dynamite.value]]),
    },
    rname.d5_k_top: {
        lname.d5_k_south_door:
            ID2Data(ID2Type.location, [[]], iname.d5_k_south_door.value),
        rname.d5_f:
            ID2Data(ID2Type.region, [[iname.d5_key.value + "*5"]]),
        rname.d5_j:
            ID2Data(ID2Type.region),
        rname.d5_k_bottom:
            ID2Data(ID2Type.region, [[iname.force_jump.value],
                                     [iname.can_phase_doors.value, iname.d5_k_south_door.value],
                                     [iname.can_phase_object.value, iname.ice.value, iname.roll.value],
                                     [iname.can_phase_dynamite.value]]),
    },
    rname.d5_k_bottom: {
        rname.d5_k_top:
            ID2Data(ID2Type.region, [[iname.can_phase_object.value, iname.ice.value, iname.roll.value]]),
        rname.d5_o_top:
            ID2Data(ID2Type.region, [[iname.d5_k_south_door.value]])
    },
    rname.d5_l: {
        lname.d5_crossway_combat:
            ID2Data(ID2Type.location, [[iname.basic_combat.value]]),
    },
    rname.d5_m: {
        lname.d5_number_blocks:
            ID2Data(ID2Type.location),
        rname.d5_h:
            ID2Data(ID2Type.region),
        rname.d5_i:
            ID2Data(ID2Type.region, [[iname.weapon_any.value]]),
    },
    rname.d5_n: {
        rname.d5_j:
            ID2Data(ID2Type.region, [[iname.basic_combat.value]]),
        rname.d5_o_left:
            ID2Data(ID2Type.region),
    },
    rname.d5_o_left: {
        rname.d5_n:
            ID2Data(ID2Type.region),
        rname.d5_s:
            ID2Data(ID2Type.region),
        rname.d5_o_right:
            ID2Data(ID2Type.region, [[iname.d5_o_block.value],
                                     [iname.ice.value, iname.fire_sword.value],
                                     [iname.can_phase_doors.value]]),
    },
    rname.d5_o_right: {
        rname.d5_o_left:
            ID2Data(ID2Type.region),
        rname.d5_p:
            ID2Data(ID2Type.region),
    },
    rname.d5_o_top: {
        lname.d5_o_block:
            ID2Data(ID2Type.location, [[]], iname.d5_o_block.value),
        rname.d5_k_bottom:
            ID2Data(ID2Type.region, [[iname.d5_k_south_door.value]]),
        rname.d5_o_left:
            ID2Data(ID2Type.region),
        rname.d5_o_right:
            ID2Data(ID2Type.region),
    },
    rname.d5_p: {
        rname.d5_l:
            ID2Data(ID2Type.region, [[iname.basic_combat.value]]),
        rname.d5_o_right:
            ID2Data(ID2Type.region),
        rname.d5_t:
            ID2Data(ID2Type.region, [[iname.d5_key.value + "*4"]]),
    },
    rname.d5_q: {
        rname.d5_h:
            ID2Data(ID2Type.region, [[iname.basic_combat.value]]),
        rname.d5_t:
            ID2Data(ID2Type.region, [[iname.d5_key.value + "*5"]]),
    },
    rname.d5_r: {
        lname.d5_keeled_fishbun:
            ID2Data(ID2Type.location, [[iname.weapon_any.value]]),
        rname.d5_h:
            ID2Data(ID2Type.region),
    },
    rname.d5_s: {
        rname.d5_o_left:
            ID2Data(ID2Type.region),
        rname.ssc_o:
            ID2Data(ID2Type.region),
    },
    rname.d5_t: {
        rname.d5_p:
            ID2Data(ID2Type.region, [[iname.d5_key.value + "*4"]]),
        rname.d5_q:
            ID2Data(ID2Type.region, [[iname.d5_key.value + "*5"]]),
        rname.d5_s:
            ID2Data(ID2Type.region, [[iname.weapon_any.value]]),
        rname.d5_u:
            ID2Data(ID2Type.region),
    },
    rname.d5_u: {
        lname.d5_land_sharks:
            ID2Data(ID2Type.location, [[iname.basic_combat.value]]),
        rname.d5_t:
            ID2Data(ID2Type.region),
    },
    # Potassium Mines
    rname.d6_a: {
        lname.d6_boss_reward:
            ID2Data(ID2Type.location, [[iname.basic_combat.value, iname.roll.value]]),
        rname.d6_b:
            ID2Data(ID2Type.region, [[iname.basic_combat.value, iname.roll.value]]),
    },
    rname.d6_b: {
        rname.d6_a:
            ID2Data(ID2Type.region),
        rname.d6_e:
            ID2Data(ID2Type.region, [[iname.d6_key.value + "*5"]]),
    },
    rname.d6_c: {
        rname.d6_d:
            ID2Data(ID2Type.region, [[iname.ice.value]]),
    },
    rname.d6_d: {
        lname.d6_ice_tutorial:
            ID2Data(ID2Type.location, [[iname.ice.value],
                                       [iname.force.value, iname.can_phase_gap.value],
                                       [iname.can_phase_dynamite.value]]),
        rname.d6_i:
            ID2Data(ID2Type.region, [[iname.ice.value],
                                     [iname.force.value, iname.can_phase_gap.value]])
    },
    rname.d6_e: {
        rname.d6_b:
            ID2Data(ID2Type.region, [[iname.d6_key.value + "*5"]]),
        rname.d6_i:
            ID2Data(ID2Type.region, [[iname.d6_key.value + "*4"]]),
    },
    rname.d6_f: {
        rname.d6_j:
            ID2Data(ID2Type.region, [[iname.weapon_any.value]]),
    },
    rname.d6_g: {
        lname.d6_crayon:
            ID2Data(ID2Type.location, [[iname.can_open_chests.value]]),
        rname.d6_l:
            ID2Data(ID2Type.region),
        rname.d6_p:
            ID2Data(ID2Type.region, [[iname.weapon_any.value]]),
    },
    rname.d6_h: {
        rname.d6_c:
            ID2Data(ID2Type.region, [[iname.ice.value, iname.melee.value],
                                     [iname.force_jump.value],
                                     [iname.can_phase_object.value, iname.ice.value, iname.roll.value]]),
        rname.d6_l:
            ID2Data(ID2Type.region, [[iname.ice.value],
                                     [iname.can_phase_gap.value, iname.roll.value]]),
    },
    rname.d6_i: {
        rname.d6_e:
            ID2Data(ID2Type.region, [[iname.d6_key.value + "*4"]]),
        rname.d6_h:
            ID2Data(ID2Type.region, [[iname.ice.value]]),
    },
    rname.d6_j: {
        lname.d6_treasure:
            ID2Data(ID2Type.location, [[iname.can_open_chests.value]]),
        rname.d6_f:
            ID2Data(ID2Type.region, [[iname.weapon_any.value]]),
        rname.d6_n:
            ID2Data(ID2Type.region, [[iname.ice.value],
                                     [iname.can_phase_gap.value, iname.roll.value]]),
    },
    rname.d6_k: {
        rname.d6_j:
            ID2Data(ID2Type.region),
        rname.d6_o_upper:
            ID2Data(ID2Type.region, [[iname.d6_key.value + "*5"]]),
    },
    rname.d6_l: {
        lname.d6_west_minecart_track:
            ID2Data(ID2Type.location),
        rname.d6_m:
            ID2Data(ID2Type.region),
    },
    rname.d6_m: {
        lname.d6_hub_room:
            ID2Data(ID2Type.location),
        rname.d6_l:
            ID2Data(ID2Type.region, [[iname.melee.value, iname.dynamite.value],
                                     [iname.can_phase_doors.value, iname.melee.value, iname.chain.value]]),
        rname.d6_i:
            ID2Data(ID2Type.region, [[iname.ice.value]]),
        rname.d6_r:
            ID2Data(ID2Type.region, [[iname.d6_key.value + "*4"]]),
        rname.d6_s:
            ID2Data(ID2Type.region, [[iname.d6_key.value + "*5"]]),
        rname.d6_u:
            ID2Data(ID2Type.region, [[iname.weapon_no_dynamite.value]]),
    },
    rname.d6_n: {
        lname.d6_number_tiles:
            ID2Data(ID2Type.location),
        rname.d6_j:
            ID2Data(ID2Type.region, [[iname.melee.value, iname.chain.value],
                                     [iname.can_phase_object.value, iname.ice.value]]),
        rname.d6_m:
            ID2Data(ID2Type.region, [[iname.weapon_any.value]]),
        rname.d6_o_upper:
            ID2Data(ID2Type.region, [[iname.weapon_any.value]]),
    },
    rname.d6_o_upper: {
        rname.d6_n:
            ID2Data(ID2Type.region, [[iname.weapon_any.value]]),
        rname.d6_k:
            ID2Data(ID2Type.region, [[iname.d6_key.value + "*5"]]),
        rname.d6_o_lower:
            ID2Data(ID2Type.region, [[iname.can_phase_dynamite.value],
                                     [iname.can_phase_enemy.value, iname.roll.value]]),
    },
    rname.d6_o_lower: {
        rname.d6_o_upper:
            ID2Data(ID2Type.region, [[iname.basic_combat.value]]),
    },
    rname.d6_p: {
        rname.d6_g:
            ID2Data(ID2Type.region, [[iname.weapon_any.value]]),
        rname.d6_q:
            ID2Data(ID2Type.region),
        rname.d6_s:
            ID2Data(ID2Type.region),
    },
    rname.d6_q: {
        rname.d6_m:
            ID2Data(ID2Type.region),
        rname.pepperpain_mountain:
            ID2Data(ID2Type.region),
    },
    rname.d6_r: {
        rname.d6_m:
            ID2Data(ID2Type.region, [[iname.d6_key.value + "*4"]]),
        rname.d6_n:
            ID2Data(ID2Type.region, [[iname.ice.value],
                                     [iname.force.value]]),
        rname.d6_o_lower:
            ID2Data(ID2Type.region),
    },
    rname.d6_s: {
        rname.d6_m:
            ID2Data(ID2Type.region, [[iname.d6_key.value + "*5"]]),
        rname.d6_p:
            ID2Data(ID2Type.region),
    },
    rname.d6_t: {
        lname.d6_south_conveyor:
            ID2Data(ID2Type.location),
        rname.d6_m:
            ID2Data(ID2Type.region),
    },
    rname.d6_u: {
        rname.d6_t:
            ID2Data(ID2Type.region),
    },
    # Boiling Grave
    rname.d7_a: {
        rname.d7_b:
            ID2Data(ID2Type.region, [[iname.melee.value]]),
        rname.d7_g:
            ID2Data(ID2Type.region, [[iname.d7_key.value + "*5"]]),
    },
    rname.d7_b: {
        lname.d7_crayon:
            ID2Data(ID2Type.location, [[iname.weapon_projectile.value],
                                       [iname.melee.value, iname.chain.value],
                                       [iname.can_phase_gap.value, iname.roll.value, iname.can_open_chests.value]]),
        rname.d7_a:
            ID2Data(ID2Type.region),
    },
    rname.d7_c: {
        rname.d7_d:
            ID2Data(ID2Type.region, [[iname.melee.value],
                                     # can just bait everything into the pit
                                     [iname.can_phase_doors.value]]),
        rname.d7_h:
            ID2Data(ID2Type.region),
    },
    rname.d7_d: {
        lname.d7_chilly_roger_combat:
            ID2Data(ID2Type.location, [[iname.basic_combat.value, iname.roll.value]]),
    },
    rname.d7_e: {
        lname.d7_boss_reward:
            ID2Data(ID2Type.location, [[iname.basic_combat.value, iname.roll.value]]),
        rname.d7_f:
            ID2Data(ID2Type.region, [[iname.basic_combat.value, iname.roll.value]]),
    },
    rname.d7_f: {
        rname.d7_e:
            ID2Data(ID2Type.region),
    },
    rname.d7_g: {
        rname.d7_a:
            ID2Data(ID2Type.region, [[iname.d7_key.value + "*5"]]),
        rname.d7_k:
            ID2Data(ID2Type.region, [[iname.melee.value],
                                     [iname.ice.value]]),
    },
    rname.d7_h: {
        rname.d7_c:
            ID2Data(ID2Type.region),
        rname.d7_g:
            ID2Data(ID2Type.region, [[iname.basic_combat.value, iname.roll.value]]),
        rname.d7_i:
            ID2Data(ID2Type.region, [[iname.d7_key.value + "*5"]]),
        rname.d7_l:
            ID2Data(ID2Type.region, [[iname.weapon_any.value]]),
    },
    rname.d7_i: {
        rname.d7_h:
            ID2Data(ID2Type.region, [[iname.d7_key.value + "*5"]]),
        rname.d7_j:
            ID2Data(ID2Type.region, [[iname.melee.value, iname.roll.value],
                                     [iname.force.value, iname.roll.value],
                                     [iname.dynamite.value, iname.roll.value]])
    },
    rname.d7_j: {
        rname.d7_f:
            ID2Data(ID2Type.region, [[iname.melee.value, iname.chain.value],
                                     [iname.can_phase_object.value, iname.weapon_no_dynamite.value]]),

    },
    rname.d7_k: {
        lname.d7_royal_tomb:
            ID2Data(ID2Type.location, [[iname.melee.value, iname.chain.value],
                                       [iname.can_phase_object.value, iname.weapon_any.value]]),
    },
    rname.d7_l: {
        rname.d7_h:
            ID2Data(ID2Type.region, [[iname.weapon_any.value]]),
        rname.d7_m:
            ID2Data(ID2Type.region, [[iname.d7_key.value + "*3"]]),
        rname.d7_aa:
            ID2Data(ID2Type.region),
    },
    rname.d7_m: {
        rname.d7_l:
            ID2Data(ID2Type.region, [[iname.d7_key.value + "*3"]]),
        rname.d7_o:
            ID2Data(ID2Type.region),
    },
    rname.d7_n: {
        rname.d7_r:
            ID2Data(ID2Type.region, [[iname.weapon_any.value]]),
    },
    rname.d7_o: {
        lname.d7_roll_pillars:
            ID2Data(ID2Type.location, [[iname.roll.value],
                                       [iname.can_phase_dynamite.value]]),
        rname.d7_s:
            ID2Data(ID2Type.region),
    },
    rname.d7_p: {
        rname.d7_m:
            ID2Data(ID2Type.region, [[iname.melee.value, iname.chain.value],
                                     [iname.can_phase_object.value, iname.weapon_any.value]]),
        rname.d7_q:
            ID2Data(ID2Type.region, [[iname.d7_key.value + "*2"]]),
        rname.d7_u:
            ID2Data(ID2Type.region, [[iname.weapon_any.value]]),
    },
    rname.d7_q: {
        rname.d7_p:
            ID2Data(ID2Type.region, [[iname.melee.value, iname.d7_key.value + "*2"],
                                     [iname.can_phase_doors.value, iname.d7_key.value + "*2"]]),
    },
    rname.d7_r: {
        rname.d7_n:
            ID2Data(ID2Type.region, [[iname.weapon_any.value]]),
        rname.d7_s:
            ID2Data(ID2Type.region, [[iname.d7_key.value + "*5"]]),
        rname.d7_v:
            ID2Data(ID2Type.region, [[iname.basic_combat.value]]),
    },
    rname.d7_s: {
        rname.d7_o:
        # when you freeze the blocks, the enemies can break them
            ID2Data(ID2Type.region, [[iname.ice.value]]),
        rname.d7_r:
            ID2Data(ID2Type.region, [[iname.d7_key.value + "*5"]]),
        rname.d7_t:
            ID2Data(ID2Type.region),
        rname.d7_x:
            ID2Data(ID2Type.region),
    },
    rname.d7_t: {
        lname.d7_skullnips_combat:
        # Technically can be done with nothing without phasing but is kind of annoying
            ID2Data(ID2Type.location, [[iname.basic_combat.value],
                                       [iname.can_phase_gap.value]]),
        rname.d7_s:
            ID2Data(ID2Type.region),
        rname.d7_u:
            ID2Data(ID2Type.region, [[iname.melee.value, iname.chain.value],
                                     [iname.weapon_projectile.value]]),
        rname.d7_y:
            ID2Data(ID2Type.region),
    },
    rname.d7_u: {
        rname.d7_q:
            ID2Data(ID2Type.region, [[iname.roll.value],
                                     [iname.can_phase_gap.value]]),
        rname.d7_t:
            ID2Data(ID2Type.region),
        rname.d7_z:
            ID2Data(ID2Type.region),
    },
    rname.d7_v: {
        rname.d7_w:
            ID2Data(ID2Type.region, [[iname.basic_combat.value, iname.roll.value]]),
    },
    rname.d7_w: {
        lname.d7_treasure:
            ID2Data(ID2Type.location, [[iname.roll.value, iname.can_open_chests.value],
                                       [iname.can_phase_object.value, iname.ice.value]]),
        rname.d7_x:
            ID2Data(ID2Type.region, [[iname.melee.value, iname.chain.value, iname.roll.value],
                                     [iname.melee.value, iname.chain.value, iname.can_phase_object.value,
                                      iname.ice.value],
                                     [iname.can_phase_dynamite.value]]),
    },
    rname.d7_x: {
        rname.d7_s:
            ID2Data(ID2Type.region),
        rname.d7_y:
            ID2Data(ID2Type.region),
    },
    rname.d7_y: {
        rname.d7_t:
            ID2Data(ID2Type.region),
        rname.d7_x:
            ID2Data(ID2Type.region),
        rname.d7_z:
            ID2Data(ID2Type.region),
        rname.frozen_court:
            ID2Data(ID2Type.region),
    },
    rname.d7_z: {
        lname.d7_titans_combat:
            ID2Data(ID2Type.location, [[iname.melee.value],
                                       [iname.can_phase_gap.value]]),
        rname.d7_u:
            ID2Data(ID2Type.region),
        rname.d7_y:
            ID2Data(ID2Type.region)
    },
    rname.d7_aa: {
        rname.d7_l:
            ID2Data(ID2Type.region),
        rname.d7_z:
            ID2Data(ID2Type.region, [[iname.melee.value, iname.chain.value],
                                     [iname.weapon_projectile.value]]),
    },
    # Grand Library
    rname.d8_a: {
        lname.d8_hexrot_combat:
            ID2Data(ID2Type.location, [[iname.basic_combat.value, iname.roll.value]]),
    },
    rname.d8_b_upper: {
        rname.d8_shifting_chambers:
            ID2Data(ID2Type.region),
        rname.d8_b_lower:
            ID2Data(ID2Type.region, [[iname.can_phase_doors.value]]),
    },
    rname.d8_b_lower: {
        rname.d8_b_upper:
            ID2Data(ID2Type.region, [[iname.basic_combat.value, iname.roll.value],
                                     [iname.can_phase_doors.value]]),
        rname.d8_f:
            ID2Data(ID2Type.region),
    },
    rname.d8_c: {
        rname.d8_h:
            ID2Data(ID2Type.region, [[iname.weapon_any.value]]),
        rname.d8_v:
            ID2Data(ID2Type.region),
    },
    rname.d8_d: {
        rname.d8_o:
            ID2Data(ID2Type.region, [[iname.d8_key.value + "*8"],
                                     [iname.glitchless.value, iname.d8_key.value + "*4"]]),
        rname.d8_w:
            ID2Data(ID2Type.region, [[iname.force.value, iname.ice.value, iname.dynamite.value],
                                     [iname.ice.value, iname.can_phase_gap.value, iname.dynamite.value]]),
    },
    rname.d8_e: {
        lname.d8_boss_key:
            ID2Data(ID2Type.location, [[iname.can_open_chests.value]]),
        rname.d8_f:
            ID2Data(ID2Type.region, [[iname.weapon_any.value]]),
        rname.d8_k_left:
            ID2Data(ID2Type.region, [[iname.d8_key.value + "*8"]]),
    },
    rname.d8_f: {
        rname.d8_b_lower:
            ID2Data(ID2Type.region),
        rname.d8_e:
            ID2Data(ID2Type.region, [[iname.weapon_any.value]]),
    },
    rname.d8_g: {
        lname.d8_treasure:
            ID2Data(ID2Type.location, [[iname.can_open_chests.value]]),
    },
    rname.d8_h: {
        rname.d8_c:
            ID2Data(ID2Type.region, [[iname.weapon_any.value]]),
        rname.d8_i:
            ID2Data(ID2Type.region, [[iname.d8_key.value + "*8"],
                                     [iname.glitchless.value, iname.d8_key.value + "*2"]]),
        rname.d8_n:
            ID2Data(ID2Type.region, [[iname.d8_key.value + "*8"],
                                     [iname.glitchless.value, iname.d8_key.value + "*1"]]),
    },
    rname.d8_i: {
        rname.d8_h:
            ID2Data(ID2Type.region, [[iname.d8_key.value + "*8"],
                                     [iname.glitchless.value, iname.d8_key.value + "*2"]]),
        rname.d8_o:
            ID2Data(ID2Type.region, [[iname.d8_key.value + "*8"],
                                     [iname.glitchless.value, iname.d8_key.value + "*3"]]),
    },
    rname.d8_j: {
        rname.d8_a:
            ID2Data(ID2Type.region, [[iname.basic_combat.value, iname.roll.value]]),
        rname.d8_k_left:
            ID2Data(ID2Type.region, [[iname.d8_k_left_door.value]]),
        rname.d8_p_left:
            ID2Data(ID2Type.region, [[iname.weapon_any.value]]),
    },
    rname.d8_k_left: {
        rname.d8_k_right:
            ID2Data(ID2Type.region),
        rname.d8_j:
            ID2Data(ID2Type.region, [[iname.d8_k_left_door.value]]),
        rname.d8_e:
            ID2Data(ID2Type.region, [[iname.d8_key.value + "*8"]]),
    },
    rname.d8_k_right: {
        lname.d8_k_left_door:
            ID2Data(ID2Type.location,
                    [[iname.ice.value, iname.melee.value, iname.chain.value, iname.weapon_projectile.value],
                     [iname.can_phase_doors.value, iname.melee.value, iname.chain.value],
                     [iname.can_phase_object.value, iname.ice.value]], iname.d8_k_left_door.value),
        rname.d8_k_left:
            ID2Data(ID2Type.region, [[iname.can_phase_doors.value, iname.d8_k_left_door.value],
                                     [iname.can_phase_object.value, iname.ice.value]]),
        rname.d8_k_bottom:
            ID2Data(ID2Type.region),
        rname.d8_l:
            ID2Data(ID2Type.region, [[iname.weapon_any.value]]),
    },
    rname.d8_k_bottom: {
        lname.d8_k_right_door:
            ID2Data(ID2Type.location,
                    [[iname.ice.value, iname.melee.value, iname.chain.value, iname.weapon_projectile.value],
                     [iname.can_phase_doors.value, iname.melee.value, iname.chain.value],
                     [iname.can_phase_dynamite.value]], iname.d8_k_right_door.value),
        rname.d8_k_right:
            ID2Data(ID2Type.region, [[iname.can_phase_doors.value, iname.d8_k_right_door.value],
                                     [iname.can_phase_dynamite.value]]),
    },
    rname.d8_l: {
        rname.d8_k_right:
            ID2Data(ID2Type.region, [[iname.d8_k_right_door.value]]),
        rname.d8_aa:
            ID2Data(ID2Type.region),
    },
    rname.d8_m: {
        rname.d8_g:
            ID2Data(ID2Type.region, [[iname.fire_sword.value, iname.chain.value],
                                     [iname.can_phase_dynamite.value, iname.fire_sword.value]]),
        rname.d8_l:
            ID2Data(ID2Type.region, [[iname.fire_mace.value],
                                     [iname.can_phase_dynamite.value, iname.fire_sword.value]]),
        rname.d8_n:
            ID2Data(ID2Type.region, [[iname.fire_mace.value],
                                     [iname.can_phase_dynamite.value, iname.fire_sword.value]]),
        rname.d8_s:
            ID2Data(ID2Type.region, [[iname.fire_mace.value],
                                     [iname.can_phase_dynamite.value, iname.fire_sword.value]]),
    },
    rname.d8_n: {
        rname.d8_h:
            ID2Data(ID2Type.region, [[iname.d8_key.value + "*8"],
                                     [iname.glitchless.value, iname.d8_key.value + "*1"]])
    },
    rname.d8_o: {
        rname.d8_d:
            ID2Data(ID2Type.region, [[iname.d8_key.value + "*8"],
                                     [iname.glitchless.value, iname.d8_key.value + "*4"]]),
        rname.d8_i:
            ID2Data(ID2Type.region, [[iname.d8_key.value + "*8"],
                                     [iname.glitchless.value, iname.d8_key.value + "*3"]]),
        rname.d8_m:
            ID2Data(ID2Type.region, [[iname.ice.value]]),
        rname.d8_u:
            ID2Data(ID2Type.region, [[iname.ice.value],
                                     [iname.can_phase_gap.value, iname.roll.value]]),
    },
    rname.d8_p_left: {
        rname.d8_j:
            ID2Data(ID2Type.region, [[iname.weapon_any.value]]),
        rname.d8_p_right:
            ID2Data(ID2Type.region, [[iname.can_phase_dynamite.value]]),
    },
    rname.d8_p_right: {
        rname.d8_p_left:
            ID2Data(ID2Type.region, [[iname.ice.value, iname.melee.value, iname.weapon_projectile.value]]),
        rname.d8_r:
            ID2Data(ID2Type.region),
    },
    rname.d8_q: {
        lname.d8_crystal_button:
            ID2Data(ID2Type.location, [[iname.ice.value, iname.force.value],
                                       [iname.ice.value, iname.can_phase_gap.value, iname.roll.value],
                                       [iname.can_phase_object.value, iname.ice.value]]),
        rname.d8_k_bottom:
            ID2Data(ID2Type.region,
                    [[iname.melee.value, iname.weapon_projectile.value, iname.dynamite.value, iname.ice.value]]),
        rname.d8_w:
            ID2Data(ID2Type.region, [[iname.d8_key.value + "*8"],
                                     [iname.glitchless.value, iname.d8_key.value + "*7"]]),
    },
    rname.d8_r: {
        rname.d8_m:
            ID2Data(ID2Type.region, [[iname.weapon_any.value]]),
        rname.d8_p_right:
            ID2Data(ID2Type.region),
        rname.d8_x:
            ID2Data(ID2Type.region, [[iname.d8_key.value + "*8"],
                                     [iname.glitchless.value, iname.d8_key.value + "*7"]]),
    },
    rname.d8_s: {
        rname.d8_z:
            ID2Data(ID2Type.region, [[iname.basic_combat.value, iname.roll.value]]),
    },
    rname.d8_t: {
        lname.d8_hidden:
            ID2Data(ID2Type.location, [[iname.force.value, iname.ice.value],
                                       [iname.can_phase_gap.value]]),
        rname.d8_z:
            ID2Data(ID2Type.region, [[iname.weapon_any.value]]),
    },
    rname.d8_u: {
        lname.d8_delayed:
            ID2Data(ID2Type.location, [[iname.force.value, iname.ice.value],
                                       [iname.can_phase_object.value, iname.force.value],
                                       [iname.can_phase_object.value, iname.ice.value]]),
        rname.d8_z:
            ID2Data(ID2Type.region),
    },
    rname.d8_v: {
        rname.d8_c:
            ID2Data(ID2Type.region),
    },
    rname.d8_w: {
        rname.d8_d:
            ID2Data(ID2Type.region),
        rname.d8_q:
            ID2Data(ID2Type.region, [[iname.d8_key.value + "*8"],
                                     [iname.glitchless.value, iname.d8_key.value + "*7"]]),
        rname.d8_x:
            ID2Data(ID2Type.region, [[iname.d8_key.value + "*8"],
                                     [iname.glitchless.value, iname.d8_key.value + "*6"]]),
    },
    rname.d8_x: {
        rname.d8_r:
            ID2Data(ID2Type.region, [[iname.d8_key.value + "*8"],
                                     [iname.glitchless.value, iname.d8_key.value + "*7"]]),
        rname.d8_w:
            ID2Data(ID2Type.region, [[iname.d8_key.value + "*8"],
                                     [iname.glitchless.value, iname.d8_key.value + "*6"]]),
        rname.d8_ab:
            ID2Data(ID2Type.region, [[iname.basic_combat.value, iname.roll.value]]),
    },
    rname.d8_y: {
        rname.d8_m:
            ID2Data(ID2Type.region, [[iname.ice.value]]),
        # can skip directly to the end by just phasing out of bounds and navigating to the loading zone
        rname.d8_shifting_chambers:
            ID2Data(ID2Type.region, [[iname.major_skips.value, iname.can_phase_doors.value]]),
        rname.lonely_road_a:
            ID2Data(ID2Type.region),
    },
    rname.d8_z: {
        rname.d8_t:
            ID2Data(ID2Type.region, [[iname.weapon_any.value]]),
        rname.d8_ac:
            ID2Data(ID2Type.region),
        rname.d8_ad:
            ID2Data(ID2Type.region),
        rname.d8_ae:
            ID2Data(ID2Type.region),
    },
    rname.d8_aa: {
        lname.d8_crayon:
            ID2Data(ID2Type.location, [[iname.weapon_projectile.value],
                                       [iname.can_phase_gap.value, iname.can_open_chests.value],
                                       [iname.can_phase_dynamite.value]]),
        rname.d8_l:
            ID2Data(ID2Type.region),
    },
    rname.d8_ab: {
        lname.d8_carrot_lobotomy:
            ID2Data(ID2Type.location, [[iname.force.value, iname.ice.value],
                                       [iname.can_phase_gap.value, iname.ice.value]]),
    },
    rname.d8_ac: {
        lname.d8_patient:
            ID2Data(ID2Type.location, [[iname.ice.value, iname.force.value, iname.fire_mace.value, iname.chain.value],
                                       [iname.can_phase_object.value, iname.ice.value, iname.fire_sword.value],
                                       [iname.can_phase_dynamite.value, iname.fire_sword.value, iname.chain.value]]),
        rname.d8_z:
            ID2Data(ID2Type.region),
    },
    rname.d8_ad: {
        lname.d8_fighter_combat:
            ID2Data(ID2Type.location, [[iname.basic_combat.value, iname.roll.value],
                                       [iname.can_phase_object.value, iname.ice.value]]),
        rname.d8_z:
            ID2Data(ID2Type.region),
    },
    rname.d8_ae: {
        lname.d8_storied:
            ID2Data(ID2Type.location, [[iname.force.value],
                                       [iname.can_phase_dynamite.value]]),
        rname.d8_z:
            ID2Data(ID2Type.region),
    },
    rname.d8_shifting_chambers: {
        rname.d8_rewards:
            ID2Data(ID2Type.region, [
                [iname.fire_sword.value, iname.dynamite.value, iname.force.value, iname.ice.value, iname.chain.value,
                 iname.roll.value],
                # Ice only is possible, but requires a bit of RNG
                [iname.can_phase_object_difficult.value, iname.ice.value, iname.dynamite.value, iname.roll.value],
                [iname.can_phase_dynamite.value, iname.melee.value, iname.chain.value],
                [iname.can_phase_enemy.value, iname.melee.value, iname.roll.value],
                [iname.can_phase_enemy.value, iname.ice.value, iname.roll.value]]),
    },
    rname.d8_rewards: {
        lname.d8_boss_reward:
            ID2Data(ID2Type.location, [[iname.can_open_chests.value]]),
        lname.d8_boss_reward_extra:
            ID2Data(ID2Type.location, [[iname.can_open_chests.value]]),
    },
    # Secret Dungeons
    # Sunken Labyrinth
    rname.s1_a: {
        rname.s1_d:
            ID2Data(ID2Type.region),
        rname.s1_n:
            ID2Data(ID2Type.region),
    },
    rname.s1_b: {
        rname.s1_e:
            ID2Data(ID2Type.region),
        rname.s1_f:
            ID2Data(ID2Type.region, [[iname.force.value],
                                     [iname.can_phase_gap.value]]),
        rname.s1_s:
            ID2Data(ID2Type.region),
    },
    rname.s1_c: {
        lname.s1_death_ogler_combat:
            ID2Data(ID2Type.location),
        rname.s1_d:
            ID2Data(ID2Type.region),
    },
    rname.s1_d: {
        rname.s1_a:
            ID2Data(ID2Type.region),
        rname.s1_c:
            ID2Data(ID2Type.region),
        rname.s1_e:
            ID2Data(ID2Type.region),
        rname.s1_h:
            ID2Data(ID2Type.region, [[iname.s1_key.value + "*2"]]),
        rname.s1_i:
            ID2Data(ID2Type.region),
    },
    rname.s1_e: {
        lname.s1_gold_titan_combat:
            ID2Data(ID2Type.location, [[iname.melee.value],
                                       [iname.ice.value],
                                       [iname.can_phase_gap.value]]),
        rname.s1_d:
            ID2Data(ID2Type.region),
        rname.s1_i:
            ID2Data(ID2Type.region, [[iname.melee.value],
                                     [iname.ice.value],
                                     [iname.can_phase_gap.value]]),
    },
    rname.s1_f: {
        rname.s1_g:
            ID2Data(ID2Type.region),
    },
    rname.s1_g: {
        lname.s1_boss_reward:
            ID2Data(ID2Type.location, [[iname.basic_combat.value, iname.roll.value]]),
        rname.s1_f:
            ID2Data(ID2Type.region, [[iname.basic_combat.value, iname.roll.value]]),
    },
    rname.s1_h: {
        rname.s1_d:
            ID2Data(ID2Type.region, [[iname.s1_key.value + "*3"]]),
        rname.s1_j:
            ID2Data(ID2Type.region),
    },
    rname.s1_i: {
        rname.s1_d:
            ID2Data(ID2Type.region),
        rname.s1_l:
            ID2Data(ID2Type.region),
        rname.s1_q_left:
            ID2Data(ID2Type.region),
    },
    rname.s1_j: {
        lname.s1_treasure:
            ID2Data(ID2Type.location),
        rname.s1_k:
            ID2Data(ID2Type.region, [[iname.force.value]]),
    },
    rname.s1_k: {
        rname.s1_m:
            ID2Data(ID2Type.region),
        rname.s1_o:
            ID2Data(ID2Type.region),
        rname.s1_p:
            ID2Data(ID2Type.region, [[iname.s1_key.value + "*2"]]),
    },
    rname.s1_l: {
        rname.s1_i:
            ID2Data(ID2Type.region),
        rname.s1_k:
            ID2Data(ID2Type.region, [[iname.force.value],
                                     [iname.can_phase_doors.value]]),
        rname.s1_m:
            ID2Data(ID2Type.region),
    },
    rname.s1_m: {
        rname.s1_l:
            ID2Data(ID2Type.region),
        rname.fluffy_fields:
            ID2Data(ID2Type.region),
    },
    rname.s1_n: {
        rname.s1_a:
            ID2Data(ID2Type.region),
        rname.s1_m:
            ID2Data(ID2Type.region),
    },
    rname.s1_o: {
        lname.s1_mimic_combat:
            ID2Data(ID2Type.location, [[iname.basic_combat.value, iname.roll.value],
                                       [iname.can_phase_enemy_difficult.value, iname.roll.value]]),
        rname.s1_k:
            ID2Data(ID2Type.region),
        rname.s1_q_left:
            ID2Data(ID2Type.region),
    },
    rname.s1_p: {
        rname.s1_k:
            ID2Data(ID2Type.region, [[iname.s1_key.value + "*3"]]),
        rname.s1_r:
            ID2Data(ID2Type.region, [[iname.basic_combat.value, iname.roll.value]]),
    },
    rname.s1_q_left: {
        rname.s1_o:
            ID2Data(ID2Type.region, [[iname.s1_q_blocks.value]]),
        rname.s1_i:
            ID2Data(ID2Type.region),
        rname.s1_q_right:
            ID2Data(ID2Type.region, [[iname.ice.value],
                                     [iname.can_phase_object.value]]),
    },
    rname.s1_q_right: {
        lname.s1_q_blocks:
            ID2Data(ID2Type.location, [[]], iname.s1_q_blocks.value),
        rname.s1_q_left:
            ID2Data(ID2Type.region),
    },
    rname.s1_r: {
        rname.s1_q_right:
            ID2Data(ID2Type.region, [[iname.basic_combat.value]]),
        rname.s1_t:
            ID2Data(ID2Type.region, [[iname.basic_combat.value]]),
    },
    rname.s1_s: {
        rname.s1_b:
            ID2Data(ID2Type.region, [[iname.force.value],
                                     [iname.can_phase_gap.value]]),
    },
    rname.s1_t: {
        rname.s1_r:
            ID2Data(ID2Type.region),
        rname.s1_s:
            ID2Data(ID2Type.region, [[iname.force.value]]),
        rname.s1_u:
            ID2Data(ID2Type.region, [[iname.s1_key.value + "*3"]]),
    },
    rname.s1_u: {
        lname.s1_crayon:
            ID2Data(ID2Type.location, [[iname.can_open_chests.value]]),
        rname.s1_r:
            ID2Data(ID2Type.region, [[iname.weapon_any.value]]),
        rname.s1_t:
            ID2Data(ID2Type.region, [[iname.s1_key.value + "*3"]]),
    },
    # Machine Fortress
    rname.s2_a: {
        rname.s2_b:
            ID2Data(ID2Type.region),
        rname.s2_d:
            ID2Data(ID2Type.region, [[iname.s2_key.value + "*5"]]),
    },
    rname.s2_b: {
        lname.s2_treasure:
            ID2Data(ID2Type.location, [[iname.can_open_chests.value]]),
        rname.s2_c:
            ID2Data(ID2Type.region, [[iname.dynamite.value, iname.weapon_no_dynamite.value]]),
    },
    rname.s2_c: {
        rname.s2_i:
            ID2Data(ID2Type.region),
    },
    rname.s2_d: {
        lname.s2_steel_skullnip_combat:
            ID2Data(ID2Type.location, [[iname.roll.value]]),
        rname.s2_a:
            ID2Data(ID2Type.region, [[iname.s2_key.value + "*5", iname.roll.value]]),
        rname.s2_e:
            ID2Data(ID2Type.region, [[iname.roll.value],
                                     [iname.s2_key.value + "*5"]]),
    },
    rname.s2_e: {
        lname.s2_light_bridge:
            ID2Data(ID2Type.location),
        rname.s2_d:
            ID2Data(ID2Type.region, [[iname.s2_key.value + "*4"]]),
        rname.s2_f:
            ID2Data(ID2Type.region),
    },
    rname.s2_f: {
        lname.s2_cannon_conveyors:
            ID2Data(ID2Type.location),
        rname.s2_e:
            ID2Data(ID2Type.region, [[iname.s2_key.value + "*3"]]),
        rname.s2_h:
            ID2Data(ID2Type.region, [[iname.s2_key.value + "*5"]]),
    },
    rname.s2_g: {
        lname.s2_boss_reward:
            ID2Data(ID2Type.location, [[iname.basic_combat.value, iname.roll.value]]),
        rname.s2_k:
            ID2Data(ID2Type.region, [[iname.basic_combat.value, iname.roll.value]]),
    },
    rname.s2_h: {
        lname.s2_number_tiles:
            ID2Data(ID2Type.location),
        rname.s2_f:
            ID2Data(ID2Type.region, [[iname.s2_key.value + "*2"]]),
        rname.s2_l:
            ID2Data(ID2Type.region),
    },
    rname.s2_i: {
        rname.s2_c:
            ID2Data(ID2Type.region),
        rname.s2_h:
            ID2Data(ID2Type.region),
        rname.s2_j:
            ID2Data(ID2Type.region, [[iname.roll.value]]),
    },
    rname.s2_j: {
        rname.s2_k:
            ID2Data(ID2Type.region, [[iname.weapon_no_dynamite.value, iname.dynamite.value],
                                     [iname.melee.value, iname.chain.value]]),
    },
    rname.s2_k: {
        rname.s2_g:
            ID2Data(ID2Type.region),
    },
    rname.s2_l: {
        lname.s2_hyperdusa_conveyor:
            ID2Data(ID2Type.location),
        rname.s2_h:
            ID2Data(ID2Type.region, [[iname.s2_key.value + "*1"]]),
        rname.s2_p:
            ID2Data(ID2Type.region),
        rname.s2_q:
            ID2Data(ID2Type.region, [[iname.dynamite.value],
                                     [iname.can_phase_object.value, iname.ice.value, iname.roll.value]]),
    },
    rname.s2_m: {
        lname.s2_crayon:
            ID2Data(ID2Type.location, [[iname.can_open_chests.value]]),
        rname.s2_l:
            ID2Data(ID2Type.region, [[iname.weapon_any.value]]),
    },
    rname.s2_n: {
        rname.s2_m:
            ID2Data(ID2Type.region, [[iname.dynamite.value],
                                     [iname.can_phase_object.value, iname.ice.value]]),
        rname.s2_o:
            ID2Data(ID2Type.region, [[iname.dynamite.value],
                                     [iname.can_phase_object.value, iname.roll.value],
                                     [iname.can_phase_object.value, iname.ice.value]]),
    },
    rname.s2_o: {
        lname.s2_bee:
            ID2Data(ID2Type.location, [[iname.can_open_chests.value]]),
    },
    rname.s2_p: {
        rname.s2_l:
            ID2Data(ID2Type.region),
        rname.fancy_ruins:
            ID2Data(ID2Type.region),
    },
    rname.s2_q: {
        rname.s2_r:
            ID2Data(ID2Type.region, [[iname.basic_combat.value]]),
    },
    rname.s2_r: {
        rname.s2_n:
            ID2Data(ID2Type.region, [[iname.basic_combat.value, iname.roll.value]]),
    },
    # Dark Hypostyle
    rname.s3_a: {
        lname.s3_initial_key:
            ID2Data(ID2Type.location),
        rname.s3_f:
            ID2Data(ID2Type.region),
    },
    rname.s3_b: {
        rname.s3_c:
            ID2Data(ID2Type.region, [[iname.ice.value, iname.melee.value]]),
    },
    rname.s3_c: {
        rname.s3_d:
            ID2Data(ID2Type.region),
    },
    rname.s3_d: {
        lname.s3_boss_reward:
            ID2Data(ID2Type.location, [[iname.basic_combat.value, iname.roll.value]]),
        rname.s3_c:
            ID2Data(ID2Type.region, [[iname.basic_combat.value, iname.roll.value]]),
    },
    rname.s3_e: {
        rname.s3_f:
            ID2Data(ID2Type.region, [[iname.s3_key.value + "*5"]]),
        rname.s3_o:
            ID2Data(ID2Type.region),
    },
    rname.s3_f: {
        rname.s3_a:
            ID2Data(ID2Type.region),
        rname.s3_e:
            ID2Data(ID2Type.region, [[iname.s3_key.value + "*4"]]),
        rname.s3_k:
            ID2Data(ID2Type.region, [[iname.s3_key.value + "*4"]]),
        rname.s3_n:
            ID2Data(ID2Type.region, [[iname.s3_key.value + "*5"]]),
        rname.s3_s:
            ID2Data(ID2Type.region),
    },
    rname.s3_g: {
        lname.s3_red_path:
            ID2Data(ID2Type.location),
        rname.s3_b:
            ID2Data(ID2Type.region, [[iname.ice.value, iname.melee.value]]),
        rname.s3_f:
            ID2Data(ID2Type.region, [[iname.weapon_any.value]]),
        rname.s3_h:
            ID2Data(ID2Type.region, [[iname.s3_key + "*5"]]),
    },
    rname.s3_h: {
        lname.s3_red_path_cannon:
            ID2Data(ID2Type.location),
        rname.s3_g:
            ID2Data(ID2Type.region, [[iname.s3_key.value + "*5"]]),
    },
    rname.s3_i: {
        rname.s3_h:
            ID2Data(ID2Type.region, [[iname.melee.value],
                                     [iname.ice.value],
                                     [iname.can_phase_doors.value]]),
        rname.s3_j:
            ID2Data(ID2Type.region),
    },
    rname.s3_j: {
        rname.s3_i:
            ID2Data(ID2Type.region),
        rname.s3_u:
            ID2Data(ID2Type.region),
    },
    rname.s3_k: {
        rname.s3_u:
            ID2Data(ID2Type.region, [[iname.weapon_any.value]]),
    },
    rname.s3_l: {
        lname.s3_yellow_path:
            ID2Data(ID2Type.location),
        rname.s3_f:
            ID2Data(ID2Type.region),
    },
    rname.s3_m: {
        rname.s3_l:
            ID2Data(ID2Type.region, [[iname.basic_combat.value, iname.roll.value]]),
    },
    rname.s3_n: {
        rname.s3_f:
            ID2Data(ID2Type.region, [[iname.s3_key.value + "*5"]]),
        rname.s3_r:
            ID2Data(ID2Type.region, [[iname.weapon_any.value]]),
    },
    rname.s3_o: {
        rname.s3_e:
            ID2Data(ID2Type.region),
        rname.s3_p:
            ID2Data(ID2Type.region),
    },
    rname.s3_p: {
        lname.s3_yellow_path_monochrome:
            ID2Data(ID2Type.location, [[iname.melee.value]]),
        rname.s3_m:
            ID2Data(ID2Type.region, [[iname.ice.value, iname.melee.value]]),
        rname.s3_o:
            ID2Data(ID2Type.region),
        rname.s3_q:
            ID2Data(ID2Type.region, [[iname.s3_key.value + "*5"]]),
    },
    rname.s3_q: {
        lname.s3_treasure:
            ID2Data(ID2Type.location),
        rname.s3_p:
            ID2Data(ID2Type.region, [[iname.s3_key.value + "*5"]]),
    },
    rname.s3_r: {
        rname.s3_w:
            ID2Data(ID2Type.region),
    },
    rname.s3_s: {
        rname.s3_f:
            ID2Data(ID2Type.region),
        rname.star_east:
            ID2Data(ID2Type.region),
    },
    rname.s3_t: {
        lname.s3_blue_path:
            ID2Data(ID2Type.location),
        rname.s3_s:
            ID2Data(ID2Type.region),
        rname.s3_v_upper:
            ID2Data(ID2Type.region),
    },
    rname.s3_u: {
        rname.s3_k:
            ID2Data(ID2Type.region, [[iname.can_phase_gap.value]]),
        rname.s3_j:
            ID2Data(ID2Type.region),
    },
    rname.s3_v_upper: {
        lname.s3_crayon:
            ID2Data(ID2Type.location, [[iname.can_open_chests.value]]),
        rname.s3_v_lower:
            ID2Data(ID2Type.region, [[iname.can_phase_enemy.value],
                                     [iname.can_phase_dynamite.value]]),
        rname.s3_t:
            ID2Data(ID2Type.region),
    },
    rname.s3_v_lower: {
        rname.s3_v_upper:
            ID2Data(ID2Type.region, [[iname.basic_combat.value, iname.roll.value]]),
    },
    rname.s3_w: {
        rname.s3_v_lower:
            ID2Data(ID2Type.region),
        rname.s3_r:
            ID2Data(ID2Type.region),
    },
    # Tomb of Simulacrum:
    rname.s4_a: {
        rname.s4_h:
            ID2Data(ID2Type.region, [[iname.melee.value, iname.force.value, iname.ice.value],
                                     [iname.can_phase_object.value, iname.roll.value],
                                     [iname.can_phase_object.value, iname.ice.value],
                                     [iname.can_phase_object.value, iname.force.value]]),
    },
    rname.s4_b: {
        rname.s4_a:
            ID2Data(ID2Type.region, [[iname.force.value, iname.ice.value],
                                     [iname.can_phase_object.value, iname.ice.value],
                                     [iname.can_phase_object.value, iname.melee.value, iname.ice.value]]),
    },
    rname.s4_c: {
        rname.s4_b:
            ID2Data(ID2Type.region, [[iname.force.value, iname.dynamite.value, iname.ice.value],
                                     [iname.can_phase_gap.value, iname.weapon_no_force.value]]),
        rname.s4_d:
            ID2Data(ID2Type.region, [[iname.s4_key.value + "*10"]]),
        rname.s4_j:
            ID2Data(ID2Type.region, [[iname.ice.value],
                                     [iname.can_phase_object.value, iname.roll.value]]),
    },
    rname.s4_d: {
        rname.s4_c:
            ID2Data(ID2Type.region, [[iname.s4_key.value + "*10"]]),
        rname.s4_k:
            ID2Data(ID2Type.region, [[iname.s4_key.value + "*10"]]),
    },
    rname.s4_e: {
        rname.s4_f:
            ID2Data(ID2Type.region),
        rname.s4_l:
            ID2Data(ID2Type.region),
    },
    rname.s4_f: {
        rname.s4_e:
            ID2Data(ID2Type.region, [[iname.dynamite.value, iname.roll.value],
                                     [iname.can_phase_gap.value]]),
        rname.s4_m:
            ID2Data(ID2Type.region, [[iname.dynamite.value, iname.roll.value],
                                     [iname.can_phase_gap.value]]),
    },
    rname.s4_g: {
        lname.s4_boss_reward:
            ID2Data(ID2Type.location, [[iname.basic_combat.value, iname.roll.value]]),
        rname.s4_n:
            ID2Data(ID2Type.region, [[iname.basic_combat.value, iname.roll.value]]),
    },
    rname.s4_h: {
        rname.s4_i:
            ID2Data(ID2Type.region, [[iname.force.value, iname.ice.value],
                                     [iname.can_phase_object.value, iname.roll.value],
                                     [iname.can_phase_object.value, iname.ice.value]]),
    },
    rname.s4_i: {
        lname.s4_treasure:
            ID2Data(ID2Type.location, [[iname.force_jump.value],
                                       [iname.can_phase_object.value, iname.ice.value,]]),
        rname.s4_j:
            ID2Data(ID2Type.region, [[iname.force_jump.value],
                                     [iname.can_phase_object.value, iname.ice.value]]),
    },
    rname.s4_j: {
        rname.s4_k:
            ID2Data(ID2Type.region, [[iname.s4_key.value + "*8"]]),
        rname.s4_ao_left:
            ID2Data(ID2Type.region),
    },
    rname.s4_k: {
        rname.s4_j:
            ID2Data(ID2Type.region, [[iname.s4_key.value + "*10"]]),
        rname.s4_d:
            ID2Data(ID2Type.region, [[iname.s4_key.value + "*9"]]),
        rname.s4_r:
            ID2Data(ID2Type.region),
    },
    rname.s4_l: {
        rname.s4_e:
            ID2Data(ID2Type.region),
    },
    rname.s4_m: {
        rname.s4_f:
            ID2Data(ID2Type.region),
        rname.s4_n:
            ID2Data(ID2Type.region),
    },
    rname.s4_n: {
        rname.s4_g:
            ID2Data(ID2Type.region),
        rname.s4_m:
            ID2Data(ID2Type.region),
        rname.s4_t:
            ID2Data(ID2Type.region),
    },
    rname.s4_o: {
        rname.s4_p:
            ID2Data(ID2Type.region, [[iname.can_phase_enemy.value, iname.s4_key.value + "*10"],
                                     [iname.can_phase_dynamite.value, iname.s4_key.value + "*10"]]),
        rname.s4_ah:
            ID2Data(ID2Type.region, [[iname.basic_combat.value, iname.roll.value],
                                     [iname.can_phase_enemy_difficult.value]]),
    },
    rname.s4_p: {
        rname.s4_o:
            ID2Data(ID2Type.region, [[iname.s4_key.value + "*2"]]),
        rname.s4_q:
            ID2Data(ID2Type.region, [[iname.basic_combat.value, iname.roll.value]]),
        rname.s4_v:
            ID2Data(ID2Type.region, [[iname.s4_key.value + "*10"]]),
    },
    rname.s4_q: {
        lname.s4_corner_torch:
            ID2Data(ID2Type.location, [[iname.fire_mace.value, iname.ice.value],
                                       [iname.can_phase_object.value, iname.ice.value]]),
        rname.s4_w:
            ID2Data(ID2Type.region, [[iname.ice.value],
                                     [iname.can_phase_gap.value, iname.roll.value]]),
    },
    rname.s4_r: {
        rname.s4_x:
            ID2Data(ID2Type.region, [[iname.s4_key.value + "*10"]]),
        rname.s4_ad:
            ID2Data(ID2Type.region),
    },
    rname.s4_s: {
        lname.s4_efcs_door:
            ID2Data(ID2Type.location),
        rname.s4_l:
            ID2Data(ID2Type.region, [[iname.fake_efcs.value]]),
        rname.s4_t:
            ID2Data(ID2Type.region),
        rname.s4_y:
            ID2Data(ID2Type.region),
        rname.s4_ad:
            ID2Data(ID2Type.region),
    },
    rname.s4_t: {
        lname.s4_spiked_orbitals:
            ID2Data(ID2Type.location),
        rname.s4_y:
            ID2Data(ID2Type.region),
    },
    rname.s4_u: {
        lname.s4_roundabout_crystal:
            ID2Data(ID2Type.location, [[iname.melee.value, iname.force.value, iname.dynamite.value, iname.ice.value],
                                       [iname.can_phase_object.value, iname.ice.value, iname.weapon_projectile.value],
                                       [iname.can_phase_object.value, iname.ice.value, iname.roll.value],
                                       [iname.can_phase_dynamite.value]]),
    },
    rname.s4_v: {
        rname.s4_p:
            ID2Data(ID2Type.region, [[iname.s4_key.value + "*1"]]),
        rname.s4_w:
            ID2Data(ID2Type.region, [[iname.ice.value]]),
    },
    rname.s4_w: {
        rname.s4_ae:
            ID2Data(ID2Type.region),
    },
    rname.s4_x: {
        rname.s4_r:
            ID2Data(ID2Type.region, [[iname.s4_key.value + "*5"]]),
        rname.s4_w:
            ID2Data(ID2Type.region, [[iname.ice.value],
                                     [iname.can_phase_gap.value, iname.roll.value]]),
        rname.s4_ac:
            ID2Data(ID2Type.region, [[iname.s4_key.value + "*10"]]),
    },
    rname.s4_y: {
        lname.s4_large_chasm:
            ID2Data(ID2Type.location, [[iname.roll.value]]),
        rname.s4_s:
            ID2Data(ID2Type.region),
        rname.s4_t:
            ID2Data(ID2Type.region),
        rname.s4_ad:
            ID2Data(ID2Type.region),
        rname.s4_ai:
            ID2Data(ID2Type.region),
        rname.s4_aj:
            ID2Data(ID2Type.region),
    },
    rname.s4_z: {
        rname.s4_u:
            ID2Data(ID2Type.region, [[iname.melee.value, iname.roll.value],
                                     [iname.ice.value, iname.roll.value]]),
        rname.s4_aa:
            ID2Data(ID2Type.region, [[iname.melee.value, iname.roll.value],
                                     [iname.ice.value, iname.roll.value]]),
        rname.s4_ae:
            ID2Data(ID2Type.region, [[iname.melee.value, iname.roll.value],
                                     [iname.ice.value, iname.roll.value]]),
    },
    rname.s4_aa: {
        rname.s4_v:
            ID2Data(ID2Type.region, [[iname.melee.value, iname.dynamite.value, iname.roll.value]]),
        rname.s4_z:
            ID2Data(ID2Type.region, [[iname.melee.value, iname.dynamite.value, iname.roll.value]]),
        rname.s4_af:
            ID2Data(ID2Type.region, [[iname.melee.value, iname.dynamite.value, iname.roll.value]]),
    },
    rname.s4_ab: {
        lname.s4_eight_tile:
            ID2Data(ID2Type.location, [[iname.force.value, iname.ice.value],
                                       [iname.can_phase_gap.value, iname.ice.value]]),
        rname.s4_w:
            ID2Data(ID2Type.region, [[iname.ice.value],
                                     [iname.can_phase_gap.value, iname.ice.value]]),
        rname.s4_aa:
            ID2Data(ID2Type.region, [[iname.force.value, iname.ice.value],
                                     # phase the ice block over the gap
                                     [iname.can_phase_gap.value, iname.ice.value]]),
    },
    rname.s4_ac: {
        lname.s4_crayon:
            ID2Data(ID2Type.location, [[iname.fake_efcs.value, iname.ice.value],
                                       [iname.can_phase_gap.value, iname.ice.value]]),
        rname.s4_x:
            ID2Data(ID2Type.region, [[iname.s4_key.value + "*4"]]),
        rname.s4_ah:
            ID2Data(ID2Type.region, [[iname.s4_key.value + "*10"]])
    },
    rname.s4_ad: {
        rname.s4_r:
            ID2Data(ID2Type.region),
        rname.s4_s:
            ID2Data(ID2Type.region),
        rname.s4_y:
            ID2Data(ID2Type.region),
        rname.s4_ai:
            ID2Data(ID2Type.region),
    },
    rname.s4_ae: {
        rname.s4_w:
            ID2Data(ID2Type.region),
        rname.s4_z:
            ID2Data(ID2Type.region),
        rname.s4_af:
            ID2Data(ID2Type.region),
        rname.s4_ak:
            ID2Data(ID2Type.region),
    },
    rname.s4_af: {
        lname.s4_self_locked_tile:
            ID2Data(ID2Type.location, [[iname.melee.value, iname.ice.value],
                                       [iname.can_phase_object.value, iname.ice.value, iname.roll.value]]),
        rname.s4_aa:
            ID2Data(ID2Type.region, [[iname.fire_mace.value, iname.force.value, iname.dynamite.value, iname.ice.value]]),
        rname.s4_ae:
            ID2Data(ID2Type.region),
        rname.s4_ag:
            ID2Data(ID2Type.region),
        rname.s4_al:
            ID2Data(ID2Type.region),
    },
    rname.s4_ag: {
        rname.s4_ab:
            ID2Data(ID2Type.region, [[iname.basic_combat.value, iname.roll.value]]),
        rname.s4_af:
            ID2Data(ID2Type.region),
    },
    rname.s4_ah: {
        rname.s4_o:
            ID2Data(ID2Type.region),
        rname.s4_ac:
            ID2Data(ID2Type.region, [[iname.s4_key.value + "*3"]]),
        rname.s4_an:
            ID2Data(ID2Type.region, [[iname.ice.value],
                                     [iname.can_phase_gap.value, iname.roll.value]]),
    },
    rname.s4_ai: {
        lname.s4_death_ogler_combat:
            ID2Data(ID2Type.location, [[iname.basic_combat.value, iname.roll.value],
                                       [iname.can_phase_enemy_difficult.value]]),
        rname.s4_y:
            ID2Data(ID2Type.region),
        rname.s4_ad:
            ID2Data(ID2Type.region),
    },
    rname.s4_aj: {
        rname.s4_y:
            ID2Data(ID2Type.region),
        rname.s4_aq:
            ID2Data(ID2Type.region, [[iname.basic_combat.value, iname.roll.value]]),
    },
    rname.s4_ak: {
        lname.s4_mercury_jello_number_tiles:
            ID2Data(ID2Type.location, [[iname.dynamite.value],
                                       [iname.can_phase_object.value, iname.ice.value, iname.roll.value]]),
        rname.s4_ae:
            ID2Data(ID2Type.region, [[iname.dynamite.value, iname.weapon_projectile.value],
                                     [iname.can_phase_object.value, iname.ice.value, iname.roll.value]]),
    },
    rname.s4_al: {
        rname.s4_af:
            ID2Data(ID2Type.region),
        rname.s4_ak:
            ID2Data(ID2Type.region, [[iname.melee.value],
                                     [iname.ice.value],
                                     [iname.can_phase_doors.value]]),
    },
    rname.s4_am: {
        rname.s4_ag:
            ID2Data(ID2Type.region, [[iname.basic_combat.value]]),
        rname.s4_al:
            ID2Data(ID2Type.region, [[iname.basic_combat.value]]),
        rname.s4_an:
            ID2Data(ID2Type.region),
    },
    rname.s4_an: {
        rname.s4_am:
            ID2Data(ID2Type.region),
        rname.forbidden_area_north:
            ID2Data(ID2Type.region),
    },
    rname.s4_ao_left: {
        rname.s4_j:
            ID2Data(ID2Type.region),
        rname.s4_an:
            ID2Data(ID2Type.region, [[iname.ice.value],
                                     [iname.can_phase_gap.value, iname.roll.value]]),
        rname.s4_ao_right:
            ID2Data(ID2Type.region, [[iname.weapon_any.value],
                                     [iname.can_phase_object.value]]),
    },
    rname.s4_ao_right: {
        rname.s4_ao_left:
            ID2Data(ID2Type.region, [[iname.force.value, iname.ice.value],
                                     [iname.can_phase_object.value, iname.roll.value]]),
        rname.s4_ap:
            ID2Data(ID2Type.region, [[iname.s4_key.value + "*10"]]),
    },
    rname.s4_ap: {
        rname.s4_ai:
            ID2Data(ID2Type.region),
        rname.s4_ao_right:
            ID2Data(ID2Type.region, [[iname.s4_key.value + "*7"]]),
        rname.s4_aq:
            ID2Data(ID2Type.region, [[iname.s4_key.value + "*10"]]),
    },
    rname.s4_aq: {
        lname.s4_molten_conveyors:
            ID2Data(ID2Type.location, [[iname.force.value, iname.dynamite.value],
                                       [iname.can_phase_gap_difficult.value, iname.roll.value]]),
        rname.s4_ap:
            ID2Data(ID2Type.region, [[iname.weapon_no_dynamite.value, iname.s4_key.value + "*6"],
                                     [iname.can_phase_doors.value, iname.s4_key.value + "*6"]]),
    },
    # Dreamworld Dungeons
    # Wizardry Lab
    rname.df_b: {
        rname.df_ah:
            ID2Data(ID2Type.region)
    },
    rname.df_c: {
        lname.df_cannon:
            ID2Data(ID2Type.location),
        rname.df_b:
            ID2Data(ID2Type.region,
                    [[iname.df_ne_generator.value, iname.df_ne_circuit.value, iname.df_nw_generator.value]]),
        rname.df_k_center:
            ID2Data(ID2Type.region)
    },
    rname.df_e: {
        lname.df_ne_circuit:
            ID2Data(ID2Type.location, [[iname.dw_vanilla.value],
                                       [iname.dw_fun.value, iname.force.value]], iname.df_ne_circuit.value),
        rname.df_l_top:
            ID2Data(ID2Type.region)
    },
    rname.df_i: {
        rname.df_w:
            ID2Data(ID2Type.region, [[iname.dw_vanilla.value],
                                     [iname.dw_fun.value, iname.force.value],
                                     [iname.dw_fun.value, iname.can_phase_gap.value, iname.ice.value, iname.melee.value,
                                      iname.roll.value]])
    },
    rname.df_j: {
        rname.df_i:
            ID2Data(ID2Type.region, [[iname.dw_vanilla.value],
                                     [iname.dw_fun.value, iname.force.value],
                                     [iname.dw_fun.value, iname.ice.value, iname.fire_mace.value, iname.chain.value]])
    },
    rname.df_k_center: {
        # The game actually doesn't care about the south generators at this point
        # and they'll be active even if you've never entered the generator rooms
        rname.df_c:
            ID2Data(ID2Type.region),
        rname.df_k_left:
            ID2Data(ID2Type.region, [[iname.dw_vanilla.value],
                                     [iname.dw_fun.value, iname.force.value, iname.melee.value],
                                     [iname.dw_fun.value, iname.can_phase_gap.value, iname.melee.value],
                                     [iname.dw_fun.value, iname.can_phase_dynamite.value]]),
        rname.df_k_right:
            ID2Data(ID2Type.region, [[iname.dw_vanilla.value],
                                     [iname.dw_fun.value, iname.force.value, iname.melee.value],
                                     [iname.dw_fun.value, iname.can_phase_gap.value, iname.melee.value],
                                     [iname.dw_fun.value, iname.can_phase_dynamite.value]]),
        rname.df_y:
            ID2Data(ID2Type.region)
    },
    rname.df_k_left: {
        rname.df_j:
            ID2Data(ID2Type.region, [[iname.weapon_any.value]]),
        rname.df_k_center:
            ID2Data(ID2Type.region, [[iname.dw_vanilla.value, iname.can_phase_gap.value],
                                     [iname.dw_fun.value, iname.can_phase_gap.value, iname.melee.value],
                                     [iname.dw_fun.value, iname.can_phase_doors.value, iname.weapon_any.value],
                                     [iname.dw_fun.value, iname.can_phase_dynamite.value]])
    },
    rname.df_k_right: {
        rname.df_l_bottom:
            ID2Data(ID2Type.region, [[iname.weapon_any.value]]),
        rname.df_k_center:
            ID2Data(ID2Type.region, [[iname.dw_vanilla.value, iname.can_phase_gap.value],
                                     [iname.dw_fun.value, iname.can_phase_gap.value, iname.melee.value],
                                     [iname.dw_fun.value, iname.can_phase_doors.value, iname.weapon_any.value],
                                     [iname.dw_fun.value, iname.can_phase_dynamite.value]])
    },
    rname.df_l_top: {
        rname.df_e:
            ID2Data(ID2Type.region),
        rname.df_l_bottom:
            ID2Data(ID2Type.region)
    },
    rname.df_l_bottom: {
        rname.df_m_top:
            ID2Data(ID2Type.region),
        rname.df_l_top:
            ID2Data(ID2Type.region, [[iname.df_ne_generator.value],
                                     [iname.can_phase_doors.value]])
    },
    rname.df_m_top: {
        rname.df_k_center:
            ID2Data(ID2Type.region, [[iname.dw_vanilla.value],
                                     [iname.dw_fun.value, iname.force.value],
                                     [iname.can_phase_gap.value],
                                     [iname.dw_fun.value, iname.can_phase_dynamite.value]]),
        rname.df_l_bottom:
            ID2Data(ID2Type.region),
        rname.df_m_bottom:
            ID2Data(ID2Type.region, [[iname.dw_vanilla.value],
                                     [iname.dw_fun.value, iname.force.value],
                                     [iname.can_phase_gap.value]]),
    },
    rname.df_m_bottom: {
        lname.df_east_mirrors:
            ID2Data(ID2Type.location, [[iname.dw_vanilla.value],
                                       [iname.dw_fun.value, iname.force.value],
                                       [iname.can_phase_gap.value]]),
        rname.df_aa:
            ID2Data(ID2Type.region),
        rname.df_m_top:
            ID2Data(ID2Type.region, [[iname.dw_vanilla.value],
                                     [iname.dw_fun.value, iname.force.value],
                                     [iname.can_phase_gap.value]])
    },
    rname.df_w: {
        lname.df_west_energy_source:
            ID2Data(ID2Type.location, [[iname.df_nw_generator.value]]),
        lname.df_nw_generator:
            ID2Data(ID2Type.location, [[iname.dw_vanilla.value],
                                       [iname.dw_fun.value, iname.force.value],
                                       [iname.can_phase_gap.value]], iname.df_nw_generator.value),
        rname.df_i:
            ID2Data(ID2Type.region),
        rname.df_k_center:
            ID2Data(ID2Type.region, [[iname.df_nw_generator.value]]),
    },
    rname.df_x: {
        lname.df_sw_circuit:
            ID2Data(ID2Type.location, [[iname.dw_vanilla.value],
                                       [iname.dw_fun.value, iname.force.value],
                                       [iname.dw_fun.value, iname.melee.value, iname.chain.value],
                                       [iname.dw_fun.value, iname.can_phase_dynamite.value]],
                    iname.df_sw_circuit.value),
        rname.df_y:
            ID2Data(ID2Type.region, [[iname.df_sw_circuit.value]]),
    },
    rname.df_y: {
        rname.df_k_center:
            ID2Data(ID2Type.region, [[iname.df_se_generator.value, iname.df_sw_generator.value,
                                      iname.df_sw_circuit.value],
                                     [iname.can_phase_doors.value]]),
        rname.df_af:
            ID2Data(ID2Type.region, [[iname.df_se_generator.value, iname.df_sw_generator.value,
                                      iname.df_sw_circuit.value],
                                     [iname.can_phase_doors.value]]),
    },
    rname.df_z: {
        lname.df_se_circuit:
            ID2Data(ID2Type.location, [[iname.dw_vanilla.value, iname.df_se_generator.value],
                                       [iname.dw_fun.value, iname.melee.value, iname.df_se_generator.value]],
                    lname.df_se_circuit.value),
        rname.df_y:
            ID2Data(ID2Type.region, [[iname.df_se_circuit.value],
                                     [iname.can_phase_doors.value, iname.ice.value, iname.melee.value,
                                      iname.chain.value]]),
    },
    rname.df_aa: {
        lname.df_ne_generator:
            ID2Data(ID2Type.location, [[iname.dw_vanilla.value],
                                       [iname.dw_fun.value, iname.force.value],
                                       [iname.dw_fun.value, iname.can_phase_gap.value, iname.weapon_any.value]],
                    iname.df_ne_generator.value),
        lname.df_east_energy_source:
            ID2Data(ID2Type.location, [[iname.df_ne_generator.value]]),
        rname.df_m_bottom:
            ID2Data(ID2Type.region),
    },
    rname.df_ae: {
        lname.df_sw_generator:
            ID2Data(ID2Type.location, [[iname.dw_vanilla.value],
                                       [iname.dw_fun.value, iname.force.value],
                                       [iname.dw_fun.value, iname.melee.value, iname.chain.value],
                                       [iname.dw_fun.value, iname.can_phase_doors.value, iname.ice.value]],
                    iname.df_sw_generator.value),
        rname.df_x:
            ID2Data(ID2Type.region, [[iname.df_sw_generator.value]]),
        rname.df_af:
            ID2Data(ID2Type.region),
    },
    rname.df_ad: {
        lname.df_entrance:
            ID2Data(ID2Type.location, [[iname.dw_vanilla.value],
                                       [iname.dw_fun.value, iname.force.value],
                                       [iname.can_phase_gap.value]]),
        rname.df_af:
            ID2Data(ID2Type.region),
        rname.dreamworld_force:
            ID2Data(ID2Type.region),
    },
    rname.df_af: {
        rname.df_y:
            ID2Data(ID2Type.region),
        rname.df_ae:
            ID2Data(ID2Type.region),
        rname.df_ag:
            ID2Data(ID2Type.region),
        rname.df_ad:
            ID2Data(ID2Type.region)
    },
    rname.df_ag: {
        lname.df_se_generator:
            ID2Data(ID2Type.location, [[iname.dw_vanilla.value],
                                       [iname.dw_fun.value, iname.force.value]], iname.df_se_generator.value),
        rname.df_z:
            ID2Data(ID2Type.region, [[iname.df_se_generator.value]]),
        rname.df_af:
            ID2Data(ID2Type.region),
    },
    rname.df_ah: {
        lname.event_finished_df:
            ID2Data(ID2Type.location, [[]], iname.dw_finished_dungeon.value),
        lname.df_reward_a:
            ID2Data(ID2Type.location),
        lname.df_reward_b:
            ID2Data(ID2Type.location),
        lname.df_reward_c:
            ID2Data(ID2Type.location),
        rname.dreamworld_force:
            ID2Data(ID2Type.region)
    },
    # Syncope
    rname.dd_a: {
        rname.dd_v:
            ID2Data(ID2Type.region),
    },
    rname.dd_b: {
        rname.dd_a:
            ID2Data(ID2Type.region),
        rname.dd_c:
            ID2Data(ID2Type.region, [[iname.can_phase_gap.value]]),
    },
    rname.dd_c: {
        lname.dd_knights_hint:
            ID2Data(ID2Type.location),
        rname.dd_b:
            ID2Data(ID2Type.region),
        rname.dd_i:
            ID2Data(ID2Type.region),
        rname.dd_z:
            ID2Data(ID2Type.region),
    },
    rname.dd_d_left: {
        lname.dd_shadow_walker:
            ID2Data(ID2Type.location),
    },
    rname.dd_d_right: {
        rname.dd_k:
            ID2Data(ID2Type.region),
    },
    rname.dd_e: {
        rname.dd_l:
            ID2Data(ID2Type.region),
        rname.dd_ao:
            ID2Data(ID2Type.region, [[iname.dd_e_block.value],
                                     [iname.dw_fun.value, iname.ice.value],
                                     [iname.can_phase_gap.value]]),
    },
    rname.dd_f: {
        lname.dd_e_block:
            ID2Data(ID2Type.location, [[]], iname.dd_e_block.value),
        rname.dd_l:
            ID2Data(ID2Type.region),
    },
    rname.dd_i: {
        rname.dd_c:
            ID2Data(ID2Type.region),
        rname.dd_r:
            ID2Data(ID2Type.region),
        rname.dd_x:
            ID2Data(ID2Type.region),
    },
    rname.dd_k: {
        lname.dd_piano:
            ID2Data(ID2Type.location),
        rname.dd_d_left:
            ID2Data(ID2Type.region, [[iname.dd_piano_code.value]]),
        rname.dd_d_right:
            ID2Data(ID2Type.region),
    },
    rname.dd_l: {
        lname.dd_north_clock:
            ID2Data(ID2Type.location, [[]], iname.dd_north_clock.value),
        rname.dd_e:
            ID2Data(ID2Type.region),
        rname.dd_f:
            ID2Data(ID2Type.region, [[iname.dd_north_clock.value, iname.dd_west_clock.value, iname.dd_east_clock.value],
                                     [iname.can_phase_doors.value],
                                     [iname.dw_fun.value, iname.can_phase_object.value, iname.ice.value]]),
        rname.dd_n:
            ID2Data(ID2Type.region),
        rname.dd_r:
            ID2Data(ID2Type.region),
        rname.dd_z:
            ID2Data(ID2Type.region),
    },
    rname.dd_n: {
        lname.dd_garden:
            ID2Data(ID2Type.location, [[iname.dw_vanilla.value, iname.dd_garden_block.value],
                                       [iname.dw_fun.value, iname.dynamite.value, iname.weapon_no_dynamite.value, iname.dd_garden_block.value],
                                       [iname.dw_fun.value, iname.dynamite.value, iname.ice.value],
                                       [iname.dw_fun.value, iname.weapon_projectile.value],
                                       [iname.can_phase_gap.value]]),
        rname.dd_l:
            ID2Data(ID2Type.region),
        rname.dd_ab:
            ID2Data(ID2Type.region, [[iname.dd_key.value + "*3"]]),
    },
    rname.dd_r: {
        rname.dd_k:
            ID2Data(ID2Type.region),
        rname.dd_i:
            ID2Data(ID2Type.region),
        rname.dd_l:
            ID2Data(ID2Type.region),
        rname.dd_y:
            ID2Data(ID2Type.region, [[iname.dd_key.value + "*3"]]),
    },
    rname.dd_v: {
        lname.dd_force_turret_maze:
            ID2Data(ID2Type.location),
        rname.dd_a:
            ID2Data(ID2Type.region),
        rname.dd_w:
            ID2Data(ID2Type.region, [[iname.dw_vanilla.value],
                                     [iname.weapon_any.value]]),
    },
    rname.dd_w: {
        lname.dd_garden_block:
            ID2Data(ID2Type.location, [[]], iname.dd_garden_block.value),
        lname.dd_piano_code:
            ID2Data(ID2Type.location, [[]], iname.dd_piano_code.value),
        rname.dd_x:
            ID2Data(ID2Type.region),
    },
    rname.dd_x: {
        rname.dd_i:
            ID2Data(ID2Type.region),
    },
    rname.dd_y: {
        lname.dd_west_clock:
            ID2Data(ID2Type.location, [[]], iname.dd_west_clock.value),
        rname.dd_r:
            # One-sided lock lol, it's free on this side
            ID2Data(ID2Type.region),
    },
    rname.dd_z: {
        lname.dd_foyer:
            ID2Data(ID2Type.location),
        rname.dd_l:
            ID2Data(ID2Type.region),
        rname.dd_sc:
            ID2Data(ID2Type.region),
    },
    rname.dd_ab: {
        lname.dd_east_clock:
            ID2Data(ID2Type.location, [[]], iname.dd_east_clock.value),
    },
    rname.dd_sc: {
        lname.dd_shifting_chamber:
            ID2Data(ID2Type.location, [[iname.dw_vanilla.value],
                                       [iname.dw_fun.value, iname.dynamite.value],
                                       [iname.can_phase_gap.value]]),
        rname.dd_z:
            ID2Data(ID2Type.region, [[iname.dw_vanilla.value, iname.dd_sc_switch.value],
                                     [iname.dw_fun.value, iname.dd_sc_switch.value, iname.dynamite.value],
                                     # works in Red-Blue state
                                     [iname.dw_fun.value, iname.ice.value, iname.weapon_projectile.value],
                                     [iname.dw_fun.value, iname.force_jump.value],
                                     [iname.can_phase_gap.value]]),
        rname.dd_an:
            ID2Data(ID2Type.region, [[iname.can_phase_gap.value]]),
    },
    rname.dd_al: {
        rname.dd_am:
            ID2Data(ID2Type.region, [[iname.dw_vanilla.value],
                                     [iname.dw_fun.value, iname.dynamite.value, iname.melee.value],
                                     [iname.dw_fun.value, iname.ice.value, iname.weapon_projectile.value]]),
        rname.dd_as:
            # one-way combat door lol
            ID2Data(ID2Type.region),
    },
    rname.dd_am: {
        lname.dd_sc_switch:
            ID2Data(ID2Type.location, [[]], iname.dd_sc_switch.value),
        lname.dd_switch_chamber:
            ID2Data(ID2Type.location),
        rname.dd_al:
            ID2Data(ID2Type.region),
        rname.dd_an:
            ID2Data(ID2Type.region),
    },
    rname.dd_an: {
        rname.dd_sc:
            ID2Data(ID2Type.region),
        rname.dd_au:
            ID2Data(ID2Type.region),
    },
    rname.dd_ao: {
        lname.dd_reward_a:
            ID2Data(ID2Type.location),
        lname.dd_reward_b:
            ID2Data(ID2Type.location),
        lname.dd_reward_c:
            ID2Data(ID2Type.location),
        lname.event_finished_dd:
            ID2Data(ID2Type.location, [[]], iname.dw_finished_dungeon.value),
        rname.dreamworld_dynamite:
            ID2Data(ID2Type.region),
    },
    rname.dd_as: {
        rname.dd_am:
            ID2Data(ID2Type.region, [[iname.dw_vanilla.value],
                                     [iname.dw_fun.value, iname.basic_combat.value]]),
        rname.dd_at:
            ID2Data(ID2Type.region),
    },
    rname.dd_at: {
        rname.dd_as:
            ID2Data(ID2Type.region, [[iname.dw_vanilla.value],
                                     [iname.dw_fun.value, iname.dynamite.value, iname.weapon_no_dynamite.value],
                                     [iname.dw_fun.value, iname.force.value, iname.weapon_no_force.value]]),
        rname.dd_au:
            ID2Data(ID2Type.region, [[iname.dd_key.value + "*3"]]),
    },
    rname.dd_au: {
        rname.dd_an:
            ID2Data(ID2Type.region),
        rname.dd_at:
            ID2Data(ID2Type.region, [[iname.dw_vanilla.value, iname.glitchless.value, iname.dd_key.value + "*1"],
                                     [iname.dd_key.value + "*3"]]),
    },
    # Antigram
    rname.dfc_a: {
        lname.dfc_reward_a:
            ID2Data(ID2Type.location),
        lname.dfc_reward_b:
            ID2Data(ID2Type.location),
        lname.dfc_reward_c:
            ID2Data(ID2Type.location),
        lname.event_finished_dfc:
            ID2Data(ID2Type.location, [[]], iname.dw_finished_dungeon.value),
        rname.dreamworld_fire_chain:
            ID2Data(ID2Type.region),
    },
    rname.dfc_b: {
        lname.dfc_west_bombs:
            ID2Data(ID2Type.location, [[iname.dw_vanilla.value],
                                       [iname.can_phase_object.value],
                                       [iname.dw_fun.value, iname.fire_sword.value, iname.chain.value],
                                       [iname.dw_fun.value, iname.melee.value, iname.chain.value, iname.dynamite.value],
                                       [iname.dw_fun.value, iname.melee.value, iname.chain.value, iname.weapon_projectile.value]]),
    },
    rname.dfc_c: {
        rname.dfc_a:
            ID2Data(ID2Type.region, [[iname.dw_vanilla.value],
                                     [iname.dw_fun.value, iname.basic_combat.value, iname.roll.value]]),
        rname.dfc_e:
            ID2Data(ID2Type.region, [[iname.dw_vanilla.value],
                                     [iname.dw_fun.value, iname.basic_combat.value, iname.roll.value]]),
    },
    rname.dfc_d: {
        lname.dfc_east_bombs:
            ID2Data(ID2Type.location, [[iname.dw_vanilla.value],
                                       [iname.can_phase_object.value],
                                       [iname.dw_fun.value, iname.fire_sword.value, iname.chain.value],
                                       [iname.dw_fun.value, iname.melee.value, iname.chain.value, iname.dynamite.value],
                                       [iname.dw_fun.value, iname.melee.value, iname.chain.value, iname.weapon_projectile.value]]),
    },
    rname.dfc_e: {
        lname.dfc_end_west_bridge:
            ID2Data(ID2Type.location),
        lname.dfc_end_east_bridge:
            ID2Data(ID2Type.location),
        rname.dfc_c:
            ID2Data(ID2Type.region, [[iname.dfc_key.value + "*4"]]),
    },
    rname.dfc_f: {
        rname.dfc_b:
            ID2Data(ID2Type.region, [[iname.dw_vanilla.value],
                                     [iname.dw_fun.value, iname.fire_sword.value],
                                     [iname.dw_fun.value, iname.dynamite.value],
                                     [iname.dw_fun.value, iname.ice.value, iname.melee.value, iname.weapon_projectile.value],
                                     [iname.dw_fun.value, iname.can_phase_object.value, iname.roll.value, iname.weapon_any.value]]),
        rname.dfc_g:
            ID2Data(ID2Type.region, [[iname.dfc_key.value + "*4"],
                                     [iname.dfc_key.value + "*3", iname.glitchless.value]]),
        rname.dfc_k:
            ID2Data(ID2Type.region),
    },
    rname.dfc_g: {
        rname.dfc_f:
            ID2Data(ID2Type.region, [[iname.dfc_key.value + "*4"]]),
        rname.dfc_h_left:
            ID2Data(ID2Type.region),
    },
    rname.dfc_h_left: {
        lname.dfc_left_switch:
            ID2Data(ID2Type.location, [[]], iname.dfc_left_switch.value),
        rname.dfc_h_center:
            ID2Data(ID2Type.region),
    },
    rname.dfc_h_center: {
        rname.dfc_e:
            ID2Data(ID2Type.region, [[iname.dw_vanilla.value, iname.dfc_left_switch.value, iname.dfc_right_switch.value],
                                     [iname.dw_fun.value, iname.dfc_left_switch.value, iname.dfc_right_switch.value, iname.melee.value, iname.chain.value],
                                     [iname.dw_fun.value, iname.dfc_left_switch.value, iname.dfc_right_switch.value, iname.weapon_projectile.value]]),
        rname.dfc_h_left:
            ID2Data(ID2Type.region, [[iname.dw_fun.value, iname.can_phase_doors.value, iname.can_phase_dynamite.value],
                                     [iname.dw_fun.value, iname.dfc_right_switch.value, iname.can_phase_dynamite.value],
                                     [iname.dw_fun.value, iname.dfc_right_switch.value, iname.can_phase_object.value, iname.ice.value, iname.roll.value]]),
        rname.dfc_h_right:
            ID2Data(ID2Type.region, [[iname.dw_fun.value, iname.can_phase_doors.value, iname.can_phase_dynamite.value],
                                     [iname.dw_fun.value, iname.dfc_left_switch.value, iname.can_phase_dynamite.value],
                                     [iname.dw_fun.value, iname.dfc_left_switch.value, iname.can_phase_object.value, iname.ice.value, iname.roll.value]]),
        rname.dfc_m:
            ID2Data(ID2Type.region),
    },
    rname.dfc_h_right: {
        lname.dfc_right_switch:
            ID2Data(ID2Type.location, [[]], iname.dfc_right_switch.value),
        rname.dfc_h_center:
            ID2Data(ID2Type.region),
    },
    rname.dfc_i: {
        rname.dfc_h_right:
            ID2Data(ID2Type.region),
        rname.dfc_j:
            ID2Data(ID2Type.region, [[iname.dfc_key.value + "*4"]]),
    },
    rname.dfc_j: {
        rname.dfc_d:
            ID2Data(ID2Type.region, [[iname.dw_vanilla.value],
                                     [iname.dw_fun.value, iname.fire_sword.value],
                                     [iname.dw_fun.value, iname.melee.value, iname.weapon_projectile.value],
                                     [iname.can_phase_object.value, iname.dynamite.value, iname.weapon_no_dynamite.value]]),
        rname.dfc_i:
            ID2Data(ID2Type.region, [[iname.dfc_key.value + "*4"],
                                     [iname.dfc_key.value + "*3", iname.glitchless.value]]),
        rname.dfc_o:
            ID2Data(ID2Type.region),
    },
    rname.dfc_k: {
        lname.dfc_west_ice:
            ID2Data(ID2Type.location, [[iname.dw_vanilla.value],
                                       [iname.dw_fun.value, iname.fire_sword.value],
                                       [iname.dw_fun.value, iname.ice.value]]),
        rname.dfc_f:
            ID2Data(ID2Type.region),
    },
    rname.dfc_l: {
        rname.dfc_k:
            ID2Data(ID2Type.region),
        rname.dfc_m:
            ID2Data(ID2Type.region),
        rname.dfc_p:
            ID2Data(ID2Type.region, [[iname.dfc_key.value + "*4"]]),
    },
    rname.dfc_m: {
        rname.dfc_h_center:
            ID2Data(ID2Type.region),
        rname.dfc_n:
            ID2Data(ID2Type.region),
        rname.dfc_q:
            ID2Data(ID2Type.region),
    },
    rname.dfc_n: {
        rname.dfc_o:
            ID2Data(ID2Type.region),
        rname.dfc_r:
            ID2Data(ID2Type.region),
    },
    rname.dfc_o: {
        lname.dfc_east_ice:
            ID2Data(ID2Type.location, [[iname.dw_vanilla.value],
                                       [iname.dw_fun.value, iname.fire_sword.value],
                                       [iname.dw_fun.value, iname.ice.value]]),
        rname.dfc_j:
            ID2Data(ID2Type.region),
    },
    rname.dfc_p: {
        lname.dfc_west_light_bridge:
            ID2Data(ID2Type.location, [[iname.dw_vanilla.value],
                                       [iname.dw_fun.value, iname.fire_sword.value, iname.chain.value],
                                       [iname.dw_fun.value, iname.fire_mace.value],
                                       [iname.can_phase_gap.value]]),
        rname.dfc_l:
            ID2Data(ID2Type.region, [[iname.dfc_key.value + "*1"]]),
    },
    rname.dfc_q: {
        rname.dfc_p:
            ID2Data(ID2Type.region),
        rname.dfc_r:
            ID2Data(ID2Type.region),
        rname.dreamworld_fire_chain:
            ID2Data(ID2Type.region),
    },
    rname.dfc_r: {
        lname.dfc_east_light_bridge:
            ID2Data(ID2Type.location, [[iname.dw_vanilla.value],
                                       [iname.dw_fun.value, iname.fire_sword.value, iname.chain.value],
                                       [iname.dw_fun.value, iname.fire_mace.value],
                                       [iname.can_phase_gap.value]]),
        lname.dfc_free:
            ID2Data(ID2Type.location),
        rname.dfc_q:
            ID2Data(ID2Type.region),
    },
    # Bottomless Tower
    rname.di_a: {
        lname.di_blue_portal:
            ID2Data(ID2Type.location),
        rname.di_b:
            ID2Data(ID2Type.region, [[iname.dw_vanilla.value],
                                     [iname.dw_fun.value, iname.ice.value],
                                     [iname.can_phase_gap.value, iname.roll.value]]),
        rname.di_t:
            ID2Data(ID2Type.region),
    },
    rname.di_b: {
        rname.di_c:
            ID2Data(ID2Type.region),
        rname.di_h:
            ID2Data(ID2Type.region),
    },
    rname.di_c: {
        lname.di_1f_key:
            ID2Data(ID2Type.location, [[iname.dw_vanilla.value],
                                       [iname.dw_fun.value, iname.ice.value, iname.melee.value],
                                       [iname.dw_fun.value, iname.weapon_projectile.value],
                                       [iname.dw_fun.value, iname.melee.value, iname.chain.value, iname.can_phase_doors.value],
                                       [iname.dw_fun.value, iname.can_phase_object.value, iname.ice.value]]),
        rname.di_b:
            ID2Data(ID2Type.region),
        rname.di_i:
            ID2Data(ID2Type.region),
    },
    rname.di_d: {
        lname.di_2f_card:
            ID2Data(ID2Type.location, [[iname.dw_vanilla.value],
                                       [iname.dw_fun.value, iname.ice.value, iname.melee.value],
                                       [iname.can_phase_object.value, iname.roll.value],
                                       [iname.can_phase_object.value, iname.ice.value]]),
        rname.di_j:
            ID2Data(ID2Type.region),
    },
    rname.di_e: {
        rname.di_k_top:
            ID2Data(ID2Type.region),
        rname.di_t:
            ID2Data(ID2Type.region),
    },
    rname.di_f: {
        lname.di_2f_key:
            ID2Data(ID2Type.location),
        rname.di_l_right:
            ID2Data(ID2Type.region),
    },
    rname.di_g: {
        lname.di_1f_card:
            ID2Data(ID2Type.location, [[iname.dw_vanilla.value],
                                       [iname.dw_fun.value, iname.ice.value, iname.melee.value],
                                       [iname.dw_fun.value, iname.force.value, iname.ice.value],
                                       [iname.can_phase_gap_difficult.value],
                                       [iname.dw_fun.value, iname.can_phase_doors.value, iname.can_phase_dynamite.value]]),
        rname.di_h:
            ID2Data(ID2Type.region),
    },
    rname.di_h: {
        rname.di_b:
            ID2Data(ID2Type.region),
        rname.di_g:
            ID2Data(ID2Type.region),
        rname.di_i:
            ID2Data(ID2Type.region),
        rname.di_n:
            ID2Data(ID2Type.region),
        rname.dreamworld_ice:
            ID2Data(ID2Type.region),
    },
    rname.di_i: {
        rname.di_c:
            ID2Data(ID2Type.region),
        rname.di_h:
            ID2Data(ID2Type.region),
        rname.di_o:
            ID2Data(ID2Type.region, [[iname.dw_vanilla.value, iname.glitchless.value, iname.di_key.value + "*1"],
                                     [iname.di_key.value + "*3"]]),
    },
    rname.di_j: {
        rname.di_d:
            ID2Data(ID2Type.region),
        rname.di_k_left:
            ID2Data(ID2Type.region),
        rname.di_p:
            ID2Data(ID2Type.region),
    },
    rname.di_k_left: {
        rname.di_k_top:
            ID2Data(ID2Type.region, [[iname.dw_vanilla.value, iname.di_2f_fire.value],
                                     [iname.dw_fun.value, iname.di_2f_fire.value, iname.ice.value, iname.melee.value],
                                     [iname.dw_fun.value, iname.fire_sword.value, iname.ice.value],
                                     [iname.dw_fun.value, iname.force_jump.value],
                                     [iname.can_phase_gap.value]]),
        rname.di_k_right:
            ID2Data(ID2Type.region, [[iname.dw_vanilla.value],
                                     [iname.dw_fun.value, iname.ice.value, iname.melee.value],
                                     [iname.dw_fun.value, iname.force_jump.value],
                                     [iname.can_phase_gap.value]]),
        rname.di_j:
            ID2Data(ID2Type.region),
    },
    rname.di_k_top: {
        rname.di_e:
            ID2Data(ID2Type.region),
        rname.di_k_left:
            ID2Data(ID2Type.region),
    },
    rname.di_k_right: {
        rname.di_k_left:
            ID2Data(ID2Type.region, [[iname.dw_fun.value, iname.force.value],
                                     [iname.can_phase_gap.value]]),
        rname.di_l_left:
            ID2Data(ID2Type.region),
    },
    rname.di_l_left: {
        rname.di_k_right:
            ID2Data(ID2Type.region),
        rname.di_l_right:
            ID2Data(ID2Type.region, [[iname.dw_vanilla.value],
                                     [iname.dw_fun.value, iname.ice.value],
                                     # maybe dumb?
                                     [iname.dw_fun.value, iname.dynamite.value],
                                     [iname.dw_fun.value, iname.force.value],
                                     [iname.dw_fun.value, iname.fire_sword.value]]),
    },
    rname.di_l_right: {
        rname.di_f:
            ID2Data(ID2Type.region),
        rname.di_r:
            ID2Data(ID2Type.region, [[iname.dw_vanilla.value, iname.glitchless.value, iname.di_key.value + "*2"],
                                     [iname.di_key.value + "*3"]]),
    },
    rname.di_m: {
        rname.di_g:
            ID2Data(ID2Type.region),
        rname.di_n:
            ID2Data(ID2Type.region),
        rname.di_p:
            ID2Data(ID2Type.region),
    },
    rname.di_n: {
        rname.di_h:
            ID2Data(ID2Type.region, [[iname.dw_vanilla.value, iname.di_1f_fire.value],
                                     [iname.dw_fun.value, iname.di_1f_fire.value, iname.melee.value],
                                     [iname.dw_fun.value, iname.fire_sword.value],
                                     [iname.can_phase_doors.value],
                                     [iname.dw_fun.value, iname.can_phase_dynamite.value]]),
        rname.di_m:
            ID2Data(ID2Type.region, [[iname.dw_vanilla.value, iname.di_1f_fire.value],
                                     [iname.dw_fun.value, iname.di_1f_fire.value, iname.melee.value],
                                     [iname.dw_fun.value, iname.fire_sword.value],
                                     [iname.can_phase_doors.value]]),
    },
    rname.di_o: {
        lname.di_1f_fire:
            ID2Data(ID2Type.location, [[iname.dw_vanilla.value],
                                       [iname.dw_fun.value, iname.melee.value, iname.ice.value],
                                       [iname.dw_fun.value, iname.can_phase_object.value, iname.melee.value]], iname.di_1f_fire.value),
        rname.di_n:
            ID2Data(ID2Type.region, [[iname.di_1f_fire.value]]),
        rname.di_i:
            ID2Data(ID2Type.region, [[iname.di_key.value + "*4", iname.dw_fun.value, iname.ice.value, iname.can_phase_object.value],
                                     [iname.di_key.value + "*4", iname.can_phase_object.value, iname.roll.value],
                                     [iname.di_key.value + "*4", iname.dw_vanilla.value, iname.can_phase_doors.value],
                                     [iname.di_key.value + "*4", iname.dw_fun.value, iname.melee.value, iname.can_phase_doors.value]]),
    },
    rname.di_p: {
        rname.di_j:
            ID2Data(ID2Type.region),
        rname.di_m:
            ID2Data(ID2Type.region),
    },
    rname.di_q: {
        lname.di_2f_fire:
            ID2Data(ID2Type.location, [[iname.dw_vanilla.value],
                                       [iname.dw_fun.value, iname.melee.value]], iname.di_2f_fire.value),
        rname.di_k_left:
            ID2Data(ID2Type.region, [[iname.di_2f_fire.value]]),
    },
    rname.di_r: {
        rname.di_l_right:
            ID2Data(ID2Type.region, [[iname.di_key.value + "*4"]]),
        rname.di_q:
            ID2Data(ID2Type.region, [[iname.dw_vanilla.value],
                                     [iname.dw_fun.value, iname.ice.value],
                                     [iname.dw_fun.value, iname.dynamite.value, iname.force.value]]),
    },
    rname.di_s: {
        rname.di_t:
            ID2Data(ID2Type.region, [[iname.di_key.value + "*4"]]),
        rname.di_v_left:
            ID2Data(ID2Type.region),
    },
    rname.di_t: {
        rname.di_a:
            ID2Data(ID2Type.region),
        rname.di_s:
            ID2Data(ID2Type.region, [[iname.di_key.value + "*3"]]),
        rname.di_u:
            ID2Data(ID2Type.region, [[iname.di_3f_fire.value],
                                     [iname.dw_fun.value, iname.fire_sword.value]]),
        rname.di_x:
            ID2Data(ID2Type.region),
        rname.di_ab:
            ID2Data(ID2Type.region),
    },
    rname.di_u: {
        rname.di_y:
            ID2Data(ID2Type.region),
    },
    rname.di_v_left: {
        rname.di_s:
            ID2Data(ID2Type.region),
        rname.di_v_right:
            ID2Data(ID2Type.region, [[iname.dw_vanilla.value],
                                     [iname.dw_fun.value, iname.ice.value],
                                     [iname.can_phase_gap.value]]),
        rname.di_ac:
            ID2Data(ID2Type.region, [[iname.di_key.value + "*4"]]),
    },
    rname.di_v_right: {
        rname.di_v_left:
            ID2Data(ID2Type.region, [[iname.dw_vanilla.value],
                                     [iname.dw_fun.value, iname.ice.value],
                                     [iname.can_phase_object.value]]),
        rname.di_w:
            ID2Data(ID2Type.region),
    },
    rname.di_w: {
        lname.di_4f_key:
            ID2Data(ID2Type.location, [[iname.dw_vanilla.value],
                                       [iname.dw_fun.value, iname.ice.value, iname.melee.value],
                                       [iname.can_phase_gap.value, iname.roll],
                                       [iname.can_phase_object.value]]),
        rname.di_v_right:
            ID2Data(ID2Type.region),
    },
    rname.di_x: {
        lname.di_3f_spike_gates:
            ID2Data(ID2Type.location, [[iname.dw_vanilla.value],
                                       [iname.dw_fun.value, iname.ice.value]]),
        rname.di_t:
            ID2Data(ID2Type.region),
    },
    rname.di_y: {
        lname.di_3f_ice_square:
            ID2Data(ID2Type.location, [[iname.dw_vanilla.value],
                                       [iname.dw_fun.value, iname.ice.value],
                                       [iname.dw_fun.value, iname.fire_sword.value]]),
        rname.di_t:
            ID2Data(ID2Type.region, [[iname.dw_vanilla.value],
                                     [iname.dw_fun.value, iname.weapon_any.value]]),
        rname.di_u:
            ID2Data(ID2Type.region),
    },
    rname.di_z: {
        lname.di_reward_a:
            ID2Data(ID2Type.location),
        lname.di_reward_b:
            ID2Data(ID2Type.location),
        lname.di_reward_c:
            ID2Data(ID2Type.location),
        lname.event_finished_di:
            ID2Data(ID2Type.location, [[]], iname.dw_finished_dungeon.value),
        rname.dreamworld_ice:
            ID2Data(ID2Type.region),
        # Super Secret!
        rname.dreamfly_nursery:
            ID2Data(ID2Type.region),
    },
    rname.di_aa: {
        lname.di_3f_fire:
            ID2Data(ID2Type.location, [[iname.dw_vanilla.value],
                                       [iname.dw_fun.value, iname.melee.value]], iname.di_3f_fire.value),
        rname.di_t:
            ID2Data(ID2Type.region, [[iname.di_3f_fire.value]]),
        rname.di_ac:
            ID2Data(ID2Type.region),
    },
    rname.di_ab: {
        lname.di_3f_key:
            ID2Data(ID2Type.location, [[iname.dw_vanilla.value],
                                       [iname.dw_fun.value, iname.ice.value, iname.melee.value],
                                       [iname.can_phase_gap.value]]),
        rname.di_t:
            ID2Data(ID2Type.region),
    },
    rname.di_ac: {
        rname.di_aa:
            ID2Data(ID2Type.region),
        rname.di_v_left:
            ID2Data(ID2Type.region, [[iname.di_key.value + "*4"]]),
        rname.di_ad:
            ID2Data(ID2Type.region, [[iname.dw_vanilla.value, iname.di_3f_fire.value],
                                     [iname.dw_fun.value, iname.di_3f_fire.value, iname.ice.value],
                                     [iname.dw_fun.value, iname.fire_sword.value, iname.ice.value]]),
    },
    rname.di_ad: {
        rname.di_ae:
            ID2Data(ID2Type.region),
    },
    rname.di_ae: {
        rname.di_z:
            ID2Data(ID2Type.region, [[iname.dw_vanilla.value],
                                     [iname.dw_fun.value, iname.ice.value, iname.roll.value],
                                     [iname.dw_fun.value, iname.fire_sword.value, iname.roll.value],
                                     [iname.dw_fun.value, iname.force.value, iname.roll.value]]),
    },
    # Quietus
    rname.da_a: {
        lname.da_nw_crystal:
            ID2Data(ID2Type.location, [[iname.dw_vanilla.value],
                                       [iname.dw_fun.value, iname.ice.value, iname.weapon_projectile.value, iname.chain.value, iname.melee.value],
                                       [iname.dw_fun.value, iname.ice.value, iname.dynamite.value, iname.roll.value, iname.melee.value, iname.chain.value, iname.can_phase_gap_difficult.value],
                                       [iname.dw_fun.value, iname.ice.value, iname.can_phase_object.value]], iname.da_crystal.value),
        rname.da_d:
            ID2Data(ID2Type.region),
        rname.da_f:
            ID2Data(ID2Type.region),
    },
    rname.da_b: {
        rname.dreamworld_end:
            ID2Data(ID2Type.region),
        rname.da_d:
            ID2Data(ID2Type.region),
        rname.da_e:
            ID2Data(ID2Type.region),
        rname.da_h:
            ID2Data(ID2Type.region),
    },
    rname.da_c: {
        lname.da_ne_crystal:
            ID2Data(ID2Type.location, [[iname.dw_vanilla.value],
                                       [iname.dw_fun.value, iname.melee.value, iname.force.value, iname.ice.value, iname.chain.value],
                                       [iname.dw_fun.value, iname.can_phase_gap.value, iname.melee.value, iname.chain.value, iname.force.value, iname.roll.value],
                                       [iname.dw_fun.value, iname.can_phase_object.value, iname.weapon_no_dynamite.value]], iname.da_crystal.value),
        rname.da_e:
            ID2Data(ID2Type.region),
        rname.da_j:
            ID2Data(ID2Type.region),
    },
    rname.da_d: {
        rname.da_a:
            ID2Data(ID2Type.region, [[iname.dw_vanilla.value, iname.roll.value],
                                     [iname.dw_fun.value, iname.weapon_projectile.value, iname.roll.value],
                                     [iname.can_phase_gap.value]]),
        rname.da_b:
            ID2Data(ID2Type.region, [[iname.dw_vanilla.value, iname.roll.value],
                                     [iname.dw_fun.value, iname.weapon_projectile.value, iname.roll.value],
                                     [iname.can_phase_gap.value]]),
    },
    rname.da_e: {
        rname.da_b:
            ID2Data(ID2Type.region, [[iname.dw_vanilla.value],
                                     [iname.dw_fun.value, iname.weapon_projectile.value]]),
        rname.da_c:
            ID2Data(ID2Type.region, [[iname.dw_vanilla.value],
                                     [iname.dw_fun.value, iname.weapon_projectile.value]]),
    },
    rname.da_f: {
        lname.da_alternating_floors:
            ID2Data(ID2Type.location, [[iname.dw_vanilla.value],
                                       [iname.dw_fun.value, iname.force.value, iname.ice.value],
                                       [iname.can_phase_gap.value]]),
        rname.da_a:
            ID2Data(ID2Type.region),
        rname.da_l:
            ID2Data(ID2Type.region),
    },
    rname.da_g: {
        lname.da_northwest_vault:
            ID2Data(ID2Type.location, [[iname.dw_vanilla.value],
                                       [iname.dw_fun.value, iname.fire_sword.value, iname.chain.value, iname.force.value, iname.ice.value],
                                       [iname.can_phase_gap.value]]),
        rname.da_m:
            ID2Data(ID2Type.region, [[iname.da_key.value + "*4"]]),
    },
    rname.da_h: {
        rname.da_b:
            ID2Data(ID2Type.region),
        rname.da_n:
            ID2Data(ID2Type.region),
    },
    rname.da_i: {
        lname.da_northeast_vault:
            ID2Data(ID2Type.location, [[iname.dw_vanilla.value],
                                       [iname.dw_fun.value, iname.force.value],
                                       [iname.can_phase_object.value]]),
        rname.da_o:
            ID2Data(ID2Type.region, [[iname.da_key.value + "*4"]]),
    },
    rname.da_j: {
        lname.da_tangled_wires:
            ID2Data(ID2Type.location, [[iname.dw_vanilla.value],
                                       [iname.dw_fun.value, iname.melee.value, iname.chain.value],
                                       [iname.dw_fun.value, iname.can_phase_dynamite.value]]),
        rname.da_c:
            ID2Data(ID2Type.region),
        rname.da_p:
            ID2Data(ID2Type.region),
    },
    rname.da_k: {
        rname.da_b:
            ID2Data(ID2Type.region),
    },
    rname.da_l: {
        rname.da_f:
            ID2Data(ID2Type.region),
        rname.da_k:
            ID2Data(ID2Type.region, [[iname.dw_vanilla.value],
                                     [iname.dw_fun.value, iname.dynamite.value]]),
        rname.da_m:
            ID2Data(ID2Type.region),
        rname.da_r:
            ID2Data(ID2Type.region),
    },
    rname.da_m: {
        rname.da_g:
            ID2Data(ID2Type.region, [[iname.da_key.value + "*4"]]),
        rname.da_l:
            ID2Data(ID2Type.region),
        rname.da_n:
            ID2Data(ID2Type.region),
    },
    rname.da_n: {
        lname.da_center:
            ID2Data(ID2Type.location),
        lname.da_center_crystal:
            ID2Data(ID2Type.location, [[iname.dw_vanilla.value],
                                       [iname.dw_fun.value, iname.ice.value, iname.force.value],
                                       [iname.dw_fun.value, iname.can_phase_gap.value, iname.melee.value, iname.chain.value],
                                       [iname.dw_fun.value, iname.can_phase_gap.value, iname.weapon_projectile.value],
                                       [iname.dw_fun.value, iname.can_phase_gap.value, iname.dynamite.value],
                                       [iname.dw_fun.value, iname.can_phase_object.value, iname.ice.value]], iname.da_center_crystal.value),
        rname.da_h:
            ID2Data(ID2Type.region),
        rname.da_m:
            ID2Data(ID2Type.region),
        rname.da_o:
            ID2Data(ID2Type.region),
        rname.da_t:
            ID2Data(ID2Type.region),
    },
    rname.da_o: {
        rname.da_i:
            ID2Data(ID2Type.region, [[iname.da_key.value + "*4"]]),
        rname.da_n:
            ID2Data(ID2Type.region),
        rname.da_p:
            ID2Data(ID2Type.region),
    },
    rname.da_p: {
        rname.da_j:
            ID2Data(ID2Type.region),
        rname.da_o:
            ID2Data(ID2Type.region),
        rname.da_q:
            ID2Data(ID2Type.region, [[iname.dw_vanilla.value],
                                     [iname.dw_fun.value, iname.dynamite.value]]),
        rname.da_v:
            ID2Data(ID2Type.region),
    },
    rname.da_q: {
        rname.da_b:
            ID2Data(ID2Type.region),
    },
    rname.da_r: {
        lname.da_push_the_coil:
            ID2Data(ID2Type.location, [[iname.dw_vanilla.value],
                                       [iname.dw_fun.value, iname.melee.value, iname.force.value, iname.dynamite.value, iname.ice.value],
                                       [iname.can_phase_object.value]]),
        rname.da_l:
            ID2Data(ID2Type.region),
        rname.da_w:
            ID2Data(ID2Type.region),
    },
    rname.da_s: {
        lname.da_southwest_vault:
            ID2Data(ID2Type.location),
        rname.da_x:
            ID2Data(ID2Type.region, [[iname.da_key.value + "*4"]]),
    },
    rname.da_t: {
        rname.da_n:
            ID2Data(ID2Type.region),
        rname.da_y:
            ID2Data(ID2Type.region, [[iname.dw_vanilla.value],
                                     [iname.dw_fun.value, iname.dynamite.value]]),
    },
    rname.da_u: {
        lname.da_southeast_vault:
            ID2Data(ID2Type.location, [[iname.dw_vanilla.value],
                                       [iname.dw_fun.value, iname.melee.value, iname.force.value, iname.ice.value],
                                       [iname.can_phase_object.value]]),
        rname.da_z:
            ID2Data(ID2Type.region, [[iname.da_key.value + "*4"]]),
    },
    rname.da_v: {
        lname.da_giant_mess:
            ID2Data(ID2Type.location, [[iname.dw_vanilla.value],
                                       [iname.dw_fun.value, iname.fire_sword.value, iname.chain.value, iname.dynamite.value, iname.ice.value],
                                       [iname.dw_fun.value, iname.can_phase_doors.value, iname.can_phase_object.value, iname.ice.value]]),
        rname.da_p:
            ID2Data(ID2Type.region, [[iname.dw_vanilla.value],
                                     [iname.dw_fun.value, iname.melee.value, iname.chain.value],
                                     [iname.can_phase_doors.value]]),
        rname.da_aa:
            ID2Data(ID2Type.region, [[iname.dw_vanilla.value],
                                     [iname.dw_fun.value, iname.fire_sword.value],
                                     [iname.can_phase_doors.value]]),
    },
    rname.da_w: {
        lname.da_sw_crystal:
            ID2Data(ID2Type.location, [[iname.dw_vanilla.value],
                                       [iname.dw_fun.value, iname.melee.value, iname.chain.value, iname.dynamite.value, iname.force.value, iname.ice.value],
                                       [iname.dw_fun.value, iname.can_phase_gap.value, iname.melee.value, iname.chain.value, iname.force.value],
                                       [iname.dw_fun.value, iname.can_phase_object.value, iname.weapon_no_dynamite.value]], iname.da_crystal.value),
        rname.da_r:
            ID2Data(ID2Type.region),
        rname.da_x:
            ID2Data(ID2Type.region),
    },
    rname.da_x: {
        rname.da_s:
            ID2Data(ID2Type.region, [[iname.da_key.value + "*4"]]),
        rname.da_w:
            ID2Data(ID2Type.region),
        rname.da_y:
            ID2Data(ID2Type.region, [[iname.dw_vanilla.value],
                                     [iname.dw_fun.value, iname.dynamite.value]]),
    },
    rname.da_y: {
        rname.da_b:
            ID2Data(ID2Type.region),
        rname.da_t:
            ID2Data(ID2Type.region),
        rname.da_x:
            ID2Data(ID2Type.region),
        rname.da_z:
            ID2Data(ID2Type.region),
        rname.da_ac:
            ID2Data(ID2Type.region, [[iname.da_crystal.value + "*4", iname.da_center_crystal.value],
                                     [iname.dw_fun.value, iname.da_center_crystal.value, iname.can_phase_object.value, iname.ice.value, iname.major_skips.value],
                                     [iname.dw_fun.value, iname.can_phase_dynamite_difficult.value, iname.major_skips.value]]),
    },
    rname.da_z: {
        rname.da_u:
            ID2Data(ID2Type.region, [[iname.da_key.value + "*4"]]),
        rname.da_y:
            ID2Data(ID2Type.region, [[iname.dw_vanilla.value],
                                     [iname.dw_fun.value, iname.dynamite.value]]),
        rname.da_aa:
            ID2Data(ID2Type.region),
    },
    rname.da_aa: {
        lname.da_se_crystal:
            ID2Data(ID2Type.location, [[iname.dw_vanilla.value],
                                       [iname.dw_fun.value, iname.melee.value, iname.chain.value, iname.force.value, iname.ice.value],
                                       [iname.dw_fun.value, iname.can_phase_gap.value, iname.melee.value, iname.chain.value, iname.ice.value],
                                       [iname.dw_fun.value, iname.can_phase_object.value, iname.weapon_no_dynamite.value]], iname.da_crystal.value),
        rname.da_z:
            ID2Data(ID2Type.region),
        rname.da_v:
            ID2Data(ID2Type.region),
    },
    rname.da_ab: {
        lname.da_reward_a:
            ID2Data(ID2Type.location),
        lname.da_reward_b:
            ID2Data(ID2Type.location),
        lname.da_reward_c:
            ID2Data(ID2Type.location),
        rname.dreamworld_end:
            ID2Data(ID2Type.region),
    },
    rname.da_ac: {
        rname.da_ad:
            ID2Data(ID2Type.region),
    },
    rname.da_ad: {
        rname.da_ab:
            ID2Data(ID2Type.region, [[iname.dw_vanilla.value, iname.roll.value],
                                     [iname.dw_fun.value, iname.dynamite.value, iname.ice.value, iname.roll.value],
                                     [iname.dw_fun.value, iname.can_phase_object.value, iname.dynamite.value, iname.ice.value, iname.roll.value]]),
        rname.da_ac:
            ID2Data(ID2Type.region),
    },

    # Portal Worlds
    rname.autumn_climb: {
        lname.autumn_climb:
            ID2Data(ID2Type.location, [[iname.can_open_chests.value]]),
        rname.ffc_a:
            ID2Data(ID2Type.region),
    },
    rname.the_vault_a: {
        rname.the_vault_b_left:
            ID2Data(ID2Type.region),
        rname.the_vault_d:
            ID2Data(ID2Type.region),
    },
    rname.the_vault_b_left: {
        rname.the_vault_a:
            ID2Data(ID2Type.region),
        rname.the_vault_b_center:
            ID2Data(ID2Type.region),
        lname.switch_vault_left:
            ID2Data(ID2Type.location, [[]], iname.the_vault_left.value)
    },
    rname.the_vault_b_center: {
        lname.the_vault:
            ID2Data(ID2Type.location,
                    [[iname.can_open_chests.value, iname.the_vault_left.value, iname.the_vault_right.value]]),
        rname.the_vault_d:
            ID2Data(ID2Type.region),
    },
    rname.the_vault_b_right: {
        rname.the_vault_c:
            ID2Data(ID2Type.region),
        rname.the_vault_b_center:
            ID2Data(ID2Type.region),
        lname.switch_vault_right:
            ID2Data(ID2Type.location, [[]], iname.the_vault_right.value),
    },
    rname.the_vault_c: {
        rname.the_vault_b_right:
            ID2Data(ID2Type.region),
        rname.the_vault_d:
            ID2Data(ID2Type.region),
    },
    rname.the_vault_d: {
        rname.the_vault_a:
            ID2Data(ID2Type.region),
        rname.the_vault_c:
            ID2Data(ID2Type.region),
        rname.scc_e:
            ID2Data(ID2Type.region),
    },
    rname.painful_plain: {
        lname.painful_plain:
            ID2Data(ID2Type.location, [[iname.basic_combat.value]]),
    },
    rname.farthest_shore: {
        lname.farthest_shore:
            ID2Data(ID2Type.location, [[iname.can_open_chests.value]]),
        rname.nowhere:
            ID2Data(ID2Type.region),
    },
    rname.scrap_yard_a: {
        lname.scrap_yard:
            ID2Data(ID2Type.location, [[iname.melee.value, iname.roll.value],
                                       [iname.force.value, iname.roll.value],
                                       [iname.dynamite.value, iname.roll.value]]),
    },
    rname.scrap_yard_b: {
        rname.scrap_yard_c_left:
            ID2Data(ID2Type.region, [[iname.basic_combat.value]]),
        rname.scrap_yard_e:
            ID2Data(ID2Type.region),
    },
    rname.scrap_yard_c_left: {
        lname.block_scrap_yard_left:
            ID2Data(ID2Type.location, [[]], iname.scrap_yard_left.value),
        rname.scrap_yard_c_center:
            ID2Data(ID2Type.region),
    },
    rname.scrap_yard_c_center: {
        rname.scrap_yard_a:
            ID2Data(ID2Type.region, [[iname.scrap_yard_left.value, iname.scrap_yard_right.value],
                                     [iname.scrap_yard_left.value, iname.ice.value],
                                     [iname.scrap_yard_right.value, iname.ice.value],
                                     [iname.can_phase_gap.value, iname.ice.value]]),
        rname.scrap_yard_c_left:
            ID2Data(ID2Type.region, [[iname.can_phase_gap.value]]),
        rname.scrap_yard_c_right:
            ID2Data(ID2Type.region, [[iname.can_phase_gap.value]]),
    },
    rname.scrap_yard_c_right: {
        lname.block_scrap_yard_right:
            ID2Data(ID2Type.location, [[]], iname.scrap_yard_right.value),
        rname.scrap_yard_c_center:
            ID2Data(ID2Type.region),
    },
    rname.scrap_yard_d: {
        rname.scrap_yard_c_right:
            ID2Data(ID2Type.region, [[iname.basic_combat.value]]),
        rname.scrap_yard_f:
            ID2Data(ID2Type.region),
    },
    rname.scrap_yard_e: {
        rname.scrap_yard_b:
            ID2Data(ID2Type.region),
        rname.scrap_yard_f:
            ID2Data(ID2Type.region),
    },
    rname.scrap_yard_f: {
        rname.scrap_yard_c_center:
            ID2Data(ID2Type.region),
        rname.scrap_yard_e:
            ID2Data(ID2Type.region),
        rname.scrap_yard_g:
            ID2Data(ID2Type.region)
    },
    rname.scrap_yard_g: {
        rname.scrap_yard_d:
            ID2Data(ID2Type.region),
        rname.scrap_yard_f:
            ID2Data(ID2Type.region, [[iname.can_phase_gap.value]]),
    },
    rname.brutal_oasis: {
        lname.brutal_oasis:
            ID2Data(ID2Type.location, [[iname.basic_combat.value, iname.roll.value]]),
        rname.swc_n:
            ID2Data(ID2Type.region),
    },
    rname.former_colossus: {
        rname.former_colossus_end:
            ID2Data(ID2Type.region, [[iname.melee.value],
                                     [iname.can_phase_object.value, iname.ice.value],
                                     [iname.can_phase_enemy_difficult.value, iname.roll.value]]),
        rname.cave_of_mystery_a:
            # technically a softlock
            ID2Data(ID2Type.region, [[iname.can_phase_gap_difficult.value, iname.roll.value]]),
        rname.swc_p:
            ID2Data(ID2Type.region),
    },
    rname.former_colossus_end: {
        lname.former_colossus:
            ID2Data(ID2Type.location, [[iname.can_open_chests.value]]),
        rname.former_colossus:
            ID2Data(ID2Type.region, [[iname.can_phase_dynamite.value],
                                     [iname.can_phase_enemy_difficult.value, iname.roll.value]]),
        rname.cave_of_mystery_a:
            ID2Data(ID2Type.region, [[iname.weapon_any.value]]),
    },
    rname.sand_crucible_a: {
        lname.sand_crucible:
            ID2Data(ID2Type.location, [[iname.basic_combat.value, iname.roll.value]]),
        rname.sand_crucible_c:
            ID2Data(ID2Type.region),
    },
    rname.sand_crucible_b: {
        rname.sand_crucible_a:
            ID2Data(ID2Type.region, [[iname.basic_combat.value, iname.roll.value]]),
    },
    rname.sand_crucible_c: {
        rname.sand_crucible_d:
            ID2Data(ID2Type.region, [[iname.weapon_any.value]]),
        rname.ssc_h:
            ID2Data(ID2Type.region),
    },
    rname.sand_crucible_d: {
        rname.sand_crucible_c:
            ID2Data(ID2Type.region, [[iname.weapon_any.value]]),
        rname.sand_crucible_b:
            ID2Data(ID2Type.region, [[iname.basic_combat.value]]),
    },
    rname.ocean_castle: {
        lname.ocean_castle:
            ID2Data(ID2Type.location, [[iname.can_open_chests.value, iname.roll.value],
                                       [iname.can_phase_dynamite.value]]),
    },
    rname.promenade_path: {
        lname.promenade_path:
            ID2Data(ID2Type.location, [[iname.weapon_any.value]]),
    },
    rname.maze_of_steel_a_left: {
        rname.maze_of_steel_a_right:
            ID2Data(ID2Type.region, [[iname.basic_combat.value],
                                     [iname.roll.value]]),
        rname.maze_of_steel_e:
            ID2Data(ID2Type.region, [[iname.weapon_any.value]]),
    },
    rname.maze_of_steel_a_right: {
        lname.maze_of_steel:
            ID2Data(ID2Type.location, [[iname.can_open_chests.value]]),
        rname.maze_of_steel_a_left:
            ID2Data(ID2Type.region, [[iname.can_phase_dynamite.value]]),
        rname.maze_of_steel_b:
            ID2Data(ID2Type.region),
    },
    rname.maze_of_steel_b: {
        rname.maze_of_steel_d:
            ID2Data(ID2Type.region),
    },
    rname.maze_of_steel_c: {
        rname.maze_of_steel_a_left:
            ID2Data(ID2Type.region, [[iname.basic_combat.value]]),
        rname.maze_of_steel_d:
            ID2Data(ID2Type.region),
    },
    rname.maze_of_steel_d: {
        rname.maze_of_steel_c:
            ID2Data(ID2Type.region),
        rname.ppc_t:
            ID2Data(ID2Type.region),
    },
    rname.maze_of_steel_e: {
        rname.maze_of_steel_a_left:
            ID2Data(ID2Type.region, [[iname.weapon_any.value]]),
        rname.maze_of_steel_f:
            ID2Data(ID2Type.region, [[iname.weapon_any.value]]),
    },
    rname.maze_of_steel_f: {
        rname.maze_of_steel_e:
            ID2Data(ID2Type.region, [[iname.weapon_any.value]]),
    },
    rname.wall_of_text_a: {
        rname.wall_of_text_b:
            ID2Data(ID2Type.region),
        rname.fcc_d:
            ID2Data(ID2Type.region),
    },
    rname.wall_of_text_b: {
        lname.wall_of_text:
            ID2Data(ID2Type.location, [[iname.can_open_chests.value, iname.roll.value],
                                       [iname.can_phase_doors.value, iname.weapon_any.value],
                                       [iname.can_phase_dynamite.value]]),
        rname.wall_of_text_c:
            ID2Data(ID2Type.region, [[iname.weapon_any.value, iname.roll.value],
                                     [iname.can_phase_doors.value, iname.weapon_any.value],
                                     [iname.can_phase_dynamite.value]])
    },
    rname.wall_of_text_c: {
        rname.wall_of_text_b:
            ID2Data(ID2Type.region, [[iname.weapon_any.value]]),
    },
    rname.lost_city_a_left: {
        rname.lost_city_a_right:
            ID2Data(ID2Type.region, [[iname.can_phase_doors.value],
                                     [iname.can_phase_dynamite.value],
                                     [iname.can_phase_enemy.value]]),
        rname.lost_city_c:
            ID2Data(ID2Type.region),
    },
    rname.lost_city_a_right: {
        rname.lost_city_a_left:
            ID2Data(ID2Type.region, [[iname.basic_combat.value],
                                     [iname.can_phase_doors.value]]),
        rname.lost_city_b:
            ID2Data(ID2Type.region),
    },
    rname.lost_city_b: {
        rname.lost_city_a_right:
            ID2Data(ID2Type.region),
        rname.lost_city_d:
            ID2Data(ID2Type.region),
    },
    rname.lost_city_c: {
        lname.lost_city:
            ID2Data(ID2Type.location, [[iname.can_open_chests.value]]),
        rname.lost_city_a_left:
            ID2Data(ID2Type.region),
        rname.lost_city_d:
            ID2Data(ID2Type.region, [[iname.melee.value, iname.chain.value],
                                     [iname.can_phase_object.value, iname.ice.value, iname.roll.value],
                                     [iname.can_phase_dynamite.value]]),
        rname.lost_city_e:
            ID2Data(ID2Type.region, [[iname.weapon_any.value]])
    },
    rname.lost_city_d: {
        rname.lost_city_b:
            ID2Data(ID2Type.region),
        rname.fcc_o:
            ID2Data(ID2Type.region),
    },
    rname.lost_city_e: {
        rname.lost_city_c:
            ID2Data(ID2Type.region, [[iname.weapon_any.value]]),
        rname.pr_q:
            ID2Data(ID2Type.region, [[iname.weapon_any.value]]),  # TODO remove vanilla requirements
    },
    rname.northern_end_a: {
        rname.northern_end_f:
            ID2Data(ID2Type.region),
    },
    rname.northern_end_b: {
        rname.northern_end_a:
            ID2Data(ID2Type.region, [[iname.basic_combat.value, iname.roll.value]]),
    },
    rname.northern_end_c: {
        rname.northern_end_b:
            ID2Data(ID2Type.region, [[iname.basic_combat.value, iname.roll.value]]),
    },
    rname.northern_end_d: {
        rname.northern_end_c:
            ID2Data(ID2Type.region, [[iname.basic_combat.value, iname.roll.value]]),
        rname.northern_end_e:
            ID2Data(ID2Type.region),
    },
    rname.northern_end_e: {
        rname.northern_end_d:
            ID2Data(ID2Type.region),
        rname.lrc_u:
            ID2Data(ID2Type.region),
    },
    rname.northern_end_f: {
        lname.northern_end:
            ID2Data(ID2Type.location, [[iname.can_open_chests.value]]),
        rname.northern_end_a:
            ID2Data(ID2Type.region),
        rname.northern_end_e:
            ID2Data(ID2Type.region),
    },
    rname.moon_garden_south: {
        rname.moon_garden_north:
            ID2Data(ID2Type.region, [[iname.basic_combat.value, iname.roll.value]]),
        rname.abyssal_plain:
            # Can just phase through the loading zone and navigate blind, using the map to help
            ID2Data(ID2Type.region, [[iname.can_phase_gap.value, iname.roll.value]]),
        rname.lrc_a:
            ID2Data(ID2Type.region),
    },
    rname.moon_garden_north: {
        lname.moon_garden:
            ID2Data(ID2Type.location, [[iname.can_open_chests.value]]),
        rname.moon_garden_south:
            ID2Data(ID2Type.region, [[iname.can_phase_dynamite.value],
                                     [iname.can_phase_enemy.value, iname.roll.value]]),
        rname.abyssal_plain:
            ID2Data(ID2Type.region),
    },
    rname.nowhere: {
        rname.farthest_shore:
            ID2Data(ID2Type.region),
    },
    rname.cave_of_mystery_a: {
        rname.cave_of_mystery_b:
            ID2Data(ID2Type.region, [[iname.weapon_any.value, iname.fake_efcs.value],
                                     [iname.weapon_any.value, iname.can_phase_doors.value],
                                     [iname.can_phase_gap.value, iname.ice.value],
                                     [iname.can_phase_dynamite.value]]),
        rname.former_colossus_end:
            ID2Data(ID2Type.region)
    },
    rname.cave_of_mystery_b: {
        rname.cave_of_mystery_a:
            ID2Data(ID2Type.region, [[iname.weapon_any.value, iname.fake_efcs.value],
                                     [iname.weapon_any.value, iname.can_phase_doors.value],
                                     [iname.can_phase_dynamite.value]]),
        rname.somewhere:
            ID2Data(ID2Type.region),
    },
    rname.somewhere: {
        rname.cave_of_mystery_b:
            ID2Data(ID2Type.region),
        rname.abandoned_house:
            ID2Data(ID2Type.region),
        rname.ludo_city:
            ID2Data(ID2Type.region),
    },
    rname.test_chamber: {
        rname.ffc_a:
            ID2Data(ID2Type.region),
    },
    rname.ludo_city: {
        lname.ludo_city:
            ID2Data(ID2Type.location, [[iname.can_open_chests.value]]),
        rname.somewhere:
            ID2Data(ID2Type.region),
    },
    rname.abyssal_plain: {
        rname.moon_garden_north:
            ID2Data(ID2Type.region),
        rname.place_p:
            ID2Data(ID2Type.region),
    },
    rname.place_a: {
        rname.place_b:
            ID2Data(ID2Type.region),
        rname.place_e:
            ID2Data(ID2Type.region),
    },
    rname.place_b: {
        rname.place_a:
            ID2Data(ID2Type.region),
        rname.place_c:
            ID2Data(ID2Type.region),
    },
    rname.place_c: {
        rname.place_b:
            ID2Data(ID2Type.region),
        rname.place_g_main:
            ID2Data(ID2Type.region),
    },
    rname.place_d: {
        rname.place_e:
            ID2Data(ID2Type.region),
    },
    rname.place_e: {
        rname.place_a:
            ID2Data(ID2Type.region),
        rname.place_d:
            ID2Data(ID2Type.region),
        rname.place_f:
            ID2Data(ID2Type.region),
    },
    rname.place_f: {
        rname.place_e:
            ID2Data(ID2Type.region),
        rname.place_g_alcove:
            ID2Data(ID2Type.region),
        rname.place_k:
            ID2Data(ID2Type.region),
    },
    rname.place_g_alcove: {
        rname.place_f:
            ID2Data(ID2Type.region),
        rname.place_g_main:
            ID2Data(ID2Type.region, [[iname.can_phase_doors.value]]),
    },
    rname.place_g_main: {
        rname.place_c:
            ID2Data(ID2Type.region),
        rname.place_g_alcove:
            ID2Data(ID2Type.region, [[iname.can_phase_doors.value]]),
        rname.place_h_alcove:
            ID2Data(ID2Type.region),
        rname.place_l_top:
            ID2Data(ID2Type.region),
    },
    rname.place_h_alcove: {
        rname.place_g_main:
            ID2Data(ID2Type.region),
        rname.place_h_main:
            ID2Data(ID2Type.region, [[iname.can_phase_doors.value]]),
    },
    rname.place_h_main: {
        rname.place_h_alcove:
            ID2Data(ID2Type.region, [[iname.can_phase_doors.value]]),
        rname.place_m:
            ID2Data(ID2Type.region),
        rname.lrc_a:
            ID2Data(ID2Type.region),
    },
    rname.place_i: {
        rname.place_j:
            ID2Data(ID2Type.region),
    },
    rname.place_j: {
        rname.place_i:
            ID2Data(ID2Type.region),
        rname.place_k:
            ID2Data(ID2Type.region),
    },
    rname.place_k: {
        rname.place_f:
            ID2Data(ID2Type.region),
        rname.place_j:
            ID2Data(ID2Type.region),
        rname.place_l_left:
            ID2Data(ID2Type.region),
        rname.place_n:
            ID2Data(ID2Type.region),
    },
    rname.place_l_top: {
        rname.place_g_main:
            ID2Data(ID2Type.region),
        rname.place_l_left:
            ID2Data(ID2Type.region, [[iname.can_phase_doors.value]]),
        rname.place_m:
            ID2Data(ID2Type.region),
    },
    rname.place_l_left: {
        rname.place_k:
            ID2Data(ID2Type.region),
        rname.place_l_top:
            ID2Data(ID2Type.region, [[iname.can_phase_doors.value]]),
    },
    rname.place_m: {
        rname.place_h_main:
            ID2Data(ID2Type.region),
        rname.place_l_top:
            ID2Data(ID2Type.region),
    },
    rname.place_n: {
        rname.place_k:
            ID2Data(ID2Type.region),
        rname.place_p:
            ID2Data(ID2Type.region),
    },
    rname.place_o: {
        rname.place_p:
            ID2Data(ID2Type.region),
    },
    rname.place_p: {
        rname.place_n:
            ID2Data(ID2Type.region),
        rname.place_o:
            ID2Data(ID2Type.region),
        rname.abyssal_plain:
            ID2Data(ID2Type.region),
    },
    rname.abandoned_house: {
        rname.somewhere:
            ID2Data(ID2Type.region),
    },
    rname.pr_b: {
        lname.promised_remedy:
            ID2Data(ID2Type.location, [[iname.weapon_any.value]]),
        rname.fcc_o:
            ID2Data(ID2Type.region),
    },
    rname.pr_c: {
        rname.pr_b:
            ID2Data(ID2Type.region, [[iname.efcs.value, iname.roll.value]]),
    },
    rname.pr_d: {
        rname.pr_c:
            ID2Data(ID2Type.region),
        rname.pr_e:
            ID2Data(ID2Type.region),
    },
    rname.pr_e: {
        rname.pr_d:
            ID2Data(ID2Type.region),
        rname.pr_g:
            ID2Data(ID2Type.region),
    },
    rname.pr_f: {
        rname.pr_j:
            ID2Data(ID2Type.region),
    },
    rname.pr_g: {
        rname.pr_e:
            ID2Data(ID2Type.region),
        rname.pr_h:
            ID2Data(ID2Type.region),
        rname.pr_k_top:
            ID2Data(ID2Type.region),
    },
    rname.pr_h: {
        rname.pr_g:
            ID2Data(ID2Type.region),
        rname.pr_t:
            ID2Data(ID2Type.region),
    },
    rname.pr_i: {
        rname.pr_j:
            ID2Data(ID2Type.region),
        rname.pr_o:
            ID2Data(ID2Type.region),
    },
    rname.pr_j: {
        rname.pr_f:
            ID2Data(ID2Type.region),
        rname.pr_i:
            ID2Data(ID2Type.region),
        rname.pr_k_middle:
            ID2Data(ID2Type.region),
    },
    rname.pr_k_top: {
        rname.pr_g:
            ID2Data(ID2Type.region),
        rname.pr_k_middle:
            ID2Data(ID2Type.region, [[iname.force.value],
                                     [iname.can_phase_object.value, iname.ice.value],
                                     [iname.can_phase_doors.value]]),
    },
    rname.pr_k_middle: {
        rname.pr_j:
            ID2Data(ID2Type.region),
        rname.pr_k_top:
            ID2Data(ID2Type.region, [[iname.can_phase_doors.value],
                                     [iname.can_phase_object.value, iname.ice.value]]),
        rname.pr_k_bottom:
            ID2Data(ID2Type.region, [[iname.force.value],
                                     [iname.can_phase_object.value, iname.ice.value],
                                     [iname.can_phase_doors.value]]),
        rname.pr_l:
            ID2Data(ID2Type.region)
    },
    rname.pr_k_bottom: {
        rname.pr_k_middle:
            ID2Data(ID2Type.region, [[iname.can_phase_object.value, iname.ice.value],
                                     [iname.can_phase_doors.value]]),
        rname.pr_q:
            ID2Data(ID2Type.region, [[iname.efcs.value]]),
    },
    rname.pr_l: {
        rname.pr_k_middle:
            ID2Data(ID2Type.region),
        rname.pr_r:
            ID2Data(ID2Type.region),
    },
    rname.pr_m: {
        rname.pr_s:
            ID2Data(ID2Type.region),
    },
    rname.pr_n: {
        rname.pr_o:
            ID2Data(ID2Type.region),
    },
    rname.pr_o: {
        rname.pr_i:
            ID2Data(ID2Type.region),
        rname.pr_n:
            ID2Data(ID2Type.region),
        rname.pr_p:
            ID2Data(ID2Type.region),
    },
    rname.pr_p: {
        rname.pr_o:
            ID2Data(ID2Type.region),
        rname.pr_q:
            ID2Data(ID2Type.region, [[iname.efcs.value]]),
    },
    rname.pr_q: {
        rname.pr_k_bottom:
            ID2Data(ID2Type.region, [[iname.efcs.value]]),
        rname.pr_p:
            ID2Data(ID2Type.region, [[iname.efcs.value]]),
        rname.fcc_o:
            ID2Data(ID2Type.region),
    },
    rname.pr_r: {
        rname.pr_l:
            ID2Data(ID2Type.region),
        rname.pr_s:
            ID2Data(ID2Type.region),
    },
    rname.pr_s: {
        rname.pr_m:
            ID2Data(ID2Type.region),
        rname.pr_r:
            ID2Data(ID2Type.region),
        rname.pr_t:
            ID2Data(ID2Type.region),
    },
    rname.pr_t: {
        rname.pr_h:
            ID2Data(ID2Type.region, [[iname.efcs.value]]),
        rname.pr_s:
            ID2Data(ID2Type.region, [[iname.efcs.value]]),
    },
    rname.house_of_secrets: {
        rname.dreamworld_hub:
            ID2Data(ID2Type.region),
    },
    rname.dreamfly_nursery: {
        rname.bad_dream:
            ID2Data(ID2Type.region),
    },
    rname.bad_dream: {
        lname.bad_dream:
            ID2Data(ID2Type.location),
        rname.fluffy_fields:
            ID2Data(ID2Type.region),
    }
}
