import rsa

try:
    with open("private.pem","rb") as f:
        privatekey = f.read()

except FileNotFoundError:
    print("KeysFileDoesNotExist")

#Keys validation
if privatekey == " " or privatekey == "":
    print("KeyError")


def decrypt(to_decrypt):
    print()
    print(rsa.decrypt(bytes.fromhex(to_decrypt), rsa.PrivateKey.load_pkcs1(privatekey)).decode())


decrypt(input("> "))