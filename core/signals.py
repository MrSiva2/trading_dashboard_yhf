from PyQt6.QtCore import QObject, pyqtSignal

# This is a global signal bus (thread-safe backbone)
# we are doing this because threads cannot touch UI
# and signals are the safe bridge
class SignalBus(QObject):
    log = pyqtSignal(str, str)  
    # level, message

signal_bus = SignalBus()
