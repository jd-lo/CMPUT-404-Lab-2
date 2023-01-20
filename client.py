import socket

BYTESTOREAD = 4096

def getFromHost(host: str, port: int, req: bytes):
    #close sock automatically
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.connect((host, port))
        sock.send(req)
        #Indicate transmission of data is terminated
        sock.shutdown(socket.SHUT_WR)

        #Recieve and print response from host
        response = sock.recv(BYTESTOREAD)
        data = b''
        while response:
            data += response
            response = sock.recv(BYTESTOREAD)
        return data

def main():
    host = "www.google.com"
    port = 80
    request = b'GET / HTTP/1.1\nHost:' + host.encode("utf-8") + b'\n\n'

    print(getFromHost(host, port, request))

if __name__ == "__main__":
    main()