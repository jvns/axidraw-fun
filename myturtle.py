import math

class Turtle:
    def __init__(self, ad):
        self.angle = 0
        self.ad = ad
        self.down = True

    def forward(self, distance):
        dx = distance * math.cos(math.radians(self.angle))
        dy = distance * math.sin(math.radians(self.angle))
        if self.down:
            self.ad.line(dx, dy)
        else:
            self.ad.move(dx, dy)
        return dx, dy

    def rotate(self, angle):
        self.angle += angle
