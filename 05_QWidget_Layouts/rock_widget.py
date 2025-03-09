from PySide6.QtWidgets import QWidget, QPushButton, QHBoxLayout, QVBoxLayout

class RockWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("RockWidget")
        button1 = QPushButton("Button 1")
        button2 = QPushButton("Button 2")
        # The below creates a layout where buttons are placed Horizontally / Vertically
        # based on the line uncommented. By default we are using Horizontal
        # To use Vertical, uncomment below line, and comment the line with QHBoxLayout
        #layout = QVBoxLayout()
        layout = QHBoxLayout()
        
        # Add buttons to the layout
        layout.addWidget(button1)
        layout.addWidget(button2)

        # Connect the clicked signals of each buttons to the respetive slot
        button1.clicked.connect(self.button1_pressed)
        button2.clicked.connect(self.button2_pressed)

        # Set the layout for the parent QWidget (in this case the self, which is a RockWidget instance)
        self.setLayout(layout)

    # Slots for button1 and button2
    def button1_pressed(self):
        print("Button 1 Pressed")

    def button2_pressed(self):
        print("Button 2 Pressed")    