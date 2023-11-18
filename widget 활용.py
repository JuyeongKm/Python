from tkinter import *
window = Tk()

label1 = Label(window, text = '파이썬')
label2 = Label(window, text = '열공', font = ('궁서체', 30), fg='blue')
label3 = Label(window, text = '합니다',bg='yellow', width=20, height=5, anchor=SE)

label1.pack()
label2.pack()
label3.pack()

window.mainloop()
