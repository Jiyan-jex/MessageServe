import socket

def client_program():
    # Create a TCP based client socket
    echoClient = socket.socket()

    # Note: No need for bind() call in client sockets...
    # Just use the socket by calling connect()
    echoClient.connect(("127.0.0.1", 32007));

    message = input(" -> ") 

    while message.lower().strip() != 'bye':
        echoClient.send(message.encode())
        data = echoClient.recv(1024).decode()

        print('Received from server: ' + data)

        message = input(" -> ")
    echoClient.close()

if __name__=='__main__':
    client_program()
