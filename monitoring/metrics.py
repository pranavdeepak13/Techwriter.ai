import time

class Metrics:
    def __init__(self):
        self.start_time = None
        self.feedback_count = 0

    def start(self):
        self.start_time = time.time()

    def stop(self):
        return round(time.time() - self.start_time, 2) if self.start_time else None

    def record_feedback(self):
        self.feedback_count += 1

    def summary(self):
        return {
            "time_elapsed": self.stop(),
            "feedback_iterations": self.feedback_count
        }
