from PyQt6.QtWidgets import QWidget, QLabel, QVBoxLayout

class BacktestTab(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()
        layout.addWidget(QLabel("Backtesting Tab"))
        self.setLayout(layout)
