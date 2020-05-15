from tkinter import *
from tkinter import ttk
import tkinter.font as font
from settings import *
from addevent import *

class ScheduleTab:
    def __init__(self, parent, frame):
        self.parent = parent
        self.scheduleFrame = frame
        self.make_schedule()
        
    def make_schedule(self):
        myFont = font.Font(size = 10, weight='bold')
        self.btn1 = Button(self.scheduleFrame, text='New Event', font=myFont,
                           command = lambda : [self.open_event_window()])
        self.btn1.place(x=SCREENWIDTH-90,y=SCREENHEIGHT-75)
    def open_event_window(self):
        #disable btn1
        self.btn1['state'] = 'disabled'
        self.eventWindow = AddEventWindow(self)
        
    def close_event_window(self):
        #release interaction lock
        self.eventWindow.window.grab_release()
        #close the window
        self.eventWindow.window.destroy()
        #set btn1 bakc to normal
        self.btn1['state'] = 'normal'
