import RPi.GPIO as GPIO
import methods as iot
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
    db = mysql.connector.connect(user='----------', password='---------', database='login')
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
    matAlu =  " "
    matriculas = []

    if GPIO.input(15) == GPIO.HIGH:
        print("Inicia proceso")
        iot.t2s("Bienvenido al Tecnologico de Monterrey, reconociendo usuario, favor de esperar")
        faceData = iot.faceRecognition()
        iot.t2s(f"Bienvenido {faceData[0]}, eres estudiante o colaborador?")
        data = iot.s2t(3)

        loop = True
        while loop == True:
            # -_-_-_-_-_-_-_-_-_-_-_-  Casos posibles, estudiante/colaborador/externo  -_-_-_-_-_-_-_-_-_-_-_-      
            if ("estudiante") in data:
                iot.t2s("Dígame su matrícula sin la primer letra") # 01 62 56 21
                matAlu = iot.s2t(5)
                matAlu = matAlu.replace(' ', '').replace(',','').replace('.','').replace('-','') # Limpieza de la data
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
                                # --- Security picture --- 
                                capture_img = './img.jpg'
                                iot.capture_photo(capture_img)

                                # --- Upload the picture ---
                                try:
                                    binPic = iot.convertToBinaryData("./img.jpg")
                                    query = "INSERT INTO memorybank (Imagen, ID_Usuario) VALUES (%s,%s)" 
                                    crsr.execute(query, (binPic, matAlu))
                                except mysql.connector.Error as error:
                                    print("Failed inserting BLOB data into MySQL table {}".format(error))

                                # --- Registro de acceso --- 
                                querySQL = "INSERT INTO accesos (Acceso, ID_Usuario) values (now() , '"+ matAlu +"')"
                                crsr.execute(querySQL)
                                db.commit()

                                # -_-_-_-_-_-_-_-_-_-_- Damos acceso -_-_-_-_-_-_-_-_-_-_-                                    
                                iot.t2s(f"Acceso aprovado, se mantendrá abierto por {n} segundos")
                                iot.ledOn(16, n)
                                loop = False
                                print("Proceso estudiante finalizado")
                        # --- Caso en que no hay coincidencias --- 
                        if (loop == True):
                            iot.t2s("Matricula actualmente inválida")
                            iot.ledOn(26, n)
                            loop = False
                    else:
                        iot.t2s("Hubo un error, por favor")    
                        print(f"Error en 3er if = {matAlu}")
                        iot.ledOn(26, n)
                except Exception as err:
                    iot.t2s("Hubo un error, por favor")
                    print(f"Unexpected {err=}, {type(err)=}")
                    iot.ledOn(26, n)
            elif ("colaborador") in data:
                iot.t2s("Dígame su matrícula sin la primer letra") # 01 62 56 21
                matAlu = iot.s2t(5)
                matAlu = matAlu.replace(' ', '').replace(',','').replace('.','').replace('-','') # Limpieza de la data
                try:
                    if(len(matAlu) == 8):
                        query = "SELECT `ID_Usuario` FROM `usuarios` WHERE `Tipo_Usuario` = 'Colaborador';"

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
                                # --- Security picture --- 
                                capture_img = './img.jpg'
                                iot.capture_photo(capture_img)

                                # --- Upload the picture ---
                                try:
                                    binPic = iot.convertToBinaryData("./img.jpg")
                                    query = "INSERT INTO memorybank (Imagen, ID_Usuario) VALUES (%s,%s)" 
                                    crsr.execute(query, (binPic, matAlu))
                                except mysql.connector.Error as error:
                                    print("Failed inserting BLOB data into MySQL table {}".format(error))

                                # --- Registro de acceso --- 
                                querySQL = "INSERT INTO accesos (Acceso, ID_Usuario) values (now() , '"+ matAlu +"')"
                                crsr.execute(querySQL)
                                db.commit()

                                # -_-_-_-_-_-_-_-_-_-_- Damos acceso -_-_-_-_-_-_-_-_-_-_-                                    
                                iot.t2s(f"Acceso aprovado, se mantendrá abierto por {n} segundos")
                                iot.ledOn(16, n)
                                loop = False
                                print("Proceso estudiante finalizado")
                        # --- Caso en que no hay coincidencias --- 
                        if (loop == True):
                            iot.t2s("Matricula actualmente inválida")
                            iot.ledOn(26, n)
                            loop = False
                    else:
                        iot.t2s("Hubo un error, por favor")    
                        print(f"Error en 3er if = {matAlu}")
                        iot.ledOn(26, n)
                except Exception as err:
                    iot.t2s("Hubo un error, por favor")
                    print(f"Unexpected {err=}, {type(err)=}")
                    iot.ledOn(26, n)
            elif ("externo") in data:
                iot.t2s("Una disculpa, no es posible que usted ingrese por este lugar, favor de retornar y entrar por la entrada principal.")
                loop = False
                iot.ledOn(26, n)
            else:
                iot.t2s("No se pudo entender su respuesta, por favor repita.")
                data = iot.s2t(4)
                print(f"Error en 2do if = {matAlu}")
                iot.ledOn(26, n)
crsr.close()
db.close()
