from Tkinter import *
from Objects import *
import tkSimpleDialog
import tkFileDialog
import os.path

# Creates a new entry on the framework list

class Framework(Frame):
        
        def __init__(self):
                global row
                self.components = []
                self.axis = None

                # Setting frame properties
                Frame.__init__(self)
                self.master.title("Framework")
                self.master.geometry("450x600")
                self.grid()
                self.grid_rowconfigure(0, minsize = 500)

                # Creating data pane for user entry and buttons
                self.datapane = Frame(self, height = 500)
                self.buttonPane = Frame(self)

                # Creating buttons
                self.addButton = Button(self.buttonPane, text = "Add row", command = self.addRow)
                self.subButton = Button(self.buttonPane, text = "Remove row", command = self.subRow)
                self.createButton = Button(self.buttonPane, text = "Create Program", command = self.create)
                self.addGraphButton = Button(self.buttonPane, text = "Add a graph", command = self.addGraph)
                self.blank = Label(self.buttonPane, text = " ")
                self.addButton.grid(row = 0, column = 2, padx = 5, sticky = E)
                self.subButton.grid(row = 0, column = 3, padx = 5, sticky = E)
                self.createButton.grid(row = 0, column = 4, padx = 5, sticky = E)
                self.addGraphButton.grid(row = 0, column = 0, padx = 5, sticky = W)
                self.blank.grid(column = 1, padx = 25)

                self.components.append(listComponent(self.datapane, row))
                row += 1
                self.datapane.grid(sticky = N, padx = 20, pady = 5)
                self.buttonPane.grid(padx = 20, pady = 45, sticky = S)

        def addRow(self):
                global row
                self.components.append(listComponent(self.datapane, row))
                row += 1

        def subRow(self):
                global row
                self.components[-1].delete()
                self.components.pop(-1)
                row -= 1

        def create(self):
                finalInfo = []
                for x in range(len(self.components)):
                        tempList = [self.components[x].getLabel(), self.components[x].getType()]
                        finalInfo.append(tempList)
                finalInfo.append(self.axis)
                in_path = save()
                pro_path = in_path + '.py'
                for_path = os.path.dirname(pro_path) + '/Formula.py'
                if (pro_path != '.py'):
                        programFile = open(pro_path, 'w')
                        formulaFile = open(for_path, 'w')
                        comString = str(finalInfo)
                        comString = comString.strip()
                        program = 'input = ' + comString + getProgram() + '\n'
                        formula = getFormula()
                        programFile.write(program)
                        formulaFile.write(formula)
                
        def addGraph(self):
                d = MyDialog(self)
                self.axis = d.result
                
                
                
# Initializing global variable for row formation
row = 1

# Running GUI
Framework().mainloop()

