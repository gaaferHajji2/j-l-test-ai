import cv2

cap = cv2.VideoCapture('video.mp4')

# Check if video opened successfully
if not cap.isOpened():
    print("Error: Could not open video.")
    exit()

# Get video properties
fps = cap.get(cv2.CAP_PROP_FPS)
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

print(f"FPS: {fps}, Resolution: {width}x{height}, Total Frames: {frame_count}")

codec = cv2.VideoWriter_fourcc(*'mp4v') # type: ignore
out = cv2.VideoWriter('output_video.mp4', codec, fps, (width, height))
while True:
    ret, frame = cap.read()
    if not ret:
        break
    out.write(frame)
    cv2.imshow('Video', frame)
    if cv2.waitKey(1) == ord('q'):
        break;
cap.release()
out.release()
cv2.destroyAllWindows()