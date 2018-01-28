from pyx import *
import datetime
import math

c = canvas.canvas()

czarna_obwodka = path.circle(0, 0, 10.3)
szara_obwodka = path.circle(0, 0, 11)
wypelnienie_srodka = path.circle(0, 0, 9.4)
os_srodka = path.circle(0, 0, 0.5)
przedzialek = path.line(0, 0, 0, 9.9)

for tick in range(0,60):
    if tick % 5 == 0:
        c.stroke(przedzialek, [style.linewidth(0.3), trafo.rotate(6*tick)])
    else:
        c.stroke(przedzialek, [trafo.rotate(6*tick)])

c.stroke(wypelnienie_srodka,[ deco.filled([color.grey(1)]), color.cmyk.White])

katy = [x*(360/12)+60 for x in range(12,0,-1)]
cyfry = [x for x in range(1,13)]

radius = 8
for cy, k  in zip(cyfry, katy):
    c.text(0, 0, str(cy), [trafo.translate(radius*math.cos(math.radians(k))-0.5,
                            radius*math.sin(math.radians(k))-0.5),
                            trafo.scale(sx=5.5, sy=5.5) ])


aktualny_czas = datetime.datetime.now().time()
wskazowka_godzina = path.line(0, 0, 0, 8.5)
wskazowka_minuta = path.line(0, 0, 0, 10.5)

c.stroke(wskazowka_godzina,[style.linewidth(0.6), trafo.translate(0, -2),
                   trafo.rotate(-30*(aktualny_czas.hour-12))])
c.stroke(wskazowka_minuta,[style.linewidth(0.2), trafo.translate(0,-2),
                  trafo.rotate(-5*aktualny_czas.minute)])
c.stroke(os_srodka, [deco.filled([color.rgb.black])])
c.stroke(szara_obwodka, [style.linewidth(1.6), color.cmyk.Gray])
c.stroke(czarna_obwodka, [style.linewidth(0.2)])

c.writePDFfile('zegar.pdf');
