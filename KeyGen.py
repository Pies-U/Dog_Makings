import rsa

def genkyes():
    publickey,privatekey = rsa.newkeys(1024)
    with open("public.pem", "wb") as f:
        f.write(publickey.save_pkcs1("PEM"))
    
    with open("private.pem", "wb") as f:
        f.write(privatekey.save_pkcs1("PEM"))

genkyes()