from enum import Enum

class ItemNames(str, Enum):
    def __str__(self) -> str:
        return self.value
    
    # only includes items that can open locations or reach a goal
    # Main Items
    melee = "Progressive Melee"
    fire_sword = "Fire Sword"
    fire_mace = "Fire Mace"
    force = "Progressive Force Wand"
    dynamite = "Progressive Dynamite"
    ice = "Progressive Ice Ring"
    chain = "Progressive Chain"
    roll = "Roll"
    fake_efcs = "Impossible Gates Pass"

    # Keys
    # All locks assume you have all keys or the key ring
    d1_keys = "Pillow Fort Keys"
    d2_keys = "Sand Castle Keys"
    d3_keys = "Art Gallery Keys"
    d4_keys = "Trash Cave Keys"
    d5_keys = "Flooded Basement Keys"
    d6_keys = "Potassium Mines Keys"
    d7_keys = "Boiling Grave Keys"
    d8_keys = "Grand Library Keys"
    s1_keys = "Sunken Labyrinth Keys"
    s2_keys = "Machine Fortress Keys"
    s3_keys = "Dark Hypostyle Keys"
    s4_keys = "Tomb of Simulacrum Keys"
    # Wizardry Lab has no keys
    dd_keys = "Syncope Keys"
    dfc_keys = "Antigram Keys"
    di_keys = "Bottomless Tower Keys"
    da_keys = "Quietus Keys"
    f_keys = "Forbidden Keys"

    # Tricks, abilities, and options
    can_open_chests = "Can Open Chests"
    can_break_weak_objects = "Can Break Weak Objects" # every weapon except roll, can be used to open caves
    can_break_stong_objects = "Can Break Strong Objects" # melee, dynamite, or ice, since force can't break everything
    can_kill_basic_enemies = "Can Kill Basic Enemies"
    can_phase_itemless = "Can Phase Itemless"
    can_phase_itemless_difficult = "Can Phase Itemless (Difficult)"
    can_phase_ice_itemless = "Can Phase to Existing Ice Blocks"
    can_phase_ice_itemless_difficult = "Can Phase to Existing Ice Blocks (Difficult)"
    can_phase_ice = "Can Phase to Ice Blocks"
    can_phase_ice_difficult = "Can Phase to Ice Blocks (Difficult)"
    can_phase_dynamite = "Can Dynamite-Ice Clip"
    can_phase_dynamite_difficult = "Can Dynamite-Ice Clip (Difficult)"
    can_phase_enemy = "Can Do Enemy Phases"
    can_phase_enemy_difficult = "Can Do Enemy Phases (Difficult)"

    # Events
    has_opened_d8 = "Has Opened Grand Library"
    has_opened_s1 = "Has Opened Sunken Labyrinth"
    has_opened_s2 = "Has Opened Machine Fortress"
    has_opened_s3 = "Has Opened Dark Hypostyle"
    has_opened_s4 = "Has Opened Tomb of Simulacrum"
    has_opened_dw = "Has Opened Dreamworld"
    has_opened_dd = "Has Opened Syncope"
    has_opened_df = "Has Opened Wizardry Lab"
    has_opened_dfc = "Has Opened Antigram"
    has_opened_di = "Has Opened Bottomless Tower"
    has_opened_da = "Has Opened Quietus"