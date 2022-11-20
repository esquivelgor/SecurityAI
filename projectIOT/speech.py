#import Rpi.GPIO as GPIO # Puertos raspberry
#import board # Creo que no sirve pa' nada
#from flask import Flask, request, jsonify # Web framework 
#from picamera import PiCamera
# from time import sleep
import methodsIOT as iot
import sqlite3

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

i = 1
while i:
    # -_-_-_-_-_-_-_-_-_-_-_-  Casos posibles, estudiante/colaborador/externo  -_-_-_-_-_-_-_-_-_-_-_-      
    if ("estudiante") in data:
        iot.t2s("Dígame su matrícula sin la primer letra") #01 625 621
        matAlu = iot.recordAudio(5)
        matAlu = matAlu.replace(' ', '').replace(',','').replace('.','').replace('-','') # Limpieza de la data
        try:
            #matAlu = "01625621" # test
            if(len(matAlu) == 8):
                matAlu = "A" + matAlu
                querySQL = "SELECT `matricula` FROM `users`;"
                matriculas = []
                # -_-_-_-_-_-_-_-_-_-_-_-  Obtenemos las matriculas en la database -_-_-_-_-_-_-_-_-_-_-_-
                for i, row in enumerate(crsr.execute(querySQL)):
                    matriculas.append(str(row).replace(',','').replace("'",'').replace('(','').replace(')',''))

                # -_-_-_-_-_-_-_-_-_-_-_-  Buscamos si alguna coincide -_-_-_-_-_-_-_-_-_-_-_-
                for i in range(len(matriculas)):
                    if str(matriculas[i]) == matAlu:
                        iot.t2s("Muchas gracias, que tenga buen dia!")
                        print(f"Texto 1 = {matAlu}")
                        i = 0
                        # Aqui se me buggeaaa, se vuelve a repetir el loop, pero ps ya al rato veo
                        # Procede a abrir las puertas
                if (i == 1):
                    iot.t2s("Matricula inválida")
                    print(f"Texto = {matAlu}")
                    i = 0
                    # Procede a no dar el paso
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
                        i = 0
                        # Aqui se me buggeaaa, se vuelve a repetir el loop, pero ps ya al rato veo
                        # Procede a abrir las puertas
                if (i == 1):
                    iot.t2s("Nomina inválida")
                    print(f"Texto = {matCol}")
                    i = 0
                    # Procede a no dar el paso
            else:
                iot.t2s("Hubo un error, por favor")    
                print(f"Texto 1= {matCol}")
        except:
            iot.t2s("Hubo un error, por favor")
            print(f"Texto 2= {matCol}")
    elif "ver" in data:
        querySQL = "SELECT `matricula` FROM `users`;"
        for row in crsr.execute(querySQL):
            print(row)
        print(crsr.execute(querySQL))
        iot.t2s("Su query fue ejecutado correctamente!")
        i = 0
    else:
        print(f"Data 2 = {data}")
        iot.t2s("No se pudo entender su respuesta, por favor repita.")
        data = iot.recordAudio(3) # Recibir audio

conn.close() # Cerramos conexion con la database
    
    
