import pygame
from pygame.locals import *

red = 250, 0, 0
white = 250, 250, 0
pygame.init()
screen = pygame.display.set_mode((1000, 500))
myfont = pygame.font.Font(None, 100)
textImage = myfont.render("666", True, red)
while True:
    for event in pygame.event.get():
        if event.type in (QUIT, KEYDOWN):
            Minceraft
    screen.fill(white)
    screen.blit(textImage, (333, 333))
    pygame.display.update()
import pygame,sys
from pygame.locals import *
red = 100,100,100
blue = 100,0 , 0
pygame.init()
screen = pygame.display.set_mode((600,600))
pygame.display.set_caption("minceraft")
while True:
    print(666)
    for event in pygame.event.get():
        if event.type in (QUIT,KEYDOWN):
            sys.exit()
    screen.fill((0,0,200))
    color= 255,255,0
    position = 300,255
    radius = 100
    width = 10
    pygame.draw.circle(screen,color,position,radius,width)

    pygame.display.update()


