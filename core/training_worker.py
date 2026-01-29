import time
from core.worker import Worker

# note: there is no model yet. this is just a workflow to check

class TrainingWorker(Worker):
    def run(self):
        self.log.emit("MODEL", "Training started")

        for epoch in range(1, 21):
            if not self._running:
                self.log.emit("SYSTEM", "Training stopped")
                break

            # Simulate training
            time.sleep(0.3)

            self.progress.emit({
                "epoch": epoch,
                "loss": 1 / epoch,
                "accuracy": epoch / 20
            })

            self.log.emit("MODEL", f"Epoch {epoch} complete")

        self.finished.emit()
