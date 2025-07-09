import os
import sys
import time
import shutil
import random

# Rocket body
rocket = [
    "    ^    ",
    "   /^\\   ",
    "   |- |  ",
    "   |  |  ",
    "  /|  |\\ ",
    " /_|__|_\\",
    "   /  \\  ",
    "  /    \\ ",
    " |      |",
    " |      |",
    " |      |",
    "/________\\"
]

# Fire frames (to animate flame flicker)
fire_frames = [
    ["   ***   ", "   ***   ", "   ***   "],
    ["   ***   ", "  *****  ", "   ***   "],
    ["   ***   ", "   ***   ", "  *****  "],
    ["  * * *  ", "   ***   ", "  * * *  "],
]

def clear_screen():
    os.system('clear' if os.name == 'posix' else 'cls')

def get_terminal_size():
    try:
        return shutil.get_terminal_size((80, 20))
    except:
        return (80, 20)

def print_centered_rocket(position):
    width, _ = get_terminal_size()
    rocket_width = len(rocket[0])
    padding = (width - rocket_width) // 2

    clear_screen()
    # Add blank lines to move rocket up
    for _ in range(position):
        print()

    # Print rocket
    for line in rocket:
        print(" " * padding + line)

    # Fire animation
    flame = random.choice(fire_frames)
    for fline in flame:
        print(" " * padding + fline)

    sys.stdout.flush()

def launch_sequence():
    for i in range(5, 0, -1):
        clear_screen()
        width, _ = get_terminal_size()
        print(" " * (width // 2 - 7) + f"T-minus {i}...")
        time.sleep(1)

    # Launch animation
    for pos in range(15, -1, -1):
        print_centered_rocket(pos)
        time.sleep(0.1)

    clear_screen()
    print("🚀 Rocket has launched into space!\n")

if __name__ == "__main__":
    launch_sequence()
