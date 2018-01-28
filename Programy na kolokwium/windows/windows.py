from pyx import *
from math import *
from pyx.metapost.path import beginknot, endknot, smoothknot, tensioncurve

scale = input('Podaj skale (1.23): ')
def drawSin(y):
    x = -0.3

    pg1, pg2, pg3 = (0 + 8 * x*scale, sin(0 + x*scale)*0.3+y), (1 + 8 * x*scale, sin(1 + x*scale)*0.3+y), (2 + 8 * x*scale, sin(2 + x*scale)*0.3+y)
    pg4, pg5, pg6 = (3 + 8 * x+(scale), sin(3 + x+(scale))*0.3+y), (4 + 8 * x+(scale), sin(4 + x+(scale))*0.3+y), (5 + 8 * x+(scale), sin(5 + x+(scale))*0.3+y)
    path = metapost.path.path([
        beginknot(*pg1), tensioncurve(), smoothknot(*pg2), tensioncurve(),
        smoothknot(*pg3), tensioncurve(), smoothknot(*pg4), tensioncurve(),
        smoothknot(*pg5), tensioncurve(), endknot(*pg6)])
    return path

c = canvas.canvas()

kolo1 = path.circle(0, 0, 3.2*scale)

styl1 = [style.linewidth(0.4*scale), style.linecap.round, color.rgb.blue]

c.stroke(kolo1, styl1)
r1 = input('Podaj R (0/255) R: ')
r2 = input('Podaj G (0/255) R: ')
r3 = input('Podaj B (0/255) R: ')

g1 = input('Podaj R (0/255) G: ')
g2 = input('Podaj G (0/255) G: ')
g3 = input('Podaj B (0/255) G: ')

b1 = input('Podaj R (0/255) B: ')
b2 = input('Podaj G (0/255) B: ')
b3 = input('Podaj B (0/255) B: ')

y1 = input('Podaj R (0/255) Y: ')
y2 = input('Podaj G (0/255) Y: ')
y3 = input('Podaj B (0/255) Y: ')
paleRed = color.rgb(r1/256.0,r2/256.0,r3/256.0)
paleGreen = color.rgb(g1/256.0,g2/256.0,g3/256.0)
paleBlue = color.rgb(b1/256.0,b2/256.0,b3/256.0)
paleYellow = color.rgb(y1/256.0,y2/256.0,y3/256.0)

c.fill(kolo1, [color.rgb.blue])
c.fill(path.rect(-1.6*scale,0*scale,1.9*scale,1.6*scale),[paleRed])
c.fill(path.rect(0.1*scale,-0.2*scale,1.7*scale,1.65*scale),[paleGreen])
c.fill(path.rect(-1.8*scale,-1.5*scale,1.7*scale,1.6*scale),[paleBlue])
c.fill(path.rect(-0.1*scale,-1.62*scale,1.7*scale,1.556*scale),[paleYellow])
c.stroke(path.line(-2*scale,-2*scale,-1.4*scale,2*scale),[style.linewidth(0.35*scale),color.rgb.blue])
c.stroke(path.line(-0.3*scale,-2*scale,0.3*scale,2*scale),[style.linewidth(0.35*scale),color.rgb.blue])
c.stroke(path.line(1.4*scale,-2*scale,2*scale,2*scale),[style.linewidth(0.35*scale),color.rgb.blue])

c.stroke(drawSin(1.45*scale), [style.linewidth(0.5*scale),color.rgb.blue])
c.stroke(drawSin(-0.1*scale), [style.linewidth(0.45*scale),color.rgb.blue])
c.stroke(drawSin(-1.75*scale), [style.linewidth(0.5*scale),color.rgb.blue])

c.writePDFfile()
