from tkinter import *
import time
import keyboard
import os
root = Tk()
root.title("PushUp Counter")
#root.iconbitmap("C:/icon.ico")   
root.geometry("430x130")

#ToDo V2
#Grafika
#Logo
#Gui
#LogOnSite

#ToDo V3
#Hud

emptyStr = ""
counter = 0
ldata = IntVar()
pompki = IntVar() 
powod = StringVar()
lerror = StringVar()



try:
    logFile = open("Log.txt", "x")
    logFile.close()

except FileExistsError:
    pass


with open("Log.txt", "w") as Log:
    Log.write(f'Operational log of pushup counter from: ' + str(time.asctime()))
    Log.write(os.linesep)
    Log.write("#LOG START#")



def unmap(event):
    if event.widget is root:
        root.deiconify()

def AddToLog(func_name):
    with open("Log.txt", "a") as Log:
        Log.write(os.linesep)
        Log.write(f"action called - " + func_name + " - at - " + str(time.asctime()))

def Error(message):
    time.sleep(0.1)
    lerror.set(str(message))
    time.sleep(0.5)
    print(lerror.get())
    AddToLog("Error " + message)    

def ErrorCancel():
    time.sleep(0.5)
    print("error cancel active")
    lerror.set("")
    AddToLog("Error Cancel Active") 

def LabelAdd(value):
    x = ldata.get()
    ldata.set(x+value)
    AddToLog("Added to label Pompki " + str(value)) 

def LabelSet(value):
    ldata.set(value)
    AddToLog("Set new label for Pompki " + str(value)) 

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
        AddToLog(f"Subbmited Add Form For " + str(pompkiTemp) + " with " + powodTemp) 

def HotKeyStroke(Amount):
    if Amount == 1:
        LabelAdd(1)
        Type = "ctrl+alt+p"
    elif Amount == 5:
        LabelAdd(5)
        Type = "ctrl+alt+l"
    AddToLog(f"HotKeyStroke "+str(Amount)+" "+Type+" "+str(time.asctime()))
 
#FrontEnd

#Buttons

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

#root.protocol('WM_DELETE_WINDOW', lambda: None)  # prevent closing
root.bind('<Unmap>', unmap)  # redisplay window when it's minimized
root.resizable(False, False)
keyboard.add_hotkey("ctrl+alt+p",lambda: HotKeyStroke(1))
keyboard.add_hotkey("ctrl+alt+l",lambda: HotKeyStroke(5))
root.mainloop()