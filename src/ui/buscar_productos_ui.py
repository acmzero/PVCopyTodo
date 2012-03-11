# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'buscar_productos.ui'
#
# Created: Sat Mar 10 17:27:09 2012
#      by: PyQt4 UI code generator 4.9.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_dialogo_busqueda_productos(object):
    def setupUi(self, dialogo_busqueda_productos):
        dialogo_busqueda_productos.setObjectName(_fromUtf8("dialogo_busqueda_productos"))
        dialogo_busqueda_productos.resize(428, 390)
        dialogo_busqueda_productos.setStyleSheet(_fromUtf8("QDialog{background: white}\n"
"QLineEdit{padding:5px}"))
        self.verticalLayout = QtGui.QVBoxLayout(dialogo_busqueda_productos)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.label_2 = QtGui.QLabel(dialogo_busqueda_productos)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.verticalLayout.addWidget(self.label_2)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label = QtGui.QLabel(dialogo_busqueda_productos)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout.addWidget(self.label)
        self.line_producto = QtGui.QLineEdit(dialogo_busqueda_productos)
        self.line_producto.setInputMask(_fromUtf8(""))
        self.line_producto.setObjectName(_fromUtf8("line_producto"))
        self.horizontalLayout.addWidget(self.line_producto)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.table_resultados = QtGui.QTableView(dialogo_busqueda_productos)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.table_resultados.setFont(font)
        self.table_resultados.setObjectName(_fromUtf8("table_resultados"))
        self.verticalLayout.addWidget(self.table_resultados)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.pushButton = QtGui.QPushButton(dialogo_busqueda_productos)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.horizontalLayout_2.addWidget(self.pushButton)
        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.retranslateUi(dialogo_busqueda_productos)
        QtCore.QMetaObject.connectSlotsByName(dialogo_busqueda_productos)

    def retranslateUi(self, dialogo_busqueda_productos):
        dialogo_busqueda_productos.setWindowTitle(QtGui.QApplication.translate("dialogo_busqueda_productos", "Dialog", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("dialogo_busqueda_productos", "Busqueda de Productos", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("dialogo_busqueda_productos", "Busqueda", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton.setText(QtGui.QApplication.translate("dialogo_busqueda_productos", "Aceptar", None, QtGui.QApplication.UnicodeUTF8))

