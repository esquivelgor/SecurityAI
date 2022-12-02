import RPi.GPIO as GPIO
import pygame 
import pyaudio
import wave
import speech_recognition as sr
import cv2
import recognitionMethods as fr
from simple_facerec import SimpleFacerec
from time import sleep
from gtts import gTTS
from picamera import PiCamera

# -_-_-_-_-_-_-_-_-_-_-_-_ Text to speech method -_-_-_-_-_-_-_-_-_-_-_-_
def t2s(msg):
    speech = gTTS(text = msg, lang = 'es')
    speech.save('computerAudio.mp3')
    pygame.mixer.init()
    pygame.mixer.music.load("computerAudio.mp3")
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy() == True:
        continue

# -_-_-_-_-_-_-_-_-_-_-_-_ Take picture -_-_-_-_-_-_-_-_-_-_-_-_
def capture_photo(file_capture):
    camera = PiCamera()
    camera.resolution = (640, 480)
    camera.framerate = 15
    sleep(2)
    camera.capture(file_capture)
    print("\r\nImage Captured! \r\n")
    camera.close()

# -_-_-_-_-_-_-_-_-_-_-_-_ Leds  -_-_-_-_-_-_-_-_-_-_-_-_
def ledOn(pin, time):
    GPIO.output(pin, GPIO.HIGH)
    sleep(time)
    GPIO.output(pin, GPIO.LOW)

# -_-_-_-_-_-_-_-_-_-_-_-_ Img2Binary -_-_-_-_-_-_-_-_-_-_-_-_
def convertToBinaryData(filename):
    with open(filename, 'rb') as file:
        binaryData = file.read()
    return binaryData

# -_-_-_-_-_-_-_-_-_-_-_-_ GetAudio -_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-
def getAudio(time):
    FRAME_PER_BUFFER = 3200
    FORMAT = pyaudio.paInt16 
    CHANNELS = 1 # Monoformat
    RATE = 16000
    
    p = pyaudio.PyAudio()
    
    stream = p.open(
        format = FORMAT,
        channels = CHANNELS,
        rate = RATE,
        input = True,
        frames_per_buffer = FRAME_PER_BUFFER
    )
    
    print(f"Grabando por {time} segundos")
    
    sec = time
    frames = []
    for i in range(0, int(RATE/FRAME_PER_BUFFER*sec)):
        data = stream.read(FRAME_PER_BUFFER)
        frames.append(data)
    
    stream.close()
    p.terminate()
    
    obj =  wave.open("output.wav","wb")
    obj.setnchannels(CHANNELS)
    obj.setsampwidth(p.get_sample_size(FORMAT))
    obj.setframerate(RATE)
    obj.writeframes(b"".join(frames))
    # obj.close()

# -_-_-_-_-_-_-_-_-_-_-_-_ s2t -_-_-_-_-_-_-_-_-_-_-_-_

def s2t(time):
    getAudio(time)
    r = sr.Recognizer()
    voice = sr.AudioFile('output.wav')
    with voice as source:
        audio = r.record(source)
    try:
        print("Reconociendo audio...")
        a = r.recognize_google(audio, language='es-ES')
        print(f"Data: {a}")
        return a # Texto reconocido
    except Exception as e:
        print(e)

    print("Reconocimiento terminado")


