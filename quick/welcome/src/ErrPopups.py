from Tkinter import *
root = Tk()
root.title('Quick Player Error Popups')
root.geometry('400x100')   

w = Label(root, text="Please check whether the 'X:\Users\XXX\Documents\.quick_player.lua'(windows) file contains unrecognized characters, or other errors can't read!", width = 400,height = 100,wraplength = 400,anchor = 'center').pack()
root.mainloop()
