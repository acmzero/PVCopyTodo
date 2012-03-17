# -*- coding: utf-8 -*-
'''
Created on 08/03/2012

@author: heli
'''
from PyQt4.QtGui import *
from PyQt4.QtCore import *
from PyQt4.QtSql import QSqlQuery
import sys

import BaseDatos
from ui.login_ui import Ui_dialogo_login 
from ventanaPuntoDeVenta import ventana_punto_de_venta

class ventana_login(QDialog, Ui_dialogo_login):
  def __init__(self):
    QDialog.__init__(self)
    self.setupUi(self)
    
    self.llenar_usuarios()
    self.list_usuarios.itemDoubleClicked.connect(self.pasar_usuario)
    self.pb_entrar.clicked.connect(self.autenticar)
    self.usuario_id = 0
    
  def llenar_usuarios(self):
    query = QSqlQuery()
    sql = "select usuario from usuarios"
    if query.exec_(sql):
      for i in range(query.size()):
        query.next()
        qn = QListWidgetItem(query.value(0).toString())
        self.list_usuarios.addItem(qn)
        
  def pasar_usuario(self):
    usuario = self.list_usuarios.currentItem().text()
    self.line_usuario.clear()
    self.line_pwd.clear()
    self.line_usuario.setFocus()
    self.line_usuario.setText(usuario)
    self.line_pwd.setFocus()
    
  def exito(self):
    query=QSqlQuery()
    query.exec_("select usuario_id from usuarios where usuario='%s'"%str(self.line_usuario.text()))
    query.next()
    self.usuario_id=int(query.value(0).toString())
    self.qvpdv = ventana_punto_de_venta()
    self.qvpdv.usuario_id = self.usuario_id
    self.qvpdv.venta.cliente_id=1
    self.qvpdv.actualizar_usuario()
    
    
    self.qvpdv.showMaximized()
    self.close()
  
  def autenticar(self):
    from hashlib import sha1
    pwd = sha1(str(self.line_pwd.text())).hexdigest()
    
    query = QSqlQuery()
    sql = "select contrasena from usuarios where usuario='%s'" % str(self.line_usuario.text())
    if query.exec_(sql):
      query.next()
      contra = query.value(0).toString()
      
      if pwd == contra:
        self.exito()
      else:
        gg = QMessageBox()
        gg.setText(u"Usuario y/o Contraseña invalida")
        gg.setStandardButtons(gg.Ok)
        gg.exec_()
   
if __name__ == "__main__":
  app = QApplication(sys.argv)
  app.setApplicationName("PVCopyTodo")
  bd = BaseDatos.base_datos()
  form = ventana_login()
  form.show()
  app.exec_()
