from PyQt6.QtWidgets import QWidget, QPushButton, QVBoxLayout, QLabel
from core.training_worker import TrainingWorker
from core.logger import log

class TrainingTab(QWidget):
    def __init__(self, main_window):
        super().__init__()
        self.main_window = main_window

        self.status = QLabel("Idle")
        self.start_btn = QPushButton("Start Training")
        self.start_btn.clicked.connect(self.start_training)

        layout = QVBoxLayout()
        layout.addWidget(self.status)
        layout.addWidget(self.start_btn)
        self.setLayout(layout)

    def start_training(self):
        log("SYSTEM", "Starting training worker")
        worker = TrainingWorker()
        self.main_window.start_worker(worker)

        worker.progress.connect(self.on_progress)
        worker.finished.connect(lambda: self.status.setText("Finished"))
        worker.log.connect(log)

    def on_progress(self, data):
        self.status.setText(
            f"Epoch {data['epoch']} | "
            f"Loss {data['loss']:.4f} | "
            f"Acc {data['accuracy']:.2f}"
        )
