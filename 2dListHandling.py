playboard = [
             ["x","o","x"],
             ["o","x","o"],
             ["x","o","x"],
            ]

def printBoard():
    print("")
    for i in playboard:
        for j in i:
            print(j, end=" ")
        print("")
    print("")

def write(x, y, value):
    try:
        playboard[x][y] = value    
    except ValueError:
        print("Argument 1 or 2 out of range")
    except TypeError:
        print("Argument 1 and 2 must be INT")   

while True:
    command = input("> ").split()
    while True:
        if command[0] == "print":
            printBoard() 
    
        if command[0] == "write":
            if len(command) > 1:
                write(command[1],command[2],command[3])

        if command[0] == "quit":
            break
    
