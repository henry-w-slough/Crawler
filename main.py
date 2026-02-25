import pygame
import include.Screen as Screen

screen = Screen.Screen(800, 1000)

running = True
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.update()