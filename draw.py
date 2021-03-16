import curses
import os
import time

from pyaxidraw import axidraw
ad = axidraw.AxiDraw()
ad.interactive()
ad.options.pen_pos_up = 50
ad.options.pen_pos_down = 10
ad.connect()

def main(win):
    dx = 0
    dy = 0
    x = 0
    y = 0
    speed = 3
    win.nodelay(True)
    key=""
    win.clear()
    win.addstr("Detected key:")
    while 1:
        try:
            key = win.getkey()
            win.addstr(str(key))
            win.addstr(str(speed))
            if str(key) == 'KEY_DOWN':
                dx, dy = 0, 0.005
            elif str(key) == 'KEY_UP':
                dx, dy = 0, -0.005
            elif str(key) == 'KEY_RIGHT':
                dx, dy = 0.005, 0
            elif str(key) == 'KEY_LEFT':
                dx, dy = -0.005, 0
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
        x += dx * speed
        y += dy * speed
        if x < 0 or y < 0:
            ad.penup()
            return
        ad.line(dx * speed, dy * speed)
        time.sleep(0.01)

curses.wrapper(main)
