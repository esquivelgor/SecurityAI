import whisper # Speech2text modelo de OpenAI
import pyaudio # Grabar audio
import wave # Grabar audio
from gtts import gTTS # Text2speech
from time import sleep 
from playsound import playsound # Reproducir sonido
import sqlite3

model = whisper.load_model("base")

# -_-_-_-_-_-_-_-_-_-_-_-_ Speech to text method -_-_-_-_-_-_-_-_-_-_-_-_
def s2t():
    result = model.transcribe("output.wav", fp16=False, language='Spanish')    
    return(result["text"].lower())

# -_-_-_-_-_-_-_-_-_-_-_-_ Text to speech method -_-_-_-_-_-_-_-_-_-_-_-_
def t2s(msg):
    speech = gTTS(text = msg, lang = 'es')
    speech.save('computerAudio.mp3')
    playsound('computerAudio.mp3')

# -_-_-_-_-_-_-_-_-_-_-_-_ Method to get the audio -_-_-_-_-_-_-_-_-_-_-_-_
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

# -_-_-_-_-_-_-_-_-_-_-_-_ Get audio and apply s2t -_-_-_-_-_-_-_-_-_-_-_-_     
def recordAudio(time):
    getAudio(time)
    data = s2t()
    return data

# -_-_-_-_-_-_-_-_-_-_-_- Connection to the database -_-_-_-_-_-_-_-_-_-_-_
conn = sqlite3.connect("users.db")
crsr = conn.cursor()

# ------------ End connection to the database -------------------------------

# -_-_-_-_-_-_-_-_-_-_-_-  Main -_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-

print("Inicia proceso")

#t2s("Bienvenido al Tecnologico de Monterrey, es usted estudiante o colaborador?")
#data = recordAudio(3)
data = "estudiante"

cont = 1
while cont:    
    if ("estudiante") in data:
        t2s("Dígame su matrícula sin la primer letra") #01625621
        matAlu = recordAudio(5)
        matAlu = matAlu.strip('., ')
        print(f"Matricula:{matAlu}!")
        try:
            if(len(matAlu) == 8 or len(matAlu) == 9):
                matAlu = int(matAlu)
                querySQL = "SELECT `matricula` FROM `users`;"
                for row in crsr.execute(querySQL):
                    print(type(row))
                print(f"Texto = {matAlu}")
                print(f"Nombre = {nombre}")
                cont = 0
                print("Se pudo!")
            else:
                t2s("Hubo un pequeño error, por favor")    
        except:
            t2s("Hubo un pequeño error, por favor")
        
    elif ("colaborador") in data:
        t2s("Bienvenido, digame su matricula")
        matCol = recordAudio(7)
        cont = 0
    elif "ver" in data:
        querySQL = "SELECT `matricula` FROM `users`;"
        for row in crsr.execute(querySQL):
            print(row)
        print(crsr.execute(querySQL))
        t2s("Su query fue ejecutado correctamente!")
        cont = 0
    else:
        print(f"Data 2 = {data}")
        t2s("No se pudo entender su respuesta, por favor repita.")
        data = recordAudio(3) # Recibir audio

conn.close()
    
    
