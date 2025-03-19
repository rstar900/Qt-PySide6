from PySide6.QtWidgets import QApplication
from custom_main_window import CustomMainWIndow
import sys

def main():
    app = QApplication(sys.argv)
    window = CustomMainWIndow(app)
    window.show()
    app.exec()

if __name__ == "__main__":
    main()
