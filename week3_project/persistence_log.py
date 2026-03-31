import os

FILE_NAME = "database.txt"

# Function to add a blocker (Append)
def add_blocker():
    blocker = input("Enter your Daily Blocker: ")

    with open(FILE_NAME, "a") as file:
        file.write(blocker + "\n")

    print(" Blocker saved successfully.\n")


# Function to read blockers (Fetch)
def fetch_blockers():
    if not os.path.exists(FILE_NAME):
        print(" File does not exist.\n")
        return

    with open(FILE_NAME, "r") as file:
        lines = file.readlines()

        if not lines:
            print(" No blockers found.\n")
        else:
            print("\n Team Daily Blockers:")
            for i, line in enumerate(lines, 1):
                print(f"{i}. {line.strip()}")
            print()


# Function to overwrite warning
def overwrite_file():
    confirm = input(" Are you sure you want to overwrite the file? (yes/no): ")

    if confirm.lower() == "yes":
        with open(FILE_NAME, "w") as file:
            file.write("")
        print(" File has been overwritten.\n")
    else:
        print(" Operation cancelled.\n")


# Main menu
def main():
    while True:
        print("=== Team Daily Status System ===")
        print("1. Add Blocker")
        print("2. Fetch Blockers")
        print("3. Overwrite File")
        print("4. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            add_blocker()
        elif choice == "2":
            fetch_blockers()
        elif choice == "3":
            overwrite_file()
        elif choice == "4":
            print(" Exiting program...")
            break
        else:
            print(" Invalid option.\n")


if __name__ == "__main__":
    main()


"""
--- ENGLISH TASKS ---

Protocol selection (3-C Rule):

1. I will reach out to the team via Slack because the issue is an immediate blocker and requires a quick response.
2. I would use Email to report the error if it requires a formal explanation and documentation.
3. I will use Jira to track the issue because it allows proper monitoring and assignment of tasks.


Vocabulary integration:

This script demonstrates Persistence by storing blockers in a text file.
It allows users to Fetch stored data and review previous entries.
The system prevents accidental Overwrite by asking for confirmation.
If an issue occurs, the user can Reach out to the team using appropriate communication channels.
"""