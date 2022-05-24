import cv2
import videocv

if __name__ == '__main__':
    video = videocv.Video('video/test.mp4')
    while video():
        cv2.imshow('frame', video.frame)
