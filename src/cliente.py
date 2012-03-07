'''
Created on 27/02/2012

@author: heli
'''
from PyQt4.QtGui import *
from PyQt4.QtCore import *
from PyQt4.QtSql import QSqlQuery
import sys
import BaseDatos
class Cliente():
  def __init__(self, id):
    self.id = id
    self.nombre = ""
    self.apellidos = ""
    self.telefono = ""
    self.celular = ""
    self.direccion = ""
    self.recuperar_datos()
    
    
  
  def recuperar_datos(self):
    query = QSqlQuery()
    sql = "select nombre,apellidos,telefono,celular,direccion from clientes where cliente_id=?"
    query.prepare(sql)
    query.addBindValue(self.id)
    query.exec_()
    
    if query.size() < 1:
      print "Error en el cliente no existe?"
      return
    
    g = lambda x:query.value(x).toString()
    query.next()
    self.nombre = g(0)
    self.apellidos = g(1)
    self.telefono = g(2)
    self.celular = g(3)
    self.direccion = g(4)
    
    
  def nuevo_cliente(self, datos):
    query = QSqlQuery()
    sql = """insert into clientes values(null,"%s","%s","%s","%s","%s")""" % datos
    
    if not query.exec_(sql):
      print "Error al crear un nuevo cliente."
    
    
app = QApplication(sys.argv)
db = BaseDatos.base_datos()
tino = Cliente(21)
for i in range(10):
  tino.nuevo_cliente(("Cliente" + str(i), "Apellidos " + str(i), str(i) * 5, str(i) * 5, "Dasdsa"))

app.exec_()  
    
