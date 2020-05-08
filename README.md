# BackDoor-Demo
BackDoor echa en python3 con trafico encriptado en base85, esta back door no se puede mover entra carpetas, pero si puede ejecutar comandos en la maquina victima, esta es una version demos, pues se espera poder desarrollar una funcion con la que desplazarse entre carpetas, esta puerta trasera uas conexiones tcp y tambien dispone de unserver http que se puede personalizar y ejecutar en el dispositivo victima con lo que se podira descargar sus archivos.

los siguientes comandos estan disponibles en la ejecucion de la backdoor

                        ---------------------------------------------------------------
                        -                      comandos disponibles                    -
                        ----------------------------------------------------------------
                        -exit                      con este finalizas las conesiones   -
                        ----------------------------------------------------------------
                        -cd                con este pordras desplazarte entre carpetas -
                        ----------------------------------------------------------------
                        -BombFork          este ejecuta una bomba fork en el pc victima-
                        ----------------------------------------------------------------
                        -cwd                    para poder ver la ruta del directorio  -
                        ----------------------------------------------------------------
                        -HttpServer           ejecuta un server Http en la pc victimma -
                        ----------------------------------------------------------------
                        -CloseHttpServer                 finaliza el server http       -
                        ----------------------------------------------------------------
                        -cd ..                         retrocede un directorio         -
                        ----------------------------------------------------------------
                        -read                           lee archivos de la pc victima  -
                        ----------------------------------------------------------------
                        -dirList  lista los archivos y carpetas del directorio actual  -
                        ----------------------------------------------------------------
                        - otros comandos compatibles con el dispositivo de la victima  -
                        ----------------------------------------------------------------

El server http permite descargar y adentraser en las carpetas del dispositivo victima, el puerto por defecto 9785.

Para ejecutar el back-door-server.py  simlemente en un sistema linux se ejecuta con ./back-door-server.py esto ejecutaria el server en el hosts local(127.0.0.1) por el puerto 6365, a  no ser que le pasemos un puerto como argumento al ejecutar el script, en ese caso usa el comando de ejecucion del script y anadie el numero del puerto como en el ejemplo [./back-door-server.py 8009] eso me abriria el server el el puerto 8009. En sistem windows recomiendo crear un .exe antes de su ejecucion, para eso puedeen usar pyinstaller, su uso es simple, descargan python3, y ejecutan lo siguiente en el cmd: 
pip install pyinstaller
despues entran a la carpeta de nuestro script y ejecutan en ese directorio con el cmd lo siguiente:
pyinstaller --onefile back-door-server.py

para poder conectarnos al backdoor ejecutamos en nuestro linux [./back-door-client.py,] en este caso el primer parametro a asignarle sera el puerto que usamos en nuestro back-door-server.py, el cual en mi caso seria 8009, aunque si no ponemos ninguno retornara en ambos script, el server y el cliente e, el puerto por defecto 6365, el segundo parametro a pasarle seria la ip publica de tu victima, en mi caso como yo estoy usando la back door solo a nivel local para no dañar a nadie uso esta solo en mi pc, en mi caso a la back-door-client.py le tendre que pasar la ip local la cual es 127.0.0.1, esto solo si lo estan haciendo a nivel local como es mi caso, sii fuera para probar con un dispositivo fuera de la red deberian ejecutar back-door-server.py en el dispositvo victima y usar la back-door-client.py con la ip publica del dispositivo victima, un ejempplo [./back-door-client.py 8009 3.134.78.134] suponiendo de que fuera una ip valida, pero como yo lo estaba aciendo a nivel local deberia ejecutar el comando [./back-door-client.py 8009 127.0.0.1]
