'''
Created on 27/02/2012

@author: heli
'''
from PyQt4.QtSql import QSqlQuery
from producto import producto
class Venta():
  def __init__(self, id):
    self.id = id
    self.cliente_id = 0
    self.fecha = None
    self.hora = None
    self.notas = ""
    self.productos = {}
    self.total = 0.0
    self.pagado = 0.0
    if self.id >= 0:
      self.recuperar_datos()
    self.es_nueva = True
    self.cliente = None
    self.usuario=None
    
  def recuperar_datos(self):
    query = QSqlQuery()
    sql = "select cliente_id,fecha,hora,notas from ventas where venta_id=%d" % self.id
    if not query.exec_(sql):
      print "Error al obtener venta."
      return
      
    g = lambda x:query.value(x).toString()
    query.next()
    self.cliente_id = int(g(0))
    self.fecha = g(1)
    self.hora = g(2)
    self.notas = g(3)
    
    self.productos = {}
    sql = """ select codigo,cantidad,descuento from detalle_ventas where venta_id=%d""" % self.id
    query.exec_(sql)
    for i in range(query.size()):
      
      query.next()
      asd = str(g(0))
      
      self.productos[asd] = producto(g(0))
      self.productos[asd].cantidad = int(g(1))
      self.productos[asd].descuento = int(g(2))
      self.productos[asd].actualizar_subtotal()
      
    self.actualizar_total()
    
      
    
  def nueva_venta(self, cliente_id):
    query = QSqlQuery()
    sql = "select max(venta_id) from ventas"
    query.exec_(sql)
    query.next()
    max_id = int(query.value(0).toString()) + 1
    self.cliente_id = cliente_id
    self.id = max_id
    
  
      
  def agregar_producto(self, codigo, cantidad, descuento):
    r = 1 #regresar para ver si pasa el producto True para pasa false para algun error
    codigo = str(codigo)
    if codigo in self.productos.keys():
      self.productos[codigo].cantidad += cantidad
      self.productos[codigo].descuento = descuento
    else:
      self.productos[codigo] = producto(codigo)
      if self.productos[codigo].existe:
        self.productos[codigo].cantidad = cantidad
        self.productos[codigo].descuento = descuento
        
        if self.productos[codigo].existencia - self.productos[codigo].cantidad < 0:
          r = 0
          self.productos[codigo].cantidad -= cantidad
          del(self.productos[codigo])
          return 0
        
        
        self.productos[codigo].actualizar_subtotal()
      else:
        del(self.productos[codigo])
        r = -1
        
    
    self.actualizar_total()
    return r
      
      
  def borrar_producto(self, codigo):
    r = True
    
    if codigo in self.productos.keys():
      del(self.productos[codigo])
    else:
      r = False
    return r
  
  def actualizar_total(self):
    tmp = 0.0
    for i in self.productos.keys():
      tmp += self.productos[i].subtotal
    self.total = tmp
      
  def efectuar_venta(self):
    print "Efectuando Venta"
    query = QSqlQuery()
    sql = "insert into ventas values(null,?,?,?,?,?,?)"
    query.prepare(sql)
    query.addBindValue(self.cliente_id)
    query.addBindValue((self.fecha))
    query.addBindValue(self.hora)
    query.addBindValue(self.notas)
    query.addBindValue(self.total)
    query.addBindValue(self.pagado)
    query.exec_()
    
    sql = "insert into detalle_ventas values"
    for i in self.productos.keys():
      
      sql += """(%d,"%s",%d,%d),""" % (self.id, i, self.productos[i].cantidad, self.productos[i].descuento)
      
    
    query.exec_(sql[:-1])
    self.es_nueva = False
    
    
      
    
      
    
      
