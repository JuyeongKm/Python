from tkinter import *
from tkinter import messagebox

def myfunc():
    messagebox.showinfo('버튼누르기','버튼을 누르셨네요')

window = Tk()
window.geometry('500x300')

button = Button(window, text='파이썬 종료',bg='white',command = myfunc)

button.pack()
window.mainloop()
