import pygame
pygame.init()

#Part A 
#Test with any integer (9)
n = 9
while n > 1:
  if n % 2 == 0:
    n = n/2
  else:
    n = 3 * n + 1
  print(n)

#When integer is 101
count = 0
num = 101 
while num > 1:
  if num % 2 == 0:
    num = num/2  
  else:
    num = 3 * num + 1
  print(num)
  count = count + 1
  print(count)

#Part B
print("The final count is:" , count)
start = 2
upper_limit = 20 
iters = {}
for start in range(start, upper_limit + 1):
    count = 0
num = 101 
while num > 1:
  if num % 2 == 0:
    num = num/2  
  else:
    num = 3 * num + 1
  print(num)
  count = count + 1
  print(count)
  iters.update({num : count})
  max_so_far = count
  if count > max_so_far:
    max_so_far = count  
  print(max_so_far)
  max_val = 25
    
print(iters)
print(max_val)
  
#Part C
display = pygame.display.set_mode()
pygame.init()
coordinates = [(304, 1), (1, 25)]
print(coordinates)
color = "black"
pygame.draw.lines(display, color, False, coordinates)
new_display = pygame.transform.flip(display, False, True)
display.blit(new_display, (0, 0))
font_name = None 
size = 5
font = pygame.font.Font(font_name, size)
msg = "How many counts are shown?"
antialias = True
color = "blue"
msg = font.render(msg, antialias, color)
rendered_message = msg
pos = (10, 10)
display.blit(rendered_message, pos)