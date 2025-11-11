import cv2

print(cv2.__version__)

img = cv2.imread('./QR.png')

cv2.imshow('Image', img); # type: ignore
cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.imwrite('Qr-02.png', img); # type: ignore