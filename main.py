import RPi.GPIO as GPIO # Puertos raspberry 
#from picamera import PiCamera
import methodsIOT as iot
#import sqlite3
#from datetime import datetime
import mysql.connector
from mysql.connector import errorcode

# -_-_-_-_-_-_-_-_-_-_-_- General Configuration -_-_-_-_-_-_-_-_-_-_-_-

# --- Sensors ---
GPIO.setmode(GPIO.BCM) # Nomenclatura NO fisica
GPIO.setwarnings(False)
GPIO.setup(16, GPIO.OUT) # Led blanco
GPIO.setup(26, GPIO.OUT) # Led Rojo
GPIO.setup(15, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # Boton

# --- Connection to the database ---

try:
    db = mysql.connector.connect(user='esquivelg', password='39932409', database='login')
except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("Something is wrong with your user name or password")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("Database does not exist")
    else:
        print(err)

crsr = db.cursor() 

# -_-_-_-_-_-_-_-_-_-_-_-  Main -_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-

while True:

    # --- Variables ---
    n = 2 # Leds time 
    data = "estudiante" # 1st choice
    matAlu = "01625621" # 2nd choice
    matriculas = []

    if GPIO.input(15) == GPIO.HIGH:
        print("Inicia proceso")
        print("Bienvenido al Tecnologico de Monterrey, ¿es usted estudiante o colaborador?")
    #    #data = iot.recordAudio(3)

        i = True
        while i == True:
            # -_-_-_-_-_-_-_-_-_-_-_-  Casos posibles, estudiante/colaborador/externo  -_-_-_-_-_-_-_-_-_-_-_-      
            if ("estudiante") in data:
                print("Dígame su matrícula sin la primer letra") # 01 62 56 21
    #            #matAlu = iot.recordAudio(5)
    #            #matAlu = matAlu.replace(' ', '').replace(',','').replace('.','').replace('-','') # Limpieza de la data
                try:
                    if(len(matAlu) == 8):
    #                    matAlu = "A" + matAlu
                        query = "SELECT `ID_Usuario` FROM `usuarios` WHERE `Tipo_Usuario` = 'Estudiante';"

                        # -_-_-_-_-_-_-_-_-_-_-_-  Get matriculas from database -_-_-_-_-_-_-_-_-_-_-_-
                        crsr.execute(query)
                        matriculasTup = list(crsr.fetchall())
                        # --- Change format ---
                        for i in matriculasTup:
                            matriculas.append(str(i))
                        # --- Clean data ---
                        for i, val in enumerate(matriculas):
                            matriculas[i] = "0" + val.replace(',','').replace("'",'').replace('(','').replace(')','')

                        print(matriculas)  
                        
                        # -_-_-_-_-_-_-_-_-_-_-_-  Buscamos si alguna coincide -_-_-_-_-_-_-_-_-_-_-_-
                        for i in range(len(matriculas)):
                            if str(matriculas[i]) == matAlu:
                                print("Muchas gracias, que tenga buen dia!")
                                i = False
                                # -_-_-_-_-_-_-_-_-_-_- Damos acceso -_-_-_-_-_-_-_-_-_-_-                                    
                                print(f"Acceso aprovado, se mantendra abierto por {n} segundos")
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
                            print("Matricula inválida")
                            print(f"Proceso finalizado alumno = {matAlu}")
                            iot.ledOn(26, n)
                            i = False
                    else:
                        print("Hubo un error, por favor")    
                        print(f"Error en 3er if = {matAlu}")
                        iot.ledOn(26, n)
                except:
                    print("Hubo un error, por favor")
                    print(f"Error en tryCatch = {matAlu}")
                    iot.ledOn(26, n)
            elif ("colaborador") in data:
                print("Camino colaborador")
            elif ("externo") in data:
                print("Una disculpa, no es posible que usted ingrese por este lugar, favor de retornar y entrar por la entrada principal.")
                i = False
                iot.ledOn(26, n)
            else:
                print("No se pudo entender su respuesta, por favor repita.")
    #            data = iot.recordAudio(3) # Recibir audio
                print(f"Error en 2do if = {matAlu}")
                iot.ledOn(26, n)
db.close()