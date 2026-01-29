from PyQt6.QtWidgets import QWidget, QLabel, QVBoxLayout

class LiveTab(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()
        layout.addWidget(QLabel("Live Trading Tab"))
        self.setLayout(layout)
