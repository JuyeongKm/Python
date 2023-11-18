from tkinter import *

def clickMouse(event):
    txt=''
    if event.num == 1:
        txt += '왼쪽 버튼 ('
    elif event.num == 3 :
        txt += '오른쪽 버튼 ('
    txt += str(event.x) + ', ' + str(event.y) +')에서 클릭 됨'
    label1.config(text=txt)

window = Tk()
window.geometry('400x400')
label1 = Label(window, text = '이곳이 바뀜')

window.bind('<Button>', clickMouse)
label1.pack(expand = 1, anchor = CENTER)
window.mainloop()
