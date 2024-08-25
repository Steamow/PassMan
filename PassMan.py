import json 
import os
import os

dataDir = "data"
#runCountFile = os.path.join(dataDir, "runNum.json")
passwordsFile = os.path.join(dataDir, "passwords.json")
usernamesFile = os.path.join(dataDir, "usernames.json")
username = {}
passwords = {}

os.makedirs(dataDir, exist_ok=True)

#if os.path.exists(runCountFile):
#    with open(runCountFile, 'r') as f:
#        data = json.load(f)
#        runCount = data.get("runNum", 0)
#else:
#    runCount = 0

#runCount += 1

#with open(runCountFile, 'w') as f:
#    json.dump({"runNum": runCount}, f)

#print(f"Run {runCount}")

choice = input("Do you want to retrieve usernames and passwords (R), add usernames and passwords (A), or delete usernames and passwords (D)? ").lower()

if choice == "r":
    if os.path.exists(passwordsFile):
        with open(passwordsFile, 'r') as f:
            data = json.load(f)
            passwords = data.get("passwords", {})
            print("Password file found.")
    else:
        passwords = {}
        with open(passwordsFile, 'w') as f:
            json.dump({"passwords": {}}, f)
        print("Password file not found, creating a new one.")

    if os.path.exists(usernamesFile):
        with open(usernamesFile, 'r') as f:
            data = json.load(f)
            username = data.get("usernames", {})
            print("Username file found.")
    else:
        username = {}
        with open(usernamesFile, 'w') as f:
            json.dump({"usernames": {}}, f)
        print("Username file not found, creating a new one.")

    print("Available labels:")
    for label in username.keys():
        print(label)

    selected_label = input("Enter the label to retrieve the username and password: ")

    if selected_label in username:
        print("Username:", username[selected_label])
        print("Password:", passwords.get(selected_label, "Password not found."))
    else:
        print("Label not found.")

elif choice == "a":
    # Prompt the user to enter a label for the username
    label = input("Enter a label for the username: ")

    # Prompt the user to enter the username
    input_username = input("Enter the username: ")

    # Prompt the user to enter the password
    input_password = input("Enter the password: ")

    # Check if the usernames file exists
    if os.path.exists(usernamesFile):
        with open(usernamesFile, 'r') as f:
            data = json.load(f)
            username = data.get("usernames", {})
    else:
        username = {}

    # Add the username to the usernames dictionary with the given label
    username[label] = input_username

    # Write the updated usernames dictionary to the usernames file
    with open(usernamesFile, 'w') as f:
        json.dump({"usernames": username}, f)

    # Check if the passwords file exists
    if os.path.exists(passwordsFile):
        with open(passwordsFile, 'r') as f:
            data = json.load(f)
            passwords = data.get("passwords", {})
    else:
        passwords = {}

    # Add the password to the passwords dictionary with the given label
    passwords[label] = input_password

    # Write the updated passwords dictionary to the passwords file
    with open(passwordsFile, 'w') as f:
        json.dump({"passwords": passwords}, f)

    print(f"Username and password for '{label}' added successfully.")

elif choice == "d":
    # Check if the usernames file exists
    if os.path.exists(usernamesFile):
        with open(usernamesFile, 'r') as f:
            data = json.load(f)
            username = data.get("usernames", {})
    else:
        username = {}

    # Check if the passwords file exists
    if os.path.exists(passwordsFile):
        with open(passwordsFile, 'r') as f:
            data = json.load(f)
            passwords = data.get("passwords", {})
    else:
        passwords = {}

    print("Available labels:")
    for label in username.keys():
        print(label)

    selected_label = input("Enter the label to delete the username and password: ")

    if selected_label in username:
        print("Username:", username[selected_label])
        print("Password:", passwords.get(selected_label, "Password not found."))

        confirm = input("Are you sure you want to delete the username and password? (Y/N): ")

        if confirm.lower() == "y":
            del username[selected_label]
            del passwords[selected_label]

            with open(usernamesFile, 'w') as f:
                json.dump({"usernames": username}, f)

            with open(passwordsFile, 'w') as f:
                json.dump({"passwords": passwords}, f)

            print(f"Username and password for '{selected_label}' deleted successfully.")
        else:
            print("Deletion canceled.")
    else:
        print("Label not found.")

else:
    print("Invalid choice")

print("Usernames file directory:", os.path.abspath(usernamesFile))
print("Passwords file directory:", os.path.abspath(passwordsFile))