# -*- coding: utf-8 -*-
'''
Created on 01/03/2012

@author: heli
'''
from venta import Venta
class Ticket():
  def __init__(self, Venta):
    self.venta = Venta
    base_dir = "./"
    self.archivo = open(base_dir + "tick.html", 'w')
    
    self.escribir_datos()
    self.archivo.close()
    
  def escribir_datos(self):
    p = lambda x:self.archivo.write("" + str(x) + "<br/>\n")
    w = lambda x:self.archivo.write(str(x) + "\n")
    
    #w("<div style='width:300px'>")
    w("""<p align=center><img src="logo.png" width=250px /></p>""")
    
    w("<div style='text-align:center'>")
    p("ACCESORIOS, REPARACION")
    p("Y MANTENIMIENTO")
    
    p("DE EQUIPO DE COMPUTO")
    p("FCO. I. MADERO #519")
    p("COL. ALTAMIRA")
    p("SANTIAGO PAPASQUIARO, DURANGO.")
    p("TEL: 674 862 45 58")
    
    w("<br/>")
    p("CLIENTE " + str(self.venta.cliente).upper())
    p("LE ATENDIO " + str(self.venta.usuario).upper())
    p("NOTA #%d" % self.venta.id)
    p(self.venta.fecha)
    p(self.venta.hora)
    w("</div>")
    p("")
    
    w("<table width=100% style='text-align:center'><tr><td>CODIGO</td><td>PRODUCTO</td></tr></table>")
    w("<table width=100% style='text-align:center'><tr><td>#</td><td>PRECIO</td><td>SUBT</td></tr></table>")
    
    for i in self.venta.productos.keys():
      
      w("<hr/>")
      w("<table width=100% style='text-align:center'><tr><td>" + str(i[:9]).upper() + "</td><td>" + str(self.venta.productos[i].nombre[:19]).upper() + "</td></tr></table>")
      w("<table width=100%" + " style='text-align:center'><tr><td>%d</td><td>$%.2f</td><td>$%.2f</td></tr></table>" % (self.venta.productos[i].cantidad, self.venta.productos[i].precio, self.venta.productos[i].subtotal))
      
    p("")
    p("")
    w("<div style='text-align:right'>")
    p("TOTAL: $" + str(self.venta.total))
    
    p("PAGADO: $" + str(self.venta.pagado))
    p("SU CAMBIO: $" + str(self.venta.pagado - self.venta.total))
    w("</div>")
    p("")
    w("<div style='text-align:center'>")
    p("GRACIAS POR SU PREFERENCIA")
    p("CAMBIOS Y ACLARACIONES")
    p("PRESENTANDO SU TICKET")
    
    w("</div>")
    #w("</div>")
    
    
    
