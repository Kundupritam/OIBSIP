import socket

def start_client():
        # Must match the server's port

    client_socket = socket.socket()
    client_socket.connect(('localhost', 9999))

    

    while True:
        message = input("You: ")
        client_socket.send(message.encode())

        data = client_socket.recv(1024).decode()
        print(f"Server: {data}")

    client_socket.close()

if __name__ == '__main__':
    start_client()
