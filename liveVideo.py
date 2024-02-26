import cv2
import os

cap = cv2.VideoCapture(0)

output_folder = r'C:\Users\Max\Desktop\CS CAP\LiveOutput'

frame_count = 0
start_time = 0

while True:
    ret, frame = cap.read()

    if not ret:
        print("Error: Can't receive frame (stream end?). Exiting...")
        break

    cv2.imshow('Live Video', frame)

    current_time = cap.get(cv2.CAP_PROP_POS_MSEC) / 500
    if current_time - start_time >= 1:
        output_path = os.path.join(output_folder, f'frame_{frame_count}.jpg')
        cv2.imwrite(output_path, frame)
        frame_count += 1
        start_time = current_time

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()