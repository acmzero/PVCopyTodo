'''
Created on 04/04/2012

@author: heli
'''

from PyQt4.QtSql import QSqlQuery

class equipo():
  def __init__(self, id=None):
    
    self.id = id
    self.cliente_id = None
    self.descripcion = ""
    self.problema = ""
    self.estado_equipo = ""
    self.solucion = ""
    self.costo = ""
    self.usuario_id = 0
    self.fecha=""
    self.hora=""
    if id != None:
      self.recuperar_datos()
    
  def recuperar_datos(self):
    query = QSqlQuery()
    sql = """ select * from equipos where equipo_id=%d""" % self.id
    
    if query.exec_(sql):
      query.next()
      g = lambda x: query.value(x).toString()
      
      self.cliente_id = int(g(1))
      self.descripcion = g(2)
      self.problema = g(3)
      self.estado_equipo = g(4)
      self.solucion = g(5)
      self.costo = float(g(6))
      self.usuario_id=int(g(7))
      self.fecha=g(8)
      
      self.hora=g(9)
      
      return True
    else:
      print "Error al obtener datos del equipo."
      return False
      
  def nuevo(self):
    query = QSqlQuery()
    datos = (self.cliente_id, self.descripcion, self.descripcion, self.problema, self.estado_equipo, self.solucion, self.costo, self.usuario_id,self.fecha,self.hora)
    
    sql = """insert into equipos values(null,%d,"%s","%s","%s","%s",%.2f,%d,"%s","%s") """ % datos
    
    if query.exec_(sql):
      sql = "select max(equipo_id) from equipos"
      if query.exec_(sql):
        query.next()
        self.id = int(query.value(0).toString())
      return True
    else:
      print "Error en Nuevo Equipo"
      return False
    
    
  
