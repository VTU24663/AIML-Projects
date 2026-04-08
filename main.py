import cv2
import mediapipe as mp
import numpy as np
import pytesseract
import time

# ✅ Tesseract path
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

# Setup
mp_hands = mp.solutions.hands
hands = mp_hands.Hands()

cap = cv2.VideoCapture(0)
cap.set(3, 1280)
cap.set(4, 720)

cv2.namedWindow("Air Writing", cv2.WINDOW_NORMAL)

canvas = None
prev_x, prev_y = 0, 0

# 👉 BLACK pen for OCR
draw_color = (0, 0, 0)

detected_text = ""

# OCR timing
last_ocr_time = 0
ocr_interval = 2

# Finger detection
def fingers_up(handLms):
    fingers = []
    fingers.append(1 if handLms.landmark[8].y < handLms.landmark[6].y else 0)
    fingers.append(1 if handLms.landmark[12].y < handLms.landmark[10].y else 0)
    return fingers

# ✅ IMPROVED OCR FUNCTION
def recognize_text(canvas):
    gray = cv2.cvtColor(canvas, cv2.COLOR_BGR2GRAY)

    # Increase contrast
    gray = cv2.convertScaleAbs(gray, alpha=2, beta=0)

    # Blur
    gray = cv2.GaussianBlur(gray, (5, 5), 0)

    # Threshold
    _, thresh = cv2.threshold(gray, 100, 255, cv2.THRESH_BINARY)

    # Invert (very important)
    thresh = cv2.bitwise_not(thresh)

    text = pytesseract.image_to_string(
        thresh,
        config='--psm 6 -c tessedit_char_whitelist=ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    )

    return text.strip()

while True:
    try:
        success, img = cap.read()
        if not success:
            continue

        img = cv2.flip(img, 1)

        # 👉 WHITE CANVAS (IMPORTANT)
        if canvas is None:
            canvas = np.ones_like(img) * 255

        rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        results = hands.process(rgb)

        # UI
        cv2.rectangle(img, (0, 0), (150, 80), (255, 0, 0), -1)
        cv2.rectangle(img, (150, 0), (300, 80), (0, 255, 0), -1)
        cv2.rectangle(img, (300, 0), (450, 80), (0, 0, 255), -1)
        cv2.rectangle(img, (450, 0), (600, 80), (0, 0, 0), -1)
        cv2.rectangle(img, (600, 0), (750, 80), (0, 255, 255), -1)
        cv2.putText(img, "CLEAR", (610, 50),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 0), 2)

        if results.multi_hand_landmarks:
            for handLms in results.multi_hand_landmarks:
                h, w, c = img.shape

                lm = handLms.landmark[8]
                cx, cy = int(lm.x * w), int(lm.y * h)

                fingers = fingers_up(handLms)

                # Selection
                if fingers == [1, 1]:
                    prev_x, prev_y = 0, 0

                    if cy < 80:
                        if cx < 150:
                            draw_color = (0, 0, 0)
                        elif cx < 750:
                            canvas = np.ones_like(img) * 255

                # Draw
                elif fingers == [1, 0]:
                    cv2.circle(img, (cx, cy), 10, draw_color, -1)

                    if prev_x == 0:
                        prev_x, prev_y = cx, cy

                    cv2.line(canvas, (prev_x, prev_y), (cx, cy), draw_color, 8)

                    prev_x, prev_y = cx, cy

        # 👉 AUTO OCR
        current_time = time.time()
        if current_time - last_ocr_time > ocr_interval:
            last_ocr_time = current_time
            try:
                detected_text = recognize_text(canvas)
            except:
                pass

        # Merge
        img = cv2.addWeighted(img, 0.5, canvas, 0.5, 0)

        # Show text
        cv2.putText(img, "Text: " + detected_text[:30], (50, 150),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

        cv2.imshow("Air Writing", img)

        key = cv2.waitKey(1) & 0xFF

        if key == 27:
            break

    except Exception as e:
        print("Error:", e)
        continue

cap.release()
cv2.destroyAllWindows()