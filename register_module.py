# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'register_module.ui'
#
# Created by: PyQt5 UI code generator 5.7.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Register_Module(QtWidgets.QMainWindow):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(548, 353)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("artwork/register.png"))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.username_label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Serif")
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.username_label.setFont(font)
        self.username_label.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignHCenter)
        self.username_label.setObjectName("username_label")
        self.verticalLayout.addWidget(self.username_label)
        self.username_line = QtWidgets.QLineEdit(self.centralwidget)
        self.username_line.setAlignment(QtCore.Qt.AlignCenter)
        self.username_line.setObjectName("username_line")
        self.verticalLayout.addWidget(self.username_line)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Serif")
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignHCenter)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.password1_line = QtWidgets.QLineEdit(self.centralwidget)
        self.password1_line.setEchoMode(QtWidgets.QLineEdit.Password)
        self.password1_line.setAlignment(QtCore.Qt.AlignCenter)
        self.password1_line.setObjectName("password1_line")
        self.verticalLayout.addWidget(self.password1_line)
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Serif")
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignHCenter)
        self.label_4.setObjectName("label_4")
        self.verticalLayout.addWidget(self.label_4)
        self.password2_line = QtWidgets.QLineEdit(self.centralwidget)
        self.password2_line.setEchoMode(QtWidgets.QLineEdit.Password)
        self.password2_line.setAlignment(QtCore.Qt.AlignCenter)
        self.password2_line.setObjectName("password2_line")
        self.verticalLayout.addWidget(self.password2_line)
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setMinimumSize(QtCore.QSize(0, 30))
        self.label_5.setText("")
        self.label_5.setObjectName("label_5")
        self.verticalLayout.addWidget(self.label_5)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.register_button = QtWidgets.QPushButton(self.centralwidget)
        self.register_button.setFocusPolicy(QtCore.Qt.NoFocus)
        self.register_button.setObjectName("register_button")
        self.horizontalLayout.addWidget(self.register_button)
        self.back_button = QtWidgets.QPushButton(self.centralwidget)
        self.back_button.setFocusPolicy(QtCore.Qt.NoFocus)
        self.back_button.setObjectName("back_button")
        self.horizontalLayout.addWidget(self.back_button)
        self.verticalLayout.addLayout(self.horizontalLayout)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.username_label.setText(_translate("MainWindow", "Username"))
        self.label_3.setText(_translate("MainWindow", "Password"))
        self.label_4.setText(_translate("MainWindow", "Repeat password"))
        self.register_button.setText(_translate("MainWindow", "Register"))
        self.back_button.setText(_translate("MainWindow", "Back"))

