from flask import Flask, request, jsonify
import RPi.GPIO as GPIO
import time
import board
import adafruit_dht


app = Flask(__name__)

# Conexion led
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(18, GPIO.OUT)

# Conexion dht11
dhtDevice = adafruit_dht.DHT11(board.D17)  

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
                return jsonify({"message": "Temperatura: {:.1f} C    Humedad: {}% ".format(temperature_c, humidity)})
            except RuntimeError as error:
                return jsonify({"message": error.args[0]})
                time.sleep(2.0)
                continue
            except Exception as error:
                dhtDevice.exit()
                raise error
            time.sleep(2.0)
    else:
        return jsonify({"message": "No es correcto"})
