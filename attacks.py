import pygame
from sprites import *

RED = (255,0,0)

class Sword(pygame.sprite.Sprite): 
    def __init(self):
        super().__init__()

    def addHolder(self, holder): 
        self.holder = holder
        holder.sword = self
        self.image = pygame.Surface((self.holder.rect.width, self.holder.rect.height // 1.5))
        self.rect = self.image.get_rect()
        self.image.fill((0,0,0)) 
        self.active = False
        self.time = 20
        self.center = 0 # front direction of 
    
    def attack(self): 
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]: 
            self.time = 20
            self.image.fill((RED))
            self.active = True
        if self.time <= 0: 
            self.image.fill((0,0,0))
            self.active = False
        self.time -= 1
        
    def update(self, player): 
        # need to check the direction of the character to put sword in corret position 
        self.rect.bottomleft = self.holder.rect.topleft
        self.attack()
        