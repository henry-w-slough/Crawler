import pygame
import src.Engine.Screen as Screen
import src.Map.MapLoader as MapLoader

screen = Screen.Screen(800, 800)

map_loader = MapLoader.MapLoader()
map_loader.load_map("assets/levels/level1/level1_tilemap.tmj", "level1")

map_loader.map_to_group(screen.layers["tiles"], "level1")

running = True
while running:

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False

	screen.update()