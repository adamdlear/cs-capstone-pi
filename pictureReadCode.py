import cv2
import os

video_path       = r'C:\Users\Max\Desktop\CS CAP\Video Input\vid.mp4'                 # Edit this for video location (iPhone .MOV format)
output_folder    = r'C:\Users\Max\Desktop\CS CAP\Pictures output'                     # Edit this for foler location

video_capture = cv2.VideoCapture(video_path)

frame_count = 0
start_time = 0

while True:
    ret, frame = video_capture.read()

    if not ret:
        break  

    frame_count = frame_count + 1

    current_time = video_capture.get(cv2.CAP_PROP_POS_MSEC) / 500                   # Change this for speed -> 1000 is every second. 
                                                                                    # 2000 is every two seconds, 5000 is every 1/2 secont
    if current_time - start_time >= 1:                                              # etc. 
        output_path = os.path.join(output_folder, f'frame_{frame_count - 1 }.jpg')
        cv2.imwrite(output_path, frame)
        
        start_time = current_time

video_capture.release()
cv2.destroyAllWindows()





