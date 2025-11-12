import cv2

cap = cv2.VideoCapture(0)

# Check if video opened successfully
if not cap.isOpened():
    print("Error: Could not open video.")
    exit()

# Get video properties
fps = cap.get(cv2.CAP_PROP_FPS)
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

print(f"FPS: {fps}, Resolution: {width}x{height}")

codec = cv2.VideoWriter_fourcc(*'mp4v') # type: ignore
out = cv2.VideoWriter('output_video_1.mp4', codec, fps, (width, height), isColor=False)
while True:
    ret, frame = cap.read()
    if not ret:
        break
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    out.write(frame)
    cv2.imshow('Video', frame)
    if cv2.waitKey(1) == ord('q'):
        break;
    # Check if window is closed
    if cv2.getWindowProperty('Video', cv2.WND_PROP_VISIBLE) < 1:
        break
cap.release()
out.release()
cv2.destroyAllWindows()