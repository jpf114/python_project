import cv2 as cv

def match_image(image_path, temp_path):
    image = cv.imread(image_path)
    temp = cv.imread(temp_path)
    th, tw = temp.shape[:2]

    # gary_image = cv.cvtColor(image, cv.COLOR_RGB2GRAY)

    methods = [cv.TM_SQDIFF_NORMED, cv.TM_CCORR_NORMED, cv.TM_CCOEFF_NORMED]
    # methods = [cv.TM_CCOEFF_NORMED]

    for md in methods:
        result = cv.matchTemplate(image, temp, md)
        min_val, max_val, min_loc, max_loc = cv.minMaxLoc(result)

        if md == cv.TM_SQDIFF_NORMED:  # cv.TM_SQDIFF_NORMED最小时最相似，其他最大时最相似
            tl = min_loc  # 左上角点位
        else:
            tl = max_loc
        br = (tl[0] + tw, tl[1] + th)
        cv.rectangle(image, tl, br, color=(0, 0, 255), thickness=2)

        # text = 'use the function in OpenCV'
        # cv.putText(image, text, tl, cv.QT_FONT_BLACK, 0.85, color=(0, 0, 255), thickness=2)
        # cv.imshow('text', image)

        cv.imshow("match-" + str(md), image)

    cv.waitKey(0)
    cv.destroyAllWindows()

# 按间距中的绿色按钮以运行脚本。
if __name__ == '__main__':
    image_path = r"match_test_picture/1414.png"
    temp_path = r"match_test_picture/1515.png"
    match_image(image_path, temp_path)