import turtle
turtle.setup(480, 320)
my_window = turtle.Screen()
my_window.title("if_else를 이용한 터틀의 움직임")
turtle.shape("turtle")
my_turtle = turtle.getturtle()
Shape = turtle.textinput("", "삼각형 T, 사각형 R 입력 : ")
if Shape == 'T': 
    my_turtle.forward(100); my_turtle.left(120)
    my_turtle.forward(100); my_turtle.left(120)
    my_turtle.forward(100); 
elif Shape == 'R': 
    my_turtle.forward(100); my_turtle.left(90)
    my_turtle.forward(100); my_turtle.left(90)
    my_turtle.forward(100); my_turtle.left(90)
    my_turtle.forward(100)
else:
    my_turtle.write("Input is incorrect") 
