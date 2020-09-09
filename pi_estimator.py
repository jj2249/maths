from math import *
from tkinter import *
from time import sleep
import random as ran

radius = 400
dots_in = 0
dots_total = 10000
n = 0
class Screen(Tk):
    def __init__(self, N, r):
        Tk.__init__(self)
        self.grid()
        self.N = N
        self.r = r

        self.background = Frame(self)
        self.background.grid()

    def draw_background(self, WIDTH, HEIGHT, COLOUR):
        self.canvas = Canvas(self.background, width=WIDTH, height=HEIGHT, bg=COLOUR)
        self.canvas.grid()
        self.label = Label(self.background, text = 0)
        self.label.grid()
        self.midhor = WIDTH/2
        self.midver = HEIGHT/2

    def draw_circle(self):
        self.canvas.create_oval(self.midhor - radius, self.midver + radius, self.midhor + radius, self.midver - radius, fill='white')

    def generate_point(self, n):

        global dots_in

        n1 = ran.randint(-radius, radius)
        n2 = ran.randint(-radius, radius)
        x1 = n1 + (self.midhor - 2)
        x2 = n1 + (self.midhor + 2)
        y1 = n2 + (self.midver - 2)
        y2 = n2 + (self.midver + 2)
        if n1**2+n2**2 < radius**2:
            dots_in += 1
            self.canvas.create_oval(x1, y1, x2, y2, fill='green')
        else:
            self.canvas.create_oval(x1, y1, x2, y2, fill='red')
        self.label.configure(text = (n + 1))

    def print_pi(self, value):
        str(value)
        self.canvas.create_text(self.midhor, self.midver, fill='white', font=('Times 20 italic bold', 60), text=value)



screen = Screen(1000, 600)
screen.draw_background(radius*2, radius*2, 'black')
screen.title('Pi Estimator')
for i in range(dots_total):
    screen.generate_point(i)
    screen.update()
pi_est = (float(dots_in)/dots_total)*4
screen.print_pi(pi_est)
screen.mainloop()


