from tkinter import *
from tkinter import messagebox

def my():
    if (chk1.get() == 1) and (chk2.get()==0):
        messagebox.showinfo('','파이선을 선택했습니다.')
    elif (chk2.get()==1) and (chk1.get()==0):
        messagebox.showinfo('','C언어를 선택했습니다.')
    elif (chk1.get()==1) and (chk2.get() ==1 ):
        messagebox.showinfo('','둘다 선택했습니다.')
    else:
        messagebox.showinfo('','선택하지 않았습니다.')

window = Tk()
window.geometry('400x200')

label = Label(window,text = '사용 가능한 프로그래밍 언어를 고르세요',bg='white')

chk1 = IntVar()
chk2 = IntVar()

cb1=Checkbutton(window,text='파이선',variable = chk1, command =my)
cb2=Checkbutton(window,text='C언어',variable = chk2, command =my)

label.pack(padx=10,pady=10)
cb1.pack(padx=10, pady=10) 
cb2.pack(padx=10, pady=10)
window.mainloop( )
