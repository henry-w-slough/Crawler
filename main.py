import pygame
import src.Engine.Screen as Screen
import src.Engine.MapLoader as MapLoader
import src.Objects.Player as Player

screen = Screen.Screen(800, 800)

map_loader = MapLoader.MapLoader()
map_loader.load_map("assets/levels/level1/level1_tilemap.tmj", "level1")
map_loader.map_to_group(screen.layers["tiles"], "level1")

player = Player.Player(32, 32, screen.layers["sprites"])
player.set_position(128, 128)

running = True
while running:

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False

	screen.update()