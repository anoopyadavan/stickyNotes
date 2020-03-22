#! /usr/bin/python3

import tkinter
import os
from tkinter.messagebox import showinfo    # for notification
from tkinter.filedialog import askopenfilename

from tkinter import *
if __name__=='__main__':
    # basics tkinter setup
    root = Tk()
    root.resizable(0,0)
    root.title("anoop notes")
    root.geometry("500x300")
    #root.iconbitmap('taskbar.png')
    #Add TextArea
    TextArea = Text(root, font="lucida 13",bg="yellow")
    file =None
    # lets create a menubar
    MenuBar=Menu(root)
    FileMenu = Menu(MenuBar,tearoff=0)
    file="/home/anoop/stickyNotes.txt"
    def saveFile():
        os.system("touch /home/anoop/stickyNotes.txt")
        #file="/home/anoop/stickyNotes.txt"
        f=open(file,"w")
        f.write(TextArea.get(1.0,END))
        f.close()

    def openFile():
        f=open(file,"r")
        TextArea.insert(1.0,f.read())
        f.close()

    #to save the current file
    FileMenu.add_command(label="Save",command = saveFile)
    FileMenu.add_separator()
    MenuBar.add_cascade(label="File",menu=FileMenu)
    root.config(menu=MenuBar)

    # showinfo("Anoop","Hello lexie welcome")    // to show the notification

    # root.destroy()   // to quit from application
    openFile()
    TextArea.pack(fill=BOTH)
    root.mainloop()

