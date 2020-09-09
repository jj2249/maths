from math import *
from tkinter import *
from time import sleep


class Pendulum(Tk):
    def __init__(self, m, a, r, omega):
        Tk.__init__(self)
        self.grid()
        self.m = m
        self.r = r
        self.a = a
        self.omega = omega
        self.play = True

        self.background = Frame(self)
        self.background.grid(column=0, row=0, rowspan=10)

        self.resetButton = Button(self, text='Set', command=lambda: self.reset())
        self.resetButton.grid(column=10, row=10)

        self.startButton = Button(self, text='Start/Stop', command=lambda: self.pause())
        self.startButton.grid(column=9, row=10)

        self.g = Scale(self, from_ = 0, to = 10, label='Gravity')
        self.g.grid(column=1, row = 10)
        self.g.set(1)

        self.cd = Scale(self, from_ = 800, to = 1000, label='Damping')
        self.cd.grid(column=2, row=10)
        self.cd.set(1000)

        self.anglei = Scale(self, from_ = -pi/2, to = pi/2, label='Angle')
        self.anglei.grid(column=3, row=10)
        self.anglei.set(pi/2)

        self.omegai = Scale(self, from_ = 0, to = 2*pi, label='Velocity')
        self.omegai.grid(column=4, row=10)
        self.omegai.set(0)

    def reset(self):
        self.a = self.anglei.get()
        self.omega = self.omegai.get()
        self.alpha = 0

    def pause(self):
        if self.play:
            self.play = False
        else:
            self.play = True

    def draw_background(self, WIDTH, HEIGHT, COLOUR):
        self.canvas = Canvas(self.background, width=WIDTH, height=HEIGHT, bg=COLOUR)
        self.canvas.grid()
        self.middle = WIDTH/2

    def get_position(self, x_shift, y_shift):
        self.x = self.r * sin(self.a)
        self.y = self.r * cos(self.a)
        self.x += x_shift
        self.y += y_shift
        return self.x, self.y

    def draw_mass(self):
        self.get_position(self.middle, 0)
        self.canvas.create_oval(self.x - self.m, self.y - self.m, self.x + self.m, self.y + self.m, fill='black', outline='black')

    def draw_rod(self):
        self.get_position(self.middle, 0)
        self.canvas.create_line(self.middle, 0, self.x, self.y, fill='black', width=2)

    def time_tick(self):
        while self.play:
            self.canvas.delete('all')
            self.draw_mass()
            self.draw_rod()
            self.canvas.update()
            self.calc_motion()
            sleep(0.01)
        while not self.play:
            pass

    def calc_motion(self):
        self.alpha = (-1*(self.g.get()/10) * sin(self.a))/self.r
        self.omega += self.alpha
        self.a += self.omega
        self.omega *= self.cd.get()/1000



screen = Pendulum(10, pi/2, 300, 0)
screen.draw_background(1000, 600, None)
screen.title('Single Pendulum')
screen.time_tick()
screen.mainloop()
