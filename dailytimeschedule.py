from tkinter import *
from tkinter import ttk
import tkinter.font as font
from settings import *

class DailyTimeSchedule:
    def __init__(self, frame, day, busyHours):
        #self.parent = parent
        self.dayFrame = frame
        self.busyHours= busyHours
        self.make_labels()
        self.make_busy_day()
       
        
    def make_busy_day(self):
        for period in self.busyHours:
            Frame(self.dayFrame,height=20,width=self.find_width(period),
                  bg='red').place(x=self.find_x(period),y = 20)
        
    def find_x(self,period):
        hour1=period[0][0]
        section1 = period[0][1]
        x=0
                
        if section1 == 'pm':
            if hour1 < 12:
                hour1+=12
        if section1 == 'am' and hour1 == 12:
            hour1 += 12
        x+=(24*hour1)
        return x-24
    
    def find_width(self,period):
        hour1=period[0][0]
        section1 = period[0][1]
        hour2=period[1][0]
        section2 = period[1][1]
        w=0
        if section1 == 'pm':
            if hour1 < 12:
                hour1+=12
        if section1 == 'am' and hour1 == 12:
            hour1 += 12
            
        if section2 == 'pm':
            if hour2 < 12:
                hour2+=12
        if section2 == 'am' and hour2 == 12:
            hour2 += 12
        w+= (24*(hour2-hour1))
        return int(w)
    
    def make_labels(self):
        for i in range(24):
            if i < 12:
                Label(self.dayFrame,text=i+1).place(x=i*24)
            else:
                Label(self.dayFrame,text=i-11).place(x=i*24)
            
