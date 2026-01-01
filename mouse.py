import cv2
import mediapipe as mp
import pyautogui
import math

# Initialize camera
cap = cv2.VideoCapture(0)

# Screen size
screen_w, screen_h = pyautogui.size()

# MediaPipe setup
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(
    static_image_mode=False,
    max_num_hands=1,
    min_detection_confidence=0.7,
    min_tracking_confidence=0.7
)
mp_draw = mp.solutions.drawing_utils

# Smoothening
prev_x, prev_y = 0, 0
smoothening = 7

print("✅ Virtual Mouse Started...")

while True:
    success, frame = cap.read()
    if not success:
        break

    frame = cv2.flip(frame, 1)
    h, w, _ = frame.shape

    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    result = hands.process(rgb)

    if result.multi_hand_landmarks:
        for hand_landmarks in result.multi_hand_landmarks:
            mp_draw.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

            # Index finger tip
            index_finger = hand_landmarks.landmark[8]
            thumb = hand_landmarks.landmark[4]

            x = int(index_finger.x * w)
            y = int(index_finger.y * h)

            # Convert to screen size
            screen_x = int(index_finger.x * screen_w)
            screen_y = int(index_finger.y * screen_h)

            # Smooth movement
            curr_x = prev_x + (screen_x - prev_x) / smoothening
            curr_y = prev_y + (screen_y - prev_y) / smoothening

            pyautogui.moveTo(curr_x, curr_y)
            prev_x, prev_y = curr_x, curr_y

            # Distance between thumb & index (click)
            tx, ty = int(thumb.x * w), int(thumb.y * h)
            distance = math.hypot(x - tx, y - ty)

            if distance < 30:
                pyautogui.click()
                cv2.circle(frame, (x, y), 15, (0, 255, 0), cv2.FILLED)

    cv2.imshow("Karan Virtual Mouse", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
