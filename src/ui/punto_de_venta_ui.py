# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'punto_de_venta.ui'
#
# Created: Mon Mar  5 17:42:31 2012
#      by: PyQt4 UI code generator 4.9.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_dialogo_pdeventa(object):
    def setupUi(self, dialogo_pdeventa):
        dialogo_pdeventa.setObjectName(_fromUtf8("dialogo_pdeventa"))
        dialogo_pdeventa.resize(683, 557)
        self.verticalLayout = QtGui.QVBoxLayout(dialogo_pdeventa)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem)
        self.lbl_logo = QtGui.QLabel(dialogo_pdeventa)
        self.lbl_logo.setMinimumSize(QtCore.QSize(250, 150))
        self.lbl_logo.setMaximumSize(QtCore.QSize(250, 150))
        self.lbl_logo.setObjectName(_fromUtf8("lbl_logo"))
        self.horizontalLayout_4.addWidget(self.lbl_logo)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.lbl_fecha = QtGui.QLabel(dialogo_pdeventa)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.lbl_fecha.setFont(font)
        self.lbl_fecha.setObjectName(_fromUtf8("lbl_fecha"))
        self.horizontalLayout_3.addWidget(self.lbl_fecha)
        self.lbl_hora = QtGui.QLabel(dialogo_pdeventa)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.lbl_hora.setFont(font)
        self.lbl_hora.setObjectName(_fromUtf8("lbl_hora"))
        self.horizontalLayout_3.addWidget(self.lbl_hora)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.vp_comercial = phonon.Phonon.VideoPlayer(dialogo_pdeventa)
        self.vp_comercial.setMinimumSize(QtCore.QSize(480, 320))
        self.vp_comercial.setMaximumSize(QtCore.QSize(480, 320))
        self.vp_comercial.setObjectName(_fromUtf8("vp_comercial"))
        self.horizontalLayout_2.addWidget(self.vp_comercial)
        self.table_productos = QtGui.QTableWidget(dialogo_pdeventa)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.table_productos.setFont(font)
        self.table_productos.setObjectName(_fromUtf8("table_productos"))
        self.table_productos.setColumnCount(0)
        self.table_productos.setRowCount(0)
        self.horizontalLayout_2.addWidget(self.table_productos)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.splitter_2 = QtGui.QSplitter(dialogo_pdeventa)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.splitter_2.setFont(font)
        self.splitter_2.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_2.setObjectName(_fromUtf8("splitter_2"))
        self.pb_pagar = QtGui.QPushButton(self.splitter_2)
        self.pb_pagar.setObjectName(_fromUtf8("pb_pagar"))
        self.splitter = QtGui.QSplitter(self.splitter_2)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName(_fromUtf8("splitter"))
        self.line_codigo = QtGui.QLineEdit(self.splitter)
        self.line_codigo.setObjectName(_fromUtf8("line_codigo"))
        self.layoutWidget = QtGui.QWidget(self.splitter)
        self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setMargin(0)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.pb_buscar = QtGui.QPushButton(self.layoutWidget)
        self.pb_buscar.setObjectName(_fromUtf8("pb_buscar"))
        self.horizontalLayout.addWidget(self.pb_buscar)
        self.pb_borrar = QtGui.QPushButton(self.layoutWidget)
        self.pb_borrar.setObjectName(_fromUtf8("pb_borrar"))
        self.horizontalLayout.addWidget(self.pb_borrar)
        self.lbl_total = QtGui.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.lbl_total.setFont(font)
        self.lbl_total.setObjectName(_fromUtf8("lbl_total"))
        self.horizontalLayout.addWidget(self.lbl_total)
        self.verticalLayout.addWidget(self.splitter_2)

        self.retranslateUi(dialogo_pdeventa)
        QtCore.QMetaObject.connectSlotsByName(dialogo_pdeventa)

    def retranslateUi(self, dialogo_pdeventa):
        dialogo_pdeventa.setWindowTitle(QtGui.QApplication.translate("dialogo_pdeventa", "CopyTodo", None, QtGui.QApplication.UnicodeUTF8))
        self.lbl_logo.setText(QtGui.QApplication.translate("dialogo_pdeventa", "Logo", None, QtGui.QApplication.UnicodeUTF8))
        self.lbl_fecha.setText(QtGui.QApplication.translate("dialogo_pdeventa", "Fecha", None, QtGui.QApplication.UnicodeUTF8))
        self.lbl_hora.setText(QtGui.QApplication.translate("dialogo_pdeventa", "Hora", None, QtGui.QApplication.UnicodeUTF8))
        self.pb_pagar.setText(QtGui.QApplication.translate("dialogo_pdeventa", "Pagar", None, QtGui.QApplication.UnicodeUTF8))
        self.pb_buscar.setText(QtGui.QApplication.translate("dialogo_pdeventa", "Buscar", None, QtGui.QApplication.UnicodeUTF8))
        self.pb_borrar.setText(QtGui.QApplication.translate("dialogo_pdeventa", "Borrar", None, QtGui.QApplication.UnicodeUTF8))
        self.lbl_total.setText(QtGui.QApplication.translate("dialogo_pdeventa", "$.", None, QtGui.QApplication.UnicodeUTF8))

from PyQt4 import phonon
