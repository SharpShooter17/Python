from pyx import *
from pyx.metapost.path import beginknot, endknot, smoothknot, tensioncurve

black = [deco.filled([color.rgb.black]), trafo.scale(sx=0.2, sy=0.2)]

wycinek_blue = [style.linewidth(6), color.rgb.blue,
                  trafo.scale(sx=0.2, sy=0.9*0.2)]

tylda_orange = [style.linewidth(4), color.cmyk.Orange,
                 trafo.scale(sx=0.2, sy=0.2)]

c = canvas.canvas()

body = path.path(path.moveto(0,0),path.lineto(246,0),
                 path.lineto(246,-110),
                  path.curveto(234,-158, 204,-206, 156,-230),
                  path.lineto(90,-230),
                 path.curveto(42,-206, 12,-158, 0,-110),
                  path.closepath())

pret1 = path.path(path.moveto(34,0),path.lineto(34,108),
                  path.lineto(62,108),path.lineto(62,0),
                 path.closepath())

pret2 = path.path(path.moveto(186,0),path.lineto(186,108),
                  path.lineto(214,108),path.lineto(214,0),
                  path.closepath())

kulka = path.circle(123,-240,35)

kabel = path.path(path.moveto(102,-240),path.lineto(102,-360),
                  path.lineto(144,-360),path.lineto(144,-240),
                  path.closepath())

wycinek = path.path(path.arc(123, -130, 85, 0, 270))

tylda = metapost.path.path([
    beginknot(*(90,-135)), tensioncurve(), smoothknot(*(125,-115)), tensioncurve(),
   smoothknot(*(160,-140)), tensioncurve(), endknot(*(190,-120))])

c.stroke(pret1, black)
c.stroke(pret2, black)
c.stroke(kulka, black)
c.stroke(kabel, black)
c.stroke(body, black)

c.stroke(wycinek, wycinek_blue)

c.stroke(tylda, tylda_orange)

c.writePDFfile('wtyczka.pdf')
