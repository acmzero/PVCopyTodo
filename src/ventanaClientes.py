# -*- coding: utf-8 -*-
'''
Created on 11/03/2012

@author: heli
'''

from PyQt4.QtGui import *
from PyQt4.QtCore import *
from PyQt4.QtSql import *
from venta import Venta
from ui.clientes_ui import Ui_dialogo_clientes
from ui.detalle_cliente_ui import Ui_dialogo_detalle_cliente
class ventana_clientes(QDialog,Ui_dialogo_clientes):
  def __init__(self,Venta):
    QDialog.__init__(self)
    self.setupUi(self)
    
    self.venta=Venta
    self.modelo=QSqlQueryModel()
    
    
    self.llenar_clientes()
    self.poner_iconos()
    self.pb_aceptar.clicked.connect(self.aceptar_cliente)
    self.pb_agregar.clicked.connect(self.nuevo_cliente)
    self.pb_editar.clicked.connect(self.editar_cliente)
    self.pb_eliminar.clicked.connect(self.eliminar_cliente)
    
  def poner_iconos(self):
    self.pb_agregar.setIcon(QIcon("imagenes/mas.png"))
    self.pb_editar.setIcon(QIcon("imagenes/editar.png"))
    self.pb_eliminar.setIcon(QIcon("imagenes/borrar.png"))
    self.pb_aceptar.setIcon(QIcon("imagenes/enviar.png"))
    
  def llenar_clientes(self):
    sql="select cliente_id,nombre from clientes"
    self.modelo.setQuery(sql)
    self.lista_clientes.setModel(self.modelo)
    self.lista_clientes.setModelColumn(1)
    
  def aceptar_cliente(self):
    cliente_id=int(self.modelo.record(self.lista_clientes.currentIndex().row()).value("cliente_id").toString())
    self.venta.cliente_id=cliente_id
    self.close()
    
  def nuevo_cliente(self):
    self.vnc=ventana_cliente("nuevo")
    self.vnc.show()
    
  def editar_cliente(self):
    cliente_id=int(self.modelo.record(self.lista_clientes.currentIndex().row()).value("cliente_id").toString())
    if not cliente_id=="":
      self.vec=ventana_cliente("editar",cliente_id)
      self.vec.show()
  
  def eliminar_cliente(self):
    cliente_id=int(self.modelo.record(self.lista_clientes.currentIndex().row()).value("cliente_id").toString())
    if not cliente_id=="":
      gg=QMessageBox()
      gg.setWindowTitle("Borrar Cliente?")
      gg.setText("Seguro que quiere eliminar este cliente?")
      gg.setStandardButtons(gg.Ok|gg.Cancel)
      gg.exec_()
      
      if gg.result()==gg.Ok:
        query=QSqlQuery()
        sql="delete from clientes where cliente_id=%d"%cliente_id
        if query.exec_(sql):
          print "Cliente eliminado"
          gg=QMessageBox()
          gg.setText("Cliente Eliminado!!")
          gg.exec_()
    
from cliente import Cliente 
class ventana_cliente(QDialog,Ui_dialogo_detalle_cliente):
  def __init__(self,modo=None,cliente_id=None):
    QDialog.__init__(self)
    self.setupUi(self)
    self.cliente_id=cliente_id
    if modo=="nuevo":
      self.pushButton.clicked.connect(self.procesar_cliente)
    elif modo=="editar":
      self.pushButton.setText("Editar")
      self.recuperar_datos()
      self.pushButton.clicked.connect(self.editar_cliente)
    
    self.datos=None
    
  def procesar_cliente(self):
    self.llenar_datos()
    nc=Cliente()
    nc.nuevo_cliente(self.datos)
    self.close()
  
  def llenar_datos(self):
    nombre=self.line_nombre.text()
    telefono=self.line_telefono.text()
    celular=self.line_celular.text()
    direccion=self.line_direccion.text()
    cp=self.line_cp.text()
    rfc=self.line_rfc.text()
    self.datos=(nombre,telefono,celular,direccion,cp,rfc)
    
    
  def recuperar_datos(self):
    ec=Cliente(self.cliente_id)
    self.line_nombre.setText(ec.nombre)
    self.line_telefono.setText(ec.telefono)
    self.line_celular.setText(ec.celular)
    self.line_direccion.setText(ec.direccion)
    self.line_cp.setText(ec.CP)
    self.line_rfc.setText(ec.RFC)
    
  def editar_cliente(self):
    self.llenar_datos()
    ec=Cliente(self.cliente_id).actualizar_cliente(self.datos)
    if ec:
      gg=QMessageBox()
      gg.setText("Cliente Actualizado!!")
      gg.exec_()
    else:
      gg=QMessageBox()
      gg.setText("Error al actualizar Cliente")
      gg.exec_()
      
    self.close()
    
    
    