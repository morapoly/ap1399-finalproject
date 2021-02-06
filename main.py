import sys
import os
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtCore import QSize
from PyQt5.QtGui import QImage, QPalette, QBrush

# from PyQt5.QtWidgets import *


def quit_bottun_callback():
    print("Quit...")
    app.quit()


Form = uic.loadUiType(os.path.join(os.getcwd(), "form2.ui"))[0]


class IntroWindow(QMainWindow, Form):
    def __init__(self):
        super(IntroWindow, self).__init__()
        self.setupUi(self)

        #  setting beckground image
        backgroun_image = QImage("./stuff/picture5.png")
        backgroun_image_scaled = backgroun_image.scaled(QSize(879, 444))
        palette = QPalette()
        palette.setBrush(QPalette.Window, QBrush(backgroun_image_scaled))
        self.setPalette(palette)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyle("Fusion")
    w = IntroWindow()
    w.show()
    sys.exit(app.exec_())