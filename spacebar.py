import curses
import os
import time
from pyaxidraw import axidraw
from myturtle import Turtle

ad = axidraw.AxiDraw()
ad.interactive()
ad.options.pen_pos_up = 50
ad.options.pen_pos_down = 10
ad.connect()

t = Turtle(ad)
ad.moveto(5.5, 8)

def main(win):
    win.nodelay(True)
    win.clear()
    win.addstr("Detected key:")
    down = True
    for i in range(600):
        try:
            key = win.getkey()
            if str(key) == ' ':
                # flip from down to not down
                down = not down
        except KeyboardInterrupt:
            ad.penup()
            return
        except Exception as e:
            # no key was pressed
            pass
        t.down = down
        t.forward(i / 3200)
        t.rotate(8)
        time.sleep(0.02)


curses.wrapper(main)
