import sys
from button_holder import ButtonHolder
from PySide6.QtWidgets import QApplication

def main():
    app = QApplication(sys.argv)
    # Try displying the 1st command line argument along with the button text (if available)
    if len(sys.argv) > 1:
        name = sys.argv[1]
    else:
        name = ""    
    buttonHolder = ButtonHolder(name)
    buttonHolder.show()
    app.exec()

if __name__ == '__main__':
    main()