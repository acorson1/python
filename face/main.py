import datetime
import facial_rec
import test
import cv2

def run_application():
    try:
        face_save()
    except ImportError as e:
        print(f"Error importing module: {e}")
    except Exception as e:
        print(f"Error executing function: {e}")
        
def face_save():
    faces = facial_rec.detect_faces_and_display()
    if faces is not None:
        recognized_cascade = faces
        
        # saves as image file
        cv2.imwrite('/face/recog_faces/cascade_{}.png'.format(datetime.datetime.now().strftime('%d%H%M%S')), recognized_cascade)
        return recognized_cascade

if __name__ == "__main__":
    run_application()