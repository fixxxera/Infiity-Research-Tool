import os
import sys

from PyQt5 import QtCore
from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt

from database_manager import DatabaseManager
from login_dialog import Login_Module
from register_module import Register_Module


# noinspection PyMethodMayBeStatic
class Main(object):
    # noinspection PyArgumentList
    def __init__(self):
        super().__init__()
        self.window = Login_Module()
        self.window.show()
        self.window.move(QtWidgets.QApplication.desktop().screen().rect().center() - self.window.rect().center())
        self.register_module = Register_Module()
        self.window.setupUi(self.window)
        self.window.register_button.clicked.connect(self.register)
        self.window.login_button.clicked.connect(self.check_info)
        self.window.login_button.setEnabled(False)
        self.window.username_line_edit.textChanged.connect(self.text_check)
        self.window.password_line_edit.textChanged.connect(self.password_check)
        self.check_accounts()

    def register(self):
        self.register_module.move(
            QtWidgets.QApplication.desktop().screen().rect().center() - self.register_module.rect().center())
        self.register_module.show()
        self.register_module.setupUi(self.register_module)
        self.register_module.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.window.hide()
        self.register_module.back_button.clicked.connect(self.goback)
        self.register_module.register_button.setEnabled(False)
        self.register_module.username_line.textChanged.connect(self.check_r_username)
        self.register_module.password1_line.textChanged.connect(self.check_r_password)
        self.register_module.password2_line.textChanged.connect(self.check_r_password2)
        self.register_module.register_button.clicked.connect(self.create_user)
        pass

    def check_info(self):
        db = DatabaseManager()
        db.open_connection()
        success = db.login(self.window.username_line_edit.text(), self.window.password_line_edit.text())
        if success:
            self.open_main_window()
        else:
            self.window.status_label.setText("<font color='Red'>Incorrect credentials</font>")
            self.window.username_line_edit.setText('')
            self.window.password_line_edit.setText('')
        pass

    def text_check(self):
        if self.window.username_line_edit.text() == '':
            self.window.login_button.setEnabled(False)
        else:
            if self.window.password_line_edit.text() == '':
                self.window.login_button.setEnabled(False)
            else:
                self.window.login_button.setEnabled(True)
        pass

    def password_check(self):
        if self.window.password_line_edit.text() == '':
            self.window.login_button.setEnabled(False)
        else:
            if self.window.username_line_edit.text() == '':
                self.window.login_button.setEnabled(False)
            else:
                self.window.login_button.setEnabled(True)
        pass

    def goback(self):
        self.window.show()
        self.window.move(QtWidgets.QApplication.desktop().screen().rect().center() - self.window.rect().center())
        self.register_module.close()
        self.check_accounts()
        pass

    def check_r_username(self):
        text = self.register_module.username_line.text()
        if text == '':
            self.register_module.register_button.setEnabled(False)
            self.register_module.label_5.setText("<font color='Red'>Empty field(s)</font>")
        else:
            if self.register_module.password1_line.text() == '' or self.register_module.password2_line.text() == '':
                self.register_module.register_button.setEnabled(False)
                self.register_module.label_5.setText("<font color='Red'>Empty field(s)</font>")
            else:
                if self.register_module.password1_line.text() != self.register_module.password2_line.text():
                    self.register_module.register_button.setEnabled(False)
                    self.register_module.label_5.setText("<font color='Red'>Passwords do no match</font>")
                else:
                    self.register_module.register_button.setEnabled(True)
                    self.register_module.label_5.setText("")

    def check_r_password2(self):
        if self.register_module.password1_line.text() == '':
            self.register_module.label_5.setText("<font color='Red'>Empty field(s)</font>")
            self.register_module.register_button.setEnabled(False)
        else:
            if self.register_module.password2_line.text() == '' or self.register_module.username_line.text() == '':
                self.register_module.register_button.setEnabled(False)
                self.register_module.label_5.setText("<font color='Red'>Empty field(s)</font>")
            else:
                if self.register_module.password1_line.text() != self.register_module.password2_line.text():
                    self.register_module.register_button.setEnabled(False)
                    self.register_module.label_5.setText("<font color='Red'>Passwords do no match</font>")
                else:
                    self.register_module.register_button.setEnabled(True)
                    self.register_module.label_5.setText("")
        pass

    def check_r_password(self):
        if self.register_module.password2_line.text() == '':
            self.register_module.label_5.setText("<font color='Red'>Empty field(s)</font>")
            self.register_module.register_button.setEnabled(False)
        else:
            if self.register_module.password1_line.text() == '' or self.register_module.username_line.text() == '':
                self.register_module.register_button.setEnabled(False)
                self.register_module.label_5.setText("<font color='Red'>Empty field(s)</font>")
            else:
                if self.register_module.password1_line.text() != self.register_module.password2_line.text():
                    self.register_module.register_button.setEnabled(False)
                    self.register_module.label_5.setText("<font color='Red'>Passwords do no match</font>")
                else:
                    self.register_module.register_button.setEnabled(True)
                    self.register_module.label_5.setText("")
        pass

    def create_user(self):
        db = DatabaseManager()
        db.open_connection()
        inserted = db.insert_user(self.register_module.username_line.text(), self.register_module.password1_line.text())
        if inserted:
            self.register_module.register_button.setEnabled(False)
            self.register_module.label_5.setText("<font color='Green'>Success! Please go back to login page</font>")
            self.register_module.username_line.setEnabled(False)
            self.register_module.password1_line.setEnabled(False)
            self.register_module.password2_line.setEnabled(False)
        else:
            self.register_module.label_5.setText("<font color='Red'>User already exists</font>")

    def open_main_window(self):

        pass

    def check_accounts(self):
        db = DatabaseManager()
        db.open_connection()
        count = db.check_accounts()
        if count < 1:
            self.window.username_line_edit.setText('')
            self.window.password_line_edit.setText('')
        else:
            self.window.register_button.setEnabled(False)
            db = DatabaseManager()
            db.open_connection()
            self.window.username_line_edit.setText(db.get_account())
            self.window.username_line_edit.setFocusPolicy(QtCore.Qt.NoFocus)
            self.window.password_line_edit.setFocusPolicy(QtCore.Qt.StrongFocus)
            self.window.password_line_edit.setText('')
            self.window.password_line_edit.setFocus(Qt.ActiveWindowFocusReason)
        pass


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    main = Main()
    app.exec_()
