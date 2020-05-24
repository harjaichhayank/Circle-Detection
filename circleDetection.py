import cv2
import numpy as np

img = cv2.imread('smarties.png', -1)
output = img.copy()
grey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
grey = cv2.medianBlur(grey, 5)
circles = cv2.HoughCircles(grey, cv2.HOUGH_GRADIENT, 1,
                           20, param1=50, param2=30, minRadius=0, maxRadius=0)

# really important to use np.uint16 and not np.uint8
detected_circles = np.uint16(np.around(circles))
for (x, y, r) in detected_circles[0, :]:
    cv2.circle(output, (x, y), r, (0, 255, 0), 3)
    cv2.circle(output, (x, y), 2, (0, 255, 255), 3)

cv2.imshow('outputImage', output)
cv2.waitKey(0)
cv2.destroyAllWindows()
