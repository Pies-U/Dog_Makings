import rsa

def genkyes(length):
    publickey,privatekey = rsa.newkeys(int(length))
    with open("public.pem", "wb") as f:
        f.write(publickey.save_pkcs1("PEM"))

    with open("private.pem", "wb") as f:
        f.write(privatekey.save_pkcs1("PEM"))

genkyes(input("KeyLength (1024 or 2048[Recommened])> "))
