import sys
import os
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow


def quit_bottun_callback():
    print("Quit...")
    app.quit()


Form = uic.loadUiType(os.path.join(os.getcwd(), "form.ui"))[0]


class IntroWindow(QMainWindow, Form):
    def __init__(self):
        super(IntroWindow, self).__init__()
        self.setupUi(self)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyle("Fusion")
    w = IntroWindow()
    w.show()
    sys.exit(app.exec_())