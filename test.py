import cv2
import videocv

if __name__ == '__main__':
    video = videocv.Video('video/test.mp4')
    writer = videocv.Writer('video/record.mp4', 30, (1280, 720))
    while video():
        image = video.frame
        writer(image)
        cv2.imshow('image', image)
