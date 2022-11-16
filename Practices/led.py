from flask import Flask, request, jsonify
import RPi.GPIO as GPIO

app = Flask(__name__)
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(18, GPIO.OUT)

@app.route('/', methods=['GET'])
def led():
    status = request.args.get('status')
    if status == 'on':
        GPIO.output(18, GPIO.HIGH)
        return jsonify({"message": "El led esta encendido!"})
    elif status == 'off':
        GPIO.output(18, GPIO.LOW)
        return jsonify({"message": "Ahora ya no"})
    else:
        return jsonify({"message": "No es correcto"})
