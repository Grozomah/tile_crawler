#!/usr/bin/python
 
import pygame
import sys
import os
import random
 


'''
------======XXXXXXXX======------
            Game menu
------======XXXXXXXX======------
'''
class GameMenu():
    def __init__(self, screen, bg_color=(0,0,0), font=None, font_size=30,
                    font_color=(255, 255, 255)):
        ## self.screen = pygame.display.set_mode((640, 480), 0, 32)
        self.screen=screen
        self.scr_width = screen.get_rect().width
        self.scr_height = screen.get_rect().height
 
        self.bg_color = bg_color
        self.clock = pygame.time.Clock()



        self.backdrop = pygame.image.load(os.path.join('images','tileCrawler_title.png')).convert()
        self.backdropbox = screen.get_rect()


        
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
 
            ## whatever

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
            ## self.screen.fill(self.bg_color)
            self.screen.blit(self.backdrop, self.backdropbox)
            for name, label, (width, height), (posx, posy) in self.items:
                self.screen.blit(label, (posx, posy))
 
            pygame.display.flip()
        return(2)



'''
------======XXXXXXXX======------
            Level 1
------======XXXXXXXX======------
'''
class Level_01():
    def __init__(self, screen, bg_color=(0,0,0), font=None, font_size=30,
                    font_color=(255, 255, 255)):
        self.screen = pygame.display.set_mode((960, 720), 0, 32)
        self.scr_width = self.screen.get_rect().width
        self.scr_height = self.screen.get_rect().height
 
        self.bg_color = bg_color
        self.clock = pygame.time.Clock()
        
        self.backdrop = pygame.image.load(os.path.join('images','level1.png')).convert()
        self.backdropbox = screen.get_rect()


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
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return 1
                if event.type == pygame.KEYUP:
                    if event.key == ord('q'):
                        return 1
                    if event.key == ord('r'):
                        print('+1 points')
 
            # Redraw the background
            self.screen.blit(self.backdrop, self.backdropbox)
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
    pygame.init()

    # Creating the screen
    screen = pygame.display.set_mode((960, 720), 0, 32)
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

