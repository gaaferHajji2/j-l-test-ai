import cv2

camera = cv2.VideoCapture(0)
# define the camera resolution
camera.set(cv2.CAP_PROP_FRAME_WIDTH, 1024)
camera.set(cv2.CAP_PROP_FRAME_HEIGHT, 640)
# define the brightness of camera
camera.set(cv2.CAP_PROP_BRIGHTNESS, 80)
# define the contrast of camera
camera.set(cv2.CAP_PROP_CONTRAST, 55)
# print the values
print("width: ", camera.get(cv2.CAP_PROP_FRAME_WIDTH))
print("height: ", camera.get(cv2.CAP_PROP_FRAME_HEIGHT))
print("brightness: ", camera.get(cv2.CAP_PROP_BRIGHTNESS))
print("Sharpness: ", camera.get(cv2.CAP_PROP_SHARPNESS))
# get the frames
while True:
    ret, frame = camera.read()
    if not ret:
        print("no ret found")
        break
    cv2.imshow('frame', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
        # Check if window is closed
    if cv2.getWindowProperty('frame', cv2.WND_PROP_VISIBLE) < 1:
        break
camera.release()
cv2.destroyAllWindows()