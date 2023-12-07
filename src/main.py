import sys
from PyQt5.QtWidgets import QApplication
from image_converter import ImageConverterApp

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWin = ImageConverterApp()
    mainWin.show()
    sys.exit(app.exec_())