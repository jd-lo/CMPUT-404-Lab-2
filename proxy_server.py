from client import getFromHost
from echo_server import startServer

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

def main():
    host = "localhost"
    port = 8080
    startServer(host, port, fwdConnection)

if __name__ == "__main__":
    main()
