import socket

BYTESTOREAD = 4096

def getFromHost(host: str, port: int, data: bytes):
    #close sock automatically
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.connect((host, port))
        sock.send(data)
        #Indicate transmission of data is terminated
        sock.shutdown(socket.SHUT_WR)

        #Recieve and print response from host
        response = sock.recv(BYTESTOREAD)
        while response:
            print(response)
            response = sock.recv(BYTESTOREAD)

def main():
    host = "www.google.com"
    port = 80
    request = b'GET / HTTP/1.1\nHost:' + host.encode("utf-8") + b'\n\n'

    getFromHost(host, port, request)

if __name__ == "__main__":
    main()