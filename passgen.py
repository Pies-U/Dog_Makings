from random import shuffle


def genpass(size):
    # Imports
    import random
    import string

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
    
