import pygame
from square import Square
from random import randint

class TheGame(object):
    def __init__(self, x, y, bombs):
        pygame.init()
        pygame.font.init()
        self.squares_x = x
        self.squares_y = y
        self.bombs = bombs
        self.screen = pygame.display.set_mode((self.squares_x*22+44, self.squares_y*22+44))
        self.clock = pygame.time.Clock()
        self.squares = [[0 for i in range(0, self.squares_x+5)] for j in range(0, self.squares_y+5)]
        self.number = [[0 for i in range(0, self.squares_x+5)] for j in range(0, self.squares_y+5)]
        self.number_2 = [[0 for i in range(0, self.squares_x+5)] for j in range(0, self.squares_y+5)]
        self.generate_squares()

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
            self.screen.fill((60, 60, 60))
            win = 0
            for i in range(0, self.squares_x):
                for j in range(0, self.squares_y):
                    self.squares[j][i].show(self.number[j][i], self.number_2[j][i])
                    if self.squares[j][i].stan == 2:
                        if self.squares[j][i].bang == 1:
                            win += 1
                        else:
                            win -=1
                    if pygame.mouse.get_pos()[0] >= self.squares[j][i].x and pygame.mouse.get_pos()[0]<=self.squares[j][i].x+self.squares[j][i].w:
                        if pygame.mouse.get_pos()[1] >= self.squares[j][i].y and pygame.mouse.get_pos()[1] <= self.squares[j][i].y + self.squares[j][i].h:
                            if pygame.mouse.get_pressed()[2]:
                                self.number[j][i] = 2

                            elif pygame.mouse.get_pressed()[1]:
                                self.number[j][i] = 1
                            elif pygame.mouse.get_pressed()[0]:
                                numer = 0
                                if self.squares[j][i].bang == 1:
                                    print("LOST")
                                else:
                                    try:
                                        for k in range(i-1, i+2):
                                            for l in range(j-1, j+2):
                                                if self.squares[l][k].bang == 1:
                                                    numer += 1
                                    except Exception:
                                        pass
                                    if numer != 0:
                                        self.number[j][i] = 3
                                        self.number_2[j][i] = numer
                                    else:
                                        for k in range(i-1, i+2):
                                            for l in range(j-1, j+2):
                                                if self.square(k, l)==1:
                                                    self.number[l][k] = 4
            if win == self.bombs:
                print("YOU WON")
            pygame.display.flip()
            self.clock.tick(60)
    def square(self, i, j):
        for k in range(i - 1, i + 2):
            for l in range(j - 1, j + 2):
                if self.squares[l][k].bang == 1:
                    print("siema")
                    return 0
        return 1
    def generate_squares(self):
        for i in range(0, self.squares_x+5):
            for j in range(0, self.squares_y+5):
                self.squares[j][i] = Square(self.screen, 0, (i + 1) * 22, (j + 1) * 22)
                self.number[j][i] = 0
                self.number_2[j][i] = 0
        for i in range(0, self.bombs):
            y1 = randint(0, self.squares_y-2)
            x1 = randint(0, self.squares_x-2)
            self.squares[y1][x1] = Square(self.screen, 1, self.squares[y1][x1].x, self.squares[y1][x1].y)


