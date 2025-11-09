import socket

def start_server():
       # Port number (can be any free port)

    # Create a socket object
    server_socket = socket.socket()
    server_socket.bind(('localhost',9999))
    server_socket.listen(1)

    
    print("Waiting for a connection...")

    conn, address = server_socket.accept()
    print(f"🎉 Connected with {address}")

    while True:
        # Receive message from client
        data = conn.recv(1024).decode()
        if not data:
            break
        print(f"Client: {data}")

        # Send reply to client
        message = input("You: ")
        conn.send(message.encode())

    conn.close()

if __name__ == '__main__':
    start_server()
