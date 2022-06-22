import cv2
import numpy as np
import videocv


def test_video():
    video = videocv.Video('video/test0.mp4')
    writer = videocv.Writer('video/record.mp4', video.fps, video.size)
    while video():
        image = video.frame

        log = '%8.2f FPS' % (1/video.timer.latency)
        cv2.putText(image, log, (0, 20), 0, 0.5, (255, 0, 0), 1)
        log = '%8d frames' % (video.timer.count)
        cv2.putText(image, log, (0, 40), 0, 0.5, (255, 0, 0), 1)
        log = '%8d / %8d' % (video.get_pos(), video.frame_count)
        cv2.putText(image, log, (0, 60), 0, 0.5, (255, 0, 0), 1)

        writer(image)
        cv2.imshow('image', image)


def test_video2():
    video = videocv.Video2('video/test0.mp4', speed=2)
    while video():
        image = video.frame

        log = '%8.2f FPS' % (1/video.timer.latency)
        cv2.putText(image, log, (0, 20), 0, 0.5, (255, 0, 0), 1)
        log = '%8d frames' % (video.timer.count)
        cv2.putText(image, log, (0, 40), 0, 0.5, (255, 0, 0), 1)
        log = '%8d / %8d' % (video.get_pos(), video.frame_count)
        cv2.putText(image, log, (0, 60), 0, 0.5, (255, 0, 0), 1)

        cv2.imshow('image', image)


def test_camera():
    video = videocv.Camera(0)
    writer = videocv.Writer('video/camera.mp4', video.fps, video.size)
    while video():
        image = video.frame

        log = '%8.2f FPS' % (1/video.timer.latency)
        cv2.putText(image, log, (0, 20), 0, 0.5, (255, 0, 0), 1)
        log = '%8d frames' % (video.timer.count)
        cv2.putText(image, log, (0, 40), 0, 0.5, (255, 0, 0), 1)

        writer(image)
        cv2.imshow('image', image)


def test_video2_cam():
    video = videocv.Video2(0, speed=0.5)
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


def test_multi():
    video0 = videocv.Video2('./video/test0.mp4')
    video1 = videocv.Video2('./video/test1.mp4')
    video2 = videocv.Video2('./video/test2.mp4')
    video3 = videocv.Video2('./video/test3.mp4')

    size = (640, 360)

    while video0():
        frame0 = video0.frame
        frame1 = video1.frame
        frame2 = video2.frame
        frame3 = video3.frame

        image0 = cv2.resize(frame0, size, interpolation=cv2.INTER_AREA)
        image1 = cv2.resize(frame1, size, interpolation=cv2.INTER_AREA)
        image2 = cv2.resize(frame2, size, interpolation=cv2.INTER_AREA)
        image3 = cv2.resize(frame3, size, interpolation=cv2.INTER_AREA)

        image_top = np.concatenate([image0, image1], axis=1)
        image_bot = np.concatenate([image2, image3], axis=1)
        image = np.concatenate([image_top, image_bot], axis=0)

        cv2.imshow('image', image)

    video0.stop()
    video1.stop()
    video2.stop()
    video3.stop()


if __name__ == '__main__':
    test_video()
    test_video2()
    # test_camera()
    # test_video2_cam()
    # test_multi()
