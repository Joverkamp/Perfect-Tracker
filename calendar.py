from tkinter import ttk
from settings import*
from tkinter import *



#vertical and horiztonal lines for calendar i
class Calendar:
    
    def __init__(self, parent):
        
        self.parent = parent
        self.create_grid()
        self.days_of_week()
        self.month_format()
        self.update_month()

    def create_grid(self):
        
        canvas = Canvas(self.parent.tab2, width=SCREENWIDTH, height=SCREENHEIGHT)
        
        #horizontal
        #top
        canvas.create_line(50,60, 650, 60)
        #bottom
        canvas.create_line(50,450, 650,450)
        #inside
        canvas.create_line(50,130, 650,130)
        canvas.create_line(50,220, 650,220)
        canvas.create_line(50,310, 650,310)
        canvas.create_line(50,390, 650,390)
        
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
        
        #create drop down menu for months
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
        self.month.bind('<<ComboxSelected>>',self.update_month())


    def update_month(self):

        ##x = 0
        ##y = 0
        ##month = self.valmonth.get()
        ##for month in MONTH_FULL:
            ##if MONTH_FULL == 'February':
                    ##for index in range(len(DAYS29)):
                        ##DAYS28[index] = Label(self.parent.tab2, text=DAYS28[index])
                        ##DAYS28[index].place(x=10+x, y=10+y)
            ##elif MONTH_FULL == 'April' or MONTH_FULL == 'June' or MONTH_FULL == 'September' or MONTH_FULL == 'Novemeber':
                ##for index in range(len(DAYS30)):
                    ##DAYS30[index] = Label(self.parent.tab2, text= DAYS28[index])
                    ##DAYS30[index].place(x=10+x, y=100+y)
            ##else:
                ##for index in range(len(DAYS31)):
                    ##DAYS31[index] = Label(self.parent.tab2, text= DAYS28[index])
                    ##DAYS31[index].place(x=10+x, y=100+y)

        month = self.valmonth.get()
        self.lbl1 = Label(self.parent.tab2, text = "1", font = 14)
        self.lbl1.place(x=53, y=65) 
        self.lbl2 = Label(self.parent.tab2, text = "2", font = 14)
        self.lbl2.place(x=137, y=65) 
        self.lbl3 = Label(self.parent.tab2, text = "3", font = 14)
        self.lbl3.place(x=225, y=65) 
        self.lbl4 = Label(self.parent.tab2, text = "4", font = 14) 
        self.lbl4.place(x=310, y=65) 
        self.lbl5 = Label(self.parent.tab2, text = "5", font = 14) 
        self.lbl5.place(x=400, y=65) 
        self.lbl6 = Label(self.parent.tab2, text = "6", font = 14) 
        self.lbl6.place(x=480, y=65) 
        self.lbl7 = Label(self.parent.tab2, text = "7", font = 14) 
        self.lbl7.place(x=565, y=65) 
        self.lbl8 = Label(self.parent.tab2, text = "8", font = 14) 
        self.lbl8.place(x=53, y=135) 
        self.lbl9 =  Label(self.parent.tab2, text = "9", font = 14) 
        self.lbl9.place(x=137, y=135) 
        self.lbl10 = Label(self.parent.tab2, text = "10", font = 14) 
        self.lbl10.place(x=225, y=135) 
        self.lbl11 = Label(self.parent.tab2, text = "11", font = 14) 
        self.lbl11.place(x=310, y=135) 
        self.lbl12 = Label(self.parent.tab2, text = "12", font = 14) 
        self.lbl12.place(x=400, y=135) 
        self.lbl13 = Label(self.parent.tab2, text = "13", font = 14)
        self.lbl13.place(x=480, y=135) 
        self.lbl14 = Label(self.parent.tab2, text = "14", font = 14)
        self.lbl14.place(x=565, y=135) 
        self.lbl15 = Label(self.parent.tab2, text = "15", font = 14)
        self.lbl15.place(x=53, y=225) 
        self.lbl16 = Label(self.parent.tab2, text = "16", font = 14)
        self.lbl16.place(x=137, y=225) 
        self.lbl17 = Label(self.parent.tab2, text = "17", font = 14)
        self.lbl17.place(x=225, y=225) 
        self.lbl18 = Label(self.parent.tab2, text = "18", font = 14)
        self.lbl18.place(x=310, y=225) 
        self.lbl19 = Label(self.parent.tab2, text = "19", font = 14)
        self.lbl19.place(x=400, y=225) 
        self.lbl20 = Label(self.parent.tab2, text = "20", font = 14)
        self.lbl20.place(x=480, y=225) 
        self.lbl21 = Label(self.parent.tab2, text = "21", font = 14)
        self.lbl21.place(x=565, y=225) 
        self.lbl22 = Label(self.parent.tab2, text = "22", font = 14)
        self.lbl22.place(x=53, y=315) 
        self.lbl23 = Label(self.parent.tab2, text = "23", font = 14)
        self.lbl23.place(x=137, y=315) 
        self.lbl24 = Label(self.parent.tab2, text = "24", font = 14)
        self.lbl24.place(x=225, y=315) 
        self.lbl25 = Label(self.parent.tab2, text = "25", font = 14)
        self.lbl25.place(x=310, y=315) 
        self.lbl26 = Label(self.parent.tab2, text = "26", font = 14)
        self.lbl26.place(x=400, y=315) 
        self.lbl27 = Label(self.parent.tab2, text = "27", font = 14)
        self.lbl27.place(x=480, y=315) 
        self.lbl28 = Label(self.parent.tab2, text = "28", font = 14)
        self.lbl28.place(x=565, y=315)
        self.lbl29 = Label(self.parent.tab2, text = "29", font = 14)
        self.lbl29.place(x=53, y=395)
        self.lbl30 = Label(self.parent.tab2, text = "30", font = 14)
        self.lbl30.place(x=137, y=395)
        self.lbl31 = Label(self.parent.tab2, text = "31", font = 14)
        self.lbl31.place(x=225, y=395)
        if month == 'February':
            self.lblfuck = Label(self.parent.tab2, text= "FUCK YOU", font = 16)
            self.lblfuck.place(x=300, y=250)
