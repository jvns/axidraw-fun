import random
import time
from pyaxidraw import axidraw
from myturtle import Turtle
ad = axidraw.AxiDraw()
ad.interactive()
ad.options.pen_pos_up = 40
ad.options.pen_pos_down = 15
ad.connect()                    # Open serial port to AxiDraw

start_x = 3
start_y = 1
ad.moveto(start_x,start_y)

def run():
    t = Turtle(ad)
    x = 0
    for i in range(800):
        t.rotate( 40/ (1 + x*x) ** (3/2)4
        dx, dy = t.forward(0.05)
        print(dx)
        x += dx
    ad.moveto(0,0)

try:
    run()
except:
    ad.plot_setup()
    ad.options.mode = "align"
    ad.plot_run()
    ad.penup()
    time.sleep(0.01)
    ad.moveto(0,0)
    time.sleep(0.01)


