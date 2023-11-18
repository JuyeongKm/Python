from tkinter import *
from tkinter import messagebox

def my():
    if chk.get() == 0:
        messagebox.showinfo('', '체크버튼 꺼짐')
    else :
        messagebox.showinfo('', '체크버튼 선택')

window = Tk()
window.geometry('300x300')

chk = IntVar()
cb1 = Checkbutton(window, text='클릭하세요',variable = chk,command=my)

cb1.pack()

window.mainloop()
