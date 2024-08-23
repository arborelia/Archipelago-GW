from dataclasses import dataclass
from typing import Dict, Any
from Options import (DefaultOnToggle, Toggle, StartInventoryPool, Choice, Range,
                     PerGameCommonOptions, OptionGroup)


class Goal(Choice):
    """
    Select the goal you need to reach to win.
    Raft Quest: Collect eight Raft Pieces and escape the island.
    Queen of Adventure: Collect eight Raft Pieces, defeat Simulacrum and get the Big Ol' Bag Of Loot, and escape the island.
    Queen of Dreams: Complete all five Dreamworld dungeons, which will let you escape the island, then do so.
    In Queen of Dreams, only one Raft Piece is in the pool, Grand Library is forced open, and you cannot set Dungeon Rewards Setting.
    Potion Hunt: Collect a specified number of potions, which will allow you to escape the island.
    In Potion Hunt, only the number of Raft Pieces you need to get all randomized checks will be in the pool.
    """
    internal_name = "goal"
    display_name = "Goal"
    option_raft_quest = 0
    option_queen_of_adventure = 1
    option_queen_of_dreams = 2
    option_potion_hunt = 3
    default = 0


class RequiredPotionCount(Range):
    """
    (Potion Hunt goal only) How many potions are required to get off the island?
    Recommended to use keysey/keyrings and reduced shard settings to have room in the pool.
    """
    internal_name = "required_potion_count"
    display_name = "Required Number of Potions (Potion Hunt)"
    range_start = 1
    range_end = 20
    default = 10


class ExtraPotions(Range):
    """
    (Potion Hunt goal only) How many extra potions should be in the pool?
    Recommended to use keysey/keyrings and reduced shard settings to have room in the pool.
    """
    internal_name = "extra_potions"
    display_name = "Extra Potions (Potion Hunt)"
    range_start = 0
    range_end = 20
    default = 5


class DungeonRewardsSetting(Choice):
    """
    Select what will be at the reward location in dungeons. In Dreamworld dungeons, the middle card is the reward.
    This can produce more dungeon-heavy seeds, as the randomizer generally tries to avoid putting items deep in dungeons.
    Anything: The reward can be anything
    Priority: The reward can have any item marked progression in the multiworld
    Rewards: The reward can be either a Raft Piece or a Forbidden Key (if Open Tomb of Simulacrum is off).
    If there are more dungeon rewards locations in the pool than available reward items, the rest will be priority locations.
    Tomb of Simulacrum can never have its reward set with this. If you want to require Tomb, use the Queen of Adventure goal.
    Quietus will also never be required.
    Incompatible with Queen of Dreams Goal (this setting will be ignored if that goal is set)
    If the goal is Potion Hunt and this is set to Rewards, dungeon rewards will be set to potions before they start being
    filled with Raft Pieces and Forbidden Keys.
    """
    internal_name = "dungeon_rewards_setting"
    display_name = "Dungeon Rewards Setting"
    option_anything = 0
    option_priority = 1
    option_rewards = 2
    default = 0


class DungeonRewardsCount(Range):
    """
    How many dungeons should have their rewards set as per the Dungeon Rewards Setting?
    Note that this will only set the reward locations for dungeons that are randomized in the pool,
    so if you set this higher than the number of randomized dungeons, it will be the number of dungeons instead.
    """
    internal_name = "dungeon_rewards_count"
    displayname = "Dungeon Rewards Count"
    range_start = 0
    range_end = 15
    default = 4


class ProgressiveItems(DefaultOnToggle):
    """
    If on, there are three Force Wands, Dynamites, Ice Rings, and Chains in the pool (vanilla behavior).
    If off, there are only one of each, and there are two upgrades available of each which will only apply
    once you've obtained the base item.
    This makes it harder to get these items.
    """
    internal_name = "progressive_items"
    display_name = "Progressive Items"


class IncludePortalWorlds(Toggle):
    """
    Randomizes any chests in Portal Worlds. Excludes the Super Secret Portal Worlds.
    """
    internal_name = "include_portal_worlds"
    display_name = "Include Portal Worlds"


class IncludeSecretDungeons(Toggle):
    """
    Randomizes any chests in the three shard dungeons and Tomb of Simulacrum.
    Even if this is off, Tomb of Simulacrum will be included if Queen of Adventure is the goal
    """
    internal_name = "include_secret_dungeons"
    display_name = "Include Secret Dungeons"


class IncludeDreamDungeons(Toggle):
    """
    Randomizes any chests and cards in the five Dreamworld dungeons.
    This will automatically be turned on if the goal is Queen of Dreams.
    """
    internal_name = "include_dream_dungeons"
    display_name = "Include Dream Dungeons"


class IncludeSuperSecrets(Toggle):
    """
    Randomizes a secret item in the Dreamworld, LUDDC, and a secret with NAAQ BLX.
    If you know, you know. If you don't, leave this off.
    (This option removes the need to be as healthy or waste your time.)
    """
    internal_name = "include_super_secrets"
    display_name = "Include Super Secrets"


class IncludeSecretSigns(Toggle):
    """
    The four incomplete signs and the eight metal signs in the eight main dungeons give you an item when they're read.
    The number and letter signs are included if Super Secrets are on.
    """
    internal_name = "include_secret_signs"
    display_name = "Include Secret Signs"


class BlockRegionConnections(Toggle):
    """
    Adds 14 area connection items which are required to travel between areas. For example, you need the
    "Connection - Fluffy Fields To Sweetwater Coast" to be able to enter Sweetwater Coast from Fluffy Fields.
    Connections are two-way, so that also allows you to enter Fluffy Fields from Sweetwater Coast.
    """
    internal_name = "block_region_connections"
    display_name = "Region Connection Blockades"


class OpenD8(Toggle):
    """
    Opens the entrance to Grand Library, removing the need to collect seven Raft Pieces.
    This setting is forced on if you have the Queen of Dreams goal.
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
    Opens the entrance the first four Dreamworld dungeons.
    This does not remove the need for a Raft Piece,
    but it does make it so you do not need items to enter the dungeons themselves.
    """
    internal_name = "open_dreamworld"
    display_name = "Open Dreamworld Dungeons"


class DreamDungeonsDoNotChangeItems(Toggle):
    """
    Dreamworld dungeons no longer restrict your items, but will also not give you the items expected to beat them.
    """
    internal_name = "dream_dungeons_do_not_change_items"
    display_name = "Dream Dungeons Do Not Change Items"


class KeySettings(Choice):
    """
    How should dungeon keys be treated by the randomizer? Forbidden Keys are not affected by this setting.
    Keys for dungeons not randomized will not be included.
    Default: Keys are individual items.
    Keyrings: All keys are removed and keyrings for each dungeon are placed in the pool instead,
    granting all the keys you need at once
    Keysey: All keys and locks are removed
    """
    internal_name = "key_settings"
    display_name = "Key_Settings"
    option_default = 0
    option_keyrings = 1
    option_keysey = 2
    default = 0


class ShardSettings(Choice):
    """
    Open: Secret Shards are not required to access any of the secret dungeons.
    Shards are removed from the pool and Extra Shards is ignored.
    Half: Sunken Labyrinth needs 4 Shards to enter, Machine Fortress needs 8, and Dark Hypostyle needs 12.
    Vanilla: Secret dungeons require their normal amount of shards to enter.
    Lockdown: Sunken Labyrinth needs 12 Shards to enter, Machine Fortress needs 24, and Dark Hypostyle needs 36.
    If Include Secret Dungeons is off, shards will not be in the pool.
    """
    # TODO Eventually add settings to make these individually customizable and random
    internal_name = "shard_settings"
    display_name = "Secret Shard Requirements"
    option_open = 0
    option_half = 1
    option_vanilla = 2
    option_lockdown = 3
    default = 2


class ExtraShards(Range):
    """
    Adds extra Secret Shards to the pool. Once you have obtained enough to open Dark Hypostyle,
    Secret Shards will give you a random heart instead.
    If Include Secret Dungeons is off, shards will not be in the pool.
    """
    internal_name = "extra_shards"
    display_name = "Extra Shards"
    range_start = 0
    range_end = 36
    default = 12


class RandomizeStick(Toggle):
    """
    Start without Ittle's stick and places an additional Progressive Melee into the pool.
    You will be unable to attack or open chests, so this severely limits your initial available locations.
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


class MajorDungeonSkips(Toggle):
    """
    Allows the following tricks:
    Early Grand Library
    Grand Library Skip
    Early Tomb of Simulacrum
    Quietus Boss without breaking the crystals
    You can keep this setting off to allow phasing in logic without it being too powerful.
    """
    internal_name = "major_dungeon_skips"
    display_name = "Major Dungeon Skips"


class PhasingSetting(Choice):
    """
    ID2 has a glitch called "Phasing" which allows you to clip over gaps and through objects.
    There are different types of phases, and this setting allows them being required in logic.
    Gap Phases: Allows phasing over pits and through loading zones (phasing through door transitions requires rolling).
    Object Phases: Allows phasing through collision to objects, including Ice Ring blocks. Also allows Gap Phases.
    Ice Dynamite Clips: Allows clipping through walls using Ice and Dynamite Clips. Also allows Gap and Object Phases.
    ALL PHASING EXPECTS A CONTROLLER.
    """
    internal_name = "phasing_setting"
    display_name = "Allow Phasing"
    option_off = 0
    option_gap_phases = 1
    option_object_phases = 2
    option_ice_dynamite_clips = 3
    default = 0


class PhasingEnemies(Toggle):
    """
    This allows the use of Enemy phases in logic, which can be used to clip through walls wherever there is an enemy.
    Turning this setting on also enables Object Phasing.
    ALL PHASING EXPECTS A CONTROLLER.
    """
    internal_name = "phasing_enemy"
    display_name = "Allow Enemy Phases"


class PhasingDifficult(Toggle):
    """
    This allows difficult, precise, or annoying phases to be in logic, depending on your other phasing settings.
    For example, you can now be expected to have to phase through room transitions without roll.
    ALL PHASING EXPECTS A CONTROLLER.
    """
    internal_name = "phasing_difficult"
    display_name = "Allow Difficult phases"


class StartWithTracker(Toggle):
    """
    Start with Tracker 3 (and removes all Progressive Trackers from the pool),
    allowing you to know where all locations in dungeons are.
    """
    internal_name = "start_with_tracker"
    display_name = "Start With Tracker 3"


class StartWithAllWarps(DefaultOnToggle):
    """
    Start with all the warps in the Warp Garden unlocked for convenience
    """
    internal_name = "start_with_all_warps"
    display_name = "Start With All Warps Unlocked"


class LockpicksInPool(Range):
    """
    Number of lockpicks to place in the pool. Lockpicks are not logically considered.
    """
    internal_name = "lockpicks_in_pool"
    display_name = "Lockpicks In Pool"
    range_start = 0
    range_end = 24
    default = 12


class CrayonsInPool(Range):
    """
    Number of crayons to place in the pool.
    """
    internal_name = "crayons_in_pool"
    display_name = "Crayons In Pool"
    range_start = 0
    range_end = 20
    default = 20


class RemoveCards(Toggle):
    """
    Due to the limited pool size, you can turn this on to remove cards from the item pool if you're having errors
    due to not having enough locations. This will only help if Include Dreamworld Dungeons is on as cards are not
    items in the pool otherwise.
    """
    internal_name = "remove_cards"
    display_name = "Remove Cards From Pool"


class TrapPercentage(Range):
    """
    Percentage of filler items replaced with the following traps:
    Bee Trap
    Random Debuff Trap
    Meteor Shower Trap
    """
    internal_name = "trap_percentage"
    display_name = "Normal Trap Percentage"
    range_start = 0
    range_end = 100
    default = 20


class SuperTrapPercentage(Range):
    """
    Percentage of filler items replaced with the following particularly debilitating traps:
    Bee Onslaught
    Free Range Snowboarding Trap
    """
    internal_name = "super_trap_percentage"
    display_name = "Debilitating Trap Percentage"
    range_start = 0
    range_end = 100
    default = 0


class RandomizePianoPuzzle(Choice):
    """
    Randomizes the Syncope piano puzzle.
    The solution to the puzzle can be found in the room with the three knights.
    Off: The solution will be the vanilla "DEAD"
    Words: The solution will be a real word, 3-7 characters long, consisting of only white keys.
    Black Keys: Same as Words, but some white keys are randomly replaced by black keys.
    Full Random: The solution is a completely random string, 3-7 characters long, including white and black keys.
    """
    internal_name = "randomize_piano_puzzle"
    display_name = "Randomize Piano Puzzle"
    option_off = 0
    option_words = 1
    option_black_keys = 2
    option_full_random = 3
    default = 0


@dataclass
class ID2Options(PerGameCommonOptions):
    start_inventory_from_pool: StartInventoryPool
    goal: Goal
    required_potion_count: RequiredPotionCount
    extra_potions: ExtraPotions
    dungeon_rewards_setting: DungeonRewardsSetting
    dungeon_rewards_count: DungeonRewardsCount
    progressive_items: ProgressiveItems
    include_portal_worlds: IncludePortalWorlds
    include_secret_dungeons: IncludeSecretDungeons
    include_dream_dungeons: IncludeDreamDungeons
    include_super_secrets: IncludeSuperSecrets
    include_secret_signs: IncludeSecretSigns
    block_region_connections: BlockRegionConnections
    open_d8: OpenD8
    open_s4: OpenS4
    open_dreamworld: OpenDreamworld
    dream_dungeons_do_not_change_items: DreamDungeonsDoNotChangeItems
    key_settings: KeySettings
    shard_settings: ShardSettings
    extra_shards: ExtraShards
    randomize_stick: RandomizeStick
    randomize_roll: RandomizeRoll
    roll_opens_chests: RollOpensChests
    major_dungeon_skips: MajorDungeonSkips
    phasing_setting: PhasingSetting
    phasing_enemies: PhasingEnemies
    phasing_difficult: PhasingDifficult
    start_with_tracker: StartWithTracker
    start_with_all_warps: StartWithAllWarps
    lockpicks_in_pool: LockpicksInPool
    crayons_in_pool: CrayonsInPool
    remove_cards: RemoveCards
    trap_percentage: TrapPercentage
    super_trap_percentage: SuperTrapPercentage
    randomize_piano_puzzle: RandomizePianoPuzzle


id2_options_groups = [
    OptionGroup("Pool Options", [
        IncludePortalWorlds,
        IncludeSecretDungeons,
        IncludeDreamDungeons,
        IncludeSuperSecrets,
        IncludeSecretSigns
    ]),
    OptionGroup("Phasing Options", [
        MajorDungeonSkips,
        PhasingSetting,
        PhasingEnemies,
        PhasingDifficult
    ])
]

id2_options_presets: Dict[str, Dict[str, Any]] = {
    "Pro": {
        "phasing_setting": PhasingSetting.option_ice_dynamite_clips,
        "phasing_enemies": True
    },
    "Allsanity": {
        "include_portal_worlds": True,
        "include_secret_dungeons": True,
        "include_dream_dungeons": True,
        "include_super_secrets": True
    },
    "Allsanity Pro": {
        "include_portal_worlds": True,
        "include_secret_dungeons": True,
        "include_dream_dungeons": True,
        "include_super_secrets": True,
        "phasing_setting": PhasingSetting.option_ice_dynamite_clips,
        "phasing_enemies": True
    }
}
