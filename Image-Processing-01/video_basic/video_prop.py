import cv2

camera = cv2.VideoCapture(0)

# define the camera resolution
camera.set(cv2.CAP_PROP_FRAME_WIDTH, 1024)
camera.set(cv2.CAP_PROP_FRAME_HEIGHT, 640)

# define the brightness of camera
camera.set(cv2.CAP_PROP_BRIGHTNESS, 80)

# define the contrast of camera
camera.set(cv2.CAP_PROP_CONTRAST, 55)

