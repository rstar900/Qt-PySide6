from PySide6.QtWidgets import QApplication
from modified_button import ModifiedQPushButton
import sys

def main():
    app = QApplication(sys.argv)
    button = ModifiedQPushButton()
    button.show()
    app.exec()

if __name__ == "__main__":
    main()    