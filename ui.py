import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from Interpreter import *

class PhotoLabel(QLabel):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setAlignment(Qt.AlignCenter)



class Template(QWidget):

    def __init__(self):
        super().__init__()
        self.title = 'Military Vehicle Identifier'
        self.interpret = Interpreter()
        self.filename = ''
        self.string_msg = ''
        self.setWindowTitle(self.title) # sets title
        self.win = QMainWindow()
        self.photo = PhotoLabel()
        self.sqD = 500 
        self.strung = QLabel('')
        self.grid = QGridLayout(self)
        label = QLabel(self.win)
        label.setText("Take an image from your file directory and this program will guess what it is")
        
        self.btn0 = QPushButton('Browse') # creates and names button obj
        
        self.btn0.clicked.connect(self.open_image) # opens file explorer
        self.setFixedWidth(750)
        self.setFixedHeight(750)
        
        self.grid.addWidget(label, 0, 0, Qt.AlignHCenter)
        self.grid.addWidget(self.photo, 1, 0, Qt.AlignHCenter)
        self.grid.addWidget(self.btn0, 2, 0, Qt.AlignHCenter)
        self.grid.addWidget(self.strung, 3, 0, Qt.AlignHCenter)
    
        self.resize(self.sqD, self.sqD)

    def open_image(self, filename=None):
        if not filename:
            filename, _ = QFileDialog.getOpenFileName(self, 'Select Photo', QDir.currentPath(), 'Images (*.png *.jpg)')
            if not filename:
                return
        self.filename = filename
        self.update()
        pmap = QPixmap(filename)
        self.photo.setPixmap(pmap)
    
    def update(self):
        self.grid.removeWidget(self.strung)
        self.string_msg = self.interpret.insert_image(self.filename, 'modelA')
        self.strung = QLabel(self.win)
        self.strung.setText(self.string_msg)
        self.grid.addWidget(self.strung, 3, 0, Qt.AlignHCenter)
        