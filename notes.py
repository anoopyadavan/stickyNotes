#! /usr/bin/python3

import tkinter
import os
import subprocess
from plyer import notification  
from time import ctime


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
    user_name=str(subprocess.check_output("whoami"))[2:-3]
    file="/home/"+user_name+"/.stickyNotes.txt"
    def saveFile():
        #os.system("touch {var}".format(var=user_name))
        #file="/home/anoop/stickyNotes.txt"
        f=open(file,"w")
        f.write(TextArea.get(1.0,END))
        f.close()

    def openFile():
        if not os.path.isfile(file):
            os.system("touch {var}".format(var=file))
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
    os.system("./notify_me.py &")
    TextArea.pack(fill=BOTH)
    root.mainloop()
    os.system("kill `pgrep notify_me.py`")
