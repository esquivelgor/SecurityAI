import RPi.GPIO as GPIO # Puertos raspberry 
#from picamera import PiCamera
import methodsIOT as iot
import mysql.connector
from datetime import datetime
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

        loop = True
        while loop == True:
            # -_-_-_-_-_-_-_-_-_-_-_-  Casos posibles, estudiante/colaborador/externo  -_-_-_-_-_-_-_-_-_-_-_-      
            if ("estudiante") in data:
                print("Dígame su matrícula sin la primer letra") # 01 62 56 21
    #            #matAlu = iot.recordAudio(5)
    #            #matAlu = matAlu.replace(' ', '').replace(',','').replace('.','').replace('-','') # Limpieza de la data
                try:
                    if(len(matAlu) == 8):
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
                        
                        # -_-_-_-_-_-_-_-_-_-_-_-  Buscamos si alguna coincide -_-_-_-_-_-_-_-_-_-_-_-
                        for i in range(len(matriculas)):
                            if str(matriculas[i]) == matAlu:
                                print("Muchas gracias, que tenga buen dia!")
                                loop = False
                                # -_-_-_-_-_-_-_-_-_-_- Damos acceso -_-_-_-_-_-_-_-_-_-_-                                    
                                print(f"Acceso aprovado, se mantendra abierto por {n} segundos")
                                iot.ledOn(16, n)
                                # --- Foto de seguridad --- 
                                date = datetime.now().strftime('%Hh-%Mm-%d-%m-%Y')
                                #capture_img = '/home/esquivelg/Documents/pictures/' + date + '.jpg'
                                #capture_photo(capture_img, date)
                                
                                # --- Registro de acceso --- 
                                querySQL = "INSERT INTO accesos (Acceso, ID_Usuario) values (now() , '"+ matAlu +"')"
                                crsr.execute(querySQL)
                                db.commit()

                                print("Proceso estudiante finalizado")
                        # --- Caso en que no hay coincidencias --- 
                        if (loop == True):
                            print("Matricula actualmente inválida")
                            iot.ledOn(26, n)
                            loop = False
                    else:
                        print("Hubo un error, por favor")    
                        print(f"Error en 3er if = {matAlu}")
                        iot.ledOn(26, n)
                except Exception as err:
                    print("Hubo un error, por favor")
                    print(f"Unexpected {err=}, {type(err)=}")
                    iot.ledOn(26, n)
            elif ("colaborador") in data:
                print("Camino colaborador")
            elif ("externo") in data:
                print("Una disculpa, no es posible que usted ingrese por este lugar, favor de retornar y entrar por la entrada principal.")
                loop = False
                iot.ledOn(26, n)
            else:
                print("No se pudo entender su respuesta, por favor repita.")
    #            data = iot.recordAudio(3) # Recibir audio
                print(f"Error en 2do if = {matAlu}")
                iot.ledOn(26, n)
db.close()