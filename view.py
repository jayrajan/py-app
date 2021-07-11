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
        self.clear_status = False


    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        # LAYOUTS
        self.main_layout = qtw.QVBoxLayout(self)
        self.form_layout = qtw.QFormLayout(self)
        self.button_layout = qtw.QHBoxLayout(self)


        # input form 
        self.name_box = qtw.QLineEdit()
        self.name_box.setFont(gui.QFont("Arial",12))
        self.project_name_box = qtw.QLineEdit()
        self.project_name_box.setFont(gui.QFont("Arial",12))
        self.from_date_box = qtw.QLineEdit()
        self.from_date_box.setFont(gui.QFont("Arial",12))
        self.to_date_box = qtw.QLineEdit()
        self.to_date_box.setFont(gui.QFont("Arial",12))

        
        self.hours_box = qtw.QLineEdit()
        self.hours_box.setFont(gui.QFont("Arial",12))

        
        self.form_layout.addRow('Name',self.name_box)
        self.form_layout.addRow('Project Name',self.project_name_box)
        self.form_layout.addRow('From Date',self.from_date_box)
        self.form_layout.addRow('To Date',self.to_date_box)
        self.form_layout.addRow('Hours',self.hours_box)

        
        # button
        self.save_button = qtw.QPushButton('Save', self)
        self.save_button.clicked.connect(self.save_items)
        self.button_layout.addWidget(self.save_button)

        self.clear_button = qtw.QPushButton('Clear', self)
        self.clear_button.clicked.connect(self.clear_items)
        self.button_layout.addWidget(self.clear_button)


        #Nesting Layouts
        self.main_layout.addLayout(self.form_layout)
        self.main_layout.addLayout(self.button_layout)


    def clear_items(self):
        self.name_box.clear()
        self.project_name_box.clear()
        self.from_date_box.clear()
        self.to_date_box.clear()
        self.hours_box.clear()
        self.clear_status = True

        return self.clear_status

    def save_items(self):
        pass


def main():
    # Create an instance of Qapplication
    app = qtw.QApplication(sys.argv)
    # Create an instance of GUI
    window = TBGUI()
    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()

