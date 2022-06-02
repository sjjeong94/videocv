import cv2
import videocv


def test_video():
    video = videocv.Video('video/test.mp4')
    writer = videocv.Writer('video/record.mp4', video.fps, video.size)
    while video():
        image = video.frame
        writer(image)
        print(video.timer.latency)
        cv2.imshow('image', image)


def test_camera():
    camera = videocv.Camera(0)
    writer = videocv.Writer('video/camera.mp4', camera.fps, camera.size)
    while camera():
        image = camera.frame
        writer(image)
        print(camera.timer.latency)
        cv2.imshow('image', image)


if __name__ == '__main__':
    test_video()
    test_camera()
