import pygame
import math
import random
import turtle

window = turtle.Screen()
window.bgcolor("blue")
theturtle = turtle.Turtle()
theturtle.color("green")
theturtle.shape("turtle")
theturtle.up()
theturtle.goto(0,0)

options = ["heads", "tails"]
outcome = random.choice(options)
print(outcome)
while outcome == "heads" or "tails": 
  if outcome == "heads":
   for i in range(4):
    theturtle.forward(50)
    theturtle.left(50)
  if outcome == "tails": 
    for i in range(4):
      theturtle.forward(50)
      theturtle.right(50)
window.exitonclick()