from tkinter import *

window = Tk()
label1 = Label(window, text = '이름')
label2 = Label(window, text = '나이')
label1.grid(row = 0)
label2.grid(row = 1)

e1 = Entry(window)
e2 = Entry(window)
e1.grid(row=0, column = 1)
e2.grid(row=1, column = 1)

window.mainloop()
