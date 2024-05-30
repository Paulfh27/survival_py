import pygame
from sprites import *

RED = (255,0,0)
RELOAD = -60        # reload speed, the lower the number the longer the reload
SLASH = "./assets/images/slash.png"

slash = pygame.image.load(SLASH)
slash = pygame.transform.scale(slash, (40,40))

slash_up = pygame.transform.rotate(slash, 90)
slash_right = slash
slash_down = pygame.transform.rotate(slash, 270)
slash_left = pygame.transform.flip(slash, True, False)

class Sword(pygame.sprite.Sprite): 
    def __init(self):
        super().__init__()

    def addHolder(self, holder): 
        self.holder = holder
        holder.attack = self
        #self.image = pygame.Surface((self.holder.rect.width, self.holder.rect.height))
        self.image = pygame.image.load(SLASH)
        self.image = pygame.transform.scale(self.image, (40, 40))
        self.rect = self.image.get_rect()
        self.image.fill((0,0,0,0)) 
        self.active = False
        self.time = -60
        self.center = 0 # front direction of 
        self.dmg = 20
    
    def attack(self): 
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE] and not self.active and self.time <= RELOAD: 
            self.time = 10
            self.image.set_alpha((255))
            self.active = True
        if self.time <= 0: 
            self.image.set_alpha((0))
            self.active = False
        self.time -= 1
        
    def update(self, player): 
        keys = pygame.key.get_pressed()
        if keys[pygame.K_DOWN]: 
            self.rect.topleft = self.holder.rect.bottomleft
            self.image = slash_down
        elif keys[pygame.K_LEFT]: 
            self.rect.bottomright = self.holder.rect.bottomleft
            self.image = slash_left
        elif keys[pygame.K_RIGHT]: 
            self.rect.bottomleft = self.holder.rect.bottomright
            self.image = slash_right
        elif keys[pygame.K_UP]: 
            self.rect.bottomleft = self.holder.rect.topleft
            self.image = slash_up
        self.attack()

class Projectile(pygame.sprite.Sprite): 
    def __init__(self): 
        super().__init__()
        self.speed_x = 0
        self.speed_y = 0
        self.active = False
        self.image = pygame.Surface((20,20))
        self.rect = self.image.get_rect()

    def fire(self, holder):
        self.active = True
        self.image = pygame.Surface((20,20))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.speed_x = 10
        self.speed_y = 0
        self.rect.bottomleft = holder.rect.center

    def update(self, player): 
        if self.active: 
            self.rect.x += self.speed_x
            self.rect.y += self.speed_y
            super().update()

class Ranged(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        one, two, three = Projectile(), Projectile(), Projectile()
        self.projectiles = [one, two, three]
        self.holder = None
        self.image = pygame.Surface((20,20))
        self.rect = self.image.get_rect()
        self.time = -60
    
    def addHolder(self, entity):
        self.holder = entity
        entity.attack = self
    # need to pass sprites so more ammo can be made and added to the list
    def update(self, player): 
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE] and not self.active and self.time <= RELOAD: 
            self.time = 10
            self.image.set_alpha((255))
            self.active = True
        if self.time <= 0: 
            self.image.set_alpha((0))
            self.active = False
        self.time -= 1
        super().update()