from PySide6.QtWidgets import QApplication, QWidget
import sys

if __name__=="__main__":
    app = QApplication(sys.argv)
    window = QWidget()
    window.show()
    app.exec()