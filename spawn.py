import pygame
import random
from sprites import *

# make more cases for where and how sprites can spawn
    # random 
    # spawn points 
    # along the edges only

def rand_enemy(sprites): 
    rate = 100
    r = random.randint(0, rate)
    if r == 1: 
        e = Enemy()
        sprites.add(e)

def rand_health(sprites): 
    rate = 200
    r = random.randint(0, rate)
    if r == 1: 
        e = Resource()
        sprites.add(e)

