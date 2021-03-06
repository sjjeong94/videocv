import time


class Timer:
    def __init__(self, alpha=0.1):
        self.alpha = alpha
        self.time_previous = time.time()

        self.count = 0
        self.latency = 1e-9

    def __call__(self):
        self.count += 1
        time_now = time.time()
        self.time_delta = time_now - self.time_previous
        self.time_previous = time_now

        a = self.alpha
        self.latency = (1-a) * self.latency + a * self.time_delta

        return self.latency
