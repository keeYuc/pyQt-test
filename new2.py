import sys

from PySide2.QtWidgets import QApplication, QWidget
from PySide2.QtUiTools import QUiLoader


class Tester():
    def __init__(self):
        self.ui = QUiLoader().load('ui/test1.ui')
        self.ui.lcdNumber.display(0)
        self.ui.pushButton.clicked.connect(self.__add__)
        self.ui.pushButton_2.clicked.connect(self.__sub__)

    def __add__(self):
        self.ui.lcdNumber.display(self.ui.lcdNumber.intValue() + 1)
    def __sub__(self):
        self.ui.lcdNumber.display(self.ui.lcdNumber.intValue() - 1)

if __name__ == '__main__':
    app = QApplication([])
    i = Tester()
    i.ui.show()
    app.exec_()
