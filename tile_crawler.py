#!/usr/bin/python
 
import pygame
import sys
import os

import random
 
pygame.init()



'''
------======XXXXXXXX======------
            Game menu
------======XXXXXXXX======------
'''
class GameMenu():
    def __init__(self, screen, bg_color=(0,0,0), font=None, font_size=30,
                    font_color=(255, 255, 255)):
        self.screen = screen
        self.scr_width = self.screen.get_rect().width
        self.scr_height = self.screen.get_rect().height
 
        self.bg_color = bg_color
        self.clock = pygame.time.Clock()
        
        items = ('*S*tart', '*Q*uit')
        self.items = items
        self.font = pygame.font.SysFont(font, font_size)
        self.font_color = font_color
 
        self.items = []
        for index, item in enumerate(items):
            label = self.font.render(item, 1, font_color)
 
            width = label.get_rect().width
            height = label.get_rect().height
 
            posx = (self.scr_width / 2) - (width / 2)
            # t_h: total height of text block
            t_h = len(items) * height
            posy = (self.scr_height / 2) - (t_h / 2) + (index * height)
 
            self.items.append([item, label, (width, height), (posx, posy)])
 
    def run(self):
        mainloop = True
        while mainloop:
            # Limit frame speed to 50 FPS
            self.clock.tick(50)
 
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    ##mainloop = False
                    ##pygame.quit()
                    ##sys.exit()
                    return 0
                if event.type == pygame.KEYUP:
                    if event.key == ord('q'):
                        ##pygame.quit()
                        ##sys.exit()
                        ##mainloop = False
                        return 0
                    if event.key == ord('s'):
                        print('Start the game!')
                        mainloop = False
 
            # Redraw the background
            self.screen.fill(self.bg_color)
 
            for name, label, (width, height), (posx, posy) in self.items:
                self.screen.blit(label, (posx, posy))
 
            pygame.display.flip()

        ## print('Test')
        ## game_items = ('PlayMe', 'Something else', 'R for points')
        ## gm_L1 = Level_01(screen, menu_items)
        ## gm_L1.run()
        return(2)



'''
------======XXXXXXXX======------
            Level 1
------======XXXXXXXX======------
'''
class Level_01():
    def __init__(self, screen, bg_color=(0,0,0), font=None, font_size=30,
                    font_color=(255, 255, 255)):
        self.screen = screen
        self.scr_width = self.screen.get_rect().width
        self.scr_height = self.screen.get_rect().height
 
        self.bg_color = bg_color
        self.clock = pygame.time.Clock()
        
        items = ('*R*eceive points', '*Q*uit')
        self.items = items
        self.font = pygame.font.SysFont(font, font_size)
        self.font_color = font_color
 
        self.items = []

        for index, item in enumerate(items):
            label = self.font.render(item, 1, font_color)
 
            width = label.get_rect().width
            height = label.get_rect().height
 
            posx = (self.scr_width / 2) - (width / 2)
            # t_h: total height of text block
            t_h = len(items) * height
            posy = (self.scr_height / 2) - (t_h / 2) + (index * height)
 
            self.items.append([item, label, (width, height), (posx, posy)])
 
    def run(self):
        mainloop = True
        while mainloop:
            # Limit frame speed to 50 FPS
            self.clock.tick(50)
            ## print('game')
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    ## mainloop = False
                    ## pygame.quit()
                    ## sys.exit()
                    return 1
                if event.type == pygame.KEYUP:
                    if event.key == ord('q'):
                        ## pygame.quit()
                        ## sys.exit()
                        ## mainloop = False
                        return 1
                    if event.key == ord('r'):
                        print('Pressed R!')
                        mainloop = False
 
            # Redraw the background
            self.screen.fill(self.bg_color)
 
            for name, label, (width, height), (posx, posy) in self.items:
                self.screen.blit(label, (posx, posy))
 
            pygame.display.flip()

        print('Test')
        sys.exit()



'''
------======XXXXXXXX======------
              MAIN
------======XXXXXXXX======------
'''
if __name__ == "__main__":
    # Creating the screen
    screen = pygame.display.set_mode((640, 480), 0, 32)

    pygame.display.set_caption('Tile Crawler')
    
    # the game loop!
    gameStatus = 1;
    while gameStatus:
        # the starter menu
        if gameStatus==1:
            gm = GameMenu(screen)
            gameStatus=gm.run()

        # the game loop
        if gameStatus==2:
            gm_L1 = Level_01(screen)
            gameStatus=gm_L1.run()


        if gameStatus==0:
            sys.exit()

