from pyx import *
from pyx.metapost.path import beginknot, endknot, smoothknot, tensioncurve

wycinek_blue = [style.linewidth(6), color.rgb.blue,
                  trafo.scale(sx=0.2, sy=0.9*0.2)]

tylda_orange = [style.linewidth(4), color.cmyk.Orange,
                 trafo.scale(sx=0.2, sy=0.2)]

c = canvas.canvas()

wycinek = path.path(path.arc(123, -130, 85, 0, 270))

tylda = metapost.path.path([
    beginknot(*(90,-135)), tensioncurve(), smoothknot(*(125,-115)), tensioncurve(),
   smoothknot(*(160,-140)), tensioncurve(), endknot(*(190,-120))])

c.stroke(wycinek, wycinek_blue)

c.stroke(tylda, tylda_orange)

c.writePDFfile('weeia.pdf')
