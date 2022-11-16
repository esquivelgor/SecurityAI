import RPi.GPIO as GPIO
import datetime
from picamera import PiCamera
from time import sleep

# GPIO configuration
GPIO.setmode(GPIO.BCM) # Nomenclatura NO fisica
GPIO.setwarnings(False)
GPIO.setup(18, GPIO.OUT) # Led
GPIO.setup(15, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # 

camera = PiCamera()
camera.resolution = (640, 480)
camera.framerate = 15

def capture_photo(file_capture, text):
    camera.annotate_text = text
    sleep(2)
    camera.capture(file_capture)
    print("\r\nImage Captured! \r\n")
    

while True:
    if GPIO.input(15) == GPIO.HIGH:
        GPIO.output(18, GPIO.HIGH) # Suposicion de que las puertas se abren
        date = datetime.datetime.now().strftime('%m-%d-%Y_%H.%M.%S')
        capture_img = '/home/esquivelg/Documents/pictures/' + date + '.jpg'
        capture_photo(capture_img, date)
    else:
        GPIO.output(18, GPIO.LOW) # Suposicion de que las puertas se cierran
