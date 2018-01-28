from pyx import *

redBox = path.rect(0,0,50,50)
blueBox = path.rect(50,0,50,50)
bigWhiteCircle = path.circle(50,25,25)
smallWhiteCircle = path.circle(50,25,23)
sectionLine = path.line(25,25,75,25)
whiteBox = path.rect(26.65,17,46.65,17)
text.set(mode="latex", pyxgraphics=0)


cv = canvas.canvas()

cv.fill(redBox, [color.rgb.red])
cv.fill(blueBox, [color.rgb.blue])   
cv.fill(bigWhiteCircle, [color.rgb.white])
cv.fill(smallWhiteCircle, [color.rgb.white])
cv.stroke(sectionLine, [color.rgb.white])

isects_circle, isects_line = smallWhiteCircle.intersect(sectionLine)
for isect in isects_circle:
    isectx, isecty = smallWhiteCircle.at(isect)
arc1, arc2 = smallWhiteCircle.split(isects_circle)
cv.fill(arc1, [color.rgb.blue])
cv.fill(arc2, [color.rgb.red])
cv.fill(whiteBox, [color.rgb.white])
# p = path.line(4, 0, 5, 0) << path.line(5, 0, 5, 1) << path.line(5, 1, 4, 1)
# p.append(path.closepath())
# cv.fill(p, [color.rgb.white])
# p1 = path.curve(0, 0, 1, 0, 6, 2, 8, 2)
# cv.stroke(p1)
cv.writePDFfile("Pepsi")
