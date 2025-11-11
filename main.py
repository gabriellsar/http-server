import socket
from tinyserver import TinyServer

def main():
    PORTA = 8080

    ts = TinyServer(PORTA)

    ts.createSocket()
    ts.bindSocket()
    ts.listen(5)
    
    try:
        ts.startLoop()
    except KeyboardInterrupt:
        print("\nServidor interrompido. Fechando o socket...")
        ts.socket.close()

if __name__ == "__main__":
    main()
