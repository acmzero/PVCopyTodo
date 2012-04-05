# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'equipos.ui'
#
# Created: Wed Apr  4 22:13:47 2012
#      by: PyQt4 UI code generator 4.9.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_formulario_equipos(object):
    def setupUi(self, formulario_equipos):
        formulario_equipos.setObjectName(_fromUtf8("formulario_equipos"))
        formulario_equipos.resize(648, 369)
        formulario_equipos.setStyleSheet(_fromUtf8("font-size:16pt;"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(formulario_equipos)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label_2 = QtGui.QLabel(formulario_equipos)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.horizontalLayout.addWidget(self.label_2)
        self.line_descripcion = QtGui.QLineEdit(formulario_equipos)
        self.line_descripcion.setObjectName(_fromUtf8("line_descripcion"))
        self.horizontalLayout.addWidget(self.line_descripcion)
        self.horizontalLayout_2.addLayout(self.horizontalLayout)
        self.splitter = QtGui.QSplitter(formulario_equipos)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName(_fromUtf8("splitter"))
        self.label = QtGui.QLabel(self.splitter)
        self.label.setObjectName(_fromUtf8("label"))
        self.cb_clientes = QtGui.QComboBox(self.splitter)
        self.cb_clientes.setObjectName(_fromUtf8("cb_clientes"))
        self.horizontalLayout_2.addWidget(self.splitter)
        self.pb_buscar = QtGui.QPushButton(formulario_equipos)
        self.pb_buscar.setObjectName(_fromUtf8("pb_buscar"))
        self.horizontalLayout_2.addWidget(self.pb_buscar)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.tabla_resultados = QtGui.QTableView(formulario_equipos)
        self.tabla_resultados.setObjectName(_fromUtf8("tabla_resultados"))
        self.horizontalLayout_3.addWidget(self.tabla_resultados)
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.pb_nuevo = QtGui.QPushButton(formulario_equipos)
        self.pb_nuevo.setObjectName(_fromUtf8("pb_nuevo"))
        self.verticalLayout.addWidget(self.pb_nuevo)
        self.pb_editar = QtGui.QPushButton(formulario_equipos)
        self.pb_editar.setObjectName(_fromUtf8("pb_editar"))
        self.verticalLayout.addWidget(self.pb_editar)
        self.pb_borrar = QtGui.QPushButton(formulario_equipos)
        self.pb_borrar.setObjectName(_fromUtf8("pb_borrar"))
        self.verticalLayout.addWidget(self.pb_borrar)
        spacerItem1 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        self.horizontalLayout_3.addLayout(self.verticalLayout)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem2)
        self.pushButton = QtGui.QPushButton(formulario_equipos)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.horizontalLayout_4.addWidget(self.pushButton)
        self.verticalLayout_2.addLayout(self.horizontalLayout_4)

        self.retranslateUi(formulario_equipos)
        QtCore.QMetaObject.connectSlotsByName(formulario_equipos)

    def retranslateUi(self, formulario_equipos):
        formulario_equipos.setWindowTitle(QtGui.QApplication.translate("formulario_equipos", "Equipos", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("formulario_equipos", "Descripcion:", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("formulario_equipos", "Clientes:", None, QtGui.QApplication.UnicodeUTF8))
        self.pb_buscar.setText(QtGui.QApplication.translate("formulario_equipos", "Buscar", None, QtGui.QApplication.UnicodeUTF8))
        self.pb_nuevo.setText(QtGui.QApplication.translate("formulario_equipos", "Nuevo", None, QtGui.QApplication.UnicodeUTF8))
        self.pb_editar.setText(QtGui.QApplication.translate("formulario_equipos", "Detalles", None, QtGui.QApplication.UnicodeUTF8))
        self.pb_borrar.setText(QtGui.QApplication.translate("formulario_equipos", "Borrar", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton.setText(QtGui.QApplication.translate("formulario_equipos", "Salir", None, QtGui.QApplication.UnicodeUTF8))

