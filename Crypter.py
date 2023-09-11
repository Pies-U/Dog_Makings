import tkinter as tk
import tkinter.scrolledtext as st
import rsa

# Public Key Generation
publickey, privatekey = rsa.newkeys(1024)
publickey = publickey.save_pkcs1("PEM")
privatekey = privatekey.save_pkcs1("PEM")


def encrypt():
    encrypted_text.delete("1.0", tk.END)
    encrypted_text.insert("1.0", rsa.encrypt(to_encrypt.get("1.0", "end-1c").encode(), rsa.PublicKey.load_pkcs1(recipientkey.get("1.0", "end-1c").encode())).hex())

def decrypt():
    decrypted_text.delete("1.0", tk.END)
    decrypted_text.insert("1.0", rsa.decrypt(bytes.fromhex(to_decrypt.get("1.0", "end-1c")), rsa.PrivateKey.load_pkcs1(privatekey)).decode())

root = tk.Tk()
root.geometry('700x640')
root.title('CrypTer Build 1.0')
root.resizable(0, 0)

# Frames Define
encryptside = tk.LabelFrame(root, text='Encrypt', bg='LightGrey', width=350, height=440)
encryptside.place(x=0, y=0)

decryptside = tk.LabelFrame(root, text='Decrypt', bg='slategray')
decryptside.place(x=350, y=0, height=440, width=350)

keystorage = tk.LabelFrame(root, text="Key Storage", bg='#212121',)
keystorage.place(x=0, y=440, height=300, width=700)

# Key storage content
yourkey = st.ScrolledText(keystorage, background="white")
yourkey.place(x=2, y=2, height=180, width=320)
yourkey.insert("end", publickey)

recipientkey = st.ScrolledText(keystorage, background="white")
recipientkey.place(x=350, y=2, height=180, width=320)

# Encrypt side content
to_encrypt = st.ScrolledText(encryptside, background="gray")
to_encrypt.place(x=2, y=2, height=180, width=320)

encrypt_button = tk.Button(encryptside, background="lightgray", text="Encrypt", command=lambda: encrypt())
encrypt_button.place(x=100, y=185, width=100, height=40)

encrypted_text = st.ScrolledText(encryptside, background="gray")
encrypted_text.place(x=2, y=230, height=180, width=320)

# Decrypt side content
to_decrypt = st.ScrolledText(decryptside, background="gray")
to_decrypt.place(x=2, y=2, height=180, width=320)

decrypt_button = tk.Button(decryptside, background="lightgray", text="Decrypt", command=lambda: decrypt())
decrypt_button.place(x=100, y=185, width=100, height=40)

decrypted_text = st.ScrolledText(decryptside, background="gray")
decrypted_text.place(x=2, y=230, height=180, width=320)

root.mainloop()