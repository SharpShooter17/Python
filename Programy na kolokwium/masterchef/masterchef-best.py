from pyx import *
import math
from pyx.metapost.path import beginknot, endknot, smoothknot, tensioncurve

c = canvas.canvas()
r = 3

kolo1 = path.arc(6, 0, 6, 90, 280)
kolo2 = path.arc(6, 0.75, 5.25, 270, 90)

kolo3 = path.arc(6, 0, 4.5, 90, 270)
kolo4 = path.arc(6, 0.75, 3.75, 0, 90)

kolo5 = path.arc(7.25, 0.75, 2.5, 276, 360)


#rysowanie lukow
c.stroke(path.path(kolo1), [style.linewidth(0.7), style.linecap.round, color.rgb(1,0.4,0)])
c.stroke(path.path(kolo2), [style.linewidth(0.7), style.linecap.round, color.rgb(1,0.4,0)])
c.stroke(path.path(kolo3), [style.linewidth(0.7), style.linecap.round, color.rgb(1,0.4,0)])
c.stroke(path.path(kolo4), [style.linewidth(0.7), style.linecap.round, color.rgb(1,0.4,0)])
c.stroke(path.path(kolo5), [style.linewidth(0.7), style.linecap.round, color.rgb(1,0.4,0)])


#rysowanie linii + podwojenie zeby dol byl przedluzony
line = path.line(3.45, -1.7, 3.45, 1)
c.stroke(line, [style.linewidth(0.6), style.linecap.round, color.rgb(1,0.4,0)])
line = path.line(3.55, -1.7, 3.55, 1)
c.stroke(line, [style.linewidth(0.6), style.linecap.round, color.rgb(1,0.4,0)])

line = path.line(5.45, -1.7, 5.45, 1)
c.stroke(line, [style.linewidth(0.6), style.linecap.round, color.rgb(1,0.4,0)])
line = path.line(5.55, -1.7, 5.55, 1)
c.stroke(line, [style.linewidth(0.6), style.linecap.round, color.rgb(1,0.4,0)])

line = path.line(7.45, -1.7, 7.45, 1)
c.stroke(line, [style.linewidth(0.6), style.linecap.round, color.rgb(1,0.4,0)])
line = path.line(7.55, -1.7, 7.55, 1)
c.stroke(line, [style.linewidth(0.6), style.linecap.round, color.rgb(1,0.4,0)])


#rysowanie linii lamanych (tekst) zeby bylo lagodne zaokraglenie a nie ostre jak w arcach
linia = path.curve(3.5, 1, 3.5, 1.75, 4.5, 1.75, 4.5, 1.75)
c.stroke(linia, [style.linewidth(0.7), style.linecap.round, color.rgb(1,0.4,0)])
linia = path.curve(4.5, 1.75, 4.5, 1.75, 5.5, 1.75, 5.5, 1)
c.stroke(linia, [style.linewidth(0.7), style.linecap.round, color.rgb(1,0.4,0)])

linia = path.curve(5.5, 1, 5.5, 1.75, 6.5, 1.75, 6.5, 1.75)
c.stroke(linia, [style.linewidth(0.7), style.linecap.round, color.rgb(1,0.4,0)])
linia = path.curve(6.5, 1.75, 6.5, 1.75, 7.5, 1.75, 7.5, 1)
c.stroke(linia, [style.linewidth(0.7), style.linecap.round, color.rgb(1,0.4,0)])

    
c.writePDFfile()
