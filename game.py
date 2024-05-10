import pygame 
import random 
from interface import *
from sprites import *
from spawn import *
from attacks import *

# Constants 
FPS = 60
SCREEN_WIDTH = 800 
SCREEN_HEIGHT = 600 
PLAYER_SIZE = 20
RESOURCE_SIZE = 10
ENEMY_SIZE = 20 
WHITE = (255, 255, 255) 
RED = (255, 0, 0) 
GREEN = (0, 255, 0)
BLACK = (0, 0, 0) 
ENEMY_SPEED = 1
PLAYER_SPEED = 3

pygame.init()  
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT)) 
pygame.display.set_caption("Survival IO Game") 
clock = pygame.time.Clock()

sprites = pygame.sprite.Group()
player = Player(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2) 
sword = Sword()
sword.addHolder(player)
resources = [Resource() for _ in range(10)] 
enemies = [Enemy() for _ in range(5)] 
coins = [Coin() for _ in range(10)]

sprites.add(player)
sprites.add(sword)
for enemy in enemies: sprites.add(enemy)
for resource in resources: sprites.add(resource)
for coin in coins: sprites.add(coin)

def restart(): 
    global sprites, player, sword, resources, enemies
    sprites = pygame.sprite.Group()
    sword = Sword()
    player = Player(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2) 
    sword.addHolder(player)
    resources = [Resource() for _ in range(10)] 
    enemies = [Enemy() for _ in range(5)] 
    sprites.add(sword)
    sprites.add(player)
    for enemy in enemies: sprites.add(enemy)
    for resource in resources: sprites.add(resource)
    for coin in coins: sprites.add(coin)

running = True 
while running: 
    screen.fill((0, 0, 0)) 
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: running = False 
    # update sprites: 
    sprites.update(player) 
    sprites.draw
    sprites.draw(screen)
    collision(sprites, player)
    draw_health_bar(screen, player)
    draw_coin_bar(screen, player)
    rand_enemy(sprites)

    if not player.isAlive(): 
        if game_over(screen, SCREEN_WIDTH, SCREEN_HEIGHT): 
            running = False
        else: 
            restart()

    # Update the display 
    pygame.display.flip() 
    clock.tick(FPS)

# Quit pygame 
pygame.quit()