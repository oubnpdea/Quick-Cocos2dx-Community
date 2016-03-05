from Tkinter import *
root = Tk()
root.title('QCC Player Error Popups')
root.geometry('400x100')   
wt = ''
import sys
w1 = sys.argv[1]
w2 = sys.argv[2]
w3 = sys.argv[3]
for i in range(4, len(sys.argv)):
	wt = wt + " " + sys.argv[i]
w = Label(root, text = wt, width = w1,height = w2,wraplength = w3,anchor = 'center').pack()
root.mainloop()
