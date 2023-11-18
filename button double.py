from tkinter import *
from tkinter import messagebox

def my1():
    messagebox.showinfo('종료 버튼누르기','종료 버튼을 누르셨네요.')

def my2():
    messagebox.showinfo('시작 버튼누르기','시작 버튼을 누르셨네요.')

window = Tk()
window.geometry('200x200')

button1 = Button(window,text='파이선 종료', bg='yellow',command=my1)
button2 = Button(window,text='파이선 시작', fg='white',bg='blue',command=my2)

button1.pack()
button2.pack()

window.mainloop()
