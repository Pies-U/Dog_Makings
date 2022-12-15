from tkinter import *
root = Tk()
root.geometry("800x600")

#variable is stored in the root object
root.counter = 0

def clicked(click_value):
    root.counter += click_value
    L['text'] = 'Button clicked: ' + str(root.counter)
        
b1 = Button(root, text="+1 Pompka", command=clicked)
b1.pack()

b2 = Button(root, text="+3 Pompki ", command=clicked)
b2.pack()

b3 = Button(root, text="+5 Pompki ", command=clicked)
b3.pack()

L = Label(root, text="No clicks yet.")
L.pack()

root.mainloop()