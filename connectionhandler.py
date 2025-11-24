import socket
from httprequest import HttpRequest
from httpresponse import HttpResponse
from configmapper import ConfigMapper

class ConnectionHandler():
    def __init__(self, client_socket, client_address):
        self.client_socket = client_socket
        self.client_address = client_address

    def handleRequest(self):
        try:
            data = self.client_socket.recv(1024).decode('utf-8')
            req = HttpRequest(data)
            resp = HttpResponse()

            http_resp = ''

            if req.method == 'GET':
                fmapp = ConfigMapper(req.path)

                if fmapp.status == 200:
                    http_resp = resp.success(fmapp.fis_path)
                else:
                    http_resp = resp.notFound()
            else:
                http_resp = resp.notImplemented()

            self.client_socket.send(http_resp)

        except socket.error as e:
            print(f"Socket error: {e}")
