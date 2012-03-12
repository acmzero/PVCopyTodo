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
  def __init__(self, id=None):
    self.id = id
    self.nombre = ""
    #self.apellidos = ""
    self.telefono = ""
    self.celular = ""
    self.direccion = ""
    self.CP = ""
    self.RFC = ""
    if not id == None:
      self.recuperar_datos()
    
    
  
  def recuperar_datos(self):
    query = QSqlQuery()
    sql = "select nombre,telefono,celular,direccion,CP,RFC from clientes where cliente_id=?"
    query.prepare(sql)
    query.addBindValue(self.id)
    query.exec_()
    
    if query.size() < 1:
      print "Error en el cliente no existe?"
      return
    
    g = lambda x:query.value(x).toString()
    query.next()
    self.nombre = g(0)
    #self.apellidos = g(1)
    self.telefono = g(1)
    self.celular = g(2)
    self.direccion = g(3)
    self.CP = g(4)
    self.RFC = g(5)
    
    
  def nuevo_cliente(self, datos):
    query = QSqlQuery()
    sql = """insert into clientes values(null,"%s","%s","%s","%s","%s","%s")""" % datos
    
    if not query.exec_(sql):
      print "Error al crear un nuevo cliente."
      
  def actualizar_cliente(self, datos):
    query = QSqlQuery()
    sql = """ update clientes set nombre="%s", telefono="%s",celular="%s",direccion="%s", CP="%s", RFC="%s" """ % datos
    sql += " where cliente_id=%d" % self.id
    
    if not query.exec_(sql):
      print "Error al actualizar Cliente"
      return False
    else:
      return True
    
    

    
