from tkinter import *
window = Tk()

window.geometry('200x200')

buttonList = [None,None,None]

for i in range(0,3) :
    buttonList[i] = Button(window,text='버튼'+str(i+1))

for b in buttonList :
    b.pack(side =RIGHT)

window.mainloop()
