import videocv
import numpy as np


def test_video():
    fps = 30.0
    size = (320, 240)
    count = 100
    writer = videocv.Writer('test.mp4', fps, size)
    for _ in range(count):
        image = np.random.randint(0, 255, size=(240, 320, 3), dtype=np.uint8)
        writer(image)
    del writer

    video = videocv.Video('test.mp4')
    assert video.fps == fps
    assert video.size == size
    i = 0
    while video():
        i += 1
    assert i == count
