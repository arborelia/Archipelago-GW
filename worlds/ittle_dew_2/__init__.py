from typing import Dict, List, Any, Union, TextIO
from Options import OptionError
from copy import deepcopy
from BaseClasses import Region, Location, Item, Tutorial, CollectionState, ItemClassification, MultiWorld
from .items import item_name_to_id, item_table, none_item_table, item_name_groups, filler_items
from .locations import location_name_groups, location_name_to_id
from .region_data import traversal_requirements as reqs, ID2Data, ID2Type
from .region_rules import create_regions_with_rules, key_count_requirements
from .options import ID2Options, id2_options_groups, id2_options_presets, KeySettings
from .names_regions import RegionNames as rname
from .names_locations import LocationNames as lname
from .names_items import ItemNames as iname
from worlds.AutoWorld import WebWorld, World
from Utils import visualize_regions


class ID2Web(WebWorld):
    tutorials = [
        Tutorial(
            tutorial_name="Multiworld Setup Guide",
            description="A guide to setting up the Ittle Dew 2 Randomizer for Archipelago multiworld games.",
            language="English",
            file_name="setup_en.md",
            link="setup/en",
            authors=["GameWyrm, ChrisIsAwesome"]  # TODO write a guide
        )
    ]
    theme = "ocean"
    game = "Ittle Dew 2"
    bug_report_page = "https://github.com/Extra-2-Dew/ArchipelagoRandomizer/issues"
    option_groups = id2_options_groups
    options_presets = id2_options_presets


class ID2Item(Item):
    game: str = "Ittle Dew 2"


class ID2Location(Location):
    game: str = "Ittle Dew 2"


class ID2World(World):
    """
    Hunting for adventure, Ittle and her magical sidekick fox Tippsie have crashed on a mysterious island.
    Explore the island and tackle its eight dungeons on a search for Raft Pieces to escape!
    However, dark secrets and ancient dreams reside within. Will Ittle get the adventure she bargained for?
    Or will she succumb to the machinations of the Queen of Adventure?
    """
    game = "Ittle Dew 2"
    web = ID2Web()

    required_dungeons: List[str] = []

    options: ID2Options
    options_dataclass = ID2Options
    item_name_groups = item_name_groups
    location_name_groups = location_name_groups

    item_name_to_id = item_name_to_id
    location_name_to_id = location_name_to_id

    traversal_requirements: Dict[rname, Dict[Union[lname, rname], ID2Data]]

    def generate_early(self) -> None:
        if not self.options.open_dreamworld:
            self.options.open_dreamworld.value = options.OpenDreamworld.option_true

        self.options.shard_settings.value = options.ShardSettings.option_open
        self.options.open_s4.value = options.OpenS4.option_true

        dungeon_count = 8
        if self.options.include_secret_dungeons:
            dungeon_count += 4
        if self.options.include_dream_dungeons:
            dungeon_count += 5
        if self.options.dungeon_rewards_setting.value != options.DungeonRewardsSetting.option_anything and self.options.dungeon_rewards_count.value > dungeon_count:
            print(f"Not enough dungeons available to place dungeon rewards in, clamping down to {dungeon_count} instead")
            self.options.dungeon_rewards_count.value = dungeon_count

        # For Universal Tracker
        if hasattr(self.multiworld, "re_gen_passthrough"):
            if "Ittle Dew 2" in self.multiworld.re_gen_passthrough:
                passthrough = self.multiworld.re_gen_passthrough["Ittle Dew 2"]
                self.options.goal.value = passthrough["goal"]
                self.options.include_portal_worlds.value = passthrough["include_portal_worlds"]
                self.options.include_secret_dungeons.value = passthrough["include_secret_dungeons"]
                self.options.include_dream_dungeons.value = passthrough["include_dream_dungeons"]
                self.options.include_super_secrets.value = passthrough["include_super_secrets"]
                self.options.open_d8.value = passthrough["open_d8"]
                self.options.open_s4.value = passthrough["open_s4"]
                self.options.open_dreamworld = passthrough["open_dreamworld"]
                self.options.dream_dungeons_do_not_change_items.value = \
                    passthrough["dream_dungeons_do_not_change_items"]
                self.options.key_settings.value = passthrough["key_settings"]
                self.options.shard_settings.value = passthrough["shard_settings"]
                self.options.randomize_stick.value = passthrough["randomize_stick"]
                self.options.randomize_roll.value = passthrough["randomize_roll"]
                self.options.roll_opens_chests.value = passthrough["roll_opens_chests"]
                self.options.phasing_itemless.value = passthrough["phasing_itemless"]
                self.options.phasing_ice.value = passthrough["phasing_ice"]
                self.options.phasing_dynamite.value = passthrough["phasing_dynamite"]
                self.options.phasing_enemies.value = passthrough["phasing_enemies"]
                self.options.phasing_difficult.value = passthrough["phasing_difficult"]

    # generate and fill our regions and locations with logic
    def create_regions(self) -> None:
        self.traversal_requirements = deepcopy(reqs)
        create_regions_with_rules(self)

    # create an item on request with the proper settings
    def create_item(self, name: str) -> ID2Item:
        # print("CREATING ITEM: " + name)
        if name in item_table.keys():
            item_data = item_table[name]
            return ID2Item(name, item_data.classification, self.item_name_to_id[name], self.player)
        else:
            item_data = none_item_table[name]
            return ID2Item(name, item_data.classification, None, self.player)

    # edit an item's base classification
    def create_item_alt(self, name: str, iclass: ItemClassification) -> ID2Item:
        return ID2Item(name, iclass, self.item_name_to_id[name], self.player)

    # Actually generate our items so they can fill the world
    def create_items(self) -> None:
        id2_items: List[ID2Item] = []

        items_to_create: Dict[str, int] = {item: data.quantity_in_item_pool for item, data in item_table.items()}

        # rafts
        if self.options.dungeon_rewards_setting.value == self.options.dungeon_rewards_setting.option_rewards:
            rafts_to_create = 8 - self.options.dungeon_rewards_count.value
            if rafts_to_create < 0:
                rafts_to_create = 0

            items_to_create[iname.raft.value] = rafts_to_create
            # TODO also FKeys

        # if randomize stick is off, give the player a free melee and remove one from the pool
        if not self.options.randomize_stick:
            self.multiworld.push_precollected(self.create_item(iname.melee.value))
            items_to_create[iname.melee.value] = 2

        # progressive vs. upgrades
        if not self.options.progressive_items:
            items_to_create[iname.force.value] = 1
            items_to_create[iname.dynamite.value] = 1
            items_to_create[iname.ice.value] = 1
            items_to_create[iname.chain.value] = 1
            items_to_create[iname.force_upgrade.value] = 2
            items_to_create[iname.dynamite_upgrade.value] = 2
            items_to_create[iname.ice_upgrade.value] = 2
            items_to_create[iname.chain_upgrade.value] = 2

        # if not randomizing roll, give to player and remove from pool
        if not self.options.randomize_roll:
            self.multiworld.push_precollected(self.create_item(iname.roll.value))
            items_to_create[iname.roll.value] = 0

        # key settings
        if self.options.key_settings == KeySettings.option_default:
            items_to_create[iname.d1_key.value] = 2
            items_to_create[iname.d2_key.value] = 2
            items_to_create[iname.d3_key.value] = 4
            items_to_create[iname.d4_key.value] = 4
            items_to_create[iname.d5_key.value] = 5
            items_to_create[iname.d6_key.value] = 5
            items_to_create[iname.d7_key.value] = 5
            items_to_create[iname.d8_key.value] = 8
            # TODO add the other keys

        elif self.options.key_settings == KeySettings.option_keyrings:
            items_to_create[iname.d1_keyring.value] = 1
            items_to_create[iname.d2_keyring.value] = 1
            items_to_create[iname.d3_keyring.value] = 1
            items_to_create[iname.d4_keyring.value] = 1
            items_to_create[iname.d5_keyring.value] = 1
            items_to_create[iname.d6_keyring.value] = 1
            items_to_create[iname.d7_keyring.value] = 1
            items_to_create[iname.d8_keyring.value] = 1
            # items_to_create[iname.s1_keyring.value] = 1
            # items_to_create[iname.s2_keyring.value] = 1
            # items_to_create[iname.s3_keyring.value] = 1
            # items_to_create[iname.s4_keyring.value] = 1
            # items_to_create[iname.dd_keyring.value] = 1
            # items_to_create[iname.dfc_keyring.value] = 1
            # items_to_create[iname.di_keyring.value] = 1
            # items_to_create[iname.da_keyring.value] = 1

        elif self.options.key_settings == KeySettings.option_keysey:
            self.multiworld.push_precollected(self.create_item(iname.keysey.value))

        # remove Forbidden Keys from pool if S4 is open
        if self.options.open_s4:
            items_to_create[iname.f_key.value] = 0

        # configure shard count (currently not supported)
        items_to_create[iname.shard.value] = 0  # self.options.shard_settings.value * 12 \
            # + self.options.extra_shards.value

        # Super Secret stuff
        if self.options.include_super_secrets:
            items_to_create[iname.outfit_apa.value] = 1
            items_to_create[iname.outfit_berry.value] = 1
            items_to_create[iname.outfit_that_guy.value] = 1
            items_to_create[iname.card_fly.value] = 1

        # major skips
        if self.options.major_dungeon_skips:
            self.multiworld.push_precollected(self.create_item(iname.major_skips.value))

        # open options
        if self.options.open_d8:
            self.multiworld.push_precollected(self.create_item(iname.open_d8.value))
        if self.options.open_s4:
            self.multiworld.push_precollected(self.create_item(iname.open_s4.value))
        if self.options.open_dreamworld:
            self.multiworld.push_precollected(self.create_item(iname.open_dw.value))

        # dreamworld
        if self.options.dream_dungeons_do_not_change_items:
            self.multiworld.push_precollected(self.create_item(iname.dw_fun.value))
        else:
            self.multiworld.push_precollected(self.create_item(iname.dw_vanilla.value))

        # phasing
        if self.options.phasing_itemless:
            self.multiworld.push_precollected(self.create_item(iname.option_phasing.value))

        if self.options.phasing_ice:
            self.multiworld.push_precollected(self.create_item(iname.option_phasing_ice.value))

        if self.options.phasing_dynamite:
            self.multiworld.push_precollected(self.create_item(iname.option_phasing_dynamite.value))

        if self.options.phasing_enemies:
            self.multiworld.push_precollected(self.create_item(iname.option_phasing_enemy.value))

        if self.options.phasing_difficult:
            self.multiworld.push_precollected(self.create_item(iname.option_phasing_difficult.value))

        if not self.options.phasing_itemless and not self.options.phasing_ice and not self.options.phasing_dynamite and not self.options.phasing_enemies:
            self.multiworld.push_precollected(self.create_item(iname.glitchless.value))

        # crayon count
        items_to_create[iname.crayon.value] = self.options.crayons_in_pool.value

        # lockpick count
        items_to_create[iname.lockpick.value] = self.options.lockpicks_in_pool.value

        # start with tracker
        if self.options.start_with_tracker:
            self.multiworld.push_precollected(self.create_item(iname.tracker.value))
            self.multiworld.push_precollected(self.create_item(iname.tracker.value))
            self.multiworld.push_precollected(self.create_item(iname.tracker.value))
            items_to_create[iname.tracker.value] = 0

        # create items
        for item_name, quantity in items_to_create.items():
            for _ in range(quantity):
                id2_item: ID2Item = self.create_item(item_name)
                id2_items.append(id2_item)

        # filler
        filler_count = len(self.multiworld.get_unfilled_locations(self.player)) - len(id2_items)
        for _ in range(filler_count):
            id2_items.append(self.create_item(self.get_filler_item_name()))

        self.multiworld.itempool += id2_items

    def get_filler_item_name(self) -> str:
        return self.random.choice(filler_items)

    def write_spoiler_header(self, spoiler_handle: TextIO) -> None:
        if self.options.dungeon_rewards_setting.value != options.DungeonRewardsSetting.option_anything:
            spoiler_handle.write("\nRequired Dungeons:\n\n")
            for dungeon in self.required_dungeons:
                spoiler_handle.write(f"  {dungeon}\n")

    def fill_slot_data(self) -> Dict[str, Any]:
        # Logic PUML graph stuff
        # state = self.multiworld.get_all_state(False)
        # state.update_reachable_regions(self.player)
        # visualize_regions(self.multiworld.get_region("Menu", self.player), "ittle_dew_2_test.puml", show_entrance_names=True, highlight_regions=state.reachable_regions[self.player])
        slot_data = self.options.as_dict(
            "goal",
            "dungeon_rewards_setting",
            "dungeon_rewards_count",
            "progressive_items",
            "include_portal_worlds",
            "include_secret_dungeons",
            "include_dream_dungeons",
            "include_super_secrets",
            "open_d8",
            "open_s4",
            "open_dreamworld",
            "dream_dungeons_do_not_change_items",
            "key_settings",
            "shard_settings",
            "extra_shards",
            "randomize_stick",
            "randomize_roll",
            "roll_opens_chests",
            "major_dungeon_skips",
            "phasing_itemless",
            "phasing_ice",
            "phasing_dynamite",
            "phasing_enemies",
            "phasing_difficult",
            "start_with_tracker",
            "start_with_all_warps",
            "lockpicks_in_pool",
            "crayons_in_pool"
        )
        slot_data["required_dungeons"] = self.required_dungeons
        print("SLOT DATA:")
        print(slot_data)
        return slot_data

    # Universal Tracker stuff
    @staticmethod
    def interpret_slot_data(slot_data: Dict[str, Any]) -> Dict[str, Any]:
        # returning slot_data so it regens, giving it back in multiworld.re_gen_passthrough
        return slot_data
