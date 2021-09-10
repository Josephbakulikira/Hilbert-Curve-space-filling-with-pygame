import pygame
from utils import *
from math import pow

Width, Height = 1000, 1000
Resolution = (Width, Height)

pygame.init()
window = pygame.display.set_mode(Resolution)
clock = pygame.time.Clock()
fps = 60

Black, White = (0, 0, 0), (255, 255, 255)

# s -> level of iterations, t-> total number of points

s = 6
n = int(pow(2, s))
t = n * n 

lineThickness = 2 

Hilbert = [None for i in range(t)]

for i in range(t):
    length = Width/n
    Hilbert[i] = GetPoint(i, length, s, True)


toggle_color = False

# set timer to the t (timer = t) if you want 
# to draw the whole fractal without animation
timer = 1
increment_speed = 1

run = True
while run:
    window.fill(Black)
    clock.tick(fps)
    frame_rate = int(clock.get_fps())
    pygame.display.set_caption("Hilbert Curve - FPS : {}".format(frame_rate))

    # Handle Events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                run = False
            if event.key == pygame.K_r:
                timer = 1
            if event.key == pygame.K_SPACE:
                toggle_color = not toggle_color
    
    for i in range(timer-1):
        c = pygame.Color(0,0,0)
        c.hsva = (i/10%360, 100, 100, 100)
        color = White if toggle_color else c
        pygame.draw.line(window, color, Hilbert[i], Hilbert[i+1], lineThickness)

    pygame.display.flip()

    timer += increment_speed
    if timer > t:
        timer = t
    
pygame.quit()
