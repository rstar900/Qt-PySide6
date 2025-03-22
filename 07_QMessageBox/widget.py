from PySide6.QtWidgets import QWidget, QMessageBox, QPushButton, QVBoxLayout

class Widget(QWidget):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("QMessageBox Intro")

        # Create buttons
        hard_btn = QPushButton("Hard")
        critical_btn = QPushButton("Critical")
        question_btn = QPushButton("Question")
        info_btn = QPushButton("Information")
        warning_btn = QPushButton("Warning")
        about_btn = QPushButton("About")

        # Create a Vertical layout and add buttons to it
        layout = QVBoxLayout()
        layout.addWidget(hard_btn)
        layout.addWidget(critical_btn)
        layout.addWidget(question_btn)
        layout.addWidget(info_btn)
        layout.addWidget(warning_btn)
        layout.addWidget(about_btn)
        
        # Set this as a layout of the main widget
        self.setLayout(layout)

        # Connect the buttons' clicked event with the respective slots
        hard_btn.clicked.connect(self.hard_clicked)
        critical_btn.clicked.connect(self.critical_clicked)
        question_btn.clicked.connect(self.question_clicked)
        info_btn.clicked.connect(self.info_clicked)
        warning_btn.clicked.connect(self.warning_clicked)
        about_btn.clicked.connect(self.about_clicked)

    # Define the slots for clicked signals foe each button

    # Logic to do the Critical QMessageBox the hard way
    def hard_clicked(self):
        msg_box = QMessageBox(self)
        msg_box.setWindowTitle("Critical Message Box (Hard Way!)")
        msg_box.setMinimumSize(700, 200) # Set the width as 800px and height as 200px

        # Set the short and descriptive texts
        msg_box.setText("Something happened")
        msg_box.setInformativeText("Do you want to do something about it")

        # The icon defines the type of message box
        msg_box.setIcon(QMessageBox.Critical)

        # Set OK and Cancel as the buttons shown inside the box, and OK as highlighted by default
        msg_box.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        msg_box.setDefaultButton(QMessageBox.Ok)

        # Show the message box
        ret = msg_box.exec()
        # Depending on the button clicked, do something (Type of button clicked is returned by exec() call)
        if ret == QMessageBox.Ok:
            print("Pressed OK")
        else:
            print("Pressed Cancel")    

    # Logic to do the Critical QMessageBox the easy way
    def critical_clicked(self):
        # In this case the initialisation of message box, setting the icon, showing and returning button click happens in one step
        ret = QMessageBox.critical(self, "Critical Message Box",
                                    "Critical Message!",
                                    QMessageBox.Ok | QMessageBox.Cancel,
                                    QMessageBox.Ok)
        # Depending on the button clicked, do something (Type of button clicked is returned by exec() call)
        if ret == QMessageBox.Ok:
            print("Pressed OK")
        else:
            print("Pressed Cancel") 

    # Logic to do the Question QMessageBox the easy way
    def question_clicked(self):
        # In this case the initialisation of message box, setting the icon, showing and returning button click happens in one step
        ret = QMessageBox.question(self, "Question Message Box",
                                    "Some Question",
                                    QMessageBox.Ok | QMessageBox.Cancel,
                                    QMessageBox.Ok)
        # Depending on the button clicked, do something (Type of button clicked is returned by exec() call)
        if ret == QMessageBox.Ok:
            print("Pressed OK")
        else:
            print("Pressed Cancel")

    # Logic to do the Information QMessageBox the easy way
    def info_clicked(self):
        # In this case the initialisation of message box, setting the icon, showing and returning button click happens in one step
        ret = QMessageBox.information(self, "Information Message Box",
                                    "Some Information",
                                    QMessageBox.Ok | QMessageBox.Cancel,
                                    QMessageBox.Ok)
        # Depending on the button clicked, do something (Type of button clicked is returned by exec() call)
        if ret == QMessageBox.Ok:
            print("Pressed OK")
        else:
            print("Pressed Cancel")

    # Logic to do the Warning QMessageBox the easy way
    def warning_clicked(self):
        # In this case the initialisation of message box, setting the icon, showing and returning button click happens in one step
        ret = QMessageBox.warning(self, "Warning Message Box",
                                    "Some Warning!",
                                    QMessageBox.Ok | QMessageBox.Cancel,
                                    QMessageBox.Ok)
        # Depending on the button clicked, do something (Type of button clicked is returned by exec() call)
        if ret == QMessageBox.Ok:
            print("Pressed OK")
        else:
            print("Pressed Cancel")

    # Logic to do the About QMessageBox the easy way
    def about_clicked(self):
        # In this case the initialisation of message box, setting the icon, showing and returning button click happens in one step
        ret = QMessageBox.about(self, "About Message Box",
                                    "About Me :)")
        # Depending on the button clicked, do something (Type of button clicked is returned by exec() call)
        if ret == QMessageBox.Ok:
            print("Pressed OK")
        else:
            # In this case it will always execute this, as OK is there by default, but we haven't set it to return anything
            print("Pressed Cancel")            