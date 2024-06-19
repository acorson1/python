import cv2
import numpy as np

def run_application():
    try:
        face_save()
    except ImportError as e:
        print(f"Error importing module: {e}")
    except Exception as e:
        print(f"Error executing function: {e}")
        
def face_save():
    faces, img = detect_faces_and_display()
    if faces is not None:
        count = 0
        for (x,y,w,h) in face_save:
            face = img[y:y+h, x:x+w] #slice the face from image        
            # saves as image file
            cv2.imwrite(str(count)+'.jpg', face)
            count+=1
            
    
if __name__ == "__main__":
    run_application()
    
def detect_faces_and_display():
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    cap = cv2.VideoCapture(0)

    while True:
        ret, img = cap.read()
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

        for (x, y, w, h) in faces:
            cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)

        cv2.imshow('Face Detection', img)

        if len(faces) > 0:
            cv2.destroyWindow('Face Detection')
            cv2.imshow('Face Detected', img)
            cv2.waitKey(10000)  # Wait for 10 seconds
            break

        if cv2.waitKey(1) & 0xFF == ord(' '):
            cv2.imshow('Face Detected', img)
            cv2.waitKey(10000)  # Wait for 10 seconds
            break

    cap.release()
    cv2.destroyAllWindows()
    return faces,img