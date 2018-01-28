from pyx import *
from pyx.metapost.path import beginknot, roughknot, endknot,smoothknot,tensioncurve

c = canvas.canvas()

p = [(1,-1),(2,-1.5),(3,-1),(4,-1.8),(3.1,-2.5),(4,-3.5),(3,-4.5),(2,-4),(1,-4.5),(0,-3)]
apple = metapost.path.path( [ beginknot(*p[5]), tensioncurve(), smoothknot(*p[6]), tensioncurve(),
                            smoothknot(*p[7]), tensioncurve(), smoothknot(*p[8]), tensioncurve(),
                            smoothknot(*p[9]), tensioncurve(), smoothknot(*p[0]), tensioncurve(),
                            smoothknot(*p[1]), tensioncurve(), smoothknot(*p[2]), tensioncurve(),
                            smoothknot(*p[3]), tensioncurve(), smoothknot(*p[4]), tensioncurve(), endknot(*p[5])])
o = [(3,0),(2.66,-0.66),(2,-1),(2.33,-0.33)]
ogon = metapost.path.path( [beginknot(*o[0]), tensioncurve(), smoothknot(*o[1]),
                            tensioncurve(), roughknot(*o[2]), tensioncurve(), smoothknot(*o[3]),
                            tensioncurve(), endknot(*o[0])])

c1=canvas.canvas([canvas.clip(apple)])
c1.stroke(path.line(0,-1,6,-1),[color.rgb.green,style.linewidth(1.6)])
c1.stroke(path.line(0,-2.6,6,-2.6),[color.rgb.red,style.linewidth(1.6)])
c1.stroke(path.line(0,-4.2,6,-4.2),[color.rgb.blue,style.linewidth(1.6)])
c.insert(c1)

c.fill(ogon, [color.rgb.green])
c.stroke(apple, [color.rgb.red])
c.writePDFfile("apple")
