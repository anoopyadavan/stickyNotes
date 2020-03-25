#!/usr/bin/python3

from plyer import notification
from time import ctime
from time import sleep
import subprocess

# notification
user_name=str(subprocess.check_output("whoami"))[2:-3]
file="/home/"+user_name+"/.stickyNotes.txt"
def notification_(file):
    f = open(file)
    for line in f:
        fields = line.strip().split()
        if(len(fields)==0):
            break
        else:
            fields=fields[0].split(":")
            cur_time=list(ctime().split(" ")[3].split(":"))
            if(fields[0]==cur_time[0] and fields[1]==cur_time[1]):
                notification.notify("Notification","You have sheduled somethings see the notes")
                sleep(58)
    f.close()


while(True):
    notification_(file)
