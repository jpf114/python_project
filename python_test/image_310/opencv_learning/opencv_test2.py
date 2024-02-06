import cv2 as cv

def video_read(video_path):
    cv_cap = cv.VideoCapture(video_path)
    while True:
        ret, frame = cv_cap.read()
        if not ret:
            break
        cv.imshow("frame", frame)
        if cv.waitKey(33) & 0xFF == ord('q'):
            break

    cv_cap.release()
    cv.destroyAllWindows()

if __name__ == '__main__':
    video_path = r"../video/video2.mp4"
    video_read(video_path)