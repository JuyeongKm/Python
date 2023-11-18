import turtle
turtle.setup(480, 320) # 캔버스 크기 설정
my_ttl = turtle.getturtle()
color = ('red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet')

my_ttl.pensize(8)

radius = 200 # 무지개 반경 200에서 시작

for x in range(7):
    my_ttl.penup()
    my_ttl.setposition(radius, -100) # 오른쪽 아래 시작점으로 이동
    my_ttl.setheading(90)
    my_ttl.pendown()
    my_ttl.pencolor(color[x]) # 무지개 색상 선택
    my_ttl.circle(radius,180) # 반원 그리기
    radius -= 12 
