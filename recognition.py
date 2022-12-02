import cv2
import face_recognition as fr
from recognitionMethods import SimpleFacerec

def faceRecognition():
    # General configuration 
    sfr = SimpleFacerec()
    sfr.load_encoding_images("images/")
    cap = cv2.VideoCapture(0)

    while True:
        ret, frame = cap.read()

        faceLocations, faceNames = sfr.detect_known_faces(frame)
        try:
            if faceNames == []:
                print("No hay usuarios")
                continue    
            elif faceNames == ['Unknown']:
                print("No te conozcoo")
                break
            else:
                print(faceNames)
                break
        except Exception():
            print("Hay errores gallo")
            continue

    cap.release()
    cv2.destroyAllWindows() 

faceRecognition()