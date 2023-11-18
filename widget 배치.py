from tkinter import *
window = Tk()
window.geometry('200x200')

button1=Button(window,text='1',bg='yellow')
button2=Button(window,text='2',fg='red')
button3=Button(window,text='3',fg='blue',bg='white')

button1.pack(side=LEFT)
button2.pack(side=LEFT)
button3.pack(side=LEFT)

window.mainloop()
