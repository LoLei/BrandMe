# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'basic.ui'
#
# Created: Sun Apr 26 22:42:01 2015
#      by: PyQt4 UI code generator 4.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(314, 266)
        self.pushButton = QtGui.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(210, 20, 75, 23))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.graphicsView = QtGui.QGraphicsView(Dialog)
        self.graphicsView.setGeometry(QtCore.QRect(30, 60, 256, 192))
        self.graphicsView.setObjectName(_fromUtf8("graphicsView"))
        self.lineEdit = QtGui.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(30, 20, 171, 20))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))

        self.retranslateUi(Dialog)
        QtCore.QObject.connect(self.pushButton, QtCore.SIGNAL(_fromUtf8("clicked()")), Dialog.update)
        QtCore.QObject.connect(self.lineEdit, QtCore.SIGNAL(_fromUtf8("textChanged(QString)")), Dialog.update)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "BrandMe", None))
        self.pushButton.setText(_translate("Dialog", "Create", None))
        self.lineEdit.setText(_translate("Dialog", "Enter company name", None))
        # Can be drop down menu or radio button etc.
        # TODO Add actual GUI elements too
        self.lineEdit.setText(_translate("Dialog", "Enter branch", None))
