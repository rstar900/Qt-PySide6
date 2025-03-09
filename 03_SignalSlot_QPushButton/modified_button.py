# Here we modify the QPushButton to have a slot to react on clicked signal

from PySide6.QtWidgets import QPushButton

class ModifiedQPushButton(QPushButton):
    # We define this slot as private so that it cannot be called from outside of the class
    # It will receive the bool (data) whether it is checked or not along with the signal
    # Since we want it to modify our button, we define it inside the class
    def __on_clicked(self, data):
        self.setText("Click Me!\nChecked Status: {}".format(data))

    def __init__(self):
        super().__init__()
        self.setText("Click Me!\nChecked Status: False") # text to start with
        self.setFixedSize(self.sizeHint()) # Adjust the size of the button accordingly
        # Set the checkable property to true, to be able to see the check status
        self.setCheckable(True)
        # Connect the clicked signal with the slot    
        self.clicked.connect(self.__on_clicked)