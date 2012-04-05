'''
Created on 04/04/2012

@author: heli
'''

from PyQt4.QtGui import *
from PyQt4.QtCore import *
import sys
import BaseDatos 
from ui.equipos_ui import Ui_formulario_equipos
from PyQt4.QtSql import *

class ventana_equipos(QWidget,Ui_formulario_equipos):
  def __init__(self):
    QWidget.__init__(self)
    self.setupUi(self)
    
    self.aplicar_modelo_clientes()
    self.aplicar_iconos()
    self.aplicar_senales()
    self.actualizar_tabla()
    
  def aplicar_senales(self):
    self.pb_buscar.clicked.connect(self.actualizar_tabla_cliente)
    self.line_descripcion.textChanged.connect(self.actualizar_tabla)
    
  def aplicar_iconos(self):
    self.pb_nuevo.setIcon(QIcon("imagenes/mas.png"))
    self.pb_buscar.setIcon(QIcon("imagenes/buscar.png"))
    self.pushButton.setIcon(QIcon("imagenes/cancelar.png"))
    self.pb_editar.setIcon(QIcon("imagenes/editar.png"))
    self.pb_borrar.setIcon(QIcon("imagenes/borrar.png"))
    
  def aplicar_modelo_clientes(self):
    self.modelo_clientes=QSqlQueryModel()
    sql="select cliente_id,nombre from clientes"
    self.modelo_clientes.setQuery(sql)
    
    self.cb_clientes.setModel(self.modelo_clientes)
    self.cb_clientes.setModelColumn(1)
    
    
  def actualizar_tabla(self,cliente=False):
    self.modelo_tabla=QSqlQueryModel()
    
    sql=""
    if not cliente:
      sql=""" select * from filtro_equipos where Equipo like "%%%s%%" """%str(self.line_descripcion.text())
    else:
      sql=""" select * from filtro_equipos where Equipo like "%%%s%%" and Cliente="%s" """%(str(self.line_descripcion.text()),str(self.cb_clientes.currentText()))
      
    
    self.modelo_tabla.setQuery(sql)
    self.tabla_resultados.setModel(self.modelo_tabla)
    self.tabla_resultados.hideColumn(0)
    
    
  def actualizar_tabla_cliente(self):
    self.actualizar_tabla(True)
    
if __name__ == "__main__":
  app = QApplication(sys.argv)
  bd = BaseDatos.base_datos()
  form = ventana_equipos()
  form.show()
  app.exec_()