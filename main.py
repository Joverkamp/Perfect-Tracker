from tkinter import *
from tkinter import ttk
from settings import *
from calendar import *


class Application:
    def __init__(self, parent):
        self.mainWindow = parent
        
        self.make_tabs()
        self.calendar = Calendar(self)
        
    def make_tabs(self):
        self.tab_parent = ttk.Notebook(self.mainWindow)
        #create tabs connected to parent notebook. Each tab is its own frame
        self.tab1 = ttk.Frame(self.tab_parent, width=SCREENWIDTH, height=SCREENHEIGHT)
        self.tab2 = ttk.Frame(self.tab_parent, width=SCREENWIDTH, height=SCREENHEIGHT)
        self.tab3 = ttk.Frame(self.tab_parent, width=SCREENWIDTH, height=SCREENHEIGHT)
        self.tab4 = ttk.Frame(self.tab_parent, width=SCREENWIDTH, height=SCREENHEIGHT)
        self.tab5 = ttk.Frame(self.tab_parent, width=SCREENWIDTH, height=SCREENHEIGHT)
        #add tabs to parent notebook   
        self.tab_parent.add(self.tab1, text="Schedule")
        self.tab_parent.add(self.tab2, text="Calendar")
        self.tab_parent.add(self.tab3, text="Up Next")
        self.tab_parent.add(self.tab4, text="Grades")
        self.tab_parent.add(self.tab5, text="Priority View")
        #pack tabs to main window
        self.tab_parent.pack()

    def calendar_create(self):
        Calendar.create_grid(self, self.tab2)
       
#create main window 
window = Tk()
window.resizable(width=False, height=False)
window.geometry("{}x{}+50+50".format(SCREENWIDTH,SCREENHEIGHT))
#adjust tabs with style
style = ttk.Style()
style.theme_create( "MyStyle", parent="alt", settings={
    "TNotebook": {"configure": {"tabmargins":[ 4, 5, -5, 0] } },
    "TNotebook.Tab": {"configure": {"padding":[32,5],
                                    "font" : ('URW Gothic L', '12', 'bold')}, }})
style.theme_use("MyStyle")
#create app
app = Application(window)
#main loop
window.mainloop()
