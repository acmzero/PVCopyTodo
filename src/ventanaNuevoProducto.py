# -*- coding: utf-8 -*-
'''
Created on 01/03/2012

@author: heli
'''
from PyQt4.QtGui import *
from PyQt4.QtCore import *

import sys

import BaseDatos
from ui.nuevo_producto_ui import Ui_dialogo_agregar_producto
from producto import producto
class ventana_nuevo_producto(QDialog,Ui_dialogo_agregar_producto):
  def __init__(self,codigo=None,edicion=False):
    QDialog.__init__(self)
    self.setupUi(self)
    if codigo==None:
      self.producto=producto(-1)
    else:
      self.producto=producto(codigo)
    
    if edicion==False:
      self.pb_aceptar.clicked.connect(self.nuevo_producto)
    else:
      self.llenar_campos()
      self.line_codigo.setEnabled(False)
      self.pb_aceptar.clicked.connect(self.finalizar_edicion)
      
      
    self.sb_existencia.setMaximum(999)
    self.dsb_precio.setMaximum(99999)
    self.pb_cancelar.clicked.connect(self.salir)
    self.llamado=False
    self.pb_aceptar.setIcon(QIcon("imagenes/enviar.png"))
    self.pb_cancelar.setIcon(QIcon("imagenes/cancelar.png"))
    
  def finalizar_edicion(self):
    datos=self.obtener_datos()[1:]
    
   
    gg=QMessageBox()
    gg.setStandardButtons(gg.Ok)
    gg.setWindowTitle("Actualizar Producto")
    if self.producto.editar_producto(datos):
      gg.setText("Producto actualizado correctamente.")
      gg.setIcon(gg.Information)
      gg.exec_()
      self.close()
    else:
      gg.setText("No actualizado, ha ocurrido un error!!")
      gg.setIcon(gg.Warning)
      gg.exec_()
    
    
  def llenar_campos(self):
    self.line_codigo.setText(self.producto.codigo)
    self.line_descripcion.setText(self.producto.descripcion)
    self.line_nombre.setText(self.producto.nombre)
    self.dsb_precio.setValue(self.producto.precio)
    self.sb_existencia.setValue(self.producto.existencia)
    
  def obtener_datos(self):
    codigo=str(self.line_codigo.text())
    nombre=str(self.line_nombre.text())
    descripcion=str(self.line_descripcion.text())
    precio=float(self.dsb_precio.value())
    cantidad=int(self.sb_existencia.value())
    return (codigo,nombre,descripcion,precio,cantidad)
  
  def nuevo_producto(self):
    if not self.datos_completos():
      gg=QMessageBox(self)
      gg.setText("Datos incompletos")
      gg.exec_()
      self.line_nombre.setFocus()
      return
    self.producto.nuevo_producto(self.obtener_datos())
    if not self.llamado:
      gg=QMessageBox(self)
      gg.setText(u"Producto Agregado Desea agregar más productos?")
      gg.setStandardButtons(gg.Ok|gg.Cancel)
      gg.exec_()
      if gg.result()==gg.Ok:
        self.prepara_nuevo_producto()
      else:
        self.close()
    else:
      gg=QMessageBox(self)
      gg.setText(u"Producto Agregado.")
      gg.setStandardButtons(gg.Ok)
      gg.exec_()
      self.close()
      
  def prepara_nuevo_producto(self):
    self.line_codigo.setEnabled(True)
    self.line_codigo.clear()
    self.line_nombre.clear()
    self.line_descripcion.clear()
    self.dsb_precio.setValue(0.0)
    self.sb_existencia.setValue(0)
    
    
    
  def salir(self):
    self.close()
    
  def datos_completos(self):
    r=True
    if len(self.line_nombre.text())==0 or len(self.line_codigo.text())==0:
      r=False
    return r
    
    
if __name__=="__main__":
  app=QApplication(sys.argv)
  bd=BaseDatos.base_datos()
  form=ventana_nuevo_producto()
  form.show()
  app.exec_()