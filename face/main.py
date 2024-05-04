import datetime
import facial_rec
import test
import cv2

def run_application():
    try:
        functions_to_execute = [test.option_select, facial_rec.detect_faces_and_display]
        for func in functions_to_execute:
            func()
    except ImportError as e:
        print(f"Error importing module: {e}")
    except Exception as e:
        print(f"Error executing function: {e}")
        
def face_save():
    haar_cascade = facial_rec.recognize_face()
    
    if haar_cascade is not None:
        recognized_cascade = haar_cascade
        
        # saves as image file
        cascade_image=cv2.imwrite('recognized_faces/cascade_{}.png'.format(datetime.datetime.now().strftime('%Y%m%d%H%M%S')), cascade_image)
        return recognized_cascade

if __name__ == "__main__":
    run_application()