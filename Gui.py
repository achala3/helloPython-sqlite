from tkinter import *
from datetime import datetime
win=Tk()

win.geometry('400x50')
win.title('What time?')
win.option_add('*Font','궁서 20')

def what_time():
    tNow=datetime.now()
    btn.config(text=tNow)

btn=Button()

#btn.config(width=10)
btn.config(text='현재시각?')
btn.config(command= what_time)
btn.pack()

win.mainloop()