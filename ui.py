import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

class PhotoLabel(QLabel):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setAlignment(Qt.AlignCenter)


class Template(QWidget):

    def __init__(self):
        super().__init__()
        self.title = 'Military Vehicle Identifier'
        self.setWindowTitle(self.title)
        
        sqD = 750
        self.photo = PhotoLabel()
        btn = QPushButton('Browse')
        
        btn.clicked.connect(self.open_image)
        grid = QGridLayout(self)
        #self.setText('\n\n Drop Image Here \n\n')
        grid.addWidget(btn, 1, 0, Qt.AlignHCenter)
        grid.addWidget(self.photo, 1, 0)
        self.resize(sqD, sqD)


    def open_image(self, filename=None):
        if not filename:
            filename, _ = QFileDialog.getOpenFileName(self, 'Select Photo', QDir.currentPath(), 'Images (*.png *.jpg)')
            if not filename:
                return
        self.photo.setPixmap(QPixmap(filename))
        


if __name__ == '__main__':
    app = QApplication(sys.argv)
    gui = Template()
    gui.show()
    sys.exit(app.exec_())