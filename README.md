# 🚁 Natural Language Drone Control in CoppeliaSim (Rule-Based Edition)

This project demonstrates intelligent drone control in CoppeliaSim using:
- A rule-based natural language parser (Python + regex)
- A GUI interface (Tkinter)
- A simulated drone that follows a `/target` object

Users can type natural commands like:

go to the hospital and up 1
go to mall and then forward 2 and down 0.5


These are parsed into structured instructions and executed in the scene.

---

## 🧠 Features

- ✅ Named waypoint commands: `mall`, `hospital`, `university`, `home`
- ✅ Directional movement: `up`, `down`, `left`, `right`, etc.
- ✅ Combo commands like `"go to mall and forward 2"`
- ✅ Tkinter GUI with status display
- ❌ No LLM or internet required

---

## 🗂 Files

|| Description |
|------|-------------|
| `| CoppeliaSim scene file with drone and `/target` object |
| `| Rule-based natural language GUI mission controller |

---

## 🔧 Requirements

```bash
pip install coppeliasim-zmqremoteapi-client

💬 Sample Commands

    go to the mall

    go up 2 and forward 1

    fly to the hospital then down 0.5

    go to home and right 1

🚀 Usage

    Open CoppeliaSim → Load drone_mission_scene.ttt

    Run the Python script:

    python3 lang_parse_combined.py

    Type your mission in the GUI and watch the drone fly!

🧭 Roadmap

Rule-based command execution

LLM integration (GPT, Falcon)

Voice input

Camera overlay

    Multi-agent coordination

🙌 Author

Daniel Christadoss
