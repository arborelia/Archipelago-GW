from random import Random
from typing import Dict, TYPE_CHECKING

from worlds.generic.Rules import set_rule, forbid_item
from BaseClasses import CollectionState
from .options import ID2Options
if TYPE_CHECKING:
    from . import ID2World

stick = "Stick"
sword = "Fire Sword"
mace = "Fire Mace"
melee = "Progressive Melee"
wand = "Progressive Force Wand"
dynamite = "Progressive Dynamite"
ice = "Progressive Ice Ring"
raft = "Raft Piece"

def has_stick(state: CollectionState, player: int) -> bool:
    return state.has("Progressive Melee", player, 1)

def has_fire_sword(state: CollectionState, player: int) -> bool:
    return state.has("Progressive Melee", player, 2)

def has_fire_mace(state: CollectionState, player: int) -> bool:
    return state.has("Progressive Melee", player, 3)

def can_open_chests(state: CollectionState, player: int, options: ID2Options) -> bool:
    can_roll_chests = False
    if options.roll_opens_chests:
        can_roll_chests = state.has("Roll", player)
    return state.has_group("Weapons", player) or can_roll_chests

def can_kill_basic_enemies(state: CollectionState, player: int) -> bool:
    return state.has_group("Weapons", player)

def can_phase_itemless(options: ID2Options) -> bool:
    return options.phasing_itemless

def can_phase_itemless_difficult(options: ID2Options) -> bool:
    return options.phasing_itemless and options.phasing_difficult

# For ice clips that use pre-existing ice blocks
def can_phase_ice_itemless(options: ID2Options) -> bool:
    return options.phasing_ice

def can_phase_ice_itemless_difficult(options: ID2Options) -> bool:
    return options.phasing_ice and options.phasing_difficult

def can_phase_ice(state: CollectionState, player: int, options: ID2Options) -> bool:
    return state.has(ice, player, 1) and options.phasing_ice

def can_phase_ice_difficult(state: CollectionState, player: int, options: ID2Options) -> bool:
    return state.has(ice, player, 1) and options.phasing_ice and options.phasing_difficult

def can_phase_dynamite(state: CollectionState, player: int, options: ID2Options) -> bool:
    return state.has(ice, player, 1) and state.has(dynamite, player, 1) and options.phasing_dynamite

def can_phase_dynamite_difficult(state: CollectionState, player: int, options: ID2Options) -> bool:
    return state.has(ice, player, 1) and state.has(dynamite, player, 1) and options.phasing_dynamite \
    and options.phasing_dynamite

def can_phase_enemy(options: ID2Options) -> bool:
    return options.phasing_enemies

def can_phase_enemy_difficult(options: ID2Options) -> bool:
    return options.phasing_enemies and options.phasing_difficult