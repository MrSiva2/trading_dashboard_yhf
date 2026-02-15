from PyQt6.QtWidgets import QWidget, QLabel, QVBoxLayout

class BacktestTab(QWidget):
    def __init__(self, main_window):
        super().__init__()
        self.main_window = main_window
        layout = QVBoxLayout()
        layout.addWidget(QLabel("Backtesting Tab"))
        self.setLayout(layout)
