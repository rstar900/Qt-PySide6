from PySide6.QtWidgets import QMainWindow, QToolBar, QStatusBar, QPushButton
from PySide6.QtGui import QAction, QIcon
from PySide6.QtCore import QSize

class CustomMainWIndow(QMainWindow):

    # Slot for exiting the application
    def quit_app(self):
        self.app.quit() # QApplication's built in exit function

    # Slot for action1's triggered signal (click event)
    def action1_pressed(self):
        print("Triggered Action1!")

    # Slot for action2's triggered signal (click event)
    def action2_pressed(self):
        print("Triggered Action2!")
        # Show a message on status bar with a timeout of 3 seconds (3000 milliseconds)
        self.statusBar().showMessage("This message disappear in 3 seconds", 3000) 

    # Slot for Button's clicked signal (click event)
    def button_pressed(self):
        print("Button Pressed!")    

    # Slot for Main Button's clicked signal (click event)
    def main_button_pressed(self):
        print("Main Button Pressed!")                

    def __init__(self, app):
        super().__init__()

        # Declare an app member (We would need this to exit the app)
        self.app = app

        self.setWindowTitle("Main Window with Menu Bar and Tool Bar")

        # Create a menu bar    
        menu_bar = self.menuBar()

        # Populate it with menu entries
        file_menu = menu_bar.addMenu("File")
        edit_menu = menu_bar.addMenu("Edit")
        window_menu = menu_bar.addMenu("Window") # Just for fun
        setting_menu = menu_bar.addMenu("Setting") # Just for fun
        help_menu = menu_bar.addMenu("Help") # Just for fun

        # Add actions to some of the menu entries

        # For File Menu
        save_action = QAction("Save", self) # Need to give the parent object in this (self)
        open_action = QAction("Open", self)
        exit_action = QAction("Exit", self)
        file_menu.addAction(open_action)
        file_menu.addAction(save_action)
        file_menu.addAction(exit_action)

        # Connect the action with a predefined slot
        exit_action.triggered.connect(self.quit_app)

        # For Edit Menu
        edit_menu.addAction("Cut") # Can add this way, then no need to give parent object as parameter
        edit_menu.addAction("Copy")
        edit_menu.addAction("Paste")
        edit_menu.addAction("Undo")
        edit_menu.addAction("Redo")

        # Create a toolbar
        tool_bar = QToolBar("My Toolbar")
        tool_bar.setIconSize(QSize(16, 16)) # Set the size for an icon
        self.addToolBar(tool_bar) # Add the toolbar to the main window

        # Add actions to the toolbar 
        tool_bar.addAction(exit_action) # reusing the exit_action
        action1 = QAction("Some Action", self)
        tool_bar.addAction(action1) # some arbitrary action
        action1.triggered.connect(self.action1_pressed)

        # Add an action with an icon
        action2 = QAction(QIcon("start.png"), "Some other Action", self)
        tool_bar.addSeparator() # Add separator between action1 and action2
        tool_bar.addAction(action2)
        action2.triggered.connect(self.action2_pressed)

        # Add a button as well to the toolbar with a separator
        tool_bar.addSeparator()
        button = QPushButton("Click Me!")
        tool_bar.addWidget(button)
        button.clicked.connect(self.button_pressed)

        # Add a button in the main area of the window
        main_button = QPushButton("Main Area")
        main_button.setCheckable(True) # To be able to toggle its colour on clicks
        self.setCentralWidget(main_button)
        main_button.clicked.connect(self.main_button_pressed) 

        # Set the status tips for the tool bar's actions
        action1.setStatusTip("This is an arbitrary action")
        action2.setStatusTip("This is an arbitrary action with an icon")
        button.setStatusTip("This is an arbitrary button")

        # Add a status bar (to be able to see the tool tips at botton)
        self.setStatusBar(QStatusBar(self))

        



