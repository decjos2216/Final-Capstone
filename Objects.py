from Tkinter import *
from Objects import *
import tkSimpleDialog
import tkFileDialog
import os.path

# listComponent creates an object that contains a Label, Text Entry, and
# Option Menu. This is to be used by the Framework program to create fields
# for user input.

class listComponent(object):

    def __init__(self, target, rowNum):
        # Creating label
        self.labelTag = Label(target, text = "Label Text: ")
        self.labelTag.grid(row = rowNum, column = 1, padx = 5)

        # Creating label input
        self.textVar = StringVar()
        self.textEntry = Entry(target, textvariable = self.textVar)
        self.textEntry.grid(row = rowNum, column = 2, padx = 5)

        # Creating data type dropdown list
        self.listVar = StringVar()
        self.dataTypeList = OptionMenu(target, self.listVar, "String", "Numbers")
        self.dataTypeList.config(width = 10)
        self.dataTypeList.grid(row = rowNum, column = 3, padx = 5)

    def getLabel(self):
        return self.textVar.get()

    def getType(self):
        return self.listVar.get()

    def delete(self):
        self.labelTag.destroy()
        self.textEntry.destroy()
        self.dataTypeList.destroy()

class listInputs(object):

    def __init__(self, target, data, rowNum):
        # Creating flag for number only inputs
        self.numOnly = data[1]
        
        # Creating label
        self.label = Label(target, text = data[0])
        self.label.grid(row = rowNum, padx = 5, sticky = W)

        # Creating label input
        self.inputVar = StringVar()
        self.entry = Entry(target, textvariable = self.inputVar)
        self.entry.grid(row = rowNum, column = 1, padx = 5)

    def getData(self):
        return self.inputVar.get()

    def getType(self):
        return self.numOnly

    def deleteData(self):
        self.entry.delete(0, 'end')

    def highlightRed(self):
        self.entry.configure(bg = 'red')

    def highlightWhite(self):
        self.entry.configure(bg = 'white')
    
        
# MyDialog creates a small pop up window to gather the axis labels for the graph
class MyDialog(tkSimpleDialog.Dialog):

    def body(self, master):

        Label(master, text="X Axis Label:").grid(row=0)
        Label(master, text="Y Axis Label:").grid(row=1)

        self.e1 = Entry(master)
        self.e2 = Entry(master)

        self.e1.grid(row=0, column=1)
        self.e2.grid(row=1, column=1)
        return self.e1 # initial focus

    def apply(self):
        first = self.e1.get()
        second = self.e2.get()
        self.result = [first, second]

# Creates a pop up window to get a file path for file writing
def save():
    Tk().withdraw()
    in_path = tkFileDialog.asksaveasfilename()
    return in_path

def getProgram():
    f = open("proFile.file", 'r')
    return f.read()

def getFormula():
    f = open("formFile.file", 'r')
    return f.read()










