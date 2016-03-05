from Tkinter import *
root = Tk()
root.title('Quick Player Error Popups')
root.geometry('400x100')   
wt = ''
import sys
for i in range(1, len(sys.argv)):
	wt = wt + " " + sys.argv[i]
w = Label(root, text="Please check whether the '"+wt+"' file contains unrecognized characters, or other errors can't read!", width = 400,height = 100,wraplength = 400,anchor = 'center').pack()
root.mainloop()
