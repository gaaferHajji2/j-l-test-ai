import cv2
import numpy as np

simple_img = np.zeros((512, 512, 3), np.uint8)
points = np.array([[115, 100], [175, 300], [215, 200], [300, 100]], np.int32)
cv2.polylines(simple_img, [points], True, (0, 0, 255), 5)
cv2.imshow('Image', simple_img)
cv2.waitKey(0)
cv2.destroyAllWindows()