import math

class Turtle:
    def __init__(self):
        self.angle = 0

    def forward(self, distance):
        dx = distance * math.cos(math.radians(self.angle))
        dy = distance * math.sin(math.radians(self.angle))
        move_relative(dx, dy)
        return dx, dy

    def rotate(self, angle):
        self.angle += angle
