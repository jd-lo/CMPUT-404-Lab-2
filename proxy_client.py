from client import getFromHost

def main():
    host = "localhost"
    port = 8080
    
    remoteHost = "www.google.com"

    request = b'GET / HTTP/1.1\nHost:' + remoteHost.encode("utf-8") + b'\n\n'

    print(getFromHost(host, port, request))

if __name__ == "__main__":
    main()
