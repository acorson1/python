import cv2

def detect_faces_and_display():
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    cap = cv2.VideoCapture(0)

    while True:
        ret, frame = cap.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

        cv2.imshow('Face Detection', frame)

        if len(faces) > 0:
            cv2.destroyWindow('Face Detection')
            cv2.imshow('Face Detected', frame)
            cv2.waitKey(10000)  # Wait for 10 seconds
            break

        if cv2.waitKey(1) & 0xFF == ord(' '):
            cv2.imshow('Face Detected', frame)
            cv2.waitKey(10000)  # Wait for 10 seconds
            break

    cap.release()
    cv2.destroyAllWindows()
    return faces
