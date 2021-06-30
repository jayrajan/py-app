# View

# FrontEnd:
# =========
# Presenting the data to the user

from PyQt5 import QtWidgets as qtw
import sys


class TBGUI(qtw.QWidget):
    def __init__(self):
        super().__init__()
        self.title = 'Time Booking System'
        self.left = 10
        self.top = 10
        self.width = 840
        self.height = 480
        self.initUI()


    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        # LAYOUTS
        self.mainLayout = qtw.QVBoxLayout(self)
        mainLabel1 = qtw.QLabel('Time-Booking System',self)
        self.mainLayout.addWidget(mainLabel1)





def main():
    # Create an instance of Qapplication
    app = qtw.QApplication(sys.argv)
    # Create an instance of GUI
    window = TBGUI()
    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()

