from pyx import *
from math import *
c = canvas.canvas()
r=6
kolo1 = path.arc(0, 0, r, 0, 360)
c.stroke(path.path(kolo1), [style.linewidth.thick, style.linestyle.dashed, color.rgb.black])
#c.text(0,r-0.6,r"12",[text.size.LARGE])
#c.text(-r+0.4,0,r"9",[text.size.LARGE])
#c.text(r-0.4,0,r"3",[text.size.LARGE])
#c.text(0,-r+0.4,r"6",[text.size.LARGE])
#c.text(3,r-1.5,r"1", [text.size.LARGE])
#c.text(4.8,r-3.5,r"2",[text.size.LARGE])
#c.text(5,-2.5, r"4",[text.size.LARGE])
#c.text(3,-4.8, r"5",[text.size.LARGE])    
#c.text(-3,-4.8, r"7",[text.size.LARGE])
#c.text(-5,-2.5, r"8",[text.size.LARGE]) 
#c.text(-5,2.5, r"10",[text.size.LARGE])
#c.text(-3,4.7, r"11",[text.size.LARGE])
hours = path.path(path.moveto(0, 4.5), path.lineto(-0.15, -0.5),
                  path.lineto(0.15, -0.5), path.closepath())
minuts=path.path(path.moveto(4.5, 0), path.lineto(-0.5, -0.1),
                  path.lineto(-0.5, 0.1), path.closepath())
seconds=path.path(path.moveto(-3, 4.0), path.lineto(0.05, -0.1),
                  path.lineto(0.1, -0.2), path.closepath())
c.stroke(hours, [style.linewidth.thick, deco.filled([color.rgb.black])])
c.stroke(minuts, [style.linewidth.thick, deco.filled([color.rgb.black])])
c.stroke(seconds, [style.linewidth.thick, deco.filled([color.rgb.red])])
c.writePDFfile("zegar-kolokwium-python")
