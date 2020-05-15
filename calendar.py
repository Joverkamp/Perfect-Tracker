
from settings import*
from tkinter import *



#vertical and horiztonal lines for calendar i
class Calendar:
    def __init__(self, parent):
        self.parent = parent
        self.create_grid()

    def create_grid(self):
        canvas = Canvas(self.parent.tab2, width=SCREENWIDTH, height=SCREENHEIGHT)
        #horizontal
        canvas.create_line(0,50, 650, 50)
        canvas.create_line(0,70, 650,480)
        #vertical
        canvas.create_line(135,50, 135,480)
        canvas.create_line(220,50, 220,480)
        canvas.create_line(305,50, 305,480)
        canvas.create_line(395,50, 395,480)
        canvas.create_line(475,50, 475,480)
        canvas.create_line(560,50, 560,480)
        canvas.create_line(645,50, 645,480)
        canvas.pack()

    def month_header(self):
        pass

    def month_dates(self):
        pass



        
