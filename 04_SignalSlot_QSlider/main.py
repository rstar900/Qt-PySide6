import sys
from PySide6.QtWidgets import QApplication, QSlider
from PySide6.QtCore import Qt # for using stuff from general Qt namespace

# Define a slot for printing the slider value on the console
def on_slide(data):
    print("Slider Moved to: {}".format(data))

def main():
    app = QApplication(sys.argv)
    slider = QSlider(Qt.Horizontal) # make it a horizontal slider

    # Set min and max values
    slider.setMinimum(0)
    slider.setMaximum(100)

    # Set default location
    slider.setValue(25)

    # Connect the valueChanged() signal to the on_slide() slot
    slider.valueChanged.connect(on_slide)

    slider.show()
    app.exec()

if __name__ == "__main__":
    main()