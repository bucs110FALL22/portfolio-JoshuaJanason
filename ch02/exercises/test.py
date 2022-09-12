import turtle



my_turtle = turtle.Turtle()
my_turtle.color("purple")
my_turtle.shape("turtle")
my_turtle.pensize(1)

sides = 4
length = 50
colors = ["red"]
CIRCLE_DEG = 360

for c in colors:
   my_turtle.color(c)
for i in [0]sides
my_turtle.left(CIRCLE_DEG / sides)
my_turtle.forward(length)