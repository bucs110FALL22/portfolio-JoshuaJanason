import pygame
import math
import random

#Part A
#Screen
screen = pygame.display.set_mode((300, 300))
width, height = pygame.display.get_window_size()
gameStart = False
print(width, height)
color = "blue"
screen.fill(color)

#pygame.draw.rect(screen, "green",(50,150,50,50))
#pygame.display.flip()
#pygame.time.wait(1000)
#pygame.draw.rect(screen, "red" ,(200,150,50,50))
#pygame.display.flip()
#pygame.time.wait(1000)

#Part C
#Choose a Player
choose_player = input("Do you think player 1 or player 2 will win?")
print(choose_player)


#Circle
color = "yellow"
pygame.draw.circle(screen, color, (150, 150), 150)
pygame.display.flip()
pygame.time.wait(500)
    
  
#Lines
color = "black"
pygame.draw.line(screen, color, (0, 150), (300, 150))
pygame.display.flip()
pygame.time.wait(100)
pygame.draw.line(screen, color, (150, 0), (150, 300))
pygame.display.flip()
pygame.time.wait(100)

#Part B
#Player 1
x2 = 150
y2 = 150
color = "green"
for i in range(10):
  random_width = random.randrange(0, 301)
  random_length = random.randrange(0, 301)
  x1 = random_width
  y1 = random_length
  distance_from_center = math.hypot(x1-x2, y1-y2) 
  is_in_circle = distance_from_center <= width/2
  print(is_in_circle)
  if is_in_circle is True: 
    color = "green"
  elif is_in_circle is False:
    color = "orange"
  pygame.draw.circle(screen, color, (x1, y1), 5)
  pygame.display.flip()
  print(distance_from_center)
  print(is_in_circle)
  pygame.time.wait(500)
  
#Player 2
for i in range(10):
  random_width = random.randrange(0, 301)
  random_length = random.randrange(0, 301)
  x1 = random_width
  y1 = random_length
  distance_from_center = math.hypot(x1-x2, y1-y2) 
  is_in_circle = distance_from_center <= width/2
  print(is_in_circle)
  if is_in_circle is True: 
    color = "red"
  elif is_in_circle is False:
    color = "purple"
  pygame.draw.circle(screen, color, (x1, y1), 5)
  pygame.display.flip()
  print(distance_from_center)
  print(is_in_circle)
  pygame.time.wait(500)

#Part C
box_width = width / 3
box_height = height / 3

red_box = pygame.Rect(0, 0, box_width, box_height)
blue_box = pygame.Rect(0, 0, box_width, box_height)
blue_box.topleft = red_box.topright
red_button = pygame.draw.rect(screen, "red", red_box)
blue_button = pygame.draw.rect(screen, "blue", blue_box)


pygame.display.flip()