import sys
from PySide6.QtCore import (QPropertyAnimation)
from PySide6.QtWidgets import (QMainWindow, QApplication)

from ui_functions import *
from ui_main import Ui_MainWindow


class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.animation = QPropertyAnimation(self.ui.frame_left_menu, b'minimumWidth')

        self.ui.pushButton_toggle_menu.clicked.connect(lambda: Ui_Functions.toggle_menu(self, 150, True))
        self.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())
