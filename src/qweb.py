# -*- coding: utf-8 -*-
'''
Created on 02/03/2012

@author: heli
'''

from PyQt4.QtGui import *
from PyQt4.QtCore import *
from PyQt4.QtWebKit import *
import BaseDatos
import sys
class ventana_web(QDialog):
  def __init__(self):
    QDialog.__init__(self)
    self.web=QWebView(self)
    self.web.show()
    qqu=QUrl("tick.html")
    self.web.setUrl(qqu)
    
    
    
    
qapp=QApplication(sys.argv)
bd=BaseDatos.base_datos()
from ticket import Ticket
from venta import Venta
a=Ticket(Venta(6))
form =ventana_web()
form.show()
qapp.exec_()
    