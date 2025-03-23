from widget import Widget
from PySide6.QtWidgets import QApplication
import sys

def main():
    app = QApplication(sys.argv)
    window = Widget()
    window.show()
    app.exec()

if __name__ == "__main__":
    main()    