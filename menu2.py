from tkinter import *

window = Tk()

mainMenu = Menu(window)
window.config(menu=mainMenu)

fileMenu = Menu(mainMenu)
mainMenu.add_cascade(label= '파일', menu=fileMenu)

fileMenu.add_command(label='열기')
fileMenu.add_separator()
fileMenu.add_command(label='종료')

editMenu = Menu(mainMenu)
mainMenu.add_cascade(label= '편집', menu=editMenu)

editMenu.add_command(label='실행취소')
editMenu.add_command(label='다시 실행')
editMenu.add_separator()
editMenu.add_command(label='잘라내기')

helpMenu = Menu(mainMenu)
mainMenu.add_cascade(label= '도움말', menu=helpMenu)

helpMenu.add_command(label='도움말 검색')
helpMenu.add_command(label='버전정보')

window.mainloop()
