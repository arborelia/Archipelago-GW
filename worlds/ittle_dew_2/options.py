from dataclasses import dataclass
from typing import Dict, Any
from Options import (DefaultOnToggle, Toggle, StartInventoryPool, Choice, Range,
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


class DungeonRewardsSetting(Choice):
    """
    Select what will be at the reward location in dungeons. In Dreamworld dungeons, the middle card is the reward.
    This can produce more dungeon-heavy seeds, as the randomizer generally tries to avoid putting items deep in dungeons.
    Anything: The reward can be anything
    Priority: The reward can have any item marked progression in the multiworld
    Rewards: The reward can be either a Raft Piece or a Forbidden Key (if Open Tomb of Simulacrum is off).
    FORBIDDEN KEYS ARE CURRENTLY NOT IN THE POOL.
    If there are more dungeon rewards locations in the pool than available reward items, the rest will be priority locations.
    Tomb of Simulacrum can never have its reward set with this. If you want to require Tomb, use the Queen of Adventure goal.
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
    range_end = 8
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
    CURRENTLY NOT SUPPORTED.
    """
    internal_name = "include_secret_dungeons"
    display_name = "Include Secret Dungeons"


class IncludeDreamDungeons(Toggle):
    """
    Randomizes any chests and cards in the five Dreamworld dungeons.
    CURRENTLY NOT SUPPORTED.
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


class OpenD8(Toggle):
    """
    Opens the entrance to Grand Library, removing the need to collect seven Raft Pieces.
    """
    internal_name = "open_d8"
    display_name = "Open Grand Library"


class OpenS4(Toggle):
    """
    Opens the entrance to Tomb of Simulacrum and removes the Forbidden Keys from the pool.
    CURRENTLY NOT SUPPORTED. FORBIDDEN KEYS ARE NOT IN THE POOL.
    """
    internal_name = "open_s4"
    display_name = "Open Tomb of Simulacrum"


class OpenDreamworld(Toggle):
    """
    Opens the entrance to Dreamworld and the five dungeons within.
    This removes the need for a Raft Piece to enter Dreamworld and items to enter dungeons.
    CURRENTLY NOT SUPPORTED. Cards are still in the pool.
    """
    internal_name = "open_dreamworld"
    display_name = "Open Dreamworld"


class DreamDungeonsDoNotChangeItems(Toggle):
    """
    Dreamworld dungeons no longer restrict your items, but will also not give you the items expected to beat them.
    CURRENTLY NOT SUPPORTED.
    """
    internal_name = "dream_dungeons_do_not_change_items"
    display_name = "Dream Dungeons Do Not Change Items"


class KeySettings(Choice):
    """
    How should dungeon keys be treated by the randomizer? Forbidden Keys are not affected by this setting.
    Default: Keys are individual items. You are logically expected to have every key for a dungeon to open a locked door
    Keyrings: All keys are removed and keyrings for each dungeon are placed in the pool instead,
    granting all the keys you need at once
    Keysey: All keys and locks are removed
    """
    # Eventually add legacy key setting to make a unique key for each lock
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
    CURRENTLY NOT SUPPORTED. Shards are not in the pool.
    """
    # Eventually add settings to make these individually customizable and random
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
    Secret Shards will give you Portal or Cave Scrolls instead.
    CURRENTLY NOT SUPPORTED. Shards are not in the pool.
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


class PhasingItemless(Toggle):
    """
    ID2 has a glitch called "Phasing" which allows you to clip over gaps and through objects.
    There are different types of phases.
    This allows the use of "itemless" phases in logic, primarily useful for crossing gaps.
    ALL PHASING EXPECTS A CONTROLLER.
    """
    internal_name = "phasing_itemless"
    display_name = "Allow Itemless Phases"


class PhasingIce(Toggle):
    """
    This allows the use of Ice Block phases in logic, which can be used to clip through walls,
    as long as you can place an ice block on the opposite side of the wall you want to clip through
    (or one already exists).
    ALL PHASING EXPECTS A CONTROLLER.
    """
    internal_name = "phasing_ice"
    display_name = "Allow Ice Block Phases"


class PhasingDynamite(Toggle):
    """
    This allows the use of Dynamite Ice Block phases in logic,
    allowing you to clip through nearly any wall and obstacle.
    ALL PHASING EXPECTS A CONTROLLER.
    """
    internal_name = "phasing_dynamite"
    display_name = "Allow Dynamite+Ice Block Phases"


class PhasingEnemies(Toggle):
    """
    This allows the use of Enemy phases in logic, which can be used to clip through walls wherever there is an enemy.
    ALL PHASING EXPECTS A CONTROLLER.
    """
    internal_name = "phasing_enemy"
    display_name = "Allow Enemy Phases"


class PhasingDifficult(Toggle):
    """
    This allows very difficult and precise phases to be in logic, depending on your other phasing settings.
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
    default = 4


class CrayonsInPool(Range):
    """
    Number of crayons to place in the pool.
    """
    internal_name = "crayons_in_pool"
    display_name = "Crayons In Pool"
    range_start = 0
    range_end = 20
    default = 20


@dataclass
class ID2Options(PerGameCommonOptions):
    start_inventory_from_pool: StartInventoryPool
    goal: Goal
    dungeon_rewards_setting: DungeonRewardsSetting
    dungeon_rewards_count: DungeonRewardsCount
    progressive_items: ProgressiveItems
    include_portal_worlds: IncludePortalWorlds
    include_secret_dungeons: IncludeSecretDungeons
    include_dream_dungeons: IncludeDreamDungeons
    include_super_secrets: IncludeSuperSecrets
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
    phasing_itemless: PhasingItemless
    phasing_ice: PhasingIce
    phasing_dynamite: PhasingDynamite
    phasing_enemies: PhasingEnemies
    phasing_difficult: PhasingDifficult
    start_with_tracker: StartWithTracker
    start_with_all_warps: StartWithAllWarps
    lockpicks_in_pool: LockpicksInPool
    crayons_in_pool: CrayonsInPool


id2_options_groups = [
    OptionGroup("Pool Options", [
        IncludePortalWorlds,
        IncludeSecretDungeons,
        IncludeDreamDungeons,
        IncludeSuperSecrets
    ]),
    OptionGroup("Phasing Options", [
        MajorDungeonSkips,
        PhasingItemless,
        PhasingIce,
        PhasingDynamite,
        PhasingEnemies,
        PhasingDifficult
    ])
]

id2_options_presets: Dict[str, Dict[str, Any]] = {
    "Pro": {
        "phasing_itemless": True,
        "phasing_ice": True,
        "phasing_dynamite": True,
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
        "phasing_itemless": True,
        "phasing_ice": True,
        "phasing_dynamite": True,
        "phasing_enemies": True
    }
}
