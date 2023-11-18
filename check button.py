from tkinter import *

def show() :
    print(‘'이름: %s \n 나이: %s ' %(e1.get(), e2.get()))
     
window = Tk()
window.geometry("300x100")

label1 = Label(window, text = "이름")
label2 = Label(window, text = "나이")
label1.grid(row = 0)
label2.grid(row = 1)

e1 = Entry(window)
e2 = Entry(window)
e1.grid(row = 0, column = 1)

e2.grid(row = 1, column = 1)
b1 = Button(window, text = "보이기", command = show)
b2 = Button(window, text = "종료", command = quit)
b1.grid(row = 3, column = 0, ipadx = 4)
b2.grid(row = 3, column = 1, sticky = W, ipadx = 4)

window.mailpp[
