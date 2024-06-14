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
roll = "Roll"
raft = "Raft Piece"

def has_stick(state: CollectionState, player: int) -> bool:
    return state.has("Progressive Melee", player, 1)

def has_fire_sword(state: CollectionState, player: int) -> bool:
    return state.has("Progressive Melee", player, 2)

def has_fire_mace(state: CollectionState, player: int) -> bool:
    return state.has("Progressive Melee", player, 3)
