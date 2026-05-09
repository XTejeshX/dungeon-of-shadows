# ⚔️ Dungeon of Shadows

A terminal-based RPG built entirely with Python to practice core programming fundamentals — from basic loops all the way to OOP and project packaging.

---

## 🚀 How to Run

```bash
# 1. Clone the project
git clone https://github.com/YOUR_USERNAME/dungeon-of-shadows.git
cd dungeon-of-shadows

# 2. No dependencies needed — uses Python stdlib only
# Just run:
python main.py
```

> Requires Python 3.8 or higher.

---

## 🎮 How to Play

| Key | Action |
|-----|--------|
| `n / s / e / w` | Move north / south / east / west |
| `p` | Pick up item in the room |
| `i` | View inventory |
| `u` | Use an item from your bag |
| `m` | Show dungeon map |
| `t` | Show player stats |
| `sv` | Save the game |
| `q` | Quit to main menu |

**Goal:** Navigate through the dungeon, collect weapons and potions, level up by defeating enemies, and beat the **Dungeon Boss** in the Throne Room.

---

## 📁 Project Structure

```
dungeon-of-shadows/
│
├── main.py              ← Entry point — run this to start the game
│
├── game/                ← The game package (all core logic lives here)
│   ├── __init__.py      ← Makes game/ a Python package, defines exports
│   ├── player.py        ← Player class (stats, leveling, serialisation)
│   ├── enemy.py         ← Enemy + Boss classes (inheritance example)
│   ├── rooms.py         ← Room class + dungeon map builder
│   ├── combat.py        ← Turn-based combat loop
│   ├── inventory.py     ← Item definitions, pickup, and use logic
│   └── save_load.py     ← JSON save/load system with robust error handling
│
├── requirements.txt     ← Project dependencies (stdlib only)
├── .gitignore           ← Files Git should never track
└── README.md            ← This file
```

---

## 🐍 Python Concepts Covered

| Phase | Concepts |
|-------|----------|
| **1 — Core Loop** | Variables, loops, conditionals, functions, `random` |
| **2 — Rooms & Items** | Nested dicts, lists, multi-file modules |
| **3 — Save System** | File I/O, `json`, `os`, `try/except` |
| **4 — OOP Refactor** | Classes, `__init__`, methods, inheritance, `@classmethod`, `__str__` |
| **5 — Packaging** | Packages, `__init__.py`, relative imports, `requirements.txt`, `.gitignore` |

---

## 🗺️ Dungeon Map

```
         [THRONE ROOM]  ← Boss fight / Win condition
               │
[PRISON] ─ [HALLWAY] ─ [ARMORY]
               │           │
          [ENTRANCE] ─ [GUARD ROOM]
               ↑
           Start here
```

---

## 📖 Development Diary

See `diary.md` for a full log of what was built on each day across all 5 phases.

---

## 🔮 Possible Extensions (great for AI/ML prep)

- **Pathfinding AI** — enemies that chase the player using BFS/DFS
- **Procedural dungeon generation** — random maps every run
- **Item recommendation system** — suggest items based on playstyle (intro to ML)
- **Unit tests** — add a `tests/` folder with `pytest`