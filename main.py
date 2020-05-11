from tkinter import *
from settings import *

class homePage(Canvas):
    def __init__(self, parent, **kwargs):
#check kwargs
#prepare super_kwargs and initialize parent
        super_kwargs = kwargs.copy()
        super().__init__(parent, super_kwargs)
#initialize variables

#make stuff
        
#bindings
     
#functions
    
window = Tk()
frame = Frame(window)
canvas = homePage(frame)
frame.pack()
canvas.pack(side='top', fill='both', expand=True)
window.geometry("{}x{}+50+50".format(SCREEN_WIDTH,SCREEN_HEIGHT))
window.mainloop()
