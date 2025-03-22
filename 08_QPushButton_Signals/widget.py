from PySide6.QtWidgets import QWidget, QPushButton, QVBoxLayout

class Widget(QWidget):
    def __init__(self):
        super().__init__()
        
        # Create a simple widget with 2 buttons
        self.setWindowTitle("QPushButton Signals Demo")

        # Simple button to demonstrate clicked, pressed, and released signals
        btn = QPushButton("Simple Button")
        # Click is a combination of press and then a release
        btn.clicked.connect(self.btn_clicked)
        btn.pressed.connect(self.btn_pressed)
        # Release can happen without triggering click, when the window is left while pressing the mouse button
        btn.released.connect(self.btn_released) 

        # Checkable button to demonstrate toggled signal
        checkable_btn = QPushButton("Checkable Button")
        checkable_btn.setCheckable(True)
        checkable_btn.toggled.connect(self.btn_toggled)

        # Add these buttons to a vertical layout
        layout = QVBoxLayout()
        layout.addWidget(btn)
        layout.addWidget(checkable_btn)
        self.setLayout(layout)

    # Slots

    def btn_clicked(self):
        print("Button is Clicked!")

    def btn_pressed(self):
        print("Button is Pressed!")

    def btn_released(self):
        print("Button is Released!")

    # In this case the signal also delivers the checked status which we take as is_checked
    def btn_toggled(self, is_checked):
        print("Button is Toggled!", "Checked:", is_checked)                