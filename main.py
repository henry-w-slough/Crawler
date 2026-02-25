import pygame
import include.Screen as Screen
import include.Texture as Texture

screen = Screen.Screen(800, 800)

running = True
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.update()