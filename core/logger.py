from core.signals import signal_bus

# everything will go through this logger so that we can maintain a record
# of logs in the UI as well as in files or console

def log(level: str, message: str):
    signal_bus.log.emit(level, message)
