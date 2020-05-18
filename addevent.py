from tkinter import *
from tkinter import ttk
import tkinter.font as font
from settings import *

class AddEventWindow:
    def __init__(self, parent):
        self.parent = parent
        self.make_event_window()
        
    def make_event_window(self):
        #create the eventWindow
        self.window = Toplevel(self.parent.scheduleFrame)
        self.window.resizable(width=False, height=False)
        self.window.geometry('{}x{}+150+150'.format(335,200))
        #create widgets for event window
        self.make_widgets()
        #lock interaction to this window
        self.window.grab_set()
        self.window.focus_set()
        #if [x] is pressed, call close_event_window
        self.window.protocol('WM_DELETE_WINDOW', self.parent.close_event_window)
    
    def make_widgets(self):
        #name#####################################################
        myLabelFont = font.Font(size = 12)
        myEntryFont = font.Font(size = 11)
        lbl1 = Label(self.window, text='Event Name',
                     font=myLabelFont)
        lbl1.place(x=10,y=10)
        ent1 = Entry(self.window,
                     font=myEntryFont,
                     width=24)
        ent1.place(x=120,y=12)
        #date#####################################################
        lbl2 = Label(self.window, text='Date',
                     font=myLabelFont)
        lbl2.place(x=10,y=55)
        #drop down menu for MONTHS
        self.valCb1 = StringVar()
        self.cb1 = ttk.Combobox(self.window,
            values=(MONTHS),
            textvariable=self.valCb1,
            state='readonly',
            width=4,
            font=myEntryFont
        )
        self.cb1.current(0)
        self.cb1.value = self.valCb1
        self.cb1.place(x=75,y=57)
        self.cb1.bind('<<ComboboxSelected>>', self.update_days)
        #drop down menu for DAYS
        self.valCb2 = StringVar()
        self.cb2 = ttk.Combobox(self.window,
            values=(DAYS31),
            textvariable=self.valCb2,
            state='readonly',
            width=3,
            font=myEntryFont
        )
        self.cb2.current(0)
        self.cb2.value = self.valCb2
        self.cb2.place(x=170,y=57)
        #drop down menu for YEARS
        self.valCb3 = StringVar()
        self.cb3 = ttk.Combobox(self.window,
            values=(YEARS),
            textvariable=self.valCb3,
            state='readonly',
            width=5,
            font=myEntryFont
        )
        self.cb3.current(0)
        self.cb3.value = self.valCb2
        self.cb3.place(x=260,y=57)
        #time#####################################################
        lbl3 = Label(self.window, text='Time',
                     font=myLabelFont)
        lbl3.place(x=10,y=95)
        
        
        lbl4 = Label(self.window, text='to',
                     font=myLabelFont)
        lbl4.place(x=185,y=100)
        #firsthour
        self.valEnt2 = StringVar()
        self.valEnt2.trace('w', self.limit_size_ent2)
        ent2 = Entry(self.window,
                     font=myEntryFont,
                     textvariable=self.valEnt2,
                     width=3)
        ent2.place(x=75,y=100)
        #first minutes
        self.valEnt3 = StringVar()
        self.valEnt3.trace('w', self.limit_size_ent3)
        ent3 = Entry(self.window,
                     font=myEntryFont,
                     textvariable=self.valEnt3,
                     width=3)
        ent3.place(x=110,y=100)
        #first am/pm
        self.valCb6 = StringVar()
        self.cb6 = ttk.Combobox(self.window,
            values=(AMPM),
            textvariable=self.valCb6,
            state='readonly',
            width=3,
            font=myEntryFont
        )
        self.cb6.current(0)
        self.cb6.value = self.valCb6
        self.cb6.place(x=140,y=100)
          
        #second hour
        self.valEnt4 = StringVar()
        self.valEnt4.trace('w', self.limit_size_ent4)
        ent4 = Entry(self.window,
                     font=myEntryFont,
                     textvariable=self.valEnt4,
                     width=3)
        ent4.place(x=210,y=100)
        #second minutes
        self.valEnt5 = StringVar()
        self.valEnt5.trace('w', self.limit_size_ent5)
        ent5 = Entry(self.window,
                     font=myEntryFont,
                     textvariable=self.valEnt5,
                     width=3)
        ent5.place(x=245,y=100)
        #second am/pm
        self.valCb7 = StringVar()
        self.cb7 = ttk.Combobox(self.window,
            values=(AMPM),
            textvariable=self.valCb7,
            state='readonly',
            width=3,
            font=myEntryFont
        )
        self.cb7.current(0)
        self.cb7.value = self.valCb7
        self.cb7.place(x=275,y=100)
        #cancel button
        myFont = font.Font(size = 10, weight='bold')
        self.btn2 = Button(self.window, text='Cancel', font=myFont,
                           command = lambda : [self.parent.close_event_window()])
        self.btn2.place(x=15,y=160)
        
        #create button
        myFont = font.Font(size = 10, weight='bold')
        self.btn3 = Button(self.window, text='Add Event', font=myFont,
                           command = lambda : [self.parent.close_event_window()])
        self.btn3.place(x=245,y=160)
    
    #change the drop down for DAYS to reflect the MONTH
    def update_days(self,event):
        month = self.valCb1.get()
        if month == 'Feb':
            self.cb2['values'] = DAYS28
        elif month == 'Apr' or month == 'Jun' or month == 'Sep' or month == 'Nov':
            self.cb2['values'] = DAYS30
        else:
            self.cb2['values'] = DAYS31
        #if selected DAY is not in the MONTH, change DAY
        if self.valCb2.get() not in self.cb2['values']:
            self.cb2.current(len(self.cb2['values'])-1)
            
    def limit_size_ent2(self,*args):
        value = self.valEnt2.get()
        if value.isdigit() == False:
            self.valEnt2.set('')
        else:
            if len(value) > 2:
                self.valEnt2.set(value[:2])
            if int(value) > 12 or int(value) < 1:
                self.valEnt2.set('1')
            if value.isdigit() == False:
                self.valEnt2.set('')
            
    def limit_size_ent3(self,*args):
        value = self.valEnt3.get()
        if value.isdigit() == False:
            self.valEnt3.set('')
        else:
            if len(value) > 2:
                self.valEnt3.set(value[:2])
            elif int(value) > 59 or int(value) < 0:
                self.valEnt3.set('00')
            if value.isdigit() == False:
                self.valEnt3.set('') 
            
    def limit_size_ent4(self,*args):
        value = self.valEnt4.get()
        if value.isdigit() == False:
            self.valEnt4.set('')
        else:
            if len(value) > 2:
                self.valEnt4.set(value[:2])
            if int(value) > 12 or int(value) < 1:
                self.valEnt4.set('1')
            if value.isdigit() == False:
                self.valEnt4.set('')
            
    def limit_size_ent5(self,*args):
        value = self.valEnt5.get()
        if value.isdigit() == False:
            self.valEnt5.set('')
        else:
            if len(value) > 2:
                self.valEnt5.set(value[:2])
            elif int(value) > 59 or int(value) < 0:
                self.valEnt5.set('00')
            if value.isdigit() == False:
                self.valEnt5.set('')
