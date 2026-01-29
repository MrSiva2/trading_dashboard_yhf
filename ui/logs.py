from PyQt6.QtWidgets import (
    QWidget, QVBoxLayout, QTextEdit, QComboBox
)
from PyQt6.QtGui import QColor, QTextCharFormat
from PyQt6.QtCore import Qt

class LogsWidget(QWidget):
    def __init__(self):
        super().__init__()

        self.filter = QComboBox()
        self.filter.addItems(["ALL", "SYSTEM", "MODEL", "DATA", "ERROR"])

        self.text = QTextEdit()
        self.text.setReadOnly(True)

        layout = QVBoxLayout()
        layout.addWidget(self.filter)
        layout.addWidget(self.text)
        self.setLayout(layout)

        self.logs = []

    def add_log(self, level, message):
        self.logs.append((level, message))
        self.refresh()

    def refresh(self):
        self.text.clear()
        selected = self.filter.currentText()

        for level, msg in self.logs:
            if selected != "ALL" and level != selected:
                continue

            self.text.append(f"[{level}] {msg}")
