import curses
import os
import time

from pyaxidraw import axidraw
ad = axidraw.AxiDraw()
ad.interactive()
ad.options.pen_pos_up = 30
ad.options.pen_pos_down = 15
ad.connect()

def main(win):
    dx = 0
    dy = 0
    win.nodelay(True)
    key=""
    win.clear()
    win.addstr("Detected key:")
    while 1:
        try:
            key = win.getkey()
            win.addstr(str(key))
            if str(key) == 'KEY_DOWN':
                dx, dy = 0, 0.02
            elif str(key) == 'KEY_UP':
                dx, dy = 0, -0.02
            elif str(key) == 'KEY_RIGHT':
                dx, dy = 0.02, 0
            elif str(key) == 'KEY_LEFT':
                dx, dy = -0.02, 0
            else:
                win.addstr("stop")
                dx, dy = 0,0
            if key == os.linesep:
                break
        except Exception as e:
            pass
        ad.line(dx, dy)
        time.sleep(0.02)

curses.wrapper(main)
