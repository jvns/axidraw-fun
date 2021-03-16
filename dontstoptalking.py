from pyaxidraw import axidraw
ad = axidraw.AxiDraw()
from myturtle import Turtle
ad.interactive()
ad.options.pen_pos_up = 50
ad.options.pen_pos_down = 15
ad.connect()                    # Open serial port to AxiDraw
t=Turtle(ad)import sounddevice as sd
seconds=0.5
fs = 44100  # Sample rate

for i in range(200):
    myrecording = sd.rec(int(seconds * fs), samplerate=fs, channels=2, blocking=True)
    amount = myrecording.max()
    if amount < 0.2:
        t.rotate(45)
    t.forward(0.03)
