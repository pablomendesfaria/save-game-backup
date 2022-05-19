from PySide6.QtCore import QEasingCurve

from main import MainWindow


class Ui_Functions(MainWindow):
    def toggle_menu(self, maxWidth, enable):
        if enable:
            width = self.ui.frame_left_menu.width()
            max_extend = maxWidth
            standard = 70

            if width == 70:
                width_extended = max_extend
            else:
                width_extended = standard

            self.animation.setDuration(400)
            self.animation.setStartValue(width)
            self.animation.setEndValue(width_extended)
            self.animation.setEasingCurve(QEasingCurve.InOutQuart)
            self.animation.start()
