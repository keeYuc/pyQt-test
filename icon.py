from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QWidget
import sys


class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()  # 界面绘制交给InitUi方法

    def initUI(self):
        #设置窗口的位置和大小
        self.setGeometry(300, 300, 300, 300)
        #设置窗口的标题
        self.setWindowTitle('Icon')
        #设置窗口的图标，引用当前目录下的web.png图片
        self.setWindowIcon(QIcon('./image/img1.jpg'))

        #显示窗口
        self.show()


if __name__ == '__main__':
    #创建应用程序和对象
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
