import cv2

# print(cv2.__version__)

img = cv2.imread('./tomato.jpg')

cv2.imshow('Image', img) # type: ignore
cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.imwrite('tomato-02.png', img) # type: ignore