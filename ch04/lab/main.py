import pygame
import math
import random

pygame.init()
surface = (900, 600)
screen = pygame.display.set_mode(surface)
pygame.display.init()
length = surface[0]
width = surface[1]
print(length, width)

#Square
coords = []
num_sides = 4
side_length = 50
offset = 100
color = "blue"
x = 200
y = 300
l = 900
w = 600
coords.append([x, y, l, w])
screen.fill("white")
pygame.draw.rect(screen, "blue", [x, y, l, w])
pygame.display.flip()
pygame.time.wait(1000)


  