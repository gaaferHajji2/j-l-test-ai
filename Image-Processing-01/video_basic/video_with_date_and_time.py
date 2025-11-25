# this is important if we have translate for video and we want to display the content of translate 
# for the video
import cv2
import datetime

# here if we set 0, then the camera will opened, then we can use an speech-to-text packages 
# to save the frames with texts for video
cap = cv2.VideoCapture('video.mp4')
# Get the width and height of video
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
# define the codec of output video
codec = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter('output_video_1.mp4', codec, 30, (width, height))

while cap.isOpened():
    # get the current frame
    ret, frame = cap.read()
    if not ret:
        break;
    now = datetime.datetime.now()
    date_time = now.strftime("%d-%m-%Y %H:%M:%S")
    font = cv2.FONT_HERSHEY_SIMPLEX
    cv2.putText(frame, date_time, (1, 50), font, 0.3, (0, 255, 255), 1, cv2.LINE_AA)
    # write the result
    out.write(frame)
    # display the result
    cv2.imshow('frame', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
out.release()
cv2.destroyAllWindows()