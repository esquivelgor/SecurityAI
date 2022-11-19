import RPi.GPIO as GPIO
import board
from flask import Flask, request, jsonify
from picamera import PiCamera
from time import sleep

app = Flask(__name__)

# GPIO configuration
GPIO.setwarnings(False)

# Funcion main de la programacion de la raspberry 
def main(channel):
    print("Proceso inicializado")
    if GPIO.input(10) == GPIO.HIGH:
        print("Procesos iniciados correctamente")
        # 
        if status == 'entrada':
            GPIO.setmode(GPIO.BCM)
            GPIO.setup(18, GPIO.OUT) # Led
            GPIO.output(18, GPIO.HIGH) # Suposicion de que las puertas se abren
            time.sleep(10) # Esperamos al que vehiculo entre
            GPIO.output(18, GPIO.LOW) # Suposicion de que las puertas se cierran
            return jsonify({"message": "Acceso aprovado"})
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

# Inicializamos procesos
while True:
    # Si el boton es presionado comenzamos a ejecutar el sistema
    # Button https://raspberrypihq.com/use-a-push-button-with-raspberry-pi-gpio/
    GPIO.setmode(GPIO.BOARD) # Use physical pin numbering
    GPIO.setup(10, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # Set pin 10 to be an input pin and set initial value to be pulled low (off)

    GPIO.add_event_detect(10,GPIO.RISING,callback=main) # Setup event on pin 10 rising edge

    message = input("Press enter to quit\n\n") # Run until someone presses enter
    time.sleep(1)
    GPIO.cleanup()
    
    

# Application
@app.route('/', methods=['GET'])
def raspberryWeb():
    status = request.args.get('status')
