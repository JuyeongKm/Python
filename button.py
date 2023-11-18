from tkinter import *

window = Tk()

window.geometry('500x300')
button = Button(window,text = '파이썬 종료', fg = 'blue',\
                bg='white', command = quit)

button.pack()

window.mainloop()
