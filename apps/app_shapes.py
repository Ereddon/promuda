from promudaLib import LCD as lcd
from math import cos,pi,sin

def DrawCircle(x, y, r, fb):
  i=0
  for i in range(360):
    angle = i;
    x1 = int(r * cos(angle * pi / 180))
    y1 = int(r * sin(angle * pi / 180))
    fb.pixel(x + x1, y + y1, 1)
  fb.show()

DrawCircle(15,15,15,lcd)


