import curses
import os
import time
from myturtle import Turtle

from pyaxidraw import axidraw
ad = axidraw.AxiDraw()
ad.interactive()
ad.options.pen_pos_up = 30
ad.options.pen_pos_down = 10
ad.connect()

def main(win):
    t = Turtle(ad)
    x = 0
    y = 0
    speed = 3
    win.nodelay(True)
    key=""
    win.clear()
    while 1:
        try:
            key = win.getkey()
            win.addstr(str(speed) + " ")
            if str(key) == 'KEY_RIGHT':
                t.rotate(60)
            elif str(key) == 'KEY_LEFT':
                t.rotate(-60)
            elif str(key) == 'f':
                speed += 1
            elif str(key) == 's':
                speed -= 1
            else:
                win.addstr("stop")
                dx, dy = 0,0
            if key == os.linesep:
                break
        except KeyboardInterrupt:
            ad.penup()
            return
        except Exception as e:
            pass
        t.forward(0.02 * speed)
        time.sleep(0.01)

curses.wrapper(main)
