import turtle

my_ttl = turtle.getturtle()
my_ttl.shape('turtle')
my_ttl.pensize(3)
my_ttl.pencolor('red')
my_ttl.speed(10) 
for i in range (10) : 
    my_ttl.circle(50)
    my_ttl.forward(30)
