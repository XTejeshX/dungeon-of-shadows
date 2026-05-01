### PHASE 1: Core Mechanics & Combat

**April 08, 2026**
* **Initialization:** Set up the main game loop and entry banner.
* **Player Setup:** Implemented `player.py` with base stats, healing mechanics, and exit functionality.

**April 09, 2026**
* **Enemy Logic:** Created `enemy.py` to handle enemy types, stats, spawning, and death states.
* **Combat Framework:** Created `combat.py` to bridge the interaction between player and enemy.

**April 10, 2026**
* **Combat Integration:**
    * `combat.py`: Implemented the turn-based damage loop.
    * `enemy.py`: Added damage calculation, health tracking, and attack values.
    * `player.py`: Added player attack methods and death state checks.

**April 13, 2026**
* **Progression:** Added leveling system to `player.py` (stat scaling for HP and Attack).
* **Mechanics:** Added a "Run Away" option in `combat.py` with a **50% success rate**.

---

### PHASE 2: World Building & Inventory

**April 14, 2026**
* **Dungeon Design:** Planned multi-room architecture with bosses and loot tables.
* **Main Loop:** Added the first "Entrance Room" logic. Future work to include a visual map.

**April 15, 2026**
* **World Logic:** Created `rooms.py`.
    * Defined descriptions, loot drops, enemy spawn probabilities, and exits.
    * Implemented movement logic and "visited" status tracking.
* **UI:** Added a text-based map printout in `main.py`.

**April 16, 2026**
* **Refactoring:** Fixed indentation bugs and naming inconsistencies across `main.py` and `rooms.py`.
* **Inventory Foundation:** Created `inventory.py` and defined item metadata.

**April 17, 2026**
* **Item Interaction:** Added core inventory functions: `pickup_item()`, `view_inventory()`, and `use_item()`.
* *Note: Identified minor bugs in item handling to be addressed in future updates.*

**April 24, 2026**
* **Bug Fix:** Resolved a dictionary error in `rooms.py` caused by a missing room definition.

---

### PHASE 3: Systems & Data Persistence

**April 24, 2026**
* **Serialization:** Created `save_load.py` to manage save file creation, deletion, and "peeking" (previewing save data).
* **UI Overhaul:** Rearranged `main.py` logic into a cleaner `main()` function and added the `sv` command for quick-saving.

**April 27, 2026**
* **Logic Completion:** Fully defined the previously empty functions in `save_load.py`.
* **Polishing:** Finalized minor state-handling tweaks in the main game loop.


---


### PHASE 4:

**April 27, 2026**
* total refactoring into oop concepts currently enemy.py and player.py files are completed.


**May 01, 2026**
* files of combat.py, inventory.py, rooms.py have been modified to accomodate the new OOP structure 
* further changes need to be done in the main.py file, save.py file