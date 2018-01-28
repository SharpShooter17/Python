from pyx import *
from pyx.metapost.path import beginknot, endknot, smoothknot, tensioncurve
c = canvas.canvas()
tylda1 = metapost.path.path([
    beginknot(*(90,-120)), tensioncurve(), smoothknot(*(125,-115)), tensioncurve(),
    smoothknot(*(160,-130)), tensioncurve(), smoothknot(*(190,-115)), tensioncurve(1.5), endknot(*(90,-120))])
tylda2 = metapost.path.path([
    beginknot(*(90,-120)), tensioncurve(), smoothknot(*(125,-115)), tensioncurve(),
    smoothknot(*(160,-130)), tensioncurve(), smoothknot(*(190,-115)), tensioncurve(1.5), endknot(*(90,-120))])
c.fill(tylda1, [style.linewidth(0.1), color.cmyk.Orange,
                 trafo.scale(sx=0.1, sy=0.1), color.rgb.blue, trafo.mirror(180), trafo.mirror(90)])
c.fill(tylda2,  [style.linewidth(0.1), color.cmyk.Orange,
                 trafo.scale(sx=0.1, sy=0.1), color.rgb.red, trafo.translate(-28,27)])
#c.text(-16,12.8,"PEPSI",[trafo.scale(5), color.rgb.blue])

#c.stroke(tylda, tylda_orange)
c.writePDFfile()
