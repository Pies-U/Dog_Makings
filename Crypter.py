import tkinter as tk
import tkinter.scrolledtext as st
import rsa
from cryptography.fernet import Fernet

# Local Keys Loading
try:
    with open("public.pem","rb") as f:
        publickey = f.read()

    with open("private.pem","rb") as f:
        privatekey = f.read()

except FileNotFoundError:
    print("KeysFileDoesNotExist")

#Symetric Key Genereation

symetrickey = Fernet.generate_key()

#Keys validation
if publickey == " " or publickey == "" or privatekey == " " or privatekey == "":
    print("KeyError")

def AsymetricEncryptionFunc():
    AsymetricEncryptedText.delete("1.0", tk.END)
    AsymetricEncryptedText.insert("1.0", rsa.encrypt(AsymetricToEncrypt.get("1.0", "end-1c").encode(), rsa.PublicKey.load_pkcs1(recipientkey.get("1.0", "end-1c").encode())).hex())

def AsymetricDecryptionFunc():
    AsymetricDecryptedText.delete("1.0", tk.END)
    AsymetricDecryptedText.insert("1.0", rsa.decrypt(bytes.fromhex(AsymetricToDecrypt.get("1.0", "end-1c")), rsa.PrivateKey.load_pkcs1(privatekey)).decode())

def SymetricEncrpytionFunc():
    SymetricOutput.delete("1.0", tk.END)
    SymetricOutput.insert("1.0", Fernet(bytes.fromhex(aeskey.get("1.0","end-1c"))).encrypt(SymetricInput.get("1.0", "end-1c").encode()).hex())

def SymetricDecrpytionFunc():
    SymetricOutput.delete("1.0", tk.END)
    SymetricOutput.insert("1.0",Fernet(bytes.fromhex(aeskey.get("1.0","end-1c"))).decrypt(bytes.fromhex(SymetricInput.get("1.0", "end-1c"))).decode())

root = tk.Tk()
root.geometry('1050x640') # width x height
root.title('CrypTer Cryptography Toolkit')
root.resizable(0,0)

# Frames Define
AsymetricEncryptionPage = tk.LabelFrame(root, text='Asymetric Encryption', bg='LightGrey', width=350, height=440)
AsymetricEncryptionPage.place(x=0, y=0)

AsymetricDecryptionPage = tk.LabelFrame(root, text='Asymetric Decryption', bg='slategray')
AsymetricDecryptionPage.place(x=350, y=0, height=440, width=350)

KeyStoragePage = tk.LabelFrame(root, text="Key Storage", bg='#212121',)
KeyStoragePage.place(x=0, y=440, height=300, width=1050)

SymetricEncryptionPage = tk.LabelFrame(root, text="SYMETRIC CRYPTOGRAPHY",bg="#D0021B")
SymetricEncryptionPage.place(x=700, y=0, width=350, height=440)

# Key Storage Page Content
yourkey = st.ScrolledText(KeyStoragePage, background="white")
yourkey.place(x=2, y=2, height=180, width=320)
yourkey.insert("end", publickey)

recipientkey = st.ScrolledText(KeyStoragePage, background="white")
recipientkey.place(x=350, y=2, height=180, width=320)

aeskey = st.ScrolledText(KeyStoragePage, background="white")
aeskey.place(x=702, y=2, height=180, width=320)
aeskey.insert("end", symetrickey.hex())

# Asymetric Encryption Page Content
AsymetricToEncrypt = st.ScrolledText(AsymetricEncryptionPage, background="gray")
AsymetricToEncrypt.place(x=2, y=2, height=180, width=320)

AsymetricEncryptButton = tk.Button(AsymetricEncryptionPage, background="lightgray", text="Encrypt", command=lambda: AsymetricEncryptionFunc())
AsymetricEncryptButton.place(x=100, y=185, width=100, height=40)

AsymetricEncryptedText = st.ScrolledText(AsymetricEncryptionPage, background="gray")
AsymetricEncryptedText.place(x=2, y=230, height=180, width=320)

# Asymetric Decryption Page Content
AsymetricToDecrypt = st.ScrolledText(AsymetricDecryptionPage, background="gray")
AsymetricToDecrypt.place(x=2, y=2, height=180, width=320)

AsymetricDecrpytButton = tk.Button(AsymetricDecryptionPage, background="lightgray", text="Decrypt", command=lambda: AsymetricDecryptionFunc())
AsymetricDecrpytButton.place(x=100, y=185, width=100, height=40)

AsymetricDecryptedText = st.ScrolledText(AsymetricDecryptionPage, background="gray")
AsymetricDecryptedText.place(x=2, y=230, height=180, width=320)

# Symetric Encrypyion Page Conetent

SymetricInput = st.ScrolledText(SymetricEncryptionPage, background="gray")
SymetricInput.place(x=2, y=2, height=180, width=320)

SymetricEncryptButton = tk.Button(SymetricEncryptionPage, background="lightgray", text="Encrypt", command=lambda: SymetricEncrpytionFunc())
SymetricEncryptButton.place(x=50, y=185, width=100, height=40)

SymetricDecryptButton = tk.Button(SymetricEncryptionPage, background="lightgray", text="Decrypt", command=lambda: SymetricDecrpytionFunc())
SymetricDecryptButton.place(x=175, y=185, width=100, height=40)

SymetricOutput = st.ScrolledText(SymetricEncryptionPage, background="gray")
SymetricOutput.place(x=2, y=230, height=180, width=320)

root.mainloop()