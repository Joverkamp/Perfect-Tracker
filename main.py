from tkinter import *
from tkinter import ttk
from settings import *

#create main window 
window = Tk()
window.resizable(width=False, height=False)
window.geometry("{}x{}+50+50".format(SCREEN_WIDTH,SCREEN_HEIGHT))

#adjust tabs with style
style = ttk.Style()
style.theme_create( "MyStyle", parent="alt", settings={
    "TNotebook": {"configure": {"tabmargins":[ 0, 5, -5, 0] } },
    "TNotebook.Tab": {"configure": {"padding":[50,5],
                                    "font" : ('URW Gothic L', '12', ' bold')}, }})
style.theme_use("MyStyle")

#notebooks acts as a parent for tabs
tab_parent = ttk.Notebook(window)

#create tabs connected to parent notebook. Each tab is its own frame
tab1 = ttk.Frame(tab_parent, width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
tab2 = ttk.Frame(tab_parent, width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
tab3 = ttk.Frame(tab_parent, width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
tab4 = ttk.Frame(tab_parent, width=SCREEN_WIDTH, height=SCREEN_HEIGHT)

#add tabs to parent notebook   
tab_parent.add(tab1, text="Schedule")
tab_parent.add(tab2, text="Up Next")
tab_parent.add(tab3, text="Grades")
tab_parent.add(tab4, text="Priority View")

#pack tabs to main window
tab_parent.pack()

#main loop
window.mainloop()
