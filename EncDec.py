import os
from cryptography.fernet import Fernet
import time
import sys

# Defines and lists
files = []
empty = []
key = 0
args = sys.argv

# Startup

try:
    print("")
    print(" /$$$$$$$$ /$$   /$$  /$$$$$$        /$$$$$$$  /$$$$$$$$  /$$$$$$ ")
    print("| $$_____/| $$$ | $$ /$$__  $$      | $$__  $$| $$_____/ /$$__  $$")
    print("| $$      | $$$$| $$| $$  \__/      | $$  \ $$| $$      | $$  \__/")
    print("| $$$$$   | $$ $$ $$| $$            | $$  | $$| $$$$$   | $$      ")
    print("| $$__/   | $$  $$$$| $$            | $$  | $$| $$__/   | $$ ")
    print("| $$      | $$\  $$$| $$    $$      | $$  | $$| $$      | $$    $$")
    print("| $$$$$$$$| $$ \  $$|  $$$$$$/      | $$$$$$$/| $$$$$$$$|  $$$$$$/")
    print("|________/|__/  \__/ \______/       |_______/ |________/ \______/")
    print("")
    time.sleep(0.5)
    print("By ")
    print(" ____  _  _____ ____")
    print("/    \/ \/   _// ___\      / \ /\"")
    print("|  \/|| ||  \  |    \_____ | | ||")
    print("|  __/| ||  /_ \___ |\____\| \_/|")
    print("\_/   \_/\____\\____/      \____/")
    time.sleep(1)
    print("")
    print("Super Simple Simetric Encrpyt/Decrpyt Software For Text")
    time.sleep(2)
    print("")

except UnicodeEncodeError:
    print("EncDec")
    print("")
    time.sleep(0.5)
    print("By")
    print("Pies-U")
    print("")
    time.sleep(1)
    print("sadly your charset cant render the fine version of this")
    print("")

# File Scan

for file in os.listdir():
    if file == "EncDec.py":
        continue
    if file == "lock.key":
        continue
    if os.path.isfile(file):
        if file.endswith(".txt"):
            files.append(file)
        else:
            continue
print("Found files:")
print(" ".join(files))
print("")
if files == empty:
    print("Found 0 .txt files use cd to change location")



# Main Loop

while True:
    print("")
    command = input("> ")

    # Key Creation & Handling
    if command == "genkey":
        with open("C:/lock.key", "rb") as thekey:
            key_content = str(thekey.read())
            if '' or '' or 'KEY-HAS-BEEN-DELETED' in key_content:
                key = Fernet.generate_key()
                with open("C:/lock.key", "wb") as thekey:
                    thekey.write(key)
                print("Successfully Generated a Key")
            else:
                print("KEY IS ALL READY GENERATED USE DelKey TO DELETE IT")

    # File encryption
    elif command == "encrypt":
        if files == empty:
            print("0 files found - Aborting encryption")
        
        else:
            with open("C:/lock.key", "rb") as thekey:
                key = thekey.read()
            for file in files:
                with open(file, "rb") as thefile:
                    contents = thefile.read()
                contents_enc = Fernet(key).encrypt(contents)
                with open(file, "wb") as thefile:
                    thefile.write(contents_enc)
            print("Successfully Encrypted Files")

    # File Decryption
    elif command == "decrypt":
        with open("C:/lock.key", "rb") as dec_key:
            key = dec_key.read()
        for file in files:
            with open(file, "rb") as enc_file:
                enc_contents = enc_file.read()
                dec_contents = Fernet(key).decrypt(enc_contents)
            with open(file, "wb") as dec_file:
                dec_file.write(dec_contents)
        print("Succesfully Decrypted Files")

    # DelKey
    elif command == "delkey":
        print("")
        print("WARNING DELETING A KEY")
        print("WITHOUT IT DECRYPTION WILL BE IMPOSSIBLE")
        print("Are you sure you want to proceed?")
        print("Y or n")
        print("")
        if input("> ") == "Y" or "y":
            with open("C:/lock.key", "wb") as thekey:
                thekey.write(bytes("KEY-HAS-BEEN-DELETED", encoding="ascii"))
            print("")
            print("Successfully Deleted The Key")
        else:
            print("Key Deletion Aborted")

    #  File System
    elif command == "ls":
        print(os.listdir())
    
    elif command == "cd" and len(command) > 1:
        command_list = command.split()
        if len(command_list) < 2:
            # no directory provided
            print("Usage: cd \"directory name\"")
            continue
        directory = command_list[1]
        try:
            os.chdir(directory)
        except OSError:
            print("Didnt find that reverting")




    elif command == "Help":
        print("")
        print("GenKey - to generate key")
        print("Encrypt - to encrypt detected files")
        print("Decrypt - to decrypt detected files")
        print("DelKey -  to delete current key")
        print("Scan - to scan current location for .txt files")
        print("cd - to change current location")
        print("")

    # Quit
    elif command == "quit":
        break

    # Scan

    elif command == "Scan":
        print("")
        for file in os.listdir():
            if file == "EncDec.py":
                continue
            if file == "lock.key":
                continue
            if os.path.isfile(file):
                if file.endswith(".txt"):
                    if file in files:
                        pass
                    else:
                        files.append(file)
            else:
                continue
        print("Found files:")
        print(" ".join(files))
        print("")

    else:
        print("Unknown Command - Try Again")
