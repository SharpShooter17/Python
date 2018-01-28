from pyx import *

c = canvas.canvas()

# E duze

duzeE = path.path(path.arcn(0,0,2,270,360))
duzeEfala1 = path.curve(-0.7,-0.2,-0.3,0.3,0.1,0.3,0.5,-0.21)
duzeEfala2 = path.curve(0.5,-0.2,0.9,-0.7,1.3,-0.7,1.6,-0.2)

c.stroke(duzeE,[style.linewidth(0.65), color.cmyk.Blue])
c.stroke(duzeEfala1,[style.linewidth(0.35), color.cmyk.Orange])
c.stroke(duzeEfala2,[style.linewidth(0.35), color.cmyk.Orange])

# W
W1 = path.curve(-2.9,-2.9,-2.9,-3,-2.9,-3,-2.9,-4.1)
W2 = path.curve(-2.9,-4.1,-2.3,-3.8,-2.4,-3.5,-2.4,-2.9)
W3 = path.curve(-2.4,-2.9,-2.4,-2.9,-2.4,-2.9,-2.4,-4.1)
W4 = path.curve(-2.4,-4.1,-1.9,-3.8,-1.8,-3.5,-1.8,-2.9)

c.stroke(W1,[style.linewidth(0.2), color.cmyk.Blue])
c.stroke(W2,[style.linewidth(0.2), color.cmyk.Blue])
c.stroke(W3,[style.linewidth(0.2), color.cmyk.Blue])
c.stroke(W4,[style.linewidth(0.2), color.cmyk.Blue])
#E ptaszek

maleE = path.path(path.arcn(-1,-3.5,0.5,270,360))
maleEfala1 = path.curve(-1.2,-3.55,-1.1,-3.35,-1,-3.35,-0.9,-3.55)
maleEfala2 = path.curve(-0.9,-3.55,-0.8,-3.75,-0.7,-3.75,-0.6,-3.55)

c.stroke(maleE,[style.linewidth(0.2), color.cmyk.Blue])
c.stroke(maleEfala1,[style.linewidth(0.1), color.cmyk.Orange])
c.stroke(maleEfala2,[style.linewidth(0.1), color.cmyk.Orange])

# E zwykle

maleEnormalne = path.path(path.arcn(0.35,-3.5,0.5,270,360))
maleEcurve = path.curve(0.95,-3.5,0.35,-3.5,0.35,-3.5,0.2,-3.5)

c.stroke(maleEnormalne,[style.linewidth(0.2), color.cmyk.Blue])
c.stroke(maleEcurve,[style.linewidth(0.2), color.cmyk.Blue])

#I

I =  path.curve(1.2,-3,1.2,-4,1.2,-4,1.2,-4)
c.stroke(I,[style.linewidth(0.2), color.cmyk.Blue])

#A

A =  path.path(path.arcn(2,-3.5,0.5,270,360))
c.stroke(A,[style.linewidth(0.2), color.cmyk.Blue])

Acurve = path.curve(2.5,-3.4,2.5,-3.5,2.5,-3.6,2.5,-3.9)
c.stroke(Acurve,[style.linewidth(0.2), color.cmyk.Blue])

c.writePDFfile("Logo")
