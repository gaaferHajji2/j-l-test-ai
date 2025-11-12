import cv2
import numpy as np

simple_img = np.zeros((256, 256, 3), np.uint8)
cv2.circle(simple_img, (128, 128), 100, (0, 0, 255), 3)
cv2.imshow('Image', simple_img)
cv2.waitKey(0)
cv2.destroyAllWindows()