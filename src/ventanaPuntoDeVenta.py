# -*- coding: utf-8 -*-
'''
Created on 01/03/2012

@author: heli
'''

from PyQt4.QtGui import *
from PyQt4.QtCore import *
from PyQt4.QtWebKit import *
from PyQt4.QtSql import *
from ui.punto_de_venta_ui import Ui_dialogo_pdeventa
import sys
from venta import Venta
import BaseDatos
from ui.pagar_ui import Ui_dialogo_pagar
from ventanaNuevoProducto import ventana_nuevo_producto
from producto import producto

from ui.buscar_productos_ui import Ui_dialogo_busqueda_productos


paso_producto = ""
class ventana_punto_de_venta(QDialog, Ui_dialogo_pdeventa):
  def __init__(self):
    QDialog.__init__(self)
    self.setupUi(self)
    self.resize(1024,768)
    self.line_codigo.setFocus()
    self.venta = Venta(-1)
    self.venta.nueva_venta(1)
    
    self.line_codigo.returnPressed.connect(self.agregar_producto)
    self.fecha = QDate.currentDate().toString()
    self.lbl_fecha.setText(self.fecha)
    self.hora = QTime.currentTime().toString()
    self.lbl_hora.setText(self.hora)
    
    self.timer = QTimer()
    self.timer.setInterval(500)
    self.timer.timeout.connect(self.actualizar_hora)
    self.timer.start()
    
    self.table_productos.setColumnCount(6)
    cabecera = (u"Código", "Producto", "Precio", "#", "Dcto", "Subtotal")
    self.table_productos.setHorizontalHeaderLabels(cabecera)
    
    self.pb_pagar.clicked.connect(self.efectuar_venta)
    self.pb_buscar.clicked.connect(self.mostrar_buscar_productos)
    icon = QIcon()
    icon.addPixmap(QPixmap("imagenes/enviar.png"), QIcon.Normal, QIcon.Off)
    self.pb_pagar.setIcon(icon)
    self.pb_buscar.setIcon(QIcon("imagenes/buscar.png"))
    self.pb_borrar.setIcon(QIcon("imagenes/borrar.png"))
    self.pb_pagar.setMinimumSize(10, 48)
    self.pb_borrar.setMinimumSize(10, 48)
    self.pb_buscar.setMinimumSize(10, 48)
    
    self.table_productos.setColumnWidth(0, 120)
    self.table_productos.setColumnWidth(1, 310)
    self.table_productos.setColumnWidth(2, 120)
    self.table_productos.setColumnWidth(3, 50)
    self.table_productos.setColumnWidth(4, 75)
    self.table_productos.setColumnWidth(5, 250)
    self.lbl_logo.setPixmap(QPixmap("imagenes/logo.png"))
    self.lbl_logo.setScaledContents(True)
    self.lbl_logo.setMinimumSize(617, 10)
    
    
    
    self.actualizar_productos()
    self.reproducir_video()
    self.usuario_id = 0
    
    #self.vp_comercial.setMinimumSize(200, 150)
    
    style = """QDialog{background:white; border:solid; padding:10px}    
    QCommandLinkButton{background:white}"""
    self.setStyleSheet(style)
    
    self.clb_cliente.clicked.connect(self.mostrar_clientes)
    self.pb_borrar.clicked.connect(self.eliminar_producto)
    self.clb_usuario.clicked.connect(self.logout)
    
  def mostrar_clientes(self):
    from ventanaClientes import ventana_clientes
    self.vmc = ventana_clientes(self.venta)
    self.vmc.show()
    
  def mostrar_buscar_productos(self):
    self.vbpp = ventana_buscar_producto()
    self.vbpp.show()
    
  def reproducir_video(self):
    #self.vp_comercial.play(phonon.Phonon.MediaSource("video.mp4"))
    pass
    
  def actualizar_cliente(self, cliente_id):
    self.venta.cliente_id = cliente_id
    query = QSqlQuery()
    sql = "select nombre from clientes where cliente_id=%d" % self.venta.cliente_id
    if query.exec_(sql):
      query.next()
      nombre = query.value(0).toString()
      self.clb_cliente.setText("Cliente: " + nombre)
      self.venta.cliente = nombre
    
    
  def efectuar_venta(self):
    self.vpagar = ventana_pagar(self.venta)
    self.vpagar.show()
    
  def actualizar_usuario(self):
    query = QSqlQuery()
    sql = "select nombre from usuarios where usuario_id=%d" % self.usuario_id
    if query.exec_(sql):
      query.next()
      nombre = query.value(0).toString()
      self.clb_usuario.setText("Atiende: %s" % nombre)
      self.venta.usuario = nombre
      self.venta.usuario_id=self.usuario_id
    self.actualizar_cliente(self.venta.cliente_id)
    

    
    
  def actualizar_hora(self):
    global paso_producto
    self.hora = QTime.currentTime().toString()
    self.lbl_hora.setText(self.hora)
    if not self.venta.es_nueva:
      self.venta = Venta(-1)
      self.actualizar_productos()
      
    if not paso_producto == "":
      self.line_codigo.setText(self.line_codigo.text() + paso_producto)
      paso_producto = ""
      self.line_codigo.setFocus()
    self.actualizar_cliente(self.venta.cliente_id)
      
    
    
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
    
    
    if producto(codigo).existe:
      resultado = self.venta.agregar_producto(codigo, cantidad, descuento)
      
      if resultado == 0:
        gg = QMessageBox()
        gg.setText("Error al agregar producto, no existe o la cantidad excedio la existencia")
        gg.setStandardButtons(gg.Ok)
        gg.setWindowTitle("CopyTodo - Advertencia")
        
        gg.exec_()
        self.line_codigo.clear()
        self.line_codigo.setFocus()
        
      
      else:
        self.line_codigo.clear()
        self.line_codigo.setFocus()
        self.actualizar_productos()
        
    else:
      gg = QMessageBox()
      gg.setText("Producto no existe desea Agregarlo??")
      gg.setStandardButtons(gg.Ok | gg.Cancel)
      gg.setWindowTitle("CopyTodo - Producto Nuevo?")
      gg.exec_()
      if gg.result() == gg.Ok:
        self.vap = ventana_nuevo_producto()
        self.vap.line_codigo.setText(codigo)
        self.vap.line_codigo.setEnabled(False)
        self.vap.llamado = True
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
    self.venta.actualizar_total()
    self.lbl_total.setText("$ " + str(self.venta.total))
    if self.venta.total <= 0:
      self.pb_pagar.setEnabled(False)
    else:
      self.pb_pagar.setEnabled(True)
      
  def eliminar_producto(self):
    codigo = str(self.table_productos.itemAt(0, self.table_productos.currentIndex().row()).text())
    
    
    self.venta.borrar_producto(codigo)
    self.actualizar_productos()
    
  def logout(self):
    from login import ventana_login
    self.vlo=ventana_login()
    self.vlo.show()
    self.close()
    

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
    self.venta.pagado = self.dsb_efectivo.value()
    self.venta.efectuar_venta()
    try:
      if self.chk_ticket.isChecked():
        from ticket import Ticket
        a = Ticket(self.venta)
        
        #htm = open("tick.html", 'r').read()
        self.web = QWebView()
        self.web.load(QUrl("tick.html"))
        
        self.qp = QPrinter()
        self.qp.setPrinterName("AFICIO")
        self.qpd = QPrintDialog(self.qp)
        self.qpd.exec_()
        #self.qp.setPrintRange(0)
        
        #self.qp.setOutputFormat(1)
        #self.qp.setOutputFileName("ticket.pdf")
        #self.web.render(self.qp)
        self.web.print_(self.qp)
    except:
      print "Error al imprimir"
    self.close()
    
    


class ventana_buscar_producto(QDialog, Ui_dialogo_busqueda_productos):
  def __init__(self):
    QDialog.__init__(self)
    self.setupUi(self)
    
    self.modelo = QSqlQueryModel()
    sql = "select * from busqueda_productos"
    self.modelo.setQuery(sql)
    self.table_resultados.setModel(self.modelo)
    self.table_resultados.setColumnWidth(1, 300)
    self.line_producto.textChanged.connect(self.actualizar_tabla)
    self.table_resultados.doubleClicked.connect(self.pasar_producto)
    self.pushButton.clicked.connect(self.pasar_producto)
    
  def actualizar_tabla(self):
    sql = "select * from busqueda_productos where nombre like '%%%s%%'" % self.line_producto.text()
    self.modelo.setQuery(sql)
    
  def pasar_producto(self):
    global paso_producto
    codigo = self.modelo.record(self.table_resultados.currentIndex().row()).value("codigo").toString()
    paso_producto = codigo
    self.close()
   
    
if __name__ == "__main__":
  app = QApplication(sys.argv)
  bd = BaseDatos.base_datos()
  form = ventana_punto_de_venta()
  form.showMaximized()
  app.exec_()
