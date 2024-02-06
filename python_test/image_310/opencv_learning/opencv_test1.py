import cv2 as cv

def image_read(image_path):
    image = cv.imread(image_path)
    cv.imshow("image", image)
    cv.waitKey(0)
    cv.destroyAllWindows()

if __name__ == '__main__':
    image_path = r"../match_test_picture/1414.png"
    image_read(image_path)