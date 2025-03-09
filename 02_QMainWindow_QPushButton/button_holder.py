# This module holds the logic for the QMainWindow which holds a QPushButton in it's center

from PySide6.QtWidgets import QMainWindow, QPushButton

# ButtonHolder class inherits QMainWindow, as it modifies it by embedding a button and modifying
# few of it's properties
class ButtonHolder(QMainWindow):
    def __init__(self, name):
        super().__init__() # Need to initialize the base class as well
        button = QPushButton()
        button.setText("Click Me!\n{}".format(name))
        # make the button borders visible
        button.setFlat(False)
        # Adjust size according to the recommended one based on the text 
        button.setFixedSize(button.sizeHint())
        self.setWindowTitle("ButtonHolder Example")
        # Set the button as a widget held inside the ButtonHolder object
        self.setCentralWidget(button)