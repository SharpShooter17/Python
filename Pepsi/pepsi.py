from pyx import *

c = canvas.canvas()

circle = path.circle(3, 2, 2)
sCircle = path.circle(3, 2, 1.75)

ramka = path.rect(0, 0, 6, 4)
c.fill(path.rect(0,0, 3, 4), [color.rgb.red])
c.fill(path.rect(3,0, 3, 4), [color.rgb.blue])
c.stroke(ramka, [style.linewidth.THICK, color.rgb.white])
c.fill(circle, [style.linewidth.THICK, color.rgb.white])

upline = path.line(0, 1, 6, 1)
downline = path.line(0,3,6,3)

isects_circle, isecLine = sCircle.intersect(upline)
isc, iscl = sCircle.intersect(downline)

arc1, arc2 = sCircle.split(isects_circle)
c.fill(arc2, [color.rgb.red])
ard1, ard2 = sCircle.split(isc);
c.fill(ard2, [color.rgb.blue]);
text.set(mode="latex", pyxgraphics=0)
text.preamble(r"\usepackage{anyfontsize}")
c.text(3, 2, r"\fontsize{26}{26} \textsf{PEPSI}", [text.halign.boxcenter, text.halign.flushcenter])
c.writePDFfile("pepsi")
