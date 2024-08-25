import json 

username = ""
password = ""

try:
    with open("data/usernames.json", 'r') as f:
        username = json.load(f)
except FileNotFoundError:
    print("usernames.json not found")

try:
    with open("data/passwords.json", "r") as f:
        password = json.load(f)
except FileNotFoundError:
    print("passwords.json not found")

print(username)
print(password) 