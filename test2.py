from tkinter import *

window = Tk()

mainMenu = Menu(window)
window.config(menu=mainMenu)

fileMenu = Menu(mainMenu)
mainMenu.add_cascade(label = '파일처리', menu=fileMenu)

fileMenu.add_command(label='텍스트파일', menu = findMenu)
findMenu.add_command(label = '열기')
findMenu.add_command(label = '찾기')

window.mainloop()
