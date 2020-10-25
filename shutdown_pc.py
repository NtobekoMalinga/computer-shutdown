"""turns off the pc."""
import os
import sys


def main():
    """Shuts down the pc.

    if user inputs s it shuts down the pc,
    if user inputs h it hibernates the pc,
    if user inputs r it restarts the pc.
    """
    commands = {'s': 'Shutdown', 'h': 'Hibernate', 'r': 'Restart'}
    command = input("Enter command 's - shutdown', 'h - hibernate', 'r - restart': ").lower()
    
    if command in commands.keys():
        confirm = input(f"{commands[command]} pc? (y/n): ").lower()
        if confirm == "y":
            os.system(f"shutdown /{command}")
        elif confirm == "n":
            print(f"Aborting {commands[command]}...")
        else:
            print(f"Invalid command. Aborting {commands[command]}...")
            sys.exit()
    else:
        print("Invalid command.")
        sys.exit()
  

if __name__ == "__main__":
    main()
