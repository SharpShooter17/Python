from pyx import *
from pyx.metapost.path import beginknot, endknot, smoothknot, tensioncurve
from PIL import ImageDraw


c = canvas.canvas()

falastart = path.arc(5, 7, 2, 248, 300)
falaend = path.arc(10, 4, 2, 30, 140)
falamid1 = path.arc(8.7, 1.4, 5.2, 80, 120)
falamid2 = path.arc(6.5, 8, 4, -120, -60)
falamid3 = path.arc(10, 1.4, 3.5, 70, 120)
falaend2 = path.arc(12.8, 6.2, 2, -120, -113)



c.stroke(path.rect(0,0,8,9.8),[style.linewidth(0.03), color.gray.white])
c.stroke(path.rect(8,0,7.6,9.8),[deco.filled([color.rgb(0.1,0.7,1)])])
c.stroke(path.rect(8,0,8,9.8),[style.linewidth(0.03), color.gray.white])
c.stroke(path.rect(0.4,0,8,9.8),[deco.filled([color.rgb.red])])

c.stroke(path.circle(8,5,5),[deco.filled([color.gray.white])])

red = path.path(path.moveto(8,5), path.arc(8,5,5,0,180), path.closepath())
blue = path.path(path.moveto(8,5), path.arc(8,5,5,180,0), path.closepath())






c.stroke(red, [deco.filled([color.rgb.red])])
c.stroke(blue, [deco.filled([color.rgb(0.3,0.05,1)])])

c.stroke(path.path(falastart), [style.linewidth(3), style.linecap.round, color.rgb.white])

c.stroke(path.path(falaend), [style.linewidth(3), style.linecap.round, color.rgb.white])
c.stroke(path.path(falaend2), [style.linewidth(2), style.linecap.round, color.rgb.white])

c.stroke(path.circle(8,5,5),[style.linewidth(0.5), color.gray.white])

c.stroke(path.path(falamid1), [style.linewidth(2), style.linecap.round, color.rgb.white])
c.stroke(path.path(falamid2), [style.linewidth(2), style.linecap.round, color.rgb.white])
c.stroke(path.path(falamid3), [style.linewidth(2), style.linecap.round, color.rgb.white])

c.writePDFfile("test.pdf")
