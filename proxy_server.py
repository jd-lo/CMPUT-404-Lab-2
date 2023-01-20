from client import getFromHost
#from echo_server import startServer -- Multithread implementation
from threading import Thread
import socket


BYTESTOREAD = 4096

#Take a request and returns to client from remote host google
def fwdConnection(conn, addr):

    remoteHost = "www.google.com"
    remotePort = 80

    with conn:
        print(f'Connected to {addr}')
        #Get request from connection
        request = conn.recv(BYTESTOREAD)
        #Returns data from google
        response = getFromHost(remoteHost, remotePort, request)
        #Send back to client
        conn.sendall(response)

#The multi-threaded server that deviates from echo_server function
def startThreadedServer(host: str, port: int, handler: callable):
    #Func defines how to handle the connection
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.bind((host, port))
        #Reuse ports to prevent port in use errors
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        #Listen for incoming data
        sock.listen(3)
        while True:
            conn, addr = sock.accept()
            thread = Thread(target = handler, args = (conn, addr))
            thread.run()

def main():
    host = "localhost"
    port = 8080
    startThreadedServer(host, port, fwdConnection)

if __name__ == "__main__":
    main()
