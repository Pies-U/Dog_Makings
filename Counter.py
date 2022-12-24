from tkinter import *
root = Tk()
root.geometry("800x600")

#variable is stored in the root object
root.counter = 0

def clicked1(): 
    root.counter += 1
    L['text'] = 'Button clicked: ' + str(root.counter)
def clicked2():
    root.counter += 3
    L['text'] = 'Button clicked: ' + str(root.counter)
def clicked3():
    root.counter += 5
    L['text'] = 'Button clicked: ' + str(root.counter)
def zero():
    root.counter = 0
    L['text'] = 'Button clicked: ' + str(root.counter)





b1 = Button(root, text="  +1 Pompka  ", command=clicked1)
b1.pack()

b2 = Button(root, text="  +3 Pompki   ", command=clicked2)
b2.pack()

b3 = Button(root, text="  +5 Pompki   ", command=clicked3)
b3.pack()

b4 = Button(root, text="Zeruj pompki ", command=zero)
b4.pack()

L = Label(root, text="Nie przypisano pompek")
L.pack()

root.mainloop()