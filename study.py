# def mingzi(m):
#     m = 1+m
#     return m
# a=1
# b = 1+mingzi(1)
# print(b)
import os, pygame
from pygame.locals import *
from sys import exit
from random import *
__author__ = {'name' : 'Hongten',
       'mail' : 'hongtenzone@foxmail.com',
       'Version' : '1.0'}
if not pygame.font:print('Warning, Can not found font!')
pygame.init()
screen = pygame.display.set_mode((255, 255), 0, 32)
screen.fill((255,255,255))
#font = pygame.font.Font('C:\\Users\\guxinkai\\Desktop\\minceraft,sea.jpg', 20)
#text = font.render('Cliked Me please!!!', True, (34, 252, 43))
mouse_x, mouse_y = 0, 0
while 1:
  for event in pygame.event.get():
    if event.type == QUIT:
      exit()
    elif event.type == MOUSEBUTTONDOWN:
      pressed_array = pygame.mouse.get_pressed()
      for index in range(len(pressed_array)):
        if pressed_array[index]:
          if index == 0:
            print('撸')
          elif index == 1:
            print('选')
          elif index == 2:
            print('用')
    elif event.type == MOUSEMOTION:
      #return the X and Y position of the mouse cursor
      pos = pygame.mouse.get_pos()
      mouse_x = pos[0]
      mouse_y = pos[1]
  screen.fill((mouse_x, mouse_y, 0))
  #screen.blit(text, (40, 100))
  pygame.display.update()
