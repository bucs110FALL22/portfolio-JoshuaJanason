import turtle
screen = turtle.Screen()

input_sides = input("Enter a value for the number of sides: ")
input_length = input("Enter a value for the length of each side: ")
input_sides = int(input_sides)
input_length = int(input_length)

my_turtle = turtle.Turtle()
my_turtle.color("blue")
my_turtle.pensize(1)
angle = 360 / input_sides

for i in [angle]*input_sides: 
  my_turtle.forward(input_length)
  my_turtle.left(i)



screen.exitonclick()