import cv2
import time
from threading import Thread
from videocv.timer import Timer, Timer2


class Video:
    def __init__(self, video_file):
        cap = cv2.VideoCapture(video_file)
        fps = cap.get(cv2.CAP_PROP_FPS)
        width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

        self.cap = cap
        self.fps = fps
        self.size = (width, height)

        self.timer = Timer2()
        self.latency = self.timer.latency

    def __call__(self):
        success, frame = self.cap.read()
        self.frame = frame

        self.latency = self.timer()

        key = cv2.waitKey(1) & 0xFF
        if key == 27:
            return False
        return success

    def __del__(self):
        self.cap.release()


class Video2:
    def __init__(self, video_file, speed=1):
        cap = cv2.VideoCapture(video_file)
        fps = cap.get(cv2.CAP_PROP_FPS)
        width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

        self.cap = cap
        self.fps = fps
        self.size = (width, height)

        self.timer = Timer2()
        self.latency = self.timer.latency

        self.success = True
        self.running = True

        self.time_sleep = 0.0
        self.speed = speed

    def __call__(self):
        self.success, self.frame = self.cap.read()
        Thread(target=self.run, args=()).start()
        return self

    def run(self):
        while self.running and self.success:
            self.success, self.frame = self.cap.read()
            self.latency = self.timer()

            time_run = self.timer.time_delta - self.time_sleep
            self.time_sleep = 1 / (self.fps * self.speed) - time_run
            if self.time_sleep < 1e-6:
                self.time_sleep = 1e-6
            time.sleep(self.time_sleep)

    def stop(self):
        self.running = False


class Writer:
    def __init__(self, video_file, fps, size):
        fourcc = cv2.VideoWriter_fourcc(*'mp4v')
        self.writer = cv2.VideoWriter(video_file, fourcc, fps, size)

    def __call__(self, image):
        self.writer.write(image)

    def __del__(self):
        self.writer.release()
