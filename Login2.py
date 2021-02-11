from PyQt5.QtWidgets import (
    QApplication,
    QComboBox,
    QDialog,
    QDialogButtonBox,
    QFormLayout,
    QGridLayout,
    QGroupBox,
    QHBoxLayout,
    QLabel,
    QLineEdit,
    QMenu,
    QMenuBar,
    QPushButton,
    QSpinBox,
    QTextEdit,
    QVBoxLayout,
    QMainWindow,
    QMessageBox,
)
from PyQt5 import QtGui, QtPrintSupport

import sys


class Login(QDialog):
    def __init__(self, parent=None):
        super(Login, self).__init__(parent)

        self.name = "none"
        self.textName = QLineEdit(self)
        self.textPass = QLineEdit(self)
        self.textPass.setEchoMode(QLineEdit.Password)
        self.doctors = ["Jahanshahi", "Fordo", "Wolf", "Abbath"]

        username = QLabel("Username")
        pw = QLabel("Password")

        self.buttonRegister = QPushButton("Register", self)
        self.buttonRegister.clicked.connect(self.handleRegister)

        self.buttonLogin = QPushButton("Login", self)
        # self.buttonLogin.clicked.connect(self.handleLogin)

        loginbox = QGridLayout(self)
        loginbox.setSpacing(10)

        loginbox.addWidget(username, 1, 0)
        loginbox.addWidget(self.textName, 1, 1)

        loginbox.addWidget(pw, 2, 0)
        loginbox.addWidget(self.textPass, 2, 1)

        loginbox.addWidget(self.buttonRegister, 3, 0)
        loginbox.addWidget(self.buttonLogin, 3, 1)

        self.setWindowTitle("SNCF Login")

        self.buttonLogin.clicked.connect(self.login)

    # def handleLogin(self):
    #     if (self.textName.text() == 'foo' and
    #             self.textPass.text() == 'bar'):
    #         self.accept()

    #        else:
    #            QtGui.QMessageBox.warning(
    #                self, 'Error', 'Bad user or password')

    def handleRegister(self):
        self.doctors.append(self.textName.text())

    def login(self):
        self.name = self.textName.text()
        name = False
        for doctor in self.doctors:
            if self.textName.text() == doctor and self.textPass.text() == "AP1399":
                name = True
                self.accept()
        if not name:
            QMessageBox.warning(self, "Error", "Wrong Password Or Undefined Name!")


#        else:
#            QtGui.QMessageBox.warning(
#                self, 'Error', 'Bad user or password')


class Window(QMainWindow):
    def __init__(self, parent=None):
        super(Window, self).__init__(parent)
        # self.ui = Ui_MainWindow()
        # self.ui.setupUi(self)


if __name__ == "__main__":

    import sys

    app = QApplication(sys.argv)
    login = Login()

    if login.exec_() == QDialog.Accepted:
        window = Window()
        window.show()
        sys.exit(app.exec_())
#    else:
#        pass