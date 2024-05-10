import pygame
BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
SCREEN_WIDTH = 800 
SCREEN_HEIGHT = 600 

def draw_health_bar(screen, player):
    width = SCREEN_WIDTH / 4
    height = SCREEN_HEIGHT / 20
    x = 0
    y = 0
    health_width = int((player.health / 100) * width)
    pygame.draw.rect(screen, RED, (x, y, width, height))
    pygame.draw.rect(screen, GREEN, (x, y, health_width, height))

def draw_coin_bar(screen, player): 
    text = "Money: " + str(player.money)
    font = pygame.font.Font(None, 30)
    text_surface = font.render(text, True, WHITE)
    text_rect = text_surface.get_rect()
    text_rect.topleft = (5, SCREEN_HEIGHT //10)
    screen.blit(text_surface, text_rect)
    
class Button(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height, color, text):
        self.rect = pygame.Rect(x, y, width, height)
        self.color = color
        self.text = text
        self.font = pygame.font.SysFont(None, 30)
    
    def draw(self, surface):
        pygame.draw.rect(surface, self.color, self.rect)
        text_surface = self.font.render(self.text, True, BLACK)
        text_rect = text_surface.get_rect(center=self.rect.center)
        surface.blit(text_surface, text_rect)

def game_over(screen, WIDTH, HEIGHT): 
    running = True
    font = pygame.font.Font(None, 36)
    text_surface = font.render("GAME OVER", True, WHITE)
    text_rect = text_surface.get_rect()
    text_rect.center = (WIDTH // 2, HEIGHT // 2)

    quit = Button(WIDTH//1.5, HEIGHT//1.5, 75, 50, RED, "QUIT")
    restart = Button(WIDTH//4, HEIGHT//1.5, 100, 50, GREEN, "RESTART")

    gameover = False
    while running: 
        for event in pygame.event.get(): 
            if event.type == pygame.QUIT: 
                running = False
                gameover = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                if quit.rect.collidepoint(event.pos):
                    running = False
                    gameover = True 
                if restart.rect.collidepoint(event.pos):
                    running = False
                    gameover = False
                    
        screen.fill(BLACK)
        screen.blit(text_surface, text_rect)
        quit.draw(screen)
        restart.draw(screen)
        pygame.display.flip()

    return gameover