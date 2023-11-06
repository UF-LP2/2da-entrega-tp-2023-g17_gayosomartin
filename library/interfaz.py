import sys
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QHBoxLayout, QGridLayout
from PyQt6.QtGui import  QColor
from library.Clases import Pacientes


class ColoredSquares(QWidget):
    def __init__(self,pac:Pacientes):
        super().__init__()
        self.pac = pac
        self.initUI()
        

    def initUI(self):
        self.setWindowTitle('Ventana principal')
        self.setGeometry(100, 100, 1000, 750)

        layout = QVBoxLayout()
        grid_layout = QGridLayout()
        
        
        colors = [QColor('red'), QColor('dark blue'), QColor('dark green'), QColor('dark yellow'),QColor('dark orange')]
 
        if(self.pac.color == "rojo"):
            button = QPushButton()
            button.setMaximumSize(30, 30)
            button.setStyleSheet(f"background-color: {colors[0].name()}")
            grid_layout.addWidget(button)

        elif(self.pac.color == "naranja"):
            button = QPushButton()
            button.setMaximumSize(30, 30)
            button.setStyleSheet(f"background-color: {colors[4].name()}")
            grid_layout.addWidget(button)
        elif(self.pac.color == "amarillo"):
            button = QPushButton()
            button.setMaximumSize(30, 30)
            button.setStyleSheet(f"background-color: {colors[3].name()}")
            grid_layout.addWidget(button)
        elif(self.pac.color == "verde"):
            button = QPushButton()
            button.setMaximumSize(30, 30)
            button.setStyleSheet(f"background-color: {colors[2].name()}")
            grid_layout.addWidget(button)
        else:
            button = QPushButton()
            button.setMaximumSize(30, 30)
            button.setStyleSheet(f"background-color: {colors[1].name()}")
            grid_layout.addWidget(button)



        layout.addLayout(grid_layout)
        self.setLayout(layout)


