import hashlib 
import os
#file to store the passwords and sitename

FILENAME= "password.text"

# function to hash the password
def hash_password(password):
    """hash a password for storing"""

    return(hashlib.sha256(password.encode()).hexdigest())

    #function save the password
    def save_password(site,password):
        """save the site name and the passoword"""
        hash_password = hash_password(password)
        with open(FILENAME,"a") as file:
            file.write(f"{site} {hash_password}\n")
     print(f"password for the site {site} saved successfully")  

     #function to get the password
     def get_password(site):
        """retrieve the password for the site"""
        print("No passwords saved yet")
        return
    with open(FILENAME,"r") as f:
        for line in f:
            stored_site, stored_password, stored_hash = line.strip().split(",")
            if site == stored_site:
            return stored_password
        print(f"No password saved for")
        return
        with open(FILENAME, "r")



        def main():
            if not os.path.exists(FILENAME)