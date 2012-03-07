'''
Created on 25/02/2012

@author: heli
'''

from PyQt4.QtSql import QSqlDatabase

class base_datos(QSqlDatabase):
  def __init__(self):
    db=self.addDatabase("QMYSQL")
    

    db.setHostName("localhost")
    db.setUserName("root")
    db.setPassword("kaka")
    db.setDatabaseName("dbCopytodo")
    if db.open():
      print "Conexion realizada =)"
    else:
      print "Error en la conexion =("