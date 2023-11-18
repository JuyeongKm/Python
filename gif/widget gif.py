from tkinter import *
window = Tk()
window.geometry('1000x600')

txt = Label(window,text='사진넣기')
photo=PhotoImage(file='')
label1=Label(window,image = photo)

txt.pack()
label1.pack()

window.mainloop()
