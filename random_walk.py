import random
from pyaxidraw import axidraw
ad = axidraw.AxiDraw()
ad.interactive()
ad.options.pen_pos_up = 50
ad.options.pen_pos_down = 15
ad.connect()                    # Open serial port to AxiDraw

start_x = 0
start_y = 0
ad.moveto(start_x,start_y)



def random_place(x, y, grid):
    for radius in range(100):
        choices = set((x+i, y+j) for i in range(-radius,radius) for j in range(-radius,radius)) & grid
        if len(choices) > 0:
            return list(choices)

def run(start_x, start_y):
    x = 0
    y = 0
    grid = set((i,j) for i in range(25 * 6) for j in range(int(25 * 3)))
    while len(grid) > 0:
        choices = set([
            (x-1, y),
            (x+1, y),
            (x, y-1),
            (x, y+1),
            ]) & grid
        if len(choices) > 0:
            x, y = random.choice(list(choices))
            grid.remove((x, y))
            ad.lineto(start_x + x * 0.04, start_y + y * 0.04)
        else:
            x, y = random.choice(list(grid))
            grid.remove((x, y))
            ad.moveto(start_x + x * 0.04, start_y + y * 0.04)
try:
    run(start_x, start_y)
except:
    ad.penup()
    time.sleep(0.01)
    ad.moveto(0,0)
    time.sleep(0.01)


