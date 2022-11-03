import RPi.GPIO as GPIO
import board
import adafruit_dht
import pyrebase
from flask import Flask, request, jsonify
from picamera import PiCamera
from time import sleep
from datetime import datetime

# Firebase configuration
config = {
    "apiKey": "AIzaSyC-k_ai6-O3NnoDllGpi9xqC9iUG2GJZiM",
    "authDomain": "fir-project-2439f.firebaseapp.com",
    "databaseURL": "https://fir-project-2439f-default-rtdb.firebaseio.com",
    "projectId": "fir-project-2439f",
    "storageBucket": "fir-project-2439f.appspot.com",
    "messagingSenderId": "99887903842",
    "appId": "1:99887903842:web:1e9011acaed708a26b8d3b",
    "measurementId": "G-FX1P0KFBV3"
}

firebase = pyrebase.initialize_app(config)
db = firebase.database()

#storage = firebase.storage()
#camera = PiCamera()

app = Flask(__name__)

# GPIO configuration
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(18, GPIO.OUT) # Led

# Dht11 configuration
dhtDevice = adafruit_dht.DHT11(board.D17)  

# Application
@app.route('/', methods=['GET'])
def led():
    status = request.args.get('status')
    if status == 'led_on':
        GPIO.output(18, GPIO.HIGH)
        return jsonify({"message": "El led esta encendido!"})
    elif status == 'led_off':
        GPIO.output(18, GPIO.LOW)
        return jsonify({"message": "Ahora ya no"})
    elif status == 'dht11':
        while True:
            try:
                temperature_c = dhtDevice.temperature
                humidity = dhtDevice.humidity
                data = {
                    "temperature_c":temperature_c,
                    "humidity":humidity
                }
                db.child("dht11").child("1-set").set(data)
                db.child("dht11").child("2-push").push(data)
                return jsonify({
                    "message": "Dht11 info enviada a db\nTemperatura: {:.1f} C    Humedad: {}%".format(temperature_c, humidity)
                    })
            except RuntimeError as error:
                return jsonify({"message": error.args[0]})
                dhtDevice.exit()
            time.sleep(2.0)
    elif status == 'photoresistor':
        pin = 4
        GPIO.setup(pin, GPIO.OUT)
        GPIO.output(pin, GPIO.LOW)

        GPIO.setup(pin, GPIO.IN)

        if(GPIO.input(pin) == GPIO.LOW):
            return jsonify({"message": "No hay luz!"})
        else:
            return jsonify({"message": "Hay luz!"})
    #elif status == 'picamera':
    #    try:
    #        while True:
    #            now = datetime.now()
    #            dt = now.strftime("%d%m%Y%H:%M:%S")
    #            name = dt+".jpg"
    #            camera.capture(name)
    #            return jsonify({"message": "Se guardo la imagen!"})
    #            storage.child(name).put(name)
    #            return jsonify({"message": "Se envio la imagen!"})
    #            os.remove(name)
    #            sleep(10)
    #    except:
    #        camera.close()
    else:
        return jsonify({"message": "No es correcto"})
