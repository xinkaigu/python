# import pygame
# import sys
# pygame.draw
# pygame.init()
# size = width, height = 640, 480
# screen = pygame.display.set_mode(size)
# blue = (255, 255, 255)
# red =(1,2,3)
# ball = pygame.image.load('C:\\Users\\guxinkai\\Desktop\\minceraft\\minceraft.jpg')
# ballrect = ball.get_rect()
#
# while True:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             sys.exit()
#     screen.fill(blue)
#     screen.fill(red)
#     screen.blit(ball, ballrect)
#     pygame.display.flip()
#     pygame.draw.circle()
import time
import pygame, sys
from pygame.locals import *
from sys import exit
red = 250, 0, 0
white = 0, 0, 0
pygame.init()
screen3 = pygame.display.set_mode((640, 480), 0, 32)
myfont3 = pygame.font.Font(None, 100)
textImage3 = myfont3.render("Chamber escape", True, red)
screen = pygame.display.set_mode((640, 480), 0, 32)
myfont = pygame.font.Font(None, 100)
textImage = myfont.render("play ", True, red)
while True:
    for event in pygame.event.get():
        if event.type in (QUIT, KEYDOWN):
            w
    screen.fill(white)
    screen.blit(textImage, (250, 250))
    screen3.blit(textImage3, (30, 100))
    pygame.display.update()
    x, y = pygame.mouse.get_pos()

