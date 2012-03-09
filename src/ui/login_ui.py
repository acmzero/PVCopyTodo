# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login.ui'
#
# Created: Fri Mar  9 12:51:20 2012
#      by: PyQt4 UI code generator 4.9.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_dialogo_login(object):
    def setupUi(self, dialogo_login):
        dialogo_login.setObjectName(_fromUtf8("dialogo_login"))
        dialogo_login.setWindowModality(QtCore.Qt.NonModal)
        dialogo_login.setEnabled(True)
        dialogo_login.resize(634, 236)
        dialogo_login.setWindowOpacity(1.0)
        dialogo_login.setStyleSheet(_fromUtf8("QLineEdit{background:#ff6600;color:white;padding:5px}\n"
"QListWidget{background:#ff6600;padding:5px;color:white}\n"
"QPushButton:hover{background:#0099ff;color:white}\n"
"QDialog{background:white url(\"imagenes/llaves.jpg\") no-repeat left }\n"
""))
        dialogo_login.setModal(False)
        self.verticalLayout_3 = QtGui.QVBoxLayout(dialogo_login)
        self.verticalLayout_3.setContentsMargins(200, -1, 32, -1)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.label_3 = QtGui.QLabel(dialogo_login)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.horizontalLayout_4.addWidget(self.label_3)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.horizontalLayout_4.addItem(spacerItem)
        self.verticalLayout_3.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        self.list_usuarios = QtGui.QListWidget(dialogo_login)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.list_usuarios.setFont(font)
        self.list_usuarios.setObjectName(_fromUtf8("list_usuarios"))
        self.horizontalLayout_5.addWidget(self.list_usuarios)
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label = QtGui.QLabel(dialogo_login)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout.addWidget(self.label)
        self.line_usuario = QtGui.QLineEdit(dialogo_login)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.line_usuario.setFont(font)
        self.line_usuario.setStyleSheet(_fromUtf8(""))
        self.line_usuario.setObjectName(_fromUtf8("line_usuario"))
        self.horizontalLayout.addWidget(self.line_usuario)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.label_2 = QtGui.QLabel(dialogo_login)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.horizontalLayout_2.addWidget(self.label_2)
        self.line_pwd = QtGui.QLineEdit(dialogo_login)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.line_pwd.setFont(font)
        self.line_pwd.setEchoMode(QtGui.QLineEdit.Password)
        self.line_pwd.setObjectName(_fromUtf8("line_pwd"))
        self.horizontalLayout_2.addWidget(self.line_pwd)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_5.addLayout(self.verticalLayout_2)
        self.verticalLayout_3.addLayout(self.horizontalLayout_5)
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        spacerItem1 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem2)
        self.pb_entrar = QtGui.QPushButton(dialogo_login)
        self.pb_entrar.setObjectName(_fromUtf8("pb_entrar"))
        self.horizontalLayout_3.addWidget(self.pb_entrar)
        self.pushButton_2 = QtGui.QPushButton(dialogo_login)
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.horizontalLayout_3.addWidget(self.pushButton_2)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.verticalLayout_3.addLayout(self.verticalLayout)

        self.retranslateUi(dialogo_login)
        QtCore.QObject.connect(self.line_usuario, QtCore.SIGNAL(_fromUtf8("returnPressed()")), self.pb_entrar.click)
        QtCore.QObject.connect(self.line_pwd, QtCore.SIGNAL(_fromUtf8("returnPressed()")), self.pb_entrar.click)
        QtCore.QObject.connect(self.pushButton_2, QtCore.SIGNAL(_fromUtf8("clicked()")), dialogo_login.reject)
        QtCore.QMetaObject.connectSlotsByName(dialogo_login)

    def retranslateUi(self, dialogo_login):
        dialogo_login.setWindowTitle(QtGui.QApplication.translate("dialogo_login", "Iniciar Sesion", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("dialogo_login", "Inicio de Sesion", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("dialogo_login", "Usuario:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("dialogo_login", "Contraseña:", None, QtGui.QApplication.UnicodeUTF8))
        self.pb_entrar.setText(QtGui.QApplication.translate("dialogo_login", "Entrar", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_2.setText(QtGui.QApplication.translate("dialogo_login", "Salir", None, QtGui.QApplication.UnicodeUTF8))

