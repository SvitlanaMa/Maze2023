import pygame
from maps import *

pygame.init()

win_w = 600
win_h = 480
FPS = 40

block_size = 40

pygame.mixer_music.load("jungles.ogg")
pygame.mixer_music.set_volume(0.1)
pygame.mixer_music.play(-1)

class GameSprite:
    def __init__(self, x, y, w, h, image):
        self.rect = pygame.Rect(x, y, w, h)
        image = pygame.transform.scale(image, (w, h))
        self.image = image
    
    def update(self):
        window.blit(self.image, (self.rect.x, self.rect.y))


class Pers(GameSprite):
    def __init__(self, x, y, w, h, image, speed):
        super().__init__(x, y, w, h, image)
        self.speed = speed

    def move(self, key_left, key_right, key_up, key_down):
        k = pygame.key.get_pressed()
        if k[key_right]:
            if self.rect.right <= win_w:
                self.rect.x += self.speed 
        elif k[key_left]:
            if self.rect.left >= 0:
                self.rect.x -= self.speed
        elif k[key_up]:
            if self.rect.y >= 0:
                self.rect.y -= self.speed
        elif k[key_down]:
            if self.rect.bottom <= win_h:
                self.rect.y += self.speed
        
window = pygame.display.set_mode((win_w, win_h))
pygame.display.set_caption("Догонялки")
clock = pygame.time.Clock()
#window.fill((2, 200, 200))

background = pygame.image.load("background.jpg")
background = pygame.transform.scale(background, (win_w, win_h))
window.blit(background, (0, 0))

pers_img = pygame.image.load("sprite1.png")
pers = Pers(250, 250, 50, 50, pers_img, 5)

gold_img = pygame.image.load("treasure.png")
gold = GameSprite(win_w - 60, win_h - 60, 50, 50, gold_img)




game = True
finish = False
while game:
    if not finish:
        window.blit(background, (0, 0))
        
        pers.move(pygame.K_a, pygame.K_d, pygame.K_w, pygame.K_s)
        pers.update()
        gold.update()
        
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False
    pygame.display.update()
    clock.tick(FPS)
