# Kaden Billin
# UWYO COSC 1010
# 11-24-2024
# Lab 10
# Lab Section: 12
# Sources, people worked with, help given to: 
# your
# comments
# here

#import modules you will need 

from hashlib import sha256 
from pathlib import Path

path = Path("rockyou.txt")
path2 = Path("hash")


def get_hash(to_hash):
    return sha256(to_hash.encode('utf-8')).hexdigest().upper()

try:
    target = path2.read_text().strip()
    
except FileNotFoundError:
    print("File not found")
    exit()

print(target)

try:
    passwords = path.read_text().splitlines()

except FileNotFoundError:
    print("File not found")
    exit()

else:
    for password in passwords:
        hashedpass = get_hash(password)
        if hashedpass == target:
            print(f"Password found: '{password}'")
            break
    else:
        print("Password not found")



# Files and Exceptions

# For this assignment, you will be writing a program to "crack" a password. You will need to open the file `hash` as this is the password you are trying to "crack."

# To begin, you will need to open the 'rockyou.txt' file:
# - This file contains a list of compromised passwords from the rockyou dump.
# - This is an abridged version, as the full version is quite large.
# - The file contains the plaintext version of the passwords. You will need to hash them to check against the password hash you are trying to crack.
#   - You can use the provided `get_hash()` function to generate the hashes.
#   - Be careful, as "hello" and "hello " would generate a different hash.

# You will need to include a try-except-catch block in your code.
# - The reading of files needs to occur in the try blocks.


# - Read in the value stored within `hash`.
#   - You must use a try and except block.


# Read in the passwords in `rockyou.txt`.
# - Again, you need a try-except-else block.
# Hash each individual password and compare it against the stored hash.
# - When you find the match, print the plaintext version of the password.
# - End your loop.
