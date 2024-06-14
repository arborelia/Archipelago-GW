from dataclasses import dataclass
from typing import Dict, Any
from Options import (DefaultOnToggle, Toggle, StartInventoryPool, Choice, Range, TextChoice, PlandoConnections,
                     PerGameCommonOptions, OptionGroup)
      
class Goal(Choice):
    """
    Select the goal you need to reach to win.
    Raft Quest: Collect eight Raft Pieces and escape the island.
    Queen of Adventure: Collect eight Raft Pieces, defeat Simulacrum, and escape the island.
    Queen of Dreams: Complete Quietus and defeat the Dream Moth. This is a short goal.
    """
    internal_name = "goal"
    display_name = "Goal"
    option_raft_quest = 0
    option_queen_of_adventure = 1
    option_queen_of_dreams = 2
    default = 0

class ProgressiveItems(Toggle):
    """
    If on, there are three Force Wands, Dynamites, and Ice Rings in the pool (vanilla behavior).
    If off, there are only one of each, and there are two upgrades available of each which will only
    apply once you've obtained the base item. This makes it harder to get these items.
    """
    internal_name = "progressive_items"
    display_name = "Progressive Items"

class IncludeCaves(Toggle):
    """
    Randomizes any chests in caves and houses. Does not include Portal Worlds.
    """
    internal_name = "include_caves"
    display_name = "Include Caves"

class IncludePortalWorlds(Toggle):
    """
    Randomizes any chests in Portal Worlds.
    """
    internal_name = "include_portal_worlds"
    display_name = "Include Portal Worlds"

class IncludeSecretDungeons(Toggle):
    """
    Randomizes any chests in the three shard dungeons and Tomb of Simulacrum.
    """
    internal_name = "include_secret_dungeons"
    display_name = "Include Secret Dungeons"

class IncludeDreamDungeons(Toggle):
    """
    Randomizes any chests in the five Dreamworld dungeons.
    """
    internal_name = "include_dream_dungeons"
    display_name = "Include Dream Dungeons"

class IncludeSuperSecrets(Toggle):
    """
    Randomizes a secret item in the Dreamworld and a secret with NAAQ BLX.
    If you know, you know. If you don't, leave this off.
    (This option removes the need to be as healthy or waste your time.)
    """
    internal_name = "include_super_secrets"
    display_name = "Include Super Secrets"

class OpenD8(Toggle):
    """
    Opens the entrance to Grand Library, removing the need to collect seven raft pieces.
    """
    internal_name = "open_d8"
    display_name = "Open Grand Library"

class OpenS4(Toggle):
    """
    Opens the entrance to Tomb of Simulacrum and removes the Forbidden Keys from the pool.
    """
    internal_name = "open_s4"
    display_name = "Open Tomb of Simulacrum"

class OpenDreamworld(Toggle):
    """
    Opens the entrance to Dreamworld and the five dungeons within.
    This removes the need for a raft piece to enter Dreamworld and items to enter dungeons.
    """
    internal_name = "open_dreamworld"
    display_name = "Open Dreamworld"

class DreamDungeonsDoNotChangeItems(Toggle):
    """
    Dreamworld dungeons no longer restrict your items, but will also not give you the items
    expected to beat them.
    """
    internal_name = "dream_dungeons_do_not_change_items"
    display_name = "Dream Dungeons Do Not Change Items"

class KeySettings(Choice):
    """
    Default: Keys are individual items. You are logically expected to have every key for a dungeon to open a locked door
    Keyrings: All keys are removed and keyrings for each dungeon are placed in the pool instead, granting
    all the keys you need at once
    Keysey: All keys and locks are removed
    """
    # Eventually add legacy key setting to make a unique key for each lock
    internal_name = "key_settings"
    display_name = "Key_Settings"
    option_default = 0
    option_keyrings = 1
    option_keysey = 2
    default = 0

class RandomizeStick(Toggle):
    """
    Start without Ittle's stick and places an additional Progressive Melee into the pool. You will be unable to attack
    or open chests, so this severely limits your initial available locations.
    """
    internal_name = "randomize_stick"
    display_name = "Start Without Stick"

class RandomizeRoll(Toggle):
    """
    Start without the ability to roll and places a Roll item into the pool.
    """
    internal_name = "randomize_roll"
    display_name = "Start Without Roll"

class RollOpensChests(Toggle):
    """
    Rolling can be used to open chests. Can be used to make Start Without Stick more viable.
    """
    internal_name = "roll_opens_chests"
    display_name = "Roll Opens Chests"

class StartWithTracker(Toggle):
    """
    Start with Tracker 3 (and removes all Progressive Trackers from the pool),
    allowing you to know where all locations in dungeons are.
    """
    internal_name = "start_with_tracker"
    display_name = "Start Without Roll"

class StartWithAllWarps(Toggle):
    """
    Start with all the warps in the Warp Garden unlocked for convenience
    """
    internal_name = "start_with_all_warps"
    display_name = "Start With All Warps Unlocked"

@dataclass
class ID2Options(PerGameCommonOptions):
    start_inventory_from_pool: StartInventoryPool
    goal: Goal
    progressive_items: ProgressiveItems
    include_caves: IncludeCaves
    include_portal_worlds: IncludePortalWorlds
    include_secret_dungeons: IncludeSecretDungeons
    include_dream_dungeons: IncludeDreamDungeons
    include_super_secrets: IncludeSuperSecrets
    open_d8: OpenD8
    open_s4: OpenS4
    open_dreamworld: OpenDreamworld
    dream_dungeons_do_not_change_items: DreamDungeonsDoNotChangeItems
    key_settings: KeySettings
    randomize_stick: RandomizeStick
    randomize_roll: RandomizeRoll
    roll_opens_chests: RollOpensChests
    start_with_tracker: StartWithTracker
    start_with_all_warps: StartWithAllWarps

# TODO add prsets and option groups
