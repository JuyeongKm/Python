from tkinter import *
window = Tk()

window.geometry('1000x500')
label1 = Label(window,text='파이썬',font='고딕 15 bold',\
               fg='red',bg='white',width=20,height=5,anchor=NW)
label2 = Label(window,text='fighting!',\
               font = ('Arial 30 bold italic'), fg='purple')
label3 = Label(window,text='*기초공학부*',font=('굴림',15),\
               bg='yellow',width=20,height=5,anchor=CENTER)

label1.pack()
label2.pack()
label3.pack()

window.mainloop()
