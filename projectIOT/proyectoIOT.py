#import Rpi.GPIO as GPIO # Puertos raspberry
#import board # Creo que no sirve pa' nada
#from flask import Flask, request, jsonify # Web framework 
#from picamera import PiCamera
# from time import sleep
import methodsIOT as iot
import sqlite3
from datetime import datetime

# General Configuration
#GPIO.setwarnings(False)

# -_-_-_-_-_-_-_-_-_-_-_- Connection to the database -_-_-_-_-_-_-_-_-_-_-_
conn = sqlite3.connect("users.db")
crsr = conn.cursor()

# -_-_-_-_-_-_-_-_-_-_-_-  Main -_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-

#if GPIO.input(10) == GPIO.HIGH:
print("Inicia proceso")

iot.t2s("Bienvenido al Tecnologico de Monterrey, ¿es usted estudiante o colaborador?")
data = iot.recordAudio(3)
#data = "estudiante"

i = True
while i == True:
    # -_-_-_-_-_-_-_-_-_-_-_-  Casos posibles, estudiante/colaborador/externo  -_-_-_-_-_-_-_-_-_-_-_-      
    if ("estudiante") in data:
        iot.t2s("Dígame su matrícula sin la primer letra") #01 625 621
        #matAlu = iot.recordAudio(5)
        #matAlu = matAlu.replace(' ', '').replace(',','').replace('.','').replace('-','') # Limpieza de la data
        try:
            matAlu = "01625621" # test
            if(len(matAlu) == 8):
                matAlu = "A" + matAlu
                querySQL = "SELECT `matricula_id` FROM `users`;"
                matriculas = []
                # -_-_-_-_-_-_-_-_-_-_-_-  Obtenemos las matriculas en la database -_-_-_-_-_-_-_-_-_-_-_-
                for i, row in enumerate(crsr.execute(querySQL)):
                    matriculas.append(str(row).replace(',','').replace("'",'').replace('(','').replace(')',''))

                # -_-_-_-_-_-_-_-_-_-_-_-  Buscamos si alguna coincide -_-_-_-_-_-_-_-_-_-_-_-
                for i in range(len(matriculas)):
                    if str(matriculas[i]) == matAlu:
                        #iot.t2s("Muchas gracias, que tenga buen dia!")
                        print(f"Texto 1 = {matAlu}")
                        i = False
                        #iot.t2s("Se supone que ya deben abrir las puertas en este punto, Viva Mexico siiiuuuuuuuu")
                        
                        # -_-_-_-_-_-_-_-_-_-_-  Insertamos la hora de acceso
                        date_time = datetime.now().strftime("%m/%d/%Y_%H:%M")

                        #querySQL = "INSERT INTO `access` (`id_Access`, `time`, `matricula_id`) values ('','"+ date_time +"','"+ matAlu +"');"
                        querySQL = "INSERT INTO `access` (`id_Access`, `time`, `matricula_id`) values ('1','holaa','A01625621');"
                        crsr.execute(querySQL)
                        print("yeap")
                        # Procede a abrir las puertas, encendemos led
                if (i == 1):
                    iot.t2s("Matricula inválida")
                    print(f"Texto = {matAlu}")
                    i = False
                    # Procede a no dar el paso, encender 2do led
            else:
                iot.t2s("Hubo un error, por favor")    
                print(f"Texto 1= {matAlu}")
        except:
            iot.t2s("Hubo un error, por favor")
            print(f"Texto 2= {matAlu}")
    elif ("colaborador") in data:
        iot.t2s("Dígame su nomina sin la primer letra") #01 625 621
        matCol = iot.recordAudio(5)
        matCol = matCol.replace(' ', '').replace(',','').replace('.','').replace('-','') # Limpieza de la data
        try:
            #matCol = "01625621" # test
            if(len(matCol) == 8):
                matCol = "L" + matCol
                querySQL = "SELECT `matricula` FROM `users`;"
                matriculas = []
                # -_-_-_-_-_-_-_-_-_-_-_-  Obtenemos las matriculas en la database -_-_-_-_-_-_-_-_-_-_-_-
                for i, row in enumerate(crsr.execute(querySQL)):
                    matriculas.append(str(row).replace(',','').replace("'",'').replace('(','').replace(')',''))

                # -_-_-_-_-_-_-_-_-_-_-_-  Buscamos si alguna coincide -_-_-_-_-_-_-_-_-_-_-_-
                for i in range(len(matriculas)):
                    if str(matriculas[i]) == matCol:
                        iot.t2s("Muchas gracias, que tenga buen dia!")
                        print(f"Texto 1 = {matCol}")
                        i = False
                        # Procede a abrir las puertas
                if (i == 1):
                    iot.t2s("Nomina inválida")
                    print(f"Texto = {matCol}")
                    i = False
                    # Procede a no dar el paso
            else:
                iot.t2s("Hubo un error, por favor")    
                print(f"Texto 1= {matCol}")
        except:
            iot.t2s("Hubo un error, por favor")
            print(f"Texto 2= {matCol}")
    elif () in data:
        iot.t2s("Una disculpa, no es posible que usted ingrese por este lugar, favor de retornar y entrar por la entrada principal.")
        i = False
    else:
        iot.t2s("No se pudo entender su respuesta, por favor repita.")
        data = iot.recordAudio(3) # Recibir audio
conn.close() # Cerramos conexion con la database
    
    
