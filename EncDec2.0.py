import os
from cryptography.fernet import Fernet
import time

# Defines and lists
files = []
empty = []
file = ""

def genkey():
    with open("C:/lock.key", "rb") as thekey:
        key_content = str(thekey.read())
        if '' or '' or 'KEY-HAS-BEEN-DELETED' in key_content:
            key = Fernet.generate_key()
            with open("C:/lock.key", "wb") as thekey:
                thekey.write(key)
            print("Successfully Generated a Key")
        else:
            print("KEY IS ALL READY GENERATED USE DelKey TO DELETE IT")

def delkey():
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

def encrypt(file):
    if file not in files:
        print("File not found - Aborting encryption")  
    else:
        with open("C:/lock.key", "rb") as thekey:
            key = thekey.read()
            with open(file, "rb") as thefile:
                contents = thefile.read()
                try:
                    contents_enc = Fernet(key).encrypt(contents)
                except Fernet.ValueError:
                    print("MissingKey - Please regenerate")
            with open(file, "wb") as thefile:
                thefile.write(contents_enc)
        print("")
        print("Successfully Encrypted File " + file)

def decrypt(file):
    if file not in files:
        print("File not found - Aborting encryption")
    else:  
        with open("C:/lock.key", "rb") as dec_key:
            key = dec_key.read()
            with open(file, "rb") as enc_file:
                enc_contents = enc_file.read()
                try:
                    dec_contents = Fernet(key).decrypt(enc_contents)
                except Fernet.ValueError:
                    print("MissingKey - Please regenerate")
            with open(file, "wb") as dec_file:
                dec_file.write(dec_contents)
        print("")
        print("Succesfully Decrypted File " + file)

def delkey():
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

def scan(visible):
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
    if visible == True:
        if files == empty:
            print("Found 0 .txt files use cd to change location")
            print("")
        else:
            print("Found files:")
            print(" ".join(files))
            print("")

def cat(file):
    if file not in files:
        print("File not found - Aborting encryption")  
    else:
        with open(file, "r") as thefile:
            contents = thefile.read()
        print("")
        print("contents of " + file)
        print("")
        print(contents)
        print("")


# Startup Seq

# Logo
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

#1st File Scan
scan(True)


# Main Loop
while True:
    command = input("> ").split(maxsplit=1)

#Encryption and Decryption
    if command[0] == "encrypt":
        if len(command) >= 2:
            if command[1] in files:
                command[1] = file
                encrypt(str(file))
            if command[1] == "all":
                for file in files:
                    encrypt(file)
            print("Successfully Encrypted All Files")
        else:
            # no directory provided
            print("Usage: encrypt 'file name'")

    elif command[0] == "decrypt":
        if len(command) >= 2:
            if command[1] in files:
                command[1] = file
                decrypt(str(file))
            if command[1] == "all":
                for file in files:
                    decrypt(file)
            print("Successfully Decrypted All Files")
        else:
            # no directory provided
            print("Usage: decrypt 'file name'")
            

#Key Handling
    elif command[0] == "genkey":
        genkey()
    
    elif command[0] == "delkey":
        delkey()
        
#Filesystem Navigation & Selection
    elif command[0] == "scan":
        if len(command) >= 2:
            if command[1] == "show" or "s":
                scan(True)
            else:
                scan(False)
        else:
            scan(False)

    elif command[0] == "files":
        print("")
        print("Found files:")
        print(" ".join(files))
        print("")
    
    elif command[0] == "ls":
        print("")
        print(" ".join(os.listdir()))
        print("")

    elif command[0] == "cd":
        if len(command) < 2:
            # no directory provided
            print("")
            print("Usage: cd \"directory name\"")
            print("")
            continue
        directory = command[1].replace('"' or "'", "")
        try:
            os.chdir(directory)
            scan(False)
        except OSError:
            print("")
            print("Didnt find that reverting")
            print("")
#Utills
    elif command[0] == "quit":
        break

    elif command[0] == "help":
        print("")
        print("genkey - to generate key")
        print("encrypt - to encrypt detected files")
        print("decrypt - to decrypt detected files")
        print("delKey -  to delete current key")
        print("scan - to scan current location for .txt files")
        print("cd - to change current location")
        print("ls - list current directory contains")
        print("files - list found files elegible for encryption")
        print("cat - check contents of files elegible for encryption")
        print("")

    elif command[0] == "cat":
        if len(command) >= 2:
            if command[1] in files:
                cat(command[1])
        else:
            # no directory provided
            print("Usage: cat 'file name'") 

    else:
        print("")
        print("Unknown Command - Try: Help")