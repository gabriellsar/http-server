import socket
from connectionhandler import ConnectionHandler

class TinyServer():
    def __init__(self, port):
        self.host = "127.0.0.1" # localhost
        self.port = port

        self.socket

    def createSocket(self):
        self.socket = socket.socket(socket.AF_NET, socket.SOCKET_STREAM)

    def bindSocket(self):
        self.socket.bind((self.host, self.port))

    def listen(self, connections:int):
        self.socket.listen(connections)
        print(f"Server listening on {self.host}:{self.port}")
    
    def startLoop(self):
        while True:
            client_socket, client_adress = self.socket.accept()
            print(f"Connections Accept {client_adress}")

            handler = ConnectionHandler(client_socket, client_adress)
            handler.handleRequest()

            client_socket.close()

