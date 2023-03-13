x_turn = False
o_turn = True
turn = ""

if o_turn == True:
    turn = "o"

elif o_turn == False:
    turn = "x"

playboard = [
             ["||","||","||"],
             ["||","||","||"],
             ["||","||","||"],
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
    printBoard()
    print("Its " + turn + " turn")
    command = input("X and Y cords > ").split()
    if command[2] == "X" or "Y":
        write(command[0],command[1],"|"+command[2]+"|")
    else:
        print("Invalid Command")