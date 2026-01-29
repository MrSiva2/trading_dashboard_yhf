from PyQt6.QtWidgets import (
    QMainWindow, QTabWidget, QDockWidget
)
from PyQt6.QtCore import Qt

from PyQt6.QtCore import QThread

from ui.logs import LogsWidget
from ui.tabs.training_tab import TrainingTab
from ui.tabs.backtest_tab import BacktestTab
from ui.tabs.live_tab import LiveTab

from core.signals import signal_bus

# Here, we are connecting the other tabs befor the main window
# so that, we will not lose any logs during the tab initializations
# I am currently not opting the buffered logging approach for simplicity

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Trading ML Dashboard")
        self.resize(1400, 900)

        # ---- Logs Dock FIRST ----
        self.logs_widget = LogsWidget()
        dock = QDockWidget("Logs", self)
        dock.setWidget(self.logs_widget)
        dock.setAllowedAreas(
            Qt.DockWidgetArea.BottomDockWidgetArea |
            Qt.DockWidgetArea.RightDockWidgetArea
        )
        self.addDockWidget(Qt.DockWidgetArea.BottomDockWidgetArea, dock)

        # ---- Connect signal FIRST ----
        signal_bus.log.connect(self.logs_widget.add_log)

        # ---- THEN create tabs ----
        self.tabs = QTabWidget()
        self.tabs.addTab(TrainingTab(), "Training")
        self.tabs.addTab(BacktestTab(), "Backtesting")
        self.tabs.addTab(LiveTab(), "Live")
        self.setCentralWidget(self.tabs)

        from core.logger import log
        log("SYSTEM", "Logger connected successfully")

    def start_worker(self, worker):
        thread = QThread()
        worker.moveToThread(thread)

        worker.log.connect(signal_bus.log)
        thread.started.connect(worker.run)
        worker.finished.connect(thread.quit)
        worker.finished.connect(worker.deleteLater)
        thread.finished.connect(thread.deleteLater)
        thread.start()
        return worker
    
