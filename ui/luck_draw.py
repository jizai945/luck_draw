# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\luck_draw.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(707, 458)
        self.gridLayout = QtWidgets.QGridLayout(Form)
        self.gridLayout.setObjectName("gridLayout")
        self.btn_setrule = QtWidgets.QPushButton(Form)
        self.btn_setrule.setObjectName("btn_setrule")
        self.gridLayout.addWidget(self.btn_setrule, 0, 0, 1, 1)
        self.btn_start = QtWidgets.QPushButton(Form)
        self.btn_start.setObjectName("btn_start")
        self.gridLayout.addWidget(self.btn_start, 0, 1, 1, 1)
        self.scrollArea = QtWidgets.QScrollArea(Form)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 687, 408))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout.addWidget(self.scrollArea, 1, 0, 1, 2)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.btn_setrule.setText(_translate("Form", "设置规则"))
        self.btn_start.setText(_translate("Form", "开始抽奖"))