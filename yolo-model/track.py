import cv2
from ultralytics import YOLO

from send_data import send_data


def track():
    # Load the YOLOv8 model
    model = YOLO("runs/detect/yolov8n_v8_50e18/weights/best.pt")

    # cap = cv2.VideoCapture(0)
    cap = cv2.VideoCapture("inference_data/pothole_video.mp4")

    max_id = 0

    while cap.isOpened():
        success, frame = cap.read()

        if success:
            results = model.track(frame, persist=True)

            for id in results[0].boxes.id:
                if id > max_id:
                    # send_data
                    max_id = id

            annotated_frame = results[0].plot()

            cv2.imshow("YOLOv8 Tracking", annotated_frame)

            if cv2.waitKey(1) & 0xFF == ord("q"):
                break
        else:
            break

    cap.release()
    cv2.destroyAllWindows()
