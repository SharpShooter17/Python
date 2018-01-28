from pyx import *
from pyx.metapost.path import beginknot, roughknot, endknot,smoothknot,tensioncurve


styll=[style.linewidth(0.4),style.linecap.round, color.cmyk.Green]
drawpath=path.line(0,-2,6,-2)
drawpath2=path.line(0,-1,6,-1)
drawpath3=path.line(0,-3,6,-3)
drawpath4=path.line(0,-4,6,-4)

c=canvas.canvas()
p1,p2,p3,p4,p5,p6,p7,p8,p9,p10=(1,-1),(2,-1.5),(3,-1),(4,-1.7),(3.2,-2.6),(4,-3.5),(3,-4.5),(2,-4),(1,-4.5),(0,-3)
o1,o2,o3,o4=(3,0),(2.66,-0.66),(2,-1),(2.33,-0.33)
tail=metapost.path.path([
        beginknot(*o1),tensioncurve(),smoothknot(*o2),tensioncurve(),
        roughknot(*o3),tensioncurve(),smoothknot(*o4),tensioncurve(),endknot(*o1)])
apple=metapost.path.path([
        beginknot(*p6),tensioncurve(),smoothknot(*p7),tensioncurve(),smoothknot(*p8),tensioncurve(),smoothknot(*p9),tensioncurve(),
        smoothknot(*p10),tensioncurve(),smoothknot(*p1),tensioncurve(),smoothknot(*p2),tensioncurve(),smoothknot(*p3),tensioncurve(),
        roughknot(*p4),tensioncurve(),smoothknot(*p5),tensioncurve(),endknot(*p6)])
c1=canvas.canvas([canvas.clip(apple)])
c1.stroke(drawpath2,[color.rgb.green,style.linewidth(1)])
c1.stroke(drawpath,[color.cmyk.Yellow,style.linewidth(1.0)])
c1.stroke(drawpath3,[color.rgb.red,style.linewidth(1.0)])
c1.stroke(drawpath4,[color.rgb.blue,style.linewidth(1.0)])
c.insert(c1)
c.stroke(tail,[color.rgb.green])
c.fill(tail,[color.rgb.green])

c.stroke(apple)
c.writePDFfile("apple")
