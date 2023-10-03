import socket 

def server_program():
    # A TCP based echo server
    # echoSocket <socket.socket fd=3, family=AddressFamily.AF_INET, type=SocketKind.SOCK_STREAM, proto=0, laddr=('0.0.0.0', 0)>
    echoSocket = socket.socket();

    # Bind the TCP socket to the IP address and the port number
    echoSocket.bind(("127.0.0.1", 32007));

    # listen for incoming connections
    echoSocket.listen();

    # clientSocket: <socket.socket fd=4, family=AddressFamily.AF_INET, type=SocketKind.SOCK_STREAM, proto=0, laddr=('127.0.0.1', 32007), raddr=('127.0.0.1', 51374)>
    # clientAddress: ('127.0.0.1', 51374)
    (clientSocket, clientAddress) = echoSocket.accept();

    # Handle one request from client
    while(True):
        data = clientSocket.recv(1024).decode();
        if not data:
            #if data is not received break
            break
        print("from connected user: " + str(data))
        data = input(' -> ')
        clientSocket.send(data.encode()) #send data to client
        clientSocket.close

if __name__=='__main__':
    server_program()
