import turtle #1. import modules
import random
import pygame
import math

# #Part A
window = turtle.Screen() # 2.  Create a screen
window.bgcolor('lightblue')

michelangelo = turtle.Turtle() # 3.  Create two turtles
leonardo = turtle.Turtle()
michelangelo.color('orange')
leonardo.color('blue')
michelangelo.shape('turtle')
leonardo.shape('turtle')

michelangelo.up() # 4. Pick up the pen so we don’t get lines
leonardo.up()
michelangelo.goto(-100,20)
leonardo.goto(-100,-20)

## 5. Your PART A code goes here
michel_number = random.randint(1, 101)
leonardo_number = random.randint(1, 101)
michelangelo.forward(michel_number) 
leonardo.forward(leonardo_number)
michelangelo.goto(-100, 20)
leonardo.goto(-100, -20)
pygame.time.wait(1000)

michel_number1 = random.randint(0, 11)
leonardo_number1 = random.randint(0, 11)
for i in range(11):
    michelangelo.forward(michel_number1)
    leonardo.forward(leonardo_number1)
    pygame.time.wait(1000)

michelangelo.goto(-100, 20)
leonardo.goto(-100, -20)

window.exitonclick()



# # PART B - complete part B here
pygame.init()
surface = (500, 500)
window_pygame = pygame.display.set_mode(surface)

#Variables
color = "blue"
coords = []         
num_sides = 3
side_length = 100
offset = 100


#Equilateral Triangle
for i in range(num_sides):
  theta = (2.0 * math.pi * (i)) / num_sides
  x = side_length * math.cos(theta) + offset
  y = side_length * math.sin(theta) + offset
  coords.append([x,y])
pygame.draw.polygon(window_pygame, color, coords)
pygame.display.flip()
pygame.time.wait(1000)
window_pygame.fill("black")
pygame.display.flip()

#Square
num_sides = 4
coords=[]
for i in range(num_sides):
  theta = (2.0 * math.pi * (i)) / num_sides
  x = side_length * math.cos(theta) + offset
  y = side_length * math.sin(theta) + offset
  coords.append([x,y])
pygame.draw.polygon(window_pygame, color, coords)
pygame.display.flip()
pygame.time.wait(1000)
window_pygame.fill("black")
pygame.display.flip()

#Hexagon
num_sides = 6
coords=[]
for i in range(num_sides):
  theta = (2.0 * math.pi * (i)) / num_sides
  x = side_length * math.cos(theta) + offset
  y = side_length * math.sin(theta) + offset
  coords.append([x,y])
pygame.draw.polygon(window_pygame, color, coords)
pygame.display.flip()
pygame.time.wait(1000)
window_pygame.fill("black")
pygame.display.flip()

#Nonagon
num_sides = 9
coords=[]
for i in range(num_sides):
  theta = (2.0 * math.pi * (i)) / num_sides
  x = side_length * math.cos(theta) + offset
  y = side_length * math.sin(theta) + offset
  coords.append([x,y])
pygame.draw.polygon(window_pygame, color, coords)
pygame.display.flip()
pygame.time.wait(1000)
window_pygame.fill("black")
pygame.display.flip()

#Circle
num_sides = 360
coords=[]
for i in range(num_sides):
  theta = (2.0 * math.pi * (i)) / num_sides
  x = side_length * math.cos(theta) + offset
  y = side_length * math.sin(theta) + offset
  coords.append([x,y])
pygame.draw.polygon(window_pygame, color, coords)
pygame.display.flip()
pygame.time.wait(1000)
window_pygame.fill("black")
pygame.display.flip()


