from pyaxidraw import axidraw
ad = axidraw.AxiDraw()
from myturtle import Turtle

ad.interactive()
ad.options.pen_pos_up = 30
ad.options.pen_pos_down = 10
ad.connect()                    # Open serial port to AxiDraw

ad.plot_setup()
ad.options.mode = "align"
ad.plot_run()
