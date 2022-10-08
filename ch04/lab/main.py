import pygame
import math
import random

#Part A
#Screen
screen = pygame.display.set_mode((300, 300))
width, height = pygame.display.get_window_size()
print(width, height)
color = "blue"
screen.fill(color)

#Circle
color = "yellow"
pygame.draw.circle(screen, color, (150, 150), 150)
pygame.display.flip()
pygame.time.wait(500)

#Lines
color = "black"
pygame.draw.line(screen, color, (0, 150), (300, 150))
pygame.display.flip()
pygame.time.wait(500)
pygame.draw.line(screen, color, (150, 0), (150, 300))
pygame.display.flip()
pygame.time.wait(500)

#Part B
color = "green"
random_width = random.randrange(0, 301)
random_length = random.randrange(0, 301)
for i in range(10):
  x1 = random_width
  y1 = random_length
pygame.draw.circle(screen, color, (x1, y1), 5)
pygame.display.flip()
pygame.time.wait(500)




