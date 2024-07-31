from tkinter import *
import tkinter.messagebox as tmsg
from tkinter.filedialog import askopenfilename, asksaveasfilename
import os

def newFile():
    global file
    root.title("Untitled - Notepad")
    file = None
    TextArea.delete(1.0,END)   

def openFile():
    global file
    file = askopenfilename(defaultextension = ".txt", filetypes = [("All Files", "*.*"), ("Text Documents", "*.txt")])

    if file=="":
        file = None
    else:
        root.title(os.path.basename(file) + "- Notepad")
        TextArea.delete(1.0,END)
        f= open(file, "r")
        TextArea.insert(1.0, f.read())   
        f.close()

def saveFile():
    global file
    if file==None:
        file = asksaveasfilename(initialfile = "Untitled.txt", 
        defaultextension = ".txt", filetypes = [("All Files", "*.*"), ("Text Documents", "*.txt")])

        if file=="":
            file = None
        else:
            #save as a new file
            f = open(file, "w")
            f.write(TextArea.get(1.0, END))
            f.close()

            root.title(os.path.basename(file) + "- Notepad")
            print("File saved")

    else:
        #save the file
        f = open(file, "w")
        f.write(TextArea.get(1.0, END))
        f.close()

def quitApp():
    root.destroy()

def cut():
    TextArea.event_generate("<<Cut>>")

def copy():
    TextArea.event_generate("<<Copy>>")

def paste():
    TextArea.event_generate("<<Paste>>")

def about():
    tmsg.showinfo("NOTEPAD", "Notepad by UJJU")  


if __name__=="__main__":
    #basic tkinter setup
    root = Tk()
    root.title("Untitled - Notepad")

    root.geometry("430x525")

    #textarea
    TextArea = Text(root, font="lucida 9")
    file = None
    TextArea.pack(expand=True, fill = BOTH)

    #create menubar
 
    ''''''''''''''''''''''''''''''''''''''''''''''File menu starts'''
    MenuBar = Menu(root) 
    FileMenu = Menu(MenuBar, tearoff = 0)
    #open new file
    FileMenu.add_command(label="New", command= newFile)
    #to open already existing file
    FileMenu.add_command(label="Open", command= openFile)
    #save the current file
    FileMenu.add_command(label="Save", command= saveFile)

    FileMenu.add_separator()
    FileMenu.add_command(label="Exit", command = quitApp)
    MenuBar.add_cascade(label = "File", menu=FileMenu)  

    '''''''''''''''''''''''''''''''''''''''''''''''''File menu ends'''

    '''''''''''''''''''''''''''''''''''''''''''''''''Edit menu starts'''
    
    EditMenu = Menu(MenuBar, tearoff=0)

    #give feature of cut, copy and paste
    EditMenu.add_command(label="Cut", command=cut)
    EditMenu.add_command(label="Copy", command=copy)
    EditMenu.add_command(label="Paste", command=paste)

    MenuBar.add_cascade(label="Edit", menu=EditMenu)

    '''''''''''''''''''''''''''''''''''''''''''''''''''Edit menu ends'''

    '''''''''''''''''''''''''''''''''''''''''''''''''''Help menu starts'''

    HelpMenu = Menu(MenuBar, tearoff=0)

    HelpMenu.add_command(label="About", command = about)

    MenuBar.add_cascade(label="Help", menu= HelpMenu)

    '''''''''''''''''''''''''''''''''''''''''''''''''''''''''Help menu ends'''

    root.config(menu=MenuBar)

    #adding scrollbar
    scrollbar = Scrollbar(TextArea)
    scrollbar.pack(side=RIGHT, fill=Y)
    scrollbar.config(command=TextArea.yview)
    TextArea.config(yscrollcommand = scrollbar.set)


    root.mainloop()