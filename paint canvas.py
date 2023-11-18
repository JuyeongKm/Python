from tkinter import *
from tkinter.colorchooser import * # askcolor() 함수 사용을 위한 모듈
from tkinter.simpledialog import *

# 함수 선언
def mouseClick(event) : # 마우스 왼쪽 버튼 드래그 했을 때 실행 함수
    global x1, y1, x2, y2 
    x1 = event.x
    y1 = event.y

def mouseDrop(event) : # 마우스 왼쪽 버튼에서 손을 뗐을 때 실행 함
    global x1, y1, x2, y2, penWidth, penColor
    x2 = event.x
    y2 = event.y
    canvas.create_line(x1, y1, x2, y2, width=penWidth, fill=penColor)

def getColor() :
    global penColor
    color = askcolor() # 색상 팔레트에서 색상 선택
    penColor = color[1] # askcolor의 반환값은 튜플 ((99, 222, 170), '#63deaa')

def getWidth() :
    global penWidth
    penWidth = askinteger('선 두께', '선 두께(1~10)를 입력', minvalue=1, maxvalue=10)

# 전역변수 선언
window = None
canvas = None
x1, y1, x2, y2 = None, None, None, None
penColor = 'black'
penWidth = 5

# 메인 프로그램
window = Tk()
window.title('그림판 짝퉁 프로그램')

canvas = Canvas(window, height=300, width = 300) # 캔버스 위젯 생성

canvas.bind('<Button-1>', mouseClick) # 왼쪽 버튼 클릭
canvas.bind('<ButtonRelease-1>', mouseDrop) # 버튼 릴리즈
canvas.pack()

mainMenu = Menu(window) # 설정 메뉴 생성
window.config(menu=mainMenu)

fileMenu = Menu(mainMenu)
mainMenu.add_cascade(label='설정', menu=fileMenu)
fileMenu.add_command(label='선 색상 선택', command=getColor)
fileMenu.add_command(label='선 두께 결정', command=getWidth)

window.mainloop()
