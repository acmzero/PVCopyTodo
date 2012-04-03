'''
Created on 27/02/2012

@author: heli
'''


from PyQt4.QtSql import QSqlQuery
import BaseDatos
import sys
class producto():
  def __init__(self, codigo):
    self.codigo = codigo
    self.nombre = ""
    self.descripcion = ""
    self.existencia = 0
    self.precio = 0.0
    self.cantidad = 0
    self.descuento = 0
    self.subtotal = 0.0
    self.existe = True
    if len(str(self.codigo)) > 2:
      
      self.recuperar_datos()
    
    
  def recuperar_datos(self):
    query = QSqlQuery()
    sql = """ select nombre,descripcion,precio,existencia from productos where codigo="%s" """ % self.codigo
    
    
    query.exec_(sql)
    if query.size()<1:
      print "Producto no existe"
      self.existe = False
      return
    g = lambda x:query.value(x).toString()
    query.next()
    self.nombre = g(0)
    self.descripcion = g(1)
    self.existencia = int(g(3))
    self.precio = float(g(2))
    
    self.existe = True
    
    
    
  def nuevo_producto(self, datos):
    query = QSqlQuery()
    sql = """ insert into productos values(null,"%s","%s","%s",%.2f,%d)""" % datos
    
    if not query.exec_(sql):
      print "Error en algun dato de producto"
      return
    
    self.codigo = datos[0]
    
  def __str__(self):
    return str(self.nombre)
  
  def actualizar_subtotal(self):
    
    tmp = 0.0
    tmp = (self.cantidad * self.precio) + 0.0
    tmp = tmp * (1 - (self.descuento / 100.))

    self.subtotal = tmp
    
  def eliminar_producto(self):
    query=QSqlQuery()
    sql="delete from productos where codigo='%s'"%self.codigo
    
    if query.exec_(sql):
      return True
    else:
      return False
    
  def editar_producto(self,datos):
    query=QSqlQuery()
    
    sql=""" update productos set nombre="%s", descripcion="%s", precio=%.2f, existencia=%d """%datos
    sql+=" where codigo='%s'"%self.codigo
    print sql
    if query.exec_(sql):
      return True
    else:
      return False
    

    
    
    
