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
            ID2Data(ID2Type.region),
        rname.sweetwater_coast:
            ID2Data(ID2Type.region),
        rname.fancy_ruins:
            ID2Data(ID2Type.region),
        rname.star_woods:
            ID2Data(ID2Type.region),
        rname.slippery_slope:
            ID2Data(ID2Type.region),
        rname.dreamworld:
            ID2Data(ID2Type.region, [[iname.has_opened_dw.value]]),  # TODO add dream world event requirements
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
        rname.ffc_t:
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
            ID2Data(ID2Type.region),
        rname.slippery_slope:
            ID2Data(ID2Type.region),
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
                                     [iname.can_phase_ice.value, iname.roll.value],
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
            ID2Data(ID2Type.region),
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
            ID2Data(ID2Type.region),
        rname.pepperpain_prairie:
            ID2Data(ID2Type.region),
        rname.frozen_court:
            ID2Data(ID2Type.region),
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
            ID2Data(ID2Type.region),
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
            ID2Data(ID2Type.region),
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
                                     [iname.can_phase_ice_difficult.value, iname.melee.value, iname.roll.value]])
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
            ID2Data(ID2Type.region),
        rname.pepperpain_prairie:
            ID2Data(ID2Type.region),
        rname.lonely_road_c_entrance:
            ID2Data(ID2Type.region),
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
            ID2Data(ID2Type.region),
        rname.slippery_slope:
            ID2Data(ID2Type.region),
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
            ID2Data(ID2Type.region),
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
            ID2Data(ID2Type.region),
    },

    # Caves
    # Fluffy Fields Caves
    rname.ffc_a: {
        rname.autumn_climb:
            ID2Data(ID2Type.region, [[iname.basic_combat.value],
                                     [iname.can_phase_itemless.value]]),
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
                                       [iname.can_phase_ice.value],
                                       [iname.can_phase_dynamite.value]]),
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
            ID2Data(ID2Type.location, [[iname.can_open_chests.value]]),
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
            ID2Data(ID2Type.location, [[iname.can_open_chests.value]])
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
            ID2Data(ID2Type.location, [[iname.weapon_any.value]])
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
            ID2Data(ID2Type.location, [[iname.can_open_chests.value]]),
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
            ID2Data(ID2Type.region),
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
                                     [iname.can_phase_itemless.value]])
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
            ID2Data(ID2Type.region),
        rname.frozen_court:
            ID2Data(ID2Type.region)
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
                                       [iname.can_phase_ice.value]
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
            ID2Data(ID2Type.location, [[iname.can_open_chests.value]])
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
            ID2Data(ID2Type.region),
        rname.pepperpain_prairie:
            ID2Data(ID2Type.region)
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
                                       [iname.can_phase_ice.value, iname.roll.value],
                                       [iname.can_phase_dynamite.value, iname.roll.value]])
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
                                       [iname.can_phase_itemless.value, iname.can_open_chests.value]]),
        rname.fcc_p:
            ID2Data(ID2Type.region, [[iname.force_jump.value],
                                     [iname.can_phase_itemless.value, iname.weapon_no_force.value]])
    },
    rname.fcc_j: {
        lname.fcc_crystal_path:
            ID2Data(ID2Type.location, [[iname.weapon_any.value],
                                       [iname.can_phase_itemless.value, iname.can_open_chests.value]])
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
            ID2Data(ID2Type.region),
        rname.d1_a:
            ID2Data(ID2Type.region, [[iname.weapon_any.value],
                                     [iname.can_phase_itemless.value]])
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
            ID2Data(ID2Type.region, [[iname.can_use_d1_keys.value]]),
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
            ID2Data(ID2Type.region, [[iname.can_use_d1_keys.value]]),
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
            ID2Data(ID2Type.region, [[iname.can_use_d1_keys.value]]),
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
            ID2Data(ID2Type.region, [[iname.can_use_d2_keys.value]])
    },
    rname.d2_f: {
        rname.d2_b:
            ID2Data(ID2Type.region, [[iname.force.value],
                                     [iname.can_phase_ice.value, iname.roll.value],
                                     [iname.can_phase_dynamite.value, iname.roll.value]]),
        rname.d2_g:
            ID2Data(ID2Type.region)
    },
    rname.d2_g: {
        lname.d2_crayon:
            ID2Data(ID2Type.location, [[iname.force.value],
                                       [iname.melee.value, iname.chain.value],
                                       [iname.dynamite.value],
                                       [iname.fire_mace.value],
                                       [iname.can_phase_ice.value],
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
                                     [iname.can_phase_ice.value],
                                     [iname.can_phase_enemy.value]]),
        rname.d2_k:
            ID2Data(ID2Type.region, [[iname.can_use_d2_keys.value]])
    },
    rname.d2_i: {
        lname.d2_orbiting_balls:
            ID2Data(ID2Type.location, [[iname.melee.value, iname.roll.value]]),
        rname.d2_e:
            ID2Data(ID2Type.region, [[iname.can_use_d2_keys.value, iname.melee.value, iname.roll.value],
                                     [iname.can_phase_itemless.value, iname.roll.value],
                                     [iname.can_phase_itemless_difficult.value],
                                     [iname.can_phase_dynamite.value]]),
        rname.d2_g:
            ID2Data(ID2Type.region)
    },
    rname.d2_j: {
        lname.d2_treasure:
            ID2Data(ID2Type.location, [[iname.can_open_chests.value]], iname.victory),
        rname.d2_h:
            ID2Data(ID2Type.region, [[iname.force.value],
                                     [iname.can_phase_ice.value, iname.roll.value],
                                     [iname.can_phase_dynamite.value]])
    },
    rname.d2_k: {
        rname.d2_h:
            ID2Data(ID2Type.region, [[iname.can_use_d2_keys.value]]),
        rname.d2_j:
            ID2Data(ID2Type.region, [[iname.basic_combat.value]])
    },

    # Portal Worlds
    rname.autumn_climb: {
        lname.autumn_climb:
            ID2Data(ID2Type.location, [[iname.can_open_chests.value]]),
        rname.ffc_a:
            ID2Data(ID2Type.region),
    }

}
