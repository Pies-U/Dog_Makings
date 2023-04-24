import time
def changeline(msg):
    print("Kij")
    print(f'{msg}', end='\r')
    time.sleep(1)


time.sleep(1)
changeline("hello")