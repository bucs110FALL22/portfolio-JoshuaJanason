#Import Modules
import turtle

#Screen
window = turtle.Screen()
turtle.screensize(500, 500)
window_color = "blue"
window.bgcolor(window_color)
screen_size = print(turtle.screensize())

#Turtle
turtle = turtle.Turtle()
turtle.color("green")
turtle.shape("turtle")
turtle.pensize(1)
turtle.pencolor("black")

#Square House
def house():
  turtle.up()
  turtle.goto(0,0)
  turtle.down()
  sides = 4
  angle = 360/sides
  square_color = "green"
  turtle.fillcolor(square_color)
  turtle.begin_fill()
  for i in [angle]*sides:
    turtle.forward(100)
    turtle.right(i)

house()
turtle.end_fill()

#Triangle Roof
def roof(): 
  turtle.up()
  turtle.goto(0,0)
  turtle.down()
  sides = 3
  angle = 360/sides
  roof_color = "orange"
  turtle.fillcolor(roof_color)
  turtle.begin_fill()
  for i in [angle]*sides:
    turtle.forward(100)
    turtle.left(i)
    
roof()
turtle.end_fill()

#Sqaure Door
def door():
  turtle.up()
  turtle.goto(50, -100)
  turtle.down()
  sides = 4
  angle = 360/sides
  door_color = "red"
  turtle.fillcolor(door_color)
  turtle.begin_fill()
  for i in [angle]*sides:
    turtle.forward(40)
    turtle.left(i)
    
door()
turtle.end_fill()

#Circle DoorKnob
def doorknob():
  turtle.up()
  turtle.goto(80, -90)
  turtle.down()
  doorknob_color = "black"
  turtle.fillcolor(doorknob_color)
  turtle.begin_fill()
  turtle.circle(5)
  
doorknob()
turtle.end_fill()

#Window
def wind():
  turtle.up()
  turtle.goto(40, 50)
  turtle.down()
  sides = 4
  angle = 360/sides
  for i in [angle]*sides:
    turtle.forward(20)
    turtle.right(i)
    
wind()

#Horizontal Window Line
def horizontal_windlines():
  turtle.up()
  turtle.goto(40, 40)
  turtle.down()
  turtle.fillcolor("black")
  turtle.begin_fill()
  turtle.forward(20)

horizontal_windlines()
turtle.end_fill()

#Vertical Window Line
def vertical_windlines():
  turtle.up()
  turtle.goto(50, 50)
  turtle.down()
  turtle.fillcolor("black")
  turtle.begin_fill()
  turtle.right(90)
  turtle.forward(20)
  
vertical_windlines()
turtle.end_fill()

#Street
def street():
  turtle.up()
  turtle.goto(100, -100)
  turtle.down()
  length = 250
  width = 100
  street_color = "black"
  turtle.fillcolor(street_color)
  turtle.begin_fill()
  for i in range(2):
    turtle.forward(width)
    turtle.right(90)
    turtle.forward(length)
    turtle.right(90)
    
street()
turtle.end_fill()

#Road Divider1
def divider():
  turtle.up()
  turtle.goto(100, -125)
  turtle.down()
  length = 60
  width = 30
  divider_color = "yellow"
  turtle.fillcolor(divider_color)
  turtle.begin_fill()
  for i in range(2):
    turtle.forward(width)
    turtle.right(90)
    turtle.forward(length)
    turtle.right(90)
  
divider()
turtle.end_fill()

#Road Divider1
def divider1():
  turtle.up()
  turtle.goto(10, -125)
  turtle.down()
  length = 60
  width = 30
  divider_color = "yellow"
  turtle.fillcolor(divider_color)
  turtle.begin_fill()
  for i in range(2):
    turtle.forward(width)
    turtle.right(90)
    turtle.forward(length)
    turtle.right(90)

divider1()
turtle.end_fill()

#Road Divider2
def divider2():
  turtle.up()
  turtle.goto(-80, -125)
  turtle.down()
  length = 60
  width = 30
  divider_color = "yellow"
  turtle.fillcolor(divider_color)
  turtle.begin_fill()
  for i in range(2):
    turtle.forward(width)
    turtle.right(90)
    turtle.forward(length)
    turtle.right(90)

divider2()
turtle.end_fill()


#Moon
def moon():
  turtle.up()
  turtle.goto(-25, 150)
  turtle.down()
  moon_color = "grey"
  turtle.fillcolor(moon_color)
  turtle.begin_fill()
  turtle.circle(35)
  
moon()
turtle.end_fill()

def end():
  turtle.hideturtle()
  window.exitonclick()

end()

def main():
  house()
  roof()
  door()
  doorknob()
  wind()
  horizontal_windlines()
  vertical_windlines()
  street()
  divider()
  divider1()
  divider2()
  moon()
  end()

main()
