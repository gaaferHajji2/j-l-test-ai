import cv2

img = cv2.imread('tomato.jpg')
cv2.imshow('Image', img); # type: ignore
cv2.waitKey(0)

img_convert = cv2.cvtColor(img, cv2.COLOR_BGR2RGB); # type: ignore
cv2.imshow('Image', img_convert)
cv2.waitKey(0)

cv2.destroyAllWindows()