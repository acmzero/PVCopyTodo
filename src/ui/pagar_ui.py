# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'pagar.ui'
#
# Created: Sat Mar  3 20:11:39 2012
#      by: PyQt4 UI code generator 4.9.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_dialogo_pagar(object):
    def setupUi(self, dialogo_pagar):
        dialogo_pagar.setObjectName(_fromUtf8("dialogo_pagar"))
        dialogo_pagar.resize(375, 209)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        dialogo_pagar.setFont(font)
        self.verticalLayout_2 = QtGui.QVBoxLayout(dialogo_pagar)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label = QtGui.QLabel(dialogo_pagar)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout.addWidget(self.label)
        self.dsb_efectivo = QtGui.QDoubleSpinBox(dialogo_pagar)
        self.dsb_efectivo.setMaximum(99999.0)
        self.dsb_efectivo.setObjectName(_fromUtf8("dsb_efectivo"))
        self.horizontalLayout.addWidget(self.dsb_efectivo)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.label_3 = QtGui.QLabel(dialogo_pagar)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.horizontalLayout_2.addWidget(self.label_3)
        self.lbl_cambio = QtGui.QLabel(dialogo_pagar)
        self.lbl_cambio.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_cambio.setObjectName(_fromUtf8("lbl_cambio"))
        self.horizontalLayout_2.addWidget(self.lbl_cambio)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem)
        self.chk_ticket = QtGui.QCheckBox(dialogo_pagar)
        self.chk_ticket.setChecked(True)
        self.chk_ticket.setTristate(False)
        self.chk_ticket.setObjectName(_fromUtf8("chk_ticket"))
        self.horizontalLayout_4.addWidget(self.chk_ticket)
        self.verticalLayout_2.addLayout(self.horizontalLayout_4)
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        spacerItem1 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem2)
        self.pb_aceptar = QtGui.QPushButton(dialogo_pagar)
        self.pb_aceptar.setObjectName(_fromUtf8("pb_aceptar"))
        self.horizontalLayout_3.addWidget(self.pb_aceptar)
        self.pb_cancelar = QtGui.QPushButton(dialogo_pagar)
        self.pb_cancelar.setObjectName(_fromUtf8("pb_cancelar"))
        self.horizontalLayout_3.addWidget(self.pb_cancelar)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.retranslateUi(dialogo_pagar)
        QtCore.QObject.connect(self.pb_cancelar, QtCore.SIGNAL(_fromUtf8("clicked()")), dialogo_pagar.close)
        QtCore.QMetaObject.connectSlotsByName(dialogo_pagar)

    def retranslateUi(self, dialogo_pagar):
        dialogo_pagar.setWindowTitle(QtGui.QApplication.translate("dialogo_pagar", "Pagar", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("dialogo_pagar", "Efectivo", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("dialogo_pagar", "Cambio", None, QtGui.QApplication.UnicodeUTF8))
        self.lbl_cambio.setText(QtGui.QApplication.translate("dialogo_pagar", "$", None, QtGui.QApplication.UnicodeUTF8))
        self.chk_ticket.setText(QtGui.QApplication.translate("dialogo_pagar", "Ticket?", None, QtGui.QApplication.UnicodeUTF8))
        self.pb_aceptar.setText(QtGui.QApplication.translate("dialogo_pagar", "Aceptar", None, QtGui.QApplication.UnicodeUTF8))
        self.pb_cancelar.setText(QtGui.QApplication.translate("dialogo_pagar", "Cancelar", None, QtGui.QApplication.UnicodeUTF8))

