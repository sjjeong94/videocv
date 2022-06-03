import cv2
import videocv


def test_video():
    video = videocv.Video('video/test.mp4')
    writer = videocv.Writer('video/record.mp4', video.fps, video.size)
    while video():
        image = video.frame
        writer(image)

        log = '%8.2f FPS' % (1/video.timer.latency)
        cv2.putText(image, log, (0, 20), 0, 0.5, (255, 0, 0), 1)
        log = '%8d frames' % (video.timer.count)
        cv2.putText(image, log, (0, 40), 0, 0.5, (255, 0, 0), 1)

        cv2.imshow('image', image)


def test_camera():
    video = videocv.Camera(0)
    writer = videocv.Writer('video/camera.mp4', video.fps, video.size)
    while video():
        image = video.frame

        writer(image)
        log = '%8.2f FPS' % (1/video.timer.latency)
        cv2.putText(image, log, (0, 20), 0, 0.5, (255, 0, 0), 1)
        log = '%8d frames' % (video.timer.count)
        cv2.putText(image, log, (0, 40), 0, 0.5, (255, 0, 0), 1)

        cv2.imshow('image', image)


def test_video2():
    video = videocv.Video2('video/test.mp4', speed=2)
    video()
    while True:
        image = video.frame

        log = '%8.2f FPS' % (1/video.timer.latency)
        cv2.putText(image, log, (0, 20), 0, 0.5, (255, 0, 0), 1)
        log = '%8d frames' % (video.timer.count)
        cv2.putText(image, log, (0, 40), 0, 0.5, (255, 0, 0), 1)

        cv2.imshow('image', image)
        if cv2.waitKey(1) == 27:
            video.stop()
            break


if __name__ == '__main__':
    test_video()
    test_camera()
    test_video2()
