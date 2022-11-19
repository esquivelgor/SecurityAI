import whisper # Speech2text modelo de OpenAI
import pyaudio # Grabar audio
import wave # Grabar audio
from gtts import gTTS # Text2speech
from time import sleep 
from playsound import playsound # Reproducir sonido
import sqlite3

model = whisper.load_model("base")

# Speech to text method
def s2t():
    result = model.transcribe("output.wav", fp16=False, language='Spanish')    
    return(result["text"])

# Text to speech method
def t2s(msg):
    speech = gTTS(text = msg, lang = 'es')
    speech.save('computerAudio.mp3')
    playsound('computerAudio.mp3')

# Method to get the audio
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
    obj.close()
    
def recordAudio(time):
    getAudio(time)
    data = s2t()
    return data

# -------------------------- Main --------------------------

#conn = sqlite3.connect("database.sql")
#crsr = conn.cursor()

print("Inicia proceso")
# Se presiona el boton

t2s("Aqui andamos chambeando profeeeeee")

#data = recordAudio(5) # Grabar audio


#if "hola" in data:
#    s2t("Holaaa")
## Hay que cambiar la .sql a .db
#if "datos" in data:
    #t2s("Mostrando los datos")
#sqlCommand = "CREATE DATABASE users"
#crsr.execute(sqlCommand)

#if ("si" or "hola") in data:
#
#    databaseConnection()
    #t2s("Por favor, mencione su matricula")
    #matricula = speech2text()
    #print(matricula)
#    t2s("Gracias, puede pasar mi chingon!")
#print(f"Texto = {data}")

conn.close()
    
    
