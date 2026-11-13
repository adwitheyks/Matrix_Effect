import cv2
import numpy as np
import random

cap = cv2.VideoCapture(0)

WIDTH, HEIGHT = 800, 600
CELL = 10

cap.set(cv2.CAP_PROP_FRAME_WIDTH, WIDTH)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, HEIGHT)

chars = "01ABCDEFGHIJKLMNOPQRSTUVWXYZ"
drops = [random.randint(-50,0)
        for _ in range(WIDTH // CELL)]

while True:
    ret , frames = cap.read()
    if not ret:
        break

    frame = cv2.flip(frames, 1)
    frame = cv2.resize(frame, (WIDTH,HEIGHT))

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    canvas = np.zeros_like(frame)

    for col in range(len(drops)):
        x = col * CELL

        for row in range(HEIGHT // CELL):
            y = row * CELL

            brightness = gray[y, x]

            if brightness >  50:
                char = random.choice(chars)
                green = int(brightness)

                cv2.putText(
                    canvas, char, (x,y),
                    cv2.FONT_HERSHEY_PLAIN,
                    0.8, (0, green, 0), 1)


        y = drops[col] * CELL

        cv2.putText(
            canvas, random.choice(chars),
            (x,y), 
            cv2.FONT_HERSHEY_PLAIN,
            1, (180, 255, 180), 1
        )

        drops[col] += 1

        if y > HEIGHT:
            drops[col] = random.randint(-20,0)



    cv2.imshow("MATRIX FILTER", canvas)

    if cv2.waitKey(30) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()

