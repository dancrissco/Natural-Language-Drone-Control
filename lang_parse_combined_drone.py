import tkinter as tk
import re
import time
from coppeliasim_zmqremoteapi_client import RemoteAPIClient

# Connect to CoppeliaSim
client = RemoteAPIClient()
sim = client.require('sim')

# Get target object
target_handle = sim.getObject('/target')
target_pos = list(sim.getObjectPosition(target_handle, -1))

# Define named locations
locations = {
    "hospital": [-2.0, 2.0, 1.0],
    "mall": [2.0, 2.0, 1.0],
    "university": [-2.0, -2.0, 1.0],
    "home": [0.0, 0.0, 1.0]
}

# Directional vectors
DIRECTIONS = {
    "up":     [0, 0, 1],
    "down":   [0, 0, -1],
    "forward":[0, 1, 0],
    "backward":[0, -1, 0],
    "right":  [1, 0, 0],
    "left":   [-1, 0, 0]
}

# Parse input into mission steps
def parse_command(text):
    text = text.lower()
    steps = []

    # Named locations
    for name in locations:
        if re.search(rf"\b{name}\b", text):
            steps.append(("goto", name))

    # Offset commands
    offsets = re.findall(r"(up|down|left|right|forward|backward)\s+([\d.]+)", text)
    for direction, value in offsets:
        steps.append(("offset", direction, float(value)))

    return steps

# Execute mission
def run_mission(steps):
    global target_pos

    for step in steps:
        if step[0] == "goto":
            place = step[1]
            target_pos = locations[place]
            sim.setObjectPosition(target_handle, -1, target_pos)
            status_label.config(text=f"Going to {place.title()} at {target_pos}")
            root.update()
            time.sleep(5)

        elif step[0] == "offset":
            direction, distance = step[1], step[2]
            dx, dy, dz = DIRECTIONS[direction]
            target_pos[0] += dx * distance
            target_pos[1] += dy * distance
            target_pos[2] += dz * distance
            sim.setObjectPosition(target_handle, -1, target_pos)
            status_label.config(text=f"Moving {direction} {distance} → {target_pos}")
            root.update()
            time.sleep(3)

    status_label.config(text="✅ Mission completed.")

# GUI
root = tk.Tk()
root.title("LLM Drone Commander (Combined Mode)")

tk.Label(root, text="Enter command:").pack()
entry = tk.Entry(root, width=50)
entry.pack()

status_label = tk.Label(root, text="")
status_label.pack()

def on_submit():
    cmd = entry.get()
    steps = parse_command(cmd)

    if not steps:
        status_label.config(text="❌ No valid actions found.")
        return

    status_label.config(text=f"🧠 Parsed mission with {len(steps)} step(s)")
    root.update()
    run_mission(steps)
    entry.delete(0, tk.END)

tk.Button(root, text="Execute Mission", command=on_submit).pack(pady=5)

root.mainloop()
