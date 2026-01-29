from PyQt6.QtCore import QObject, pyqtSignal

class Worker(QObject):
    finished = pyqtSignal()
    progress = pyqtSignal(dict)
    log = pyqtSignal(str, str)

    def __init__(self):
        super().__init__()
        self._running = True

    def stop(self):
        self._running = False
        self.log.emit("SYSTEM", "Worker stop requested")
