from PySide6.QtWidgets import QApplication
from rock_widget import RockWidget
import sys

def main():
    app = QApplication(sys.argv)
    rockWidget = RockWidget()
    rockWidget.show()
    app.exec()

if __name__ == "__main__":
    main()    