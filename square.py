import pygame

class Square(object):
    def __init__(self, screen, bang, x, y):
        self.w = 20
        self.h = 20
        self.bang = bang
        self.screen = screen
        self.x = x
        self.y = y
        self.color = (100,100,100)
        self.stan = 0

        self.myfont = pygame.font.SysFont('Comic Sans MS', 13)
    def show(self, i, g):
        self.stan = i
        if(i==0):
            pygame.draw.rect(self.screen, self.color, (self.x, self.y, self.w, self.h))
        if i==1:
            textsurface = self.myfont.render("?", False, (0, 0, 0))
            pygame.draw.rect(self.screen, self.color, (self.x, self.y, self.w, self.h))
            self.screen.blit(textsurface, (self.x+5, self.y + 1))
        if i==2:
            textsurface = self.myfont.render("!", False, (100, 0, 0))
            pygame.draw.rect(self.screen, self.color, (self.x, self.y, self.w, self.h))
            self.screen.blit(textsurface, (self.x + 9, self.y + 1))
        if i==3:
            g =  str(g).encode("utf-8").decode("utf-8")
            g1 = int(g)
            self.color = (255-g1*5, 10 +g1*5, 30+g1*6)
            textsurface = self.myfont.render(g, False, (60, 0, 40))
            pygame.draw.rect(self.screen, self.color, (self.x, self.y, self.w, self.h))
            self.screen.blit(textsurface, (self.x + 9, self.y + 1))
        if i==4:
            self.color = (150, 150, 150)
            pygame.draw.rect(self.screen, self.color, (self.x, self.y, self.w, self.h))