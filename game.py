import pygame 
from interface import *
from sprites import *
from spawn import *
from attacks import *

# Constants 
FPS = 60
SCREEN_WIDTH = 800 
SCREEN_HEIGHT = 600 
WHITE = (255, 255, 255) 
RED = (255, 0, 0) 
GREEN = (0, 255, 0)
BLACK = (0, 0, 0) 

BACKGROUND = "./assets/images/grass_background.png"

pygame.init()  
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT)) 
pygame.display.set_caption("Survival IO Game") 
clock = pygame.time.Clock()

background = pygame.image.load(BACKGROUND)
background = pygame.transform.scale(background, (SCREEN_WIDTH, SCREEN_HEIGHT))
background_rect = background.get_rect()

sprites = pygame.sprite.Group()
player = Player(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2) 
resources = [Resource() for _ in range(10)] 
enemies = [Enemy() for _ in range(5)] 
coins = [Coin() for _ in range(10)]

sword = Sword()
sword.addHolder(player)
sprites.add(sword)

#ranged = Ranged()
#ranged.addHolder(player)
#sprites.add(ranged)

sprites.add(player)
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

PAUSE = False
running = True 
while running: 
    screen.blit(background, background_rect)
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            running = False 
        elif event.type == pygame.KEYDOWN: 
            if event.key == pygame.K_q: 
                PAUSE = True 
                print(PAUSE)

    if PAUSE == False: 
        sprites.update(player) 
        sprites.draw(screen)

        collision(sprites, player)
        draw_health_bar(screen, player)
        draw_coin_bar(screen, player)
        draw_ammo(screen, player)
        inf_round(sprites)
        if not player.isAlive(): 
            if game_over(screen, player, SCREEN_WIDTH, SCREEN_HEIGHT): 
                running = False
            else: 
                restart()
    elif PAUSE == True: 
        PAUSE = pauseMenu(screen, sprites)

    # Update the display 
    pygame.display.flip() 
    clock.tick(FPS)

# Quit pygame 
pygame.quit()