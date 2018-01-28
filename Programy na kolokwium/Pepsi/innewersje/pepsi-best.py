from pyx import *
from pyx.metapost.path import beginknot, endknot, smoothknot, tensioncurve

c = canvas.canvas()

marginesy = path.path(
    path.moveto(0,0), path.lineto(0,1), path.closepath(),
    path.moveto(284,0),path.lineto(284,1), path.closepath()
)

lewy_czerwony = path.path(
    path.moveto(102, -8), path.lineto(8, -8), path.lineto(8, -192), path.lineto(102, -192),
    path.closepath()
)

prawy_niebieski = path.path(
    path.moveto(180, -8), path.lineto(275, -8), path.lineto(275, -192), path.lineto(180, -192),
    path.closepath()
)

pusty_srodek = path.circle(141, -100, 98)

lezka_gora = metapost.path.path([
    beginknot(64,-56), tensioncurve(), smoothknot(100,-21), tensioncurve(),
    smoothknot(141,-10), tensioncurve(), smoothknot(185,-21), tensioncurve(),
    endknot(225,-70),
    beginknot(225,-70), tensioncurve(), smoothknot(180,-56), tensioncurve(),
    smoothknot(142,-60), tensioncurve(),smoothknot(100,-66), tensioncurve(),
    endknot(64,-56)
])

lezka_dol = metapost.path.path([
    beginknot(58,-130), tensioncurve(), smoothknot(100,-145), tensioncurve(),
    smoothknot(140,-140), tensioncurve(), smoothknot(178,-134), tensioncurve(),
    endknot(218,-144),
    beginknot(218,-144), tensioncurve(), smoothknot(190,-174), tensioncurve(),
    smoothknot(141,-190), tensioncurve(),smoothknot(91,-174), tensioncurve(),
    endknot(58,-130)
])


c.stroke(lewy_czerwony, [deco.filled([color.rgb.red]), color.rgb.red ])
c.stroke(prawy_niebieski, [deco.filled([color.cmyk.Cyan]), color.cmyk.Cyan ])
c.stroke(pusty_srodek, [deco.filled([color.cmyk.White]), color.cmyk.White ])
#c.text(54,-120, "PEPSI", [trafo.scale(sx=170, sy=160), color.cmyk.Blue])
c.stroke(marginesy, [color.cmyk.White, style.linewidth(1)])

c.stroke(lezka_gora, [deco.filled([color.rgb.red]), color.rgb.red])
c.stroke(lezka_dol, [deco.filled([color.cmyk.Blue]), color.cmyk.Blue])

c.writePDFfile('pepsi.pdf')
