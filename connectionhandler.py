from handlerequest import HttpRequest
from handleresponse import HttpResponse
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

            if req.method == 'GET':
                fmapp = ConfigMapper(req.path)
                if fmapp.status == 200: # HTTP/1.1 200 OK
                    resp.Success(fmapp.fis_path)
                else: # HTTP/1.1 404 Not Found
                    resp.notFound()
            else:
                resp.notImplemented()
        except socket.error as e:
            print(f"Socket error: {e}")
