import cv2
import time

from detector import model, important_objects
from navigation import get_position, estimate_distance
from audio_alert import speak

cap = cv2.VideoCapture(0)

last_alert_time = 0

while True:

    start_time = time.time()

    ret, frame = cap.read()

    if not ret:
        break

    frame_width = frame.shape[1]
    frame_height = frame.shape[0]

    results = model(frame, conf=0.5)

    largest_area = 0
    closest_object = None

    for box in results[0].boxes:

        cls = int(box.cls[0])
        name = model.names[cls]

        if name not in important_objects:
            continue

        x1, y1, x2, y2 = box.xyxy[0]

        center_x = (x1 + x2) / 2

        position = get_position(center_x, frame_width)

        width = x2 - x1
        height = y2 - y1

        area = width * height

        distance = estimate_distance(area)

        if area > largest_area:

            largest_area = area

            closest_object = {
                "name": name,
                "position": position,
                "distance": distance,
                "center_x": center_x
            }

        cv2.rectangle(
            frame,
            (int(x1), int(y1)),
            (int(x2), int(y2)),
            (0, 255, 0),
            2
        )

        cv2.putText(
            frame,
            f"{name} | {distance} | {position}",
            (int(x1), int(y1) - 10),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.6,
            (0, 255, 0),
            2
        )

    current_time = time.time()

    if (
        closest_object is not None
        and current_time - last_alert_time > 3
    ):

        name = closest_object["name"]
        position = closest_object["position"]
        distance = closest_object["distance"]
        center_x = closest_object["center_x"]

        if distance == "very close":

            if position == "center":

                if center_x < frame_width / 2:
                    speak(f"{name} ahead. Move right")

                else:
                    speak(f"{name} ahead. Move left")

            elif position == "left":

                speak(f"Caution. {name} on your left")

            else:

                speak(f"Caution. {name} on your right")

            last_alert_time = current_time

        elif distance == "close":

            speak(f"{name} nearby")

            last_alert_time = current_time

    # Danger Zone
    cv2.rectangle(
        frame,
        (frame_width // 3, 0),
        (2 * frame_width // 3, frame_height),
        (0, 0, 255),
        2
    )

    cv2.putText(
        frame,
        "DANGER ZONE",
        (frame_width // 3 + 20, 40),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.8,
        (0, 0, 255),
        2
    )

    fps = 1 / (time.time() - start_time)

    cv2.putText(
        frame,
        f"FPS: {fps:.2f}",
        (20, 40),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.8,
        (255, 0, 0),
        2
    )

    cv2.imshow("AI Assistive Navigation System", frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()