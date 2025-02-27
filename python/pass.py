import hashlib
import os
import string
import random

FILENAME = "passwords.txt"

# Function to hash the password
def hash_password(password):
    """Hash a password for storing."""
    return hashlib.sha256(password.encode()).hexdigest()

# Function to save password
def save_password(site, password):
    hashed_password = hash_password(password)
    with open(FILENAME, "a") as file:
        file.write(f"{site} {hashed_password}\n")
    print(f"Password for {site} saved successfully.")

# Function to get the password
def get_password(site):
    if not os.path.exists(FILENAME):
        print("No password saved yet.")
        return None

    with open(FILENAME, "r") as f:
        for line in f:
            parts = line.strip().split(" ")
            if len(parts) < 2:
                continue  # Skip improperly formatted lines
            stored_site, stored_password = parts
            if stored_site == site:
                return stored_password

    print(f"No password saved for {site}.")
    return None

def generate_password(length=10):
    """Generate a random password with letters, digits, and special characters."""
    characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choices(characters, k=length))

def main():
    if not os.path.exists(FILENAME):
        with open(FILENAME, "w"):
            pass  # Create the file if it does not exist

    action = input("Enter 'save' to save a password or 'get' to get a password: ").strip().lower()

    if action == "save":
        site = input("Enter the site name: ").strip()
        password = generate_password()
        print(f"Generated password: {password}")
        save_password(site, password)

    elif action == "get":
        site = input("Enter the site name: ").strip()
        password = get_password(site)
        if password:
            print(f"Stored hashed password for {site}: {password}")

    else:
        print("Invalid action. Please enter 'save' or 'get'.")

if __name__ == "__main__":
    main()
