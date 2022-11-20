import whisper # Speech2text model from OpenAI
import pyaudio # Record audio
import wave # Record audio
from gtts import gTTS # Text2speech
from playsound import playsound # Run sound


# General configuration
model = whisper.load_model("base")

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

# -_-_-_-_-_-_-_-_-_-_-_-_ Speech to text method -_-_-_-_-_-_-_-_-_-_-_-_
def s2t():
    result = model.transcribe("output.wav", fp16=False, language='Spanish')    
    return(result["text"].lower())

# -_-_-_-_-_-_-_-_-_-_-_-_ Text to speech method -_-_-_-_-_-_-_-_-_-_-_-_
def t2s(msg):
    speech = gTTS(text = msg, lang = 'es')
    speech.save('computerAudio.mp3')
    playsound('computerAudio.mp3')

# -_-_-_-_-_-_-_-_-_-_-_-_ Get audio and apply s2t -_-_-_-_-_-_-_-_-_-_-_-_     
def recordAudio(time):
    getAudio(time)
    data = s2t()
    return data