from pyaxidraw import axidraw
from myturtle import Turtle

ad = axidraw.AxiDraw()


ad.interactive()
ad.options.pen_pos_up = 50
ad.options.pen_pos_down = 10
ad.options.speed_penup = 100
ad.options.speed_pendown = 100
ad.connect()

t = Turtle(ad)

print("What you can do:")
print("ad.lineto(x, y) # move absolute (pen down)")
print("ad.moveto(x, y) # move absolute (pen up)")
print("ad.line(x, y)   # move relative (pen down)")
print("ad.move(x, y)   # move relative (pen up)")
print("t.forward(x)    # move turtle forward x inches")
print("t.rotate(DEG)   # rotate turtle DEG degrees")
