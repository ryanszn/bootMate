"""
menu.py

Description:
    Displays the main terminal interface for bootMate.
    Handles user input and selection of apps to launch.
    
"""

from pathlib import Path

def load_ascii_art(filename):
    path = Path("assets/ascii") / filename
    try:
        with open(path, "r", encoding="utf-8") as file:
            return file.read()
    except FileNotFoundError:
        return "[ASCII ART MISSING]"

def main_menu():
    while True:
        # Clear the terminal screen
        print("\033c", end="")

        # Show welcome ASCII art
        print(load_ascii_art("welcome.txt"))
        print("=" * 60)
        print("Welcome to bootMate! Choose an app to launch:\n")
        print("1. VS Code")
        print("2. Firefox")
        print("3. File Explorer")
        print("Q. Quit")
        print("=" * 60)

        choice = input("Enter your choice: ").strip().lower()

        if choice == "1":
            print("Launching VS Code... (stub)")
        elif choice == "2":
            print("Launching Firefox... (stub)")
        elif choice == "3":
            print("Opening File Explorer... (stub)")
        elif choice == "q":
            print("Goodbye!")
            break
        else:
            print("Invalid input. Please try again.")

        input("\nPress Enter to return to the menu...")
