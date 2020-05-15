from tkinter import *
from tkinter import ttk
import tkinter.font as font
from settings import *
from addevent import *
from dailytimeschedule import *

class ScheduleTab:
    def __init__(self, parent, frame):
        self.parent = parent
        self.scheduleFrame = frame
        self.make_schedule_widgets()
        
    def make_schedule_widgets(self):
        myFont = font.Font(size = 10, weight='bold')
        self.btn1 = Button(self.scheduleFrame, text='New Event', font=myFont,
                           command = lambda : [self.open_event_window()])
        self.btn1.place(x=SCREENWIDTH-90, y = 10)
        
        self.frame1 = Frame(self.scheduleFrame, width=576, height=40)
        sunBusyTimes= [[[1,'pm'],[3,'pm']],[[5,'pm'],[6,'pm']]]
        self.sunday = DailyTimeSchedule(self.frame1, 'Sunday', sunBusyTimes)
        self.frame1.pack(side=BOTTOM,padx = 20,pady=10)
        Label(self.scheduleFrame,text='Sun', font=myFont).place(x=15,y=420)
        
        self.frame2 = Frame(self.scheduleFrame, width=576, height=40)
        satBusyTimes= [[[11,'am'],[5,'pm']],[[7,'pm'],[10,'pm']]]
        self.sunday = DailyTimeSchedule(self.frame2, 'Saturday', satBusyTimes)
        self.frame2.pack(side=BOTTOM,padx = 20,pady=10)
        Label(self.scheduleFrame,text='Sat', font=myFont).place(x=15,y=360)
        
        self.frame3 = Frame(self.scheduleFrame, width=576, height=40)
        friBusyTimes= [[[12,'pm'],[2,'pm']],[[9,'pm'],[12,'am']]]
        self.friday = DailyTimeSchedule(self.frame3, 'Friday', friBusyTimes)
        self.frame3.pack(side=BOTTOM,padx = 20,pady=10)
        Label(self.scheduleFrame,text='Fri', font=myFont).place(x=15,y=300)
        
        self.frame4 = Frame(self.scheduleFrame, width=576, height=40)
        thuBusyTimes= [[[2,'pm'],[6,'pm']],[[8,'am'],[10,'am']]]
        self.thursday = DailyTimeSchedule(self.frame4, 'Thursday', thuBusyTimes)
        self.frame4.pack(side=BOTTOM,padx = 20,pady=10)
        Label(self.scheduleFrame,text='Thu', font=myFont).place(x=15,y=240)
        
        self.frame5 = Frame(self.scheduleFrame, width=576, height=40)
        wedBusyTimes= [[[7,'am'],[11,'am']],[[8,'pm'],[9,'pm']]]
        self.wednesday = DailyTimeSchedule(self.frame5, 'Wednesday', wedBusyTimes)
        self.frame5.pack(side=BOTTOM,padx = 20,pady=10)
        Label(self.scheduleFrame,text='Wed', font=myFont).place(x=15,y=180)
        
        self.frame6 = Frame(self.scheduleFrame, width=576, height=40)
        tueBusyTimes= [[[1,'pm'],[3,'pm']],[[5,'pm'],[6,'pm']]]
        self.tuesday = DailyTimeSchedule(self.frame6, 'Tuesday', tueBusyTimes)
        self.frame6.pack(side=BOTTOM,padx = 20,pady=10)
        Label(self.scheduleFrame,text='Tue', font=myFont).place(x=15,y=120)
        
        self.frame7 = Frame(self.scheduleFrame, width=576, height=40)
        monBusyTimes= [[[12,'pm'],[3,'pm']],[[4,'pm'],[5,'pm']]]
        self.monday = DailyTimeSchedule(self.frame7, 'Monday', monBusyTimes)
        self.frame7.pack(side=BOTTOM,padx = 20,pady=10)
        Label(self.scheduleFrame,text='Mon', font=myFont).place(x=15,y=60)
        
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
