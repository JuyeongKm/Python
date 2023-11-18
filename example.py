import turtle
turtle.setup(480, 320)
my_window = turtle.Screen()
my_window.title("Nested if를 이용한 터틀의 움직임")
turtle.shape('turtle')
my_turtle = turtle.getturtle()
Shape = turtle.textinput("", "Type T for a triangle or R for a rectangle: ")
if Shape == 'T':
    Side = turtle.textinput("", "Type S for a small triangle or L for large: ")
    if Side == 'S': 
        length = 50 # Side length of a triangle
    else: # Side = L’
        length = 100
        my_turtle.forward(length); my_turtle.left(120)
        my_turtle.forward(length); my_turtle.left(120)
        my_turtle.forward(length);
elif Shape == 'R':
    Side = turtle.textinput("", "Type S for a small rectangle or L for large: ")
    if Side == 'S': 
        length = 50 # Side length of a rectangle
    else: # Side = 'L'
        length = 100
        my_turtle.forward(length); my_turtle.left(90)
        my_turtle.forward(length); my_turtle.left(90)
        my_turtle.forward(length); my_turtle.left(90)
        my_turtle.forward(length)
else:
    my_turtle.write("Input is incorrect")
