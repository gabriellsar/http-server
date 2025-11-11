import os 

class HttpResponse():
    def __init__(self):
        pass

    def success(self, path):
        status = 'HTTP/1.1 200 OK\r\n'

        body = b''
        with open(path, 'rb') as file:
            body = file.read()

        extensao = os.path.splitext(path)[1]
        tipos_mime = {
            '.html': 'text/html',
            '.txt':  'text/plain',
            '.jpg':  'image/jpeg',
            '.jpeg': 'image/jpeg',
            '.png':  'image/png'
        }
        content_type = tipos_mime.get(extensao, 'application/octet-stream')

        header_type = f'Content-Type: {content_type}\r\n'
        header_len = f'Content-Length: {len(body)}\r\n'        
        blank_line = '\r\n'

        header = header_type + header_len + blank_line
        resposta_final_em_bytes = status.encode('utf-8') + header.encode('utf-8') + body

        return resposta_final_em_bytes

    def notFound(self):
        status = 'HTTP/1.1 404 Not Found\r\n'
        header = 'Content-Type: text/html\r\nContent-Length: 37\r\n\r\n'
        body = '<html><body>404 Not Found</body></html>'

        return (status + header + body).encode('utf-8')

    def notImplemented(self):
        status = 'HTTP/1.1 501 Not Implemented\r\n'
        header = 'Content-Type: text/html\r\nContent-Length: 43\r\n\r\n'
        body = '<html><body>501 Not Implemented</body></html>'

        return (status + header + body).encode('utf-8')
