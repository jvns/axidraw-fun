from pyaxidraw import axidraw
ad = axidraw.AxiDraw()
from myturtle import Turtle
ad.interactive()
ad.options.pen_pos_up = 50
ad.options.pen_pos_down = 15
ad.connect()                    # Open serial port to AxiDraw
t=Turtle(ad)
import sounddevice as sd
fs = 44100  # Sample rate

ad.moveto(2,2)
seconds = 0.1
for j in range(100, 0, -1):
    myrecording = sd.rec(int(seconds * fs), samplerate=fs, channels=1, blocking=True)
    amount = myrecording.max()
    if amount < 0.3:
        t.forward(j/500)
        t.rotate(16)
    else:
        forward = j/500
        for i in range(4):
            t.rotate(80)
            t.forward(forward/4)
            t.rotate(-80)
            t.forward(forward/4)
        t.rotate(16)
