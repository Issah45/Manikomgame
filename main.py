import pygame
from pygame.locals import *

from player import Player
from dialog import Dialog
from spike import Spike

width, height = 992, 600
display = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()
tile_size = 32

def approx(a):
	a = round(a/tile_size) * tile_size

platforms = [
	pygame.Rect(0, 0, 32, 608),
	pygame.Rect(0, 0, 992, 32),
	pygame.Rect(960, 0, 32, 576),
	pygame.Rect(0, 576, 992, 32),
	pygame.Rect(192, 160, 768, 32),
	pygame.Rect(32, 288, 576, 32),
	pygame.Rect(256, 224, 32, 64),
	pygame.Rect(320, 192, 32, 64),
	pygame.Rect(384, 224, 32, 64),
	pygame.Rect(448, 192, 32, 64),
	pygame.Rect(512, 224, 32, 64),
	pygame.Rect(576, 192, 32, 64),
	pygame.Rect(608, 288, 320, 32),
	pygame.Rect(896, 320, 32, 128),
	pygame.Rect(672, 256, 256, 32),
	pygame.Rect(736, 224, 192, 32),
	pygame.Rect(640, 544, 224, 32),
	pygame.Rect(640, 512, 192, 32),
	pygame.Rect(640, 480, 160, 32),
	pygame.Rect(640, 448, 128, 32),
	pygame.Rect(640, 416, 64, 32),
	pygame.Rect(640, 384, 32, 32),
	pygame.Rect(608, 416, 32, 160),
	pygame.Rect(576, 448, 32, 128),
	pygame.Rect(544, 480, 32, 96),
	pygame.Rect(512, 512, 32, 64),
	pygame.Rect(480, 544, 32, 32),
	pygame.Rect(384, 544, 32, 32),
	pygame.Rect(320, 320, 32, 224),
	pygame.Rect(256, 544, 32, 32),
	pygame.Rect(192, 320, 32, 224),
	pygame.Rect(128, 544, 32, 32),
	pygame.Rect(32, 320, 96, 64),
	pygame.Rect(192, 32, 640, 32),
	pygame.Rect(192, 64, 352, 32),
	pygame.Rect(192, 96, 64, 32),
]

spikes = [
	Spike(928, 128),
	Spike(768, 128),
	Spike(576, 128),
	Spike(128, 256),
	Spike(96, 256),
	Spike(864, 544),
	Spike(800, 480),
	Spike(704, 416),
	Spike(576, 416),
	Spike(512, 480),
	Spike(384, 512),
	Spike(64, 544),
]

player = Player(850, 70, platforms)

player.x = 896
player.y = 64

while True:
	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit()
	display.fill((50, 150, 250))

	for platform in platforms:
		w = round(platform.width / tile_size)
		h = round(platform.height / tile_size)
		img = pygame.image.load("images/tile4.png")
		imger = pygame.transform.scale(img, (tile_size, tile_size))
		for i in range(w):
			display.blit(imger, (platform.x+(i*tile_size), platform.y))
			for j in range(h):
				display.blit(imger, (platform.x+(i*tile_size), platform.y+(j*tile_size)))
		# pygame.draw.rect(display, (0, 0, 0), platform)

	# Renders
	player.render()

	# Updates
	player.update()

	for spike in spikes:
		spike.render()
		# print(spike.rect)
		if spike.rect.colliderect(player.rect):
			pygame.quit()

	pygame.display.update()
	clock.tick(60)