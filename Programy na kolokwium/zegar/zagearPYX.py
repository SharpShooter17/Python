from pyx import *
import time as tm
import datetime as dt
import math as mt


c = canvas.canvas()
circle = path.circle(0, 0, 6)
c.stroke(circle, [style.linewidth.Thick])
hourLine = path.line(0, 6, 0, 5)
c.stroke(hourLine, [style.linewidth.Thick])
#rysowanie zegara bez wskazowek
for i in range(12):
    c.stroke(hourLine, [trafo.rotate(30.1*i), style.linewidth.Thick])

t = tm.localtime()
hour = t.tm_hour % 12
minutes = t.tm_min
seconds = t.tm_sec
w_min_ray = 3

wskazowkaH = path.line(
    0, 0,
    w_min_ray * mt.sin(mt.radians(360 * (hour * 60 + minutes) / 720)),
    w_min_ray * mt.cos(mt.radians(360 * (hour * 60 + minutes) / 720))
)
w_min_ray = 4
wskazowkaMin = path.line(
    0, 0,
    w_min_ray * mt.sin(mt.radians(360 * (minutes * 60 + seconds) / 3600)),
    w_min_ray * mt.cos(mt.radians(360 * (minutes * 60 + seconds) / 3600))
)
w_min_ray = 5
wskazowkaSec = path.line(
    0, 0,
    w_min_ray * mt.sin(mt.radians(360 * seconds / 60)),
    w_min_ray * mt.cos(mt.radians(360 * seconds / 60))
)

c.stroke(wskazowkaH, [style.linewidth(0.3), style.linecap.round, color.rgb.blue])
c.stroke(wskazowkaMin, [style.linewidth(0.2), style.linecap.round, color.rgb.green])
c.stroke(wskazowkaSec, [style.linewidth(0.1), style.linecap.round, color.rgb.red])
c.writePDFfile()
