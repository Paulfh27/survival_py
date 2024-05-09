import pygame 
import random 

# Constants 
FPS = 30
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

class Player(pygame.sprite.Sprite): 
    def __init__(self, x, y): 
        super().__init__()
        self.x_speed = 0
        self.y_speed = 0

        self.color = WHITE 
        self.health = 100 
        self.image = pygame.Surface((PLAYER_SIZE, PLAYER_SIZE))
        self.image.fill(self.color)
        self.rect = self.image.get_rect()
        self.rect.x = SCREEN_WIDTH // 2
        self.rect.y = SCREEN_HEIGHT // 2

    def update(self):
        keys = pygame.key.get_pressed()
        self.x_speed = 0
        self.y_speed = 0
        if keys[pygame.K_LEFT]:
            self.x_speed = -PLAYER_SPEED
        if keys[pygame.K_RIGHT]:
            self.x_speed = PLAYER_SPEED
        if keys[pygame.K_UP]:
            self.y_speed = -PLAYER_SPEED
        if keys[pygame.K_DOWN]:
            self.y_speed = PLAYER_SPEED

        self.rect.x += self.x_speed
        self.rect.y += self.y_speed
        
class Enemy(pygame.sprite.Sprite): 
    def __init__(self): 
        super().__init__() 
        self.move_clock = 0
        self.xpointer = 10
        self.ypointer = 10

        self.image = pygame.Surface((ENEMY_SIZE, ENEMY_SIZE))
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, SCREEN_WIDTH - ENEMY_SIZE) 
        self.rect.y = random.randint(0, SCREEN_HEIGHT - ENEMY_SIZE) 
        self.image.fill(GREEN)
        self.color = GREEN  

    def update(self): 
        if self.move_clock <= 0: 
            self.move_clock = 10
            self.xpointer = random.randint(-ENEMY_SPEED, ENEMY_SPEED)
            self.ypointer = random.randint(-ENEMY_SPEED, ENEMY_SPEED)
        
        if self.rect.left <= 0: 
            self.rect.x = 5
        elif self.rect.right >= SCREEN_WIDTH:
            self.rect.x = SCREEN_WIDTH - ENEMY_SIZE - 5
        elif self.rect.top <= 0:
            self.rect.y = 5
        elif self.rect.bottom >= SCREEN_HEIGHT:
            self.rect.y = SCREEN_HEIGHT - ENEMY_SIZE - 5
        else: 
            self.rect.x += self.xpointer
            self.rect.y += self.ypointer

        self.move_clock -= 1

# Resource class 
class Resource(pygame.sprite.Sprite): 
    def __init__(self): 
        super().__init__()
        self.image = pygame.Surface((RESOURCE_SIZE, RESOURCE_SIZE))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, SCREEN_WIDTH - RESOURCE_SIZE) 
        self.rect.y = random.randint(0, SCREEN_HEIGHT - RESOURCE_SIZE) 
    
    def update(self): 
        pass

# list of all sprites on the map    
sprites = pygame.sprite.Group()
# Create player 
player = Player(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2) 
# Create resources 
resources = [Resource() for _ in range(10)] 
# Create enemies 
enemies = [Enemy() for _ in range(5)] 
sprites.add(player)
for enemy in enemies:
    sprites.add(enemy)
for resource in resources: 
    sprites.add(resource)

def collision(): 
    for sprite in sprites:
        if sprite == player:
            continue
        if pygame.sprite.collide_rect(player, sprite):
            if isinstance(sprite, Enemy): 
                player.health -= 1
            elif isinstance(sprite, Resource): 
                player.health += 1
            
def draw_health_bar():
    width = SCREEN_WIDTH / 4
    height = SCREEN_HEIGHT / 20
    x = 0
    y = 0
    health_width = int((player.health / 100) * width)
    pygame.draw.rect(screen, RED, (x, y, width, height))
    pygame.draw.rect(screen, GREEN, (x, y, health_width, height))

# Game loop 
running = True 
while running: 
    screen.fill((0, 0, 0)) 
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: running = False 
    # update sprites: 
    sprites.update() 
    sprites.draw(screen)
    collision()
    draw_health_bar()
    # Update the display 
    pygame.display.flip() 
    clock.tick(FPS)

# Quit pygame 
pygame.quit()