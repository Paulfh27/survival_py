import pygame
import random
import math

SCREEN_WIDTH = 800 
SCREEN_HEIGHT = 600 
PLAYER_SIZE = 20
RESOURCE_SIZE = 10
ENEMY_SIZE = 20 
WHITE = (255, 255, 255) 
RED = (255, 0, 0) 
GREEN = (0, 255, 0)
BLACK = (0, 0, 0) 
YELLOW = (255, 255, 255)
ENEMY_SPEED = 1
PLAYER_SPEED = 3
FOLLOW = 100

class Player(pygame.sprite.Sprite): 
    def __init__(self, x, y): 
        super().__init__()
        self.x_speed = 0
        self.y_speed = 0

        self.color = WHITE 
        self.health = 100 
        self.money = 0
        self.image = pygame.Surface((PLAYER_SIZE, PLAYER_SIZE))
        self.image.fill(self.color)
        self.rect = self.image.get_rect()
        self.rect.x = SCREEN_WIDTH // 2
        self.rect.y = SCREEN_HEIGHT // 2

    def isAlive(self):
        if self.health <= 0: return False 
        else: return True

    def update(self, player):
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

        if self.health > 100: self.health = 100
        
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

    def follow(self, player): 
        x = (self.rect.centerx - player.rect.centerx) 
        y = (self.rect.centery - player.rect.centery)
        distance = math.hypot(x, y)
        if distance < FOLLOW: 
            self.move_clock = 1
            if distance != 0: 
                self.xpointer = -(x / distance)
                self.ypointer = -(y / distance)
            else: 
                self.xpointer = 0
                self.ypointer = 0

    def update(self, player): 
        self.follow(player)
        if self.move_clock <= 0: 
            self.move_clock = 40
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

class Resource(pygame.sprite.Sprite): 
    def __init__(self): 
        super().__init__()
        self.image = pygame.Surface((RESOURCE_SIZE, RESOURCE_SIZE))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, SCREEN_WIDTH - RESOURCE_SIZE) 
        self.rect.y = random.randint(0, SCREEN_HEIGHT - RESOURCE_SIZE) 
    
    def update(self, player): 
        pass


class Coin(pygame.sprite.Sprite): 
    def __init__(self): 
        super().__init__()
        self.image = pygame.Surface((RESOURCE_SIZE, RESOURCE_SIZE))
        self.rect = self.image.get_rect()
        self.image.fill(YELLOW)
        self.rect.x = random.randint(0, SCREEN_WIDTH - RESOURCE_SIZE) 
        self.rect.y = random.randint(0, SCREEN_HEIGHT - RESOURCE_SIZE) 
