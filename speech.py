import speech_recognition as sr
from gtts import gTTS
from time import sleep
from playsound import playsound

def speech2text():
    r = sr.Recognizer()
    speech = sr.Microphone(device_index=1)
    with speech as source:
        print("Escuchando...")
        audio = r.adjust_for_ambient_noise(source)
        audio = r.listen(source)
    try:
        recog = r.recognize_google(audio, language = 'es-MX')
        return recog

    except sr.UnknownValueError:
        text2speech("Perdon, no se pudo entender tu audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))

def text2speech(msg):
    speech = gTTS(text = msg, lang = 'es')
    speech.save('DataFlair.mp3')
    playsound('DataFlair.mp3')

while True:
    text2speech("Bienvenido usuario promedio, usted ya se encuentra registrado?")
    text = speech2text()
    if "si" in text:
        text2speech("Por favor, mencione su matricula")
        matricula = speech2text()
        print(matricula)
        text2speech("Gracias, puede pasar mi chingon!")
    print(text)
    
    
    
