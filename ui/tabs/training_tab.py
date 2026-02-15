from PyQt6.QtWidgets import QWidget, QPushButton, QVBoxLayout, QLabel
import pyqtgraph as pg

from core.training_worker import TrainingWorker
from core.logger import log


class TrainingTab(QWidget):
    def __init__(self, main_window):
        super().__init__()
        self.main_window = main_window

        # ----- Data Storage -----
        self.epochs = []
        self.losses = []
        self.accuracies = []

        # ----- UI Elements -----
        self.status = QLabel("Idle")
        self.start_btn = QPushButton("Start Training")
        self.start_btn.clicked.connect(self.start_training)

        # ----- Plot -----
        self.plot_widget = pg.PlotWidget()
        self.plot_widget.setBackground('k') # dark background
        self.plot_widget.addLegend()

        self.loss_curve = self.plot_widget.plot(
            [], [], pen='r', name="Loss"
        )
        self.acc_curve = self.plot_widget.plot(
            [], [], pen='g', name="Accuracy"
        )

        # ----- Layout -----
        layout = QVBoxLayout()
        layout.addWidget(self.status)
        layout.addWidget(self.start_btn)
        layout.addWidget(self.plot_widget)
        self.setLayout(layout)

    def start_training(self):
        log("SYSTEM", "Starting training worker")

        # Reset data
        self.epochs.clear()
        self.losses.clear()
        self.accuracies.clear()
        self.loss_curve.setData([], [])
        self.acc_curve.setData([], [])

        worker = TrainingWorker()
        self.main_window.start_worker(worker)

        worker.progress.connect(self.on_progress)
        worker.finished.connect(lambda: self.status.setText("Finished"))
        worker.log.connect(log)

    def on_progress(self, data):
        epoch = data["epoch"]
        loss = data["loss"]
        acc = data["accuracy"]

        self.epochs.append(epoch)
        self.losses.append(loss)
        self.accuracies.append(acc)

        self.loss_curve.setData(self.epochs, self.losses)
        self.acc_curve.setData(self.epochs, self.accuracies)

        self.status.setText(
            f"Epoch {epoch} | Loss {loss:.4f} | Acc {acc:.2f}"
        )
