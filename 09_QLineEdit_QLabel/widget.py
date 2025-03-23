from PySide6.QtWidgets import QWidget, QPushButton, QLineEdit, QHBoxLayout, QVBoxLayout, QLabel

class Widget(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QLineEdit Demo")
        label1 = QLabel("First Name: ")
        label2 = QLabel("Last Name: ")

        # We define the QLineEdits and a QLabel (show_label) as private class members, because we want to manipulate them via internal methods
        self.__line_edit1 = QLineEdit()
        self.__line_edit2 = QLineEdit()
        grab_btn = QPushButton("Grab Data")
        self.__show_label = QLabel("There you go!")
        
        # Add the label1 and label2 along with the text_edits to their own horizontal layouts
        h_layout1 = QHBoxLayout()
        h_layout2 = QHBoxLayout()
        h_layout1.addWidget(label1)
        h_layout1.addWidget(self.__line_edit1)
        h_layout2.addWidget(label2)
        h_layout2.addWidget(self.__line_edit2)

        # Add these horizontal layouts, along with the button and the show_label to an englobing vertical layout
        v_layout = QVBoxLayout()
        v_layout.addLayout(h_layout1)
        v_layout.addLayout(h_layout2)
        v_layout.addWidget(grab_btn)
        v_layout.addWidget(self.__show_label)
        self.setLayout(v_layout)

        # Connect the grab data button with a respective slot
        grab_btn.clicked.connect(self.__grab_fn)

        # Trying out the different signals in QLineEdit for line_edit1
        #self.__line_edit1.cursorPositionChanged.connect(self.__cursor_pos_fn)
        #self.__line_edit1.selectionChanged.connect(self.__selection_changed_fn)
        #self.__line_edit1.returnPressed.connect(self.__return_pressed_fn)
        # editingFinished signal is like returnPressed, but also triggered when input is changed, and we click on another element to leave the focus of the QLineEdit
        #self.__line_edit1.editingFinished.connect(self.__editing_finished_fn)
        #self.__line_edit1.textChanged.connect(self.__text_changed_fn)
        # This is like textChanged, but is not emitted when the text is changed by something other than the user, like by setText()
        #self.__line_edit1.textEdited.connect(self.__text_edited_fn)


    # Slots

    def __grab_fn(self):
        self.__show_label.setText(f"Hello, {self.__line_edit1.text()} {self.__line_edit2.text()}")
        # Uncomment the below line to test difference between textChanged and textEdited signals
        #self.__line_edit1.setText("DEFAULT :)") 

    def __cursor_pos_fn(self, x, y):
        print(f"Cursor Position: {x},{y}")            

    def __selection_changed_fn(self):
        print(f"Current selection: {self.__line_edit1.selectedText()}")

    def __return_pressed_fn(self):
        print("Enter key Pressed!")

    def __editing_finished_fn(self):
        print("Editing Finished!") 

    def __text_changed_fn(self, arg):
        print(f"Current Text: {arg}")

    def __text_edited_fn(self, arg):
        print(f"Current Text: {arg}")        