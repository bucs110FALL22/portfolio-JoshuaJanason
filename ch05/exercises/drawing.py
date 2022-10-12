import turtle
window = turtle.Screen()
window.bgcolor("white")
turtle = turtle.Turtle()
turtle.color("green")
turtle.shape("turtle")

def drawEqShape(turtle, num_sides, side_length):
    for i in range(num_sides):
      turtle.forward(side_length)
      turtle.left(90)

num_sides = int(input("How many sides would you like?: "))
side_length = int(input("How long would you like each side?: "))

drawEqShape(turtle, num_sides, side_length)

window.exitonclick()

