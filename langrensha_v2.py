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
            exit()
    screen.fill(white)
    screen.blit(textImage, (250, 250))
    screen3.blit(textImage3, (30, 100))
    pygame.display.update()
    x, y = pygame.mouse.get_pos()
    if x < 392:
        if x > 253:
            if y > 254:
                if y < 320:
                    for event in pygame.event.get():
                        if event.type == QUIT:
                            exit()
                        elif event.type == MOUSEBUTTONDOWN:
                            pressed_array = pygame.mouse.get_pressed()
                            for index in range(len(pressed_array)):
                                if pressed_array[index]:
                                    if index == 0:
                                        exit()
# import time
# import pygame, sys
# from pygame.locals import *
# from sys import exit
# mc = pygame.display.set_mode((1000,500))
# hi = pygame.image.load("C:\\Users\\Administrator\\Desktop\\mincearft\\1.png")
# while True:
#
