from tkinter import *
import time
root = Tk()
root.geometry("500x300")

emptyStr = ""
counter = 0
ldata = IntVar()
pompki = IntVar()
powod = StringVar()
lerror = StringVar()


def Error(message):
    time.sleep(0.1)
    lerror.set(str(message))
    time.sleep(0.5)
    print(lerror.get())

def ErrorCancel():
    time.sleep(0.5)
    print("error cancel active")
    lerror.set("")


def LabelAdd(value):
    x = ldata.get()
    ldata.set(x+value)

def LabelSet(value):
    ldata.set(value)

def FormSubmit():
    #Import Form
    powodTemp = powod.get()
    try:
        pompkiTemp = pompki.get()
    except TclError:
        Error("Pompki muszą być liczbą")
    #Errors 
    if pompkiTemp > 20:
        Error("Pompki > 20")
    elif powodTemp == emptyStr:
        Error("Powód Empty")
    else:
        LabelAdd(pompkiTemp)
        print(powodTemp)
        print(pompkiTemp)
        ErrorCancel()
    
    


def Debug():
    print()

#FrontEnd

#Buttons
Debug()

b1 = Button(root, text="  +1 Pompka  ", command=lambda: LabelAdd(1), justify='center').grid(row=2, column=0)

b2 = Button(root, text="  +3 Pompka  ", command=lambda: LabelAdd(3), justify='center').grid(row=3, column=0)

b3 = Button(root, text="Reset", command=lambda: LabelSet(0)).grid(row=1, column=3)

b4 = Button(root, text="Dodaj", command=lambda: FormSubmit()).grid(row=4, column=6)

#Labels
l1 = Label(root, textvariable=ldata).grid(row=1, column=2)

l2 = Label(root, text="Pompki:").grid(row=1, column=1)

l3 = Label(root, text="Dodaj Własne:").grid(row=2, column=4)

l4 = Label(root, text="Pompki:").grid(row=3, column=3)

l5 = Label(root, text="Powód:").grid(row=4, column=3)

l6 = Label(root, text="Max 20").grid(row=3, column=5)

l7 = Label(root, textvariable=lerror).grid(row=5, column=3)

#Entries
entry1 = Entry(root, textvariable=pompki).grid(row=3, column=4) #Pompki
entry2 = Entry(root, textvariable=powod).grid(row=4, column=4) #Powód

root.mainloop()