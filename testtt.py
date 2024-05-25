import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QDialog
from ui_main import Ui_MainWindow
from guide_window import Ui_Dialog
from PyQt5.QtGui import QPixmap
from PyQt5 import QtCore

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.confirm.clicked.connect(self.open_dialog)
        self.dialog = Dialog(self)
    def open_dialog(self):
        a = self.hero_choose.setItemText
        b = self.rule_choose.setItemText
        if a == "Void Spirit" and b == "Мид":
            self.dialog.show()
            self.dialog.setWindowModality(QtCore.Qt.NonModal)

class Dialog(QDialog, Ui_Dialog):
    def __init__(self, main_window):
        super().__init__()
        self.setupUi(self)
        self.main_window = main_window


if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    MainWindow = MainWindow()
    MainWindow.show()
    sys.exit(app.exec_())