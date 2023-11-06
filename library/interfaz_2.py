import sys
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel, QColorDialog
from PyQt6.QtGui import QColor
from PyQt6.QtCore import Qt

class MainWindow(QWidget):
    def __init__(self, patients):
        super().__init__()

        self.patients = patients
        self.initUI()

    def initUI(self):
        self.layout = QVBoxLayout()

        for patient in self.patients:
            label = QLabel()
            label.setFixedSize(100, 100)
            label.setAutoFillBackground(True)
            label.setStyleSheet(f"background-color: {patient.color}")
            self.layout.addWidget(label)

        self.setLayout(self.layout)
        self.setWindowTitle('Pacientes')
        self.show()


    
    