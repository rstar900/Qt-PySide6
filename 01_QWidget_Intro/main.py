from PySide6.QtWidgets import QApplication, QWidget # QT Imports
import sys # To take in commandline args

def main():
    # Wrapper for managing a QT application instance
    app = QApplication(sys.argv)

    # Create a QWidget with a title bar text
    window = QWidget(windowTitle="Hello QT")
    
    # Need to call this to show the QWidget
    window.show()
    # To Keep the event loop for the QT application running
    app.exec() 

if __name__=="__main__":
    main()