import socket
from threading import Thread

BYTESTOREAD = 4096

#Takes the data recieved and sends it back to client
def handleConnection(conn, addr):
    #Close connection socket once done
    with conn:
        print(f'Connected to {addr}')
        response = conn.recv(BYTESTOREAD)
        while response:
            conn.send(response)
            response = conn.recv(BYTESTOREAD)

#Start the server
def startServer(host: str, port: int, handler: callable):
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
    host = "localhost" #'127.0.01' or wildcard '0.0.0.0' would also work
    port = 8080

    startServer(host, port, handleConnection)

if __name__ == "__main__":
    main()