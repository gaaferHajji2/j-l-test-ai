import cv2
import numpy as np

simple_img = np.zeros((512, 512, 3), np.uint8)
simple_cv_font = cv2.FONT_HERSHEY_TRIPLEX
cv2.putText(simple_img, 'JLoka', (150, 256), simple_cv_font, 3, (0, 0, 255), 3, cv2.LINE_8)
cv2.imshow('Image', simple_img)
cv2.waitKey(0)
cv2.destroyAllWindows()