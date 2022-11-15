import whisper # Speech2text modelo de OpenAI
import pyaudio # Grabar audio
import wave # Grabar audio
from gtts import gTTS # Text2speech
from time import sleep 
from playsound import playsound # Reproducir sonido
#from dataclasses import dataclass, asdic

model = whisper.load_model("base")

def s2tWhisper():
    result = model.transcribe("output.wav", fp16=False, language='Spanish')    
    return(result["text"])

def t2s(msg):
    speech = gTTS(text = msg, lang = 'es')
    speech.save('DataFlair.mp3')
    playsound('DataFlair.mp3')

def getAudio():
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
    
    print("Start recording")
    
    sec = 10
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
    obj.close()


#while True:
print("proceso")
#t2s("Bienvenido usuario promedio, usted ya se encuentra registrado?")
getAudio() # Grabar audio
text = s2tWhisper()
if "si" in text:
    print("Se reconoce perroo")
    #t2s("Por favor, mencione su matricula")
    #matricula = speech2text()
    #print(matricula)
    #t2("Gracias, puede pasar mi chingon!")
print(text)

    
    
