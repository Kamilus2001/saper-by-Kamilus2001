from tkinter import *
from main import TheGame
from threading import Thread
class StartScreen:
    def __init__(self, master):
        self.X = Label(text="squares in row: ")
        self.X_answer = Entry()
        self.Y = Label(text="squares in column: ")
        self.Y_answer = Entry()
        self. Bombs = Label(text="bombs in game: ")
        self.Bombs_answer = Entry()
        self.finish = Button(text="---START THE GAME---")
        self.X.grid(row=0, column=0)
        self.Y.grid(row=1, column=0)
        self.Bombs.grid(row=2, column=0)
        self.X_answer.grid(row=0, column=1)
        self.Y_answer.grid(row=1, column=1)
        self.Bombs_answer.grid(row=2, column=1)
        self.finish.grid(row=3, columnspan=2)
        self.finish.bind("<Button-1>", self.start)
    def start(self, master):
        x = self.X_answer.get()
        x = int(x)
        y = self.Y_answer.get()
        y = int(y)
        bomb = self.Bombs_answer.get()
        bomb = int(bomb)
        T1 = Thread(target=TheGame, args=(x, y, bomb))
        T1.start()

if __name__ == '__main__':
    window = Tk()
    R = StartScreen(window)
    window.mainloop()