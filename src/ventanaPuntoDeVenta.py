# -*- coding: utf-8 -*-
'''
Created on 01/03/2012

@author: heli
'''

from PyQt4.QtGui import *
from PyQt4.QtCore import *
from PyQt4.QtWebKit import *
from ui.punto_de_venta_ui import Ui_dialogo_pdeventa
import sys
from venta import Venta
import BaseDatos
from ui.pagar_ui import Ui_dialogo_pagar
from ventanaNuevoProducto import ventana_nuevo_producto
from producto import producto
from PyQt4 import phonon
class ventana_punto_de_venta(QDialog, Ui_dialogo_pdeventa):
  def __init__(self):
    QDialog.__init__(self)
    self.setupUi(self)
    self.line_codigo.setFocus()
    self.venta = Venta(-1)
    self.venta.nueva_venta(1)
    
    self.line_codigo.returnPressed.connect(self.agregar_producto)
    self.fecha = QDate.currentDate().toString()
    self.lbl_fecha.setText(self.fecha)
    self.hora = QTime.currentTime().toString()
    self.lbl_hora.setText(self.hora)
    
    self.timer = QTimer()
    self.timer.setInterval(1000)
    self.timer.timeout.connect(self.actualizar_hora)
    self.timer.start()
    
    self.table_productos.setColumnCount(6)
    cabecera = (u"Código", "Producto", "Precio", "#", "Dcto", "Subtotal")
    self.table_productos.setHorizontalHeaderLabels(cabecera)
    
    self.pb_pagar.clicked.connect(self.efectuar_venta)
    
    icon=QIcon()
    icon.addPixmap(QPixmap("imagenes/enviar.png"),QIcon.Normal,QIcon.Off)
    self.pb_pagar.setIcon(icon)
    self.pb_buscar.setIcon(QIcon("imagenes/buscar.png"))
    self.pb_borrar.setIcon(QIcon("imagenes/borrar.png"))
    self.pb_pagar.setMinimumSize(10, 48)
    self.pb_borrar.setMinimumSize(10, 48)
    self.pb_buscar.setMinimumSize(10, 48)
    
    self.table_productos.setColumnWidth(0,120)
    self.table_productos.setColumnWidth(1,310)
    self.table_productos.setColumnWidth(2,120)
    self.table_productos.setColumnWidth(3,75)
    self.table_productos.setColumnWidth(4,75)
    self.table_productos.setColumnWidth(5,250)
    self.lbl_logo.setPixmap(QPixmap("imagenes/logo.png"))
    self.lbl_logo.setScaledContents(True)
    self.lbl_logo.setMinimumSize(617, 10)
    style="QDialog{background:white; border:solid; padding:10px}"
    self.setStyleSheet(style)
    
    self.actualizar_productos()
    self.reproducir_video()
    
  def reproducir_video(self):
    self.vp_comercial.play(phonon.Phonon.MediaSource("video.mp4"))
    
    
  def efectuar_venta(self):
    self.vpagar = ventana_pagar(self.venta)
    self.vpagar.show()
    

    
    
  def actualizar_hora(self):
    self.hora = QTime.currentTime().toString()
    self.lbl_hora.setText(self.hora)
    if not self.venta.es_nueva:
      self.venta = Venta(-1)
      self.actualizar_productos()
    
    
  def agregar_producto(self):
    codigo = self.line_codigo.text()
    if len(codigo) < 3:
      self.line_codigo.clear()
      return
    cantidad = 1
    if len(codigo.split('*')) == 1:
      cantidad = 1
    else:
      cantidad = int(codigo.split('*')[0])
      codigo = str(codigo.split('*')[1])
      
    descuento = 0
    if len(codigo.split('/')) == 2:
      descuento = int(codigo.split('/')[0])
      codigo = str(codigo.split('/')[1])
    
    print producto(codigo).existe
    if producto(codigo).existe:
      resultado = self.venta.agregar_producto(codigo, cantidad, descuento)
      print resultado
      if resultado == 0:
        gg = QMessageBox(self)
        gg.setText("Error al agregar producto, no existe o la cantidad excedio la existencia")
        gg.setStandardButtons(gg.Ok)
        gg.exec_()
        self.line_codigo.clear()
        self.line_codigo.setFocus()
        
      
      else:
        self.line_codigo.clear()
        self.line_codigo.setFocus()
        self.actualizar_productos()
        
    else:
      gg=QMessageBox()
      gg.setText("Producto no existe desea Agregarlo??")
      gg.setStandardButtons(gg.Ok|gg.Cancel)
      gg.exec_()
      if gg.result()==gg.Ok:
        self.vap=ventana_nuevo_producto()
        self.vap.line_codigo.setText(codigo)
        self.vap.line_codigo.setEnabled(False)
        self.vap.llamado=True
        self.vap.show()
      else:
        self.line_codigo.setFocus()
        self.line_codigo.clear()
      
    
  
  def actualizar_productos(self):
    numero_productos = len(self.venta.productos.keys())
    self.table_productos.setRowCount(numero_productos)
    cont = 0
    for i in self.venta.productos.keys():
      g = self.venta.productos[i]
      qcod = QTableWidgetItem(g.codigo)
      self.table_productos.setItem(cont, 0, qcod)
      
      qnom = QTableWidgetItem(g.nombre)
      qpre = QTableWidgetItem(str(g.precio))
      qcan = QTableWidgetItem(str(g.cantidad))
      
      qdes = QTableWidgetItem(str(g.descuento))
      qsub = QTableWidgetItem(str(g.subtotal))
      
      self.table_productos.setItem(cont, 1, qnom)
      self.table_productos.setItem(cont, 2, qpre)
      self.table_productos.setItem(cont, 3, qcan)
      self.table_productos.setItem(cont, 4, qdes)
      self.table_productos.setItem(cont, 5, qsub)
      
      
      cont += 1
    
    self.lbl_total.setText("$ " + str(self.venta.total))
    if self.venta.total<=0:
      self.pb_pagar.setEnabled(False)
    else:
      self.pb_pagar.setEnabled(True)
    

class ventana_pagar(QDialog, Ui_dialogo_pagar):
  def __init__(self, Venta):
    QDialog.__init__(self)
    self.setupUi(self)
    self.venta = Venta
    self.total = self.venta.total
    
    self.pb_aceptar.setEnabled(False)
    self.dsb_efectivo.valueChanged.connect(self.cambio_valor)
    self.pb_aceptar.clicked.connect(self.efectuar_venta)
    
  def cambio_valor(self):
    asd = float(self.dsb_efectivo.value())
    self.lbl_cambio.setText("$%.2f" % (asd - self.total))
    if asd - self.total >= 0:
      self.pb_aceptar.setEnabled(True)
    else:
      self.pb_aceptar.setEnabled(False)
    
    
  def efectuar_venta(self):
    self.venta.fecha = QDate.currentDate().toString("yyyy-MM-dd")
    self.venta.hora = QTime.currentTime().toString("hh:mm")
    self.venta.pagado=self.dsb_efectivo.value()
    self.venta.efectuar_venta()
    if self.chk_ticket.isChecked():
      from ticket import Ticket
      a=Ticket(self.venta)
      
      htm=open("tick.html",'r').read()
      self.web=QWebView()
      self.web.load(QUrl("http://localhost/~heli/tick.html"))
      self.web.show()
      self.qp=QPrinter()
      self.qp.setOutputFormat(1)
      self.qp.setOutputFileName("ticket.pdf")
      self.web.print_(self.qp)
      
      
      
    
    
    
    self.close()
    
      
      
      
    
    
if __name__ == "__main__":
  app = QApplication(sys.argv)
  bd = BaseDatos.base_datos()
  form = ventana_punto_de_venta()
  form.showMaximized()
  app.exec_()
