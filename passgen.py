import random
import string

def genpass(size):
    # Defines
    password = ""
    chars = list(string.ascii_letters+string.digits+string.punctuation)

    # Work
    while size > 1:
        password += random.choice(chars)
        size -= 1

    # Returns    
    return password


print(genpass(15))
    
