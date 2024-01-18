from socket import socket, AF_INET, SOCK_STREAM


class TCPServer:
    def __init__(self):
        self.server_socket = socket(family=AF_INET, type=SOCK_STREAM)
        self.server_address = ('localhost', 8000)
        self.server_socket.bind(self.server_address)
        self.server_socket.listen(5)

    def tcp_server(self):
        while True:
            print("Waiting for Client to connect!!")

            client_socket, addr = self.server_socket.accept()

            print(f"Connected address {addr}")

            while True:
                data = client_socket.recv(1024)

                if not data or data.decode('utf-8') == 'END':
                    break
                print(f'Received data from Client: {data.decode("utf-8")}')

                try:
                    client_socket.send(bytes('Hello Client', 'utf-8'))

                except OSError as e:
                    print(f"\nExited by user, Error: {e}")

            client_socket.close()

    def close_server(self):
        self.server_socket.close()


if __name__ == '__main__':
    app = TCPServer()

    try:
        app.tcp_server()
    except KeyboardInterrupt:
        pass
    finally:
        app.close_server()
