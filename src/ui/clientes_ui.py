# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'clientes.ui'
#
# Created: Sun Mar 11 12:13:10 2012
#      by: PyQt4 UI code generator 4.9.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_dialogo_clientes(object):
    def setupUi(self, dialogo_clientes):
        dialogo_clientes.setObjectName(_fromUtf8("dialogo_clientes"))
        dialogo_clientes.resize(364, 403)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        dialogo_clientes.setFont(font)
        dialogo_clientes.setStyleSheet(_fromUtf8("QDialog{background:white}\n"
"QPushButton{font-size:14pt}"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(dialogo_clientes)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.label = QtGui.QLabel(dialogo_clientes)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName(_fromUtf8("label"))
        self.verticalLayout_3.addWidget(self.label)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.lista_clientes = QtGui.QListView(dialogo_clientes)
        self.lista_clientes.setObjectName(_fromUtf8("lista_clientes"))
        self.horizontalLayout.addWidget(self.lista_clientes)
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem)
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.pb_agregar = QtGui.QPushButton(dialogo_clientes)
        self.pb_agregar.setObjectName(_fromUtf8("pb_agregar"))
        self.verticalLayout.addWidget(self.pb_agregar)
        self.pb_editar = QtGui.QPushButton(dialogo_clientes)
        self.pb_editar.setObjectName(_fromUtf8("pb_editar"))
        self.verticalLayout.addWidget(self.pb_editar)
        self.pb_eliminar = QtGui.QPushButton(dialogo_clientes)
        self.pb_eliminar.setObjectName(_fromUtf8("pb_eliminar"))
        self.verticalLayout.addWidget(self.pb_eliminar)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        spacerItem1 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem1)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.verticalLayout_3.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem2)
        self.pb_aceptar = QtGui.QPushButton(dialogo_clientes)
        self.pb_aceptar.setObjectName(_fromUtf8("pb_aceptar"))
        self.horizontalLayout_2.addWidget(self.pb_aceptar)
        self.verticalLayout_3.addLayout(self.horizontalLayout_2)

        self.retranslateUi(dialogo_clientes)
        QtCore.QMetaObject.connectSlotsByName(dialogo_clientes)

    def retranslateUi(self, dialogo_clientes):
        dialogo_clientes.setWindowTitle(QtGui.QApplication.translate("dialogo_clientes", "Clientes", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("dialogo_clientes", "Clientes", None, QtGui.QApplication.UnicodeUTF8))
        self.pb_agregar.setText(QtGui.QApplication.translate("dialogo_clientes", "Agregar", None, QtGui.QApplication.UnicodeUTF8))
        self.pb_editar.setText(QtGui.QApplication.translate("dialogo_clientes", "Editar", None, QtGui.QApplication.UnicodeUTF8))
        self.pb_eliminar.setText(QtGui.QApplication.translate("dialogo_clientes", "Eliminar", None, QtGui.QApplication.UnicodeUTF8))
        self.pb_aceptar.setText(QtGui.QApplication.translate("dialogo_clientes", "Aceptar", None, QtGui.QApplication.UnicodeUTF8))

