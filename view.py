# View

# FrontEnd:
# =========
# Presenting the data to the user

from PyQt5 import QtWidgets as qtw
from PyQt5 import QtCore as qtc
from PyQt5 import QtGui as gui

import sys

# import PyQt5
# from PyQt5.QtCore import Qt
# from PyQt5.QtGui import QFont


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
        self.main_layout = qtw.QVBoxLayout(self)
        self.form_layout = qtw.QFormLayout(self)


        # main_header = qtw.QLabel("Time-Booking System",self)
        # self.form_layout.addWidget(main_header)
        
        # col_name =qtw.QLabel("Name",self)
        name_box = qtw.QLineEdit()
        name_box.setFont(gui.QFont("Arial",12))
        project_name_box = qtw.QLineEdit()
        project_name_box.setFont(gui.QFont("Arial",12))
        date_box = qtw.QLineEdit()
        date_box.setFont(gui.QFont("Arial",12))
        hours_box = qtw.QLineEdit()
        hours_box.setFont(gui.QFont("Arial",12))



        self.form_layout.addRow('Name',name_box)
        self.form_layout.addRow('Project Name',project_name_box)
        self.form_layout.addRow('Date',date_box)
        self.form_layout.addRow('Hours',hours_box)


        #Nesting Layouts
        self.main_layout.addLayout(self.form_layout)





def main():
    # Create an instance of Qapplication
    app = qtw.QApplication(sys.argv)
    # Create an instance of GUI
    window = TBGUI()
    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()

