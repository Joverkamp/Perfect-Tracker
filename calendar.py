
from settings import*
from tkinter import *



#vertical and horiztonal lines for calendar i
class Calendar:
    
    def __init__(self, parent):
        
        self.parent = parent
        self.create_grid()
        self.days_of_week()
        self.month_format()

    def create_grid(self):
        
        canvas = Canvas(self.parent.tab2, width=SCREENWIDTH, height=SCREENHEIGHT)
        
        #horizontal
        #top
        canvas.create_line(50,60, 650, 60)
        #bottom
        canvas.create_line(50,450, 650,450)
        #inside
        canvas.create_line(50,160, 650,160)
        canvas.create_line(50,260, 650,260)
        canvas.create_line(50,360, 650,360)
        
        #vertical
        canvas.create_line(50,50, 50,450)
        canvas.create_line(135,50, 135,450)
        canvas.create_line(220,50, 220,450)
        canvas.create_line(305,50, 305,450)
        canvas.create_line(395,50, 395,450)
        canvas.create_line(475,50, 475,450)
        canvas.create_line(560,50, 560,450)
        canvas.create_line(650,50, 650,450)
        canvas.pack()

    def days_of_week(self):
        
        #Monday
        Monlbl = Label(self.parent.tab2, text='Monday')
        Monlbl.place(x=67, y=37)
        
        #Tuesday
        Tuelbl = Label(self.parent.tab2, text='Tuesday')
        Tuelbl.place(x=155, y=37)
        
        #Wednesday
        Wedlbl = Label(self.parent.tab2, text='Wednesday')
        Wedlbl.place(x=230, y=37)
        
        #Thursday
        Thurlbl = Label(self.parent.tab2, text='Thursday')
        Thurlbl.place(x=325, y=37)
        
        #Friday
        Frilbl = Label(self.parent.tab2, text='Friday')
        Frilbl.place(x=418, y=37)
        
        #Saturday
        Satlbl = Label(self.parent.tab2, text='Saturday')
        Satlbl.place(x=495, y=37)
        
        #Sunday
        Sunlbl = Label(self.parent.tab2, text='Sunday')
        Sunlbl.place(x=585, y=37)

    def month_format(self):
        self.valmonth = StringVar()
        self.month = ttk.Combobox(self.parent.tab2,
                values=(MONTH_FULL),
                textvariable = self.valmonth,
                state='readonly',
                width=10,
                font=14)
        self.month.current(9)
        self.month.value = self.valmonth
        self.month.place(x=300, y=10)
        self.month.bind('<<ComboxSelected>>',self.update_month)


    def update_month(self):
        pass



        
