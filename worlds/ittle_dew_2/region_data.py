from typing import Dict, List, NamedTuple, Optional, Union
from enum import IntEnum
from .names_regions import RegionNames as rname
from .names_locations import LocationNames as lname
from .names_items import ItemNames as iname

class ID2Type(IntEnum):
    location = 1
    region = 2

class ID2Data(NamedTuple):
    type: ID2Type # Either Location or Region
    rules: List[List[str]] = [[]] # List of rules for access requirements
    # for rules to be satisfied, you need to have at least one set of the rules items
    grant_event: Optional[str] = None # grants the specified event item when the location is collected

# First Union is the source region
# Second Union is the destination region or location
# The ID2Data is a list of requirements
traversal_requirements: Dict[rname, Dict[Union[lname, rname], ID2Data]] = {
    # Currently vanilla start will be the only available starting location
    # For now MVP is going to move starting logical location to be Sweetwater Coast
    rname.menu: {
        # rname.fluffy_fields: 
            # ID2Data(ID2Type.region),
        rname.sweetwater_coast:
            ID2Data(ID2Type.region),
        # dummy locations
        # lname.ffc_artist_backroom:
        #     ID2Data(ID2Type.location),
        # lname.ffc_double_spikebun_combat:
        #     ID2Data(ID2Type.location),
        # lname.ffc_goldbun_combat:
        #     ID2Data(ID2Type.location),
        # lname.ffc_hermit_hint:
        #     ID2Data(ID2Type.location),
        # lname.ffc_ice_blockade:
        #     ID2Data(ID2Type.location),
        # lname.ffc_jenny_berry_house:
        #     ID2Data(ID2Type.location),
        # lname.ffc_potion_bar:
        #     ID2Data(ID2Type.location),
        # lname.d1_boss_reward:
        #     ID2Data(ID2Type.location),
        # lname.d1_crayon:
        #     ID2Data(ID2Type.location),
        # lname.d1_safety_jenny_gate:
        #     ID2Data(ID2Type.location),
        # lname.d1_shellbun_nest:
        #     ID2Data(ID2Type.location),
    },
    # Overworld regions
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
            ID2Data(ID2Type.region, [[iname.can_break_strong_objects]]),
        rname.scc_c:
            ID2Data(ID2Type.region),
        rname.scc_f:
            # transitional cave, gives access to d and e
            ID2Data(ID2Type.region, [[iname.can_break_weak_objects],
                                     [iname.can_phase_dynamite],
                                     [iname.can_phase_ice, iname.roll],
                                     [iname.can_phase_enemy_difficult, iname.roll]]),
        rname.scc_g:
            ID2Data(ID2Type.region, [[iname.can_break_strong_objects]]),
        rname.scc_h:
            ID2Data(ID2Type.region),
        rname.scc_i:
            ID2Data(ID2Type.region),
        rname.scc_j:
            ID2Data(ID2Type.region, [[iname.roll]]),
        rname.scc_k:
            ID2Data(ID2Type.region),
        rname.scc_l:
            ID2Data(ID2Type.region, [[iname.can_break_weak_objects]]),
        rname.scc_m:
            ID2Data(ID2Type.region),
        rname.scc_n:
            ID2Data(ID2Type.region),
        rname.scc_o:
            ID2Data(ID2Type.region, [[iname.can_break_weak_objects]]),
        rname.scc_p:
            ID2Data(ID2Type.region),
        rname.scc_q:
            ID2Data(ID2Type.region),
        rname.d2_g:
            ID2Data(ID2Type.region)
    },

    # Caves
    # Sweetwater Caves
    rname.scc_a: {
        # rock performance
    },
    rname.scc_b: {
        lname.scc_white_gates_combat:
            ID2Data(ID2Type.location, [[iname.can_kill_basic_enemies]])
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
        rname.scc_d:
            ID2Data(ID2Type.region),
        rname.scc_e:
            ID2Data(ID2Type.region, [[iname.can_break_weak_objects]]),
    },
    rname.scc_g: {
        lname.scc_feral_gates_combat:
            ID2Data(ID2Type.location, [[iname.can_open_chests]])
    },
    rname.scc_h: {
        lname.scc_three_teleporters:
            ID2Data(ID2Type.location, [[iname.can_open_chests]])
    },
    rname.scc_i: {
        lname.scc_four_candy_snakes_combat:
            ID2Data(ID2Type.location, [[iname.can_kill_basic_enemies]])
    },
    rname.scc_j: {
        lname.scc_portal_spikes_chest:
            ID2Data(ID2Type.location, [[iname.can_break_weak_objects]])
    },
    rname.scc_k: {
        lname.scc_hint_hermit:
            ID2Data(ID2Type.location, [[iname.can_open_chests]])
    },
    rname.scc_l: {
        lname.scc_fake_chest_cave:
            ID2Data(ID2Type.location, [[iname.melee],
                                       [iname.force],
                                       [iname.ice]])
    },
    rname.scc_m: {
        lname.scc_wooden_balls_spike_floor:
            ID2Data(ID2Type.location, [[iname.can_open_chests]])
    },
    rname.scc_n: {
        lname.scc_kung_fu_jenny:
            ID2Data(ID2Type.location, [[iname.can_open_chests]])
    },
    rname.scc_o: {
        rname.painful_plain:
            ID2Data(ID2Type.region, [[iname.can_break_weak_objects]])
    },
    rname.scc_p: {
        # Transition cave to Fancy
    },
    rname.scc_q: {
        # Changing Tent
    },

    # Dungeons
    # Sand Castle
    rname.d2_a: {
        lname.d2_boss_reward:
            ID2Data(ID2Type.location, [[iname.can_kill_basic_enemies, iname.roll]]),#, iname.victory),
        rname.d2_b:
            ID2Data(ID2Type.region, [[iname.can_kill_basic_enemies, iname.roll]])
    },
    rname.d2_b: {
        rname.d2_a:
            ID2Data(ID2Type.region),
        rname.d2_f:
            ID2Data(ID2Type.region)
    },
    rname.d2_c: {
        rname.d2_d:
            ID2Data(ID2Type.region, [[iname.can_break_weak_objects]]),
        rname.d2_h:
            ID2Data(ID2Type.region, [[iname.can_break_weak_objects]])
    },
    rname.d2_d: {
        lname.d2_spikebun_dunes:
            ID2Data(ID2Type.location, [[iname.can_break_weak_objects]]),
        rname.d2_c:
            ID2Data(ID2Type.region, [[iname.can_break_weak_objects]]),
        rname.d2_h:
            ID2Data(ID2Type.region)
    },
    rname.d2_e: {
        rname.d2_f:
            ID2Data(ID2Type.region, [[iname.can_kill_basic_enemies]]),
        rname.d2_i:
            ID2Data(ID2Type.region, [[iname.can_use_d2_keys]])
    },
    rname.d2_f: {
        rname.d2_b:
            ID2Data(ID2Type.region, [[iname.force],
                                     [iname.can_phase_ice, iname.roll],
                                     [iname.can_phase_dynamite, iname.roll]]),
        rname.d2_g:
            ID2Data(ID2Type.region)
    },
    rname.d2_g: {
        lname.d2_crayon:
            ID2Data(ID2Type.location, [[iname.force],
                                       [iname.melee, iname.chain],
                                       [iname.dynamite],
                                       [iname.fire_mace],
                                       [iname.can_phase_ice],
                                       [iname.can_open_chests, iname.can_phase_enemy]]),
        rname.d2_h:
            ID2Data(ID2Type.region),
        rname.d2_i:
            ID2Data(ID2Type.region),
        rname.d2_f:
            ID2Data(ID2Type.region, [[iname.fire_sword]]),
        rname.sweetwater_coast:
            ID2Data(ID2Type.region)
    },
    rname.d2_h: {
        rname.d2_c:
            ID2Data(ID2Type.region, [[iname.can_break_weak_objects]]),
        rname.d2_d:
            ID2Data(ID2Type.region),
        rname.d2_g:
            ID2Data(ID2Type.region),
        rname.d2_j:
            ID2Data(ID2Type.region, [[iname.dynamite],
                                     [iname.can_phase_ice],
                                     [iname.can_phase_enemy]]),
        rname.d2_k:
            ID2Data(ID2Type.region, [[iname.can_use_d2_keys]])
    },
    rname.d2_i: {
        lname.d2_orbiting_balls:
            ID2Data(ID2Type.location, [[iname.melee, iname.roll]]),
        rname.d2_e:
            ID2Data(ID2Type.region, [[iname.can_use_d2_keys, iname.melee, iname.roll]]),
        rname.d2_g:
            ID2Data(ID2Type.region)
    },
    rname.d2_j: {
        lname.d2_treasure:
            ID2Data(ID2Type.location, [[iname.can_open_chests]]),
        rname.d2_h:
            ID2Data(ID2Type.region, [[iname.force],
                                     [iname.can_phase_ice, iname.roll],
                                     [iname.can_phase_dynamite]])
    },
    rname.d2_k: {
        rname.d2_h:
            ID2Data(ID2Type.region, [[iname.can_use_d2_keys]]),
        rname.d2_j:
            ID2Data(ID2Type.region, [[iname.can_kill_basic_enemies]])
    }
}