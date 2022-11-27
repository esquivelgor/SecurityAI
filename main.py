import RPi.GPIO as GPIO # Puertos raspberry 
#from picamera import PiCamera
import methodsIOT as iot
#import sqlite3
#from datetime import datetime
#import mysql.connector

# -_-_-_-_-_-_-_-_-_-_-_- General Configuration -_-_-_-_-_-_-_-_-_-_-_-

# --- Sensors ---
GPIO.setmode(GPIO.BCM) # Nomenclatura NO fisica
GPIO.setwarnings(False)
GPIO.setup(16, GPIO.OUT) # Led blanco
GPIO.setup(26, GPIO.OUT) # Led Rojo
GPIO.setup(15, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # Boton

# --- Variables ---
n = 2 # Leds time 
data = "estudiante" # 1st choice
matAlu = "01625621" # 2nd choice

## -_-_-_-_-_-_-_-_-_-_-_- Connection to the database -_-_-_-_-_-_-_-_-_-_-_
#
#db = mysql.connector.connect(
#  host="localhost",
#  user="root",
#  password="",
#  database="login"
#)
#crsr = db.cursor() 
#
#print(db) 
## -_-_-_-_-_-_-_-_-_-_-_-  Main -_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-

while True:
    if GPIO.input(15) == GPIO.HIGH:
        print("Inicia proceso")
    #    iot.t2s("Bienvenido al Tecnologico de Monterrey, ¿es usted estudiante o colaborador?")
    #    #data = iot.recordAudio(3)

        i = True
        while i == True:
            # -_-_-_-_-_-_-_-_-_-_-_-  Casos posibles, estudiante/colaborador/externo  -_-_-_-_-_-_-_-_-_-_-_-      
            if ("estudiante") in data:
    #            #iot.t2s("Dígame su matrícula sin la primer letra") #01 625 621
                print("Digame matricula...")
    #            #matAlu = iot.recordAudio(5)
    #            #matAlu = matAlu.replace(' ', '').replace(',','').replace('.','').replace('-','') # Limpieza de la data
                try:
                    if(len(matAlu) == 8):
    #                    matAlu = "A" + matAlu
    #                    query = "SELECT `ID_Usuario` FROM `usuarios`;"
    #                    
    #                    # -_-_-_-_-_-_-_-_-_-_-_-  Obtenemos las matriculas en la database -_-_-_-_-_-_-_-_-_-_-_-
    #                    crsr.execute(query)
    #                    matriculas = crsr.fetchall()
    #                    # matriculas.append(str(row).replace(',','').replace("'",'').replace('(','').replace(')',''))
    #
    #                    # -_-_-_-_-_-_-_-_-_-_-_-  Buscamos si alguna coincide -_-_-_-_-_-_-_-_-_-_-_-
    #                    for i in range(len(matriculas)):
    #                        if str(matriculas[i]) == matAlu:
    #                            #iot.t2s("Muchas gracias, que tenga buen dia!")
    #                            print(f"Texto 1 = {matAlu}")
                        i = False

                                # -_-_-_-_-_-_-_-_-_-_- Damos acceso -_-_-_-_-_-_-_-_-_-_-                                    
                                #iot.t2s(f"Acceso aprovado, se mantendra abierto por {n}")
                        iot.ledOn(16, n)
                                # -_-_-_-_-_-_-_-_-_- Foto de seguridad -_-_-_-_-_-_-_-_-_-_- 
                                #date = datetime.datetime.now().strftime('%m-%d-%Y_%H.%M.%S')
                                #capture_img = '/home/esquivelg/Documents/pictures/' + date + '.jpg'
                                #capture_photo(capture_img, date)
                                
                                # -_-_-_-_-_-_-_-_-_-  Registro de acceso -_-_-_-_-_-_-_-_-_-_- 
    #                            querySQL = "INSERT INTO `access` (`id_Access`, `time`, `matricula_id`) values ('','"+ date_time +"','"+ matAlu +"');"
    #                            querySQL = "INSERT INTO `access` (`id_Access`, `time`, `matricula_id`) values ('1','holaa','A01625621');"
    #                            crsr.execute(querySQL)
                        print("Proceso estudiante finalizado")
                        if (i == True):
                            #iot.t2s("Matricula inválida")
                            print(f"Proceso finalizado alumno = {matAlu}")
                            # Procede a no dar el paso, encender 2do led
                            iot.ledOn(26, n)
                            i = False
                    else:
    #                    iot.t2s("Hubo un error, por favor")    
                        print(f"Error en 3er if = {matAlu}")
                        iot.ledOn(26, n)
                except:
    #                iot.t2s("Hubo un error, por favor")
                    print(f"Error en tryCatch = {matAlu}")
                    iot.ledOn(26, n)
            elif ("colaborador") in data:
                print("Camino colaborador")
            elif ("externo") in data:
    #            iot.t2s("Una disculpa, no es posible que usted ingrese por este lugar, favor de retornar y entrar por la entrada principal.")
                i = False
                iot.ledOn(26, n)
            else:
    #            iot.t2s("No se pudo entender su respuesta, por favor repita.")
    #            data = iot.recordAudio(3) # Recibir audio
                print(f"Error en 2do if = {matAlu}")
                iot.ledOn(26, n)