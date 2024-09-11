from typing import Dict, List, Any, Union, TextIO
from copy import deepcopy

import Options
from BaseClasses import Location, Item, Tutorial, ItemClassification
from Options import OptionError
from math import floor
from Utils import visualize_regions
from .items import item_name_to_id, item_table, none_item_table, item_name_groups, filler_items, trap_items, super_trap_items
from .locations import location_name_groups, location_name_to_id
from .region_data import traversal_requirements as reqs, ID2Data, ID2Type
from .region_rules import create_regions_with_rules
from .options import ID2Options, id2_options_groups, id2_options_presets, KeySettings
from .names_regions import RegionNames as rname
from .names_locations import LocationNames as lname
from .names_items import ItemNames as iname
from worlds.AutoWorld import WebWorld, World


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
    piano_puzzle: str = "DEAD"
    hint_seed = 0

    options: ID2Options
    options_dataclass = ID2Options
    item_name_groups = item_name_groups
    location_name_groups = location_name_groups

    item_name_to_id = item_name_to_id
    location_name_to_id = location_name_to_id

    traversal_requirements: Dict[rname, Dict[Union[lname, rname], ID2Data]]

    def generate_early(self) -> None:
        self.piano_puzzle = self.generate_piano_puzzle()
        if self.options.goal.value == options.Goal.option_queen_of_dreams:
            self.options.include_dream_dungeons.value = options.IncludeDreamDungeons.option_true
            self.options.dungeon_rewards_setting.value = options.DungeonRewardsSetting.option_anything
            self.options.open_d8.value = options.OpenD8.option_true

        if self.options.trap_percentage.value + self.options.super_trap_percentage.value > 100:
            self.options.super_trap_percentage.value = 100 - self.options.trap_percentage.value

        if not self.options.include_dream_dungeons:
            self.options.remove_cards.value = options.RemoveCards.option_true

        if self.options.block_region_connections:
            self.options.start_with_all_warps.value = options.StartWithAllWarps.option_false

        self.hint_seed = self.random.randint(0, 2000000000)

        dungeon_count = 8
        if self.options.include_secret_dungeons:
            dungeon_count += 3
        else:
            self.options.open_s4.value = options.OpenS4.option_false
            self.options.shard_settings.value = options.ShardSettings.option_open
            self.options.extra_shards.value = 0
        if self.options.include_dream_dungeons:
            dungeon_count += 4
        if self.options.dungeon_rewards_setting.value != options.DungeonRewardsSetting.option_anything and self.options.dungeon_rewards_count.value > dungeon_count:
            print(f"Not enough dungeons available to place dungeon rewards in, clamping down to {dungeon_count} instead")
            self.options.dungeon_rewards_count.value = dungeon_count

        # For Universal Tracker
        if hasattr(self.multiworld, "re_gen_passthrough"):
            if "Ittle Dew 2" in self.multiworld.re_gen_passthrough:
                passthrough = self.multiworld.re_gen_passthrough["Ittle Dew 2"]
                self.options.goal.value = passthrough["goal"]
                self.options.required_potion_count = passthrough["required_potion_count"]
                self.options.include_portal_worlds.value = passthrough["include_portal_worlds"]
                self.options.include_secret_dungeons.value = passthrough["include_secret_dungeons"]
                self.options.include_dream_dungeons.value = passthrough["include_dream_dungeons"]
                self.options.include_super_secrets.value = passthrough["include_super_secrets"]
                self.options.include_secret_signs.value = passthrough["include_secret_signs"]
                self.options.block_region_connections.value = passthrough["block_region_connections"]
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
                self.options.phasing_setting.value = passthrough["phasing_setting"]
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

        potions_to_create = 0
        if self.options.goal.value == options.Goal.option_potion_hunt:
            potions_to_create = self.options.required_potion_count.value + self.options.extra_potions.value
            items_to_create[iname.potion.value] = potions_to_create

        # rafts and fkeys
        if self.options.dungeon_rewards_setting.value == self.options.dungeon_rewards_setting.option_rewards:
            spill = 0
            potions_to_create -= self.options.dungeon_rewards_count.value
            if potions_to_create < 0:
                spill = -potions_to_create
                potions_to_create = 0

            if self.options.goal.value == options.Goal.option_potion_hunt:
                rafts_to_create = 0
                if self.options.include_dream_dungeons:
                    rafts_to_create = 1 - spill
                if not self.options.open_d8:
                    rafts_to_create = 7 - spill
            else:
                rafts_to_create = 8 - spill
            if rafts_to_create < 0:
                spill = -rafts_to_create
                rafts_to_create = 0
            else:
                spill = 0

            items_to_create[iname.raft.value] = rafts_to_create

            fkeys_to_create = 4 - spill
            if fkeys_to_create < 0:
                fkeys_to_create = 0

            items_to_create[iname.f_key.value] = fkeys_to_create

        items_to_create[iname.potion.value] = potions_to_create

        if self.options.goal.value == options.Goal.option_queen_of_dreams:
            items_to_create[iname.raft.value] = 1

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
            if self.options.include_secret_dungeons:
                items_to_create[iname.s1_key.value] = 3
                items_to_create[iname.s2_key.value] = 5
                items_to_create[iname.s3_key.value] = 5
            if self.options.include_secret_dungeons or self.options.goal == options.Goal.option_queen_of_adventure:
                items_to_create[iname.s4_key.value] = 10
            if self.options.include_dream_dungeons:
                items_to_create[iname.dd_key.value] = 3
                items_to_create[iname.dfc_key.value] = 4
                items_to_create[iname.di_key.value] = 4
                items_to_create[iname.da_key.value] = 4

        elif self.options.key_settings == KeySettings.option_keyrings:
            items_to_create[iname.d1_keyring.value] = 1
            items_to_create[iname.d2_keyring.value] = 1
            items_to_create[iname.d3_keyring.value] = 1
            items_to_create[iname.d4_keyring.value] = 1
            items_to_create[iname.d5_keyring.value] = 1
            items_to_create[iname.d6_keyring.value] = 1
            items_to_create[iname.d7_keyring.value] = 1
            items_to_create[iname.d8_keyring.value] = 1
            if self.options.include_secret_dungeons:
                items_to_create[iname.s1_keyring.value] = 1
                items_to_create[iname.s2_keyring.value] = 1
                items_to_create[iname.s3_keyring.value] = 1
            if self.options.include_secret_dungeons or self.options.goal == options.Goal.option_queen_of_adventure:
                items_to_create[iname.s4_keyring.value] = 1
            if self.options.include_dream_dungeons:
                items_to_create[iname.dd_keyring.value] = 1
                items_to_create[iname.dfc_keyring.value] = 1
                items_to_create[iname.di_keyring.value] = 1
                items_to_create[iname.da_keyring.value] = 1

        elif self.options.key_settings == KeySettings.option_keysey:
            self.multiworld.push_precollected(self.create_item(iname.keysey.value))

        # remove Forbidden Keys from pool if S4 is open
        if self.options.open_s4:
            items_to_create[iname.f_key.value] = 0

        # configure shard count
        items_to_create[iname.shard.value] = self.options.shard_settings.value * 12 + self.options.extra_shards.value

        # cards
        if self.options.remove_cards:
            for card in items_to_create.keys():
                if card in item_name_groups["Cards"]:
                    items_to_create[card] = 0

        # Connections items
        for connection in items_to_create.keys():
            if connection in item_name_groups["Connections"]:
                if self.options.block_region_connections:
                    items_to_create[connection] = 1
                else:
                    self.multiworld.push_precollected(self.create_item(connection))

        # Super Secret stuff
        if self.options.include_super_secrets:
            items_to_create[iname.outfit_apa.value] = 1
            items_to_create[iname.outfit_berry.value] = 1
            items_to_create[iname.outfit_that_guy.value] = 1
            items_to_create[iname.card_fly.value] = 1
        else:
            items_to_create[iname.outfit_apa.value] = 0
            items_to_create[iname.outfit_berry.value] = 0
            items_to_create[iname.outfit_that_guy.value] = 0
            items_to_create[iname.card_fly.value] = 0

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
        if self.options.phasing_enemies:
            if self.options.phasing_setting.value < options.PhasingSetting.option_object_phases:
                self.options.phasing_setting.value = options.PhasingSetting.option_object_phases
            self.multiworld.push_precollected(self.create_item(iname.option_phasing_enemy.value))

        if self.options.phasing_difficult:
            self.multiworld.push_precollected(self.create_item(iname.option_phasing_difficult.value))

        if self.options.phasing_setting.value >= options.PhasingSetting.option_gap_phases:
            self.multiworld.push_precollected(self.create_item(iname.option_phasing.value))
            if self.options.phasing_setting.value >= options.PhasingSetting.option_object_phases:
                self.multiworld.push_precollected(self.create_item(iname.option_phasing_objects.value))
                if self.options.phasing_setting.value >= options.PhasingSetting.option_ice_dynamite_clips:
                    self.multiworld.push_precollected(self.create_item(iname.option_phasing_dynamite.value))

        if self.options.phasing_setting == options.PhasingSetting.option_off and not self.options.phasing_enemies:
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
        if filler_count < 0:
            raise OptionError(f"Not enough space in the pool! Need space for {-filler_count} more items. {self.player_name}, "
                              f"try reducing the number of items in your world. Try reducing the number of crayons and lockpicks, "
                              f"using keyrings or keysey, the number of shards required, or turning on Remove Cards From Pool.\n"
                              f"{self.player_name}, please fix your yaml.")
        trap_count = floor((self.options.trap_percentage * 0.01) * filler_count)
        super_trap_count = floor((self.options.super_trap_percentage * 0.01) * filler_count)
        filler_count -= trap_count + super_trap_count

        for _ in range(filler_count):
            id2_items.append(self.create_item(self.get_filler_item_name()))
        for _ in range(trap_count):
            id2_items.append(self.create_item(self.get_trap_item_name()))
        for _ in range(super_trap_count):
            id2_items.append(self.create_item(self.get_super_trap_item_name()))

        self.multiworld.itempool += id2_items

        # early weapon choice
        if self.options.early_weapon_choice.value != options.EarlyWeaponChoice.option_off:
            early_item_name = ""
            if self.options.early_weapon_choice.value == options.EarlyWeaponChoice.option_melee:
                early_item_name = iname.melee.value
            elif self.options.early_weapon_choice.value == options.EarlyWeaponChoice.option_force_wand:
                early_item_name = iname.force.value
            elif self.options.early_weapon_choice.value == options.EarlyWeaponChoice.option_dynamite:
                early_item_name = iname.dynamite.value
            elif self.options.early_weapon_choice.value == options.EarlyWeaponChoice.option_ice_ring:
                early_item_name = iname.ice.value
            self.multiworld.local_early_items[self.player][early_item_name] = 1


    def get_filler_item_name(self) -> str:
        return self.random.choice(filler_items)

    def get_trap_item_name(self) -> str:
        return self.random.choice(trap_items)

    def get_super_trap_item_name(self) -> str:
        return self.random.choice(super_trap_items)

    def write_spoiler_header(self, spoiler_handle: TextIO) -> None:
        if self.options.dungeon_rewards_setting.value != options.DungeonRewardsSetting.option_anything:
            spoiler_handle.write("\nRequired Dungeons:\n\n")
            for dungeon in self.required_dungeons:
                spoiler_handle.write(f"  {dungeon}\n")
        spoiler_handle.write(f"\nSyncope Piano Code: {self.piano_puzzle}\n")

    def fill_slot_data(self) -> Dict[str, Any]:
        # Logic PUML graph stuff
        # state = self.multiworld.get_all_state(False)
        # state.update_reachable_regions(self.player)
        # visualize_regions(self.multiworld.get_region("Menu", self.player), "ittle_dew_2_test.puml", show_entrance_names=True, highlight_regions=state.reachable_regions[self.player])
        slot_data = self.options.as_dict(
            "goal",
            "required_potion_count",
            "extra_potions",
            "dungeon_rewards_setting",
            "dungeon_rewards_count",
            "progressive_items",
            "include_portal_worlds",
            "include_secret_dungeons",
            "include_dream_dungeons",
            "include_super_secrets",
            "include_secret_signs",
            "block_region_connections",
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
            "phasing_setting",
            "phasing_enemies",
            "phasing_difficult",
            "start_with_tracker",
            "start_with_all_warps",
            "lockpicks_in_pool",
            "crayons_in_pool",
            "trap_percentage",
            "super_trap_percentage"
        )
        slot_data["required_dungeons"] = self.required_dungeons
        slot_data["piano_puzzle"] = self.piano_puzzle
        slot_data["hint_seed"] = self.hint_seed
        # print("SLOT DATA:")
        # print(slot_data)
        return slot_data

    # Universal Tracker stuff
    @staticmethod
    def interpret_slot_data(slot_data: Dict[str, Any]) -> Dict[str, Any]:
        # returning slot_data so it regens, giving it back in multiworld.re_gen_passthrough
        return slot_data

    def generate_piano_puzzle(self) -> str:
        # To make parsing the hint easier on the mod side, we make white keys uppercase while black keys are lowercase
        white_keys: List[str] = ["C", "D", "E", "F", "G", "A", "B"]
        black_keys: Dict[str, str] = {
            "C": "c",
            "D": "d",
            "F": "f",
            "G": "g",
            "A": "a"
        }
        words: List[str] = [
            "ACE", "ADD", "AGE",
            "ACED", "AGED",
            "ADAGE",
            "ACCEDE",
            "ACCEDED",
            "BAA", "BAD", "BAG", "BED", "BEE", "BEG",
            "BABE", "BADE", "BEAD", "BEEF",
            "BADGE",
            "BADGED", "BAGGED", "BEADED", "BEDDED", "BEEFED", "BEGGED",
            "CAB", "CAD",
            "CAFE", "CAGE", "CEDE",
            "CAGED", "CEDED",
            "CABBED",
            "CABBAGE",
            "DAB", "DAD", "DAG",
            "DACE", "DEAD", "DEAF", "DEED",
            "DECAF",
            "DABBED", "DECADE", "DEEDED", "DEFACE",
            "DEFACED",
            "EBB", "EGG",
            "EDGE", "EGAD",
            "EBBED", "EDGED",
            "EFFACE",
            "EFFACED",
            "FAB", "FAD", "FED", "FEE",
            "FACE", "FADE", "FEED",
            "FACED", "FADED",
            "FACADE",
            "FEEDBAG",
            "GAB", "GAG", "GAD",
            "GAFF",
            "GAFFE",
            "GAFFED", "GAGGED"
        ]
        piano_text = "DEAD"

        piano_option = self.options.randomize_piano_puzzle.value
        if piano_option != options.RandomizePianoPuzzle.option_off:
            new_text = ""
            if piano_option == options.RandomizePianoPuzzle.option_full_random:
                word_length = self.random.randint(3, 7)
                for _ in range(word_length):
                    rnd = self.random.randint(0, len(white_keys) - 1)
                    new_text += white_keys[rnd]
            else:
                rnd = self.random.randint(0, len(words) - 1)
                new_text = words[rnd]
            if piano_option != options.RandomizePianoPuzzle.option_words:
                sharp_text = ""
                for letter in new_text:
                    new_letter = letter
                    if letter in black_keys.keys():
                        rnd = self.random.randint(0, 1)
                        if rnd == 0:
                            new_letter = black_keys[letter]
                    sharp_text += new_letter
                new_text = sharp_text
            piano_text = new_text

        return piano_text
