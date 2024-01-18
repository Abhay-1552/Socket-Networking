from socket import socket, AF_INET, SOCK_DGRAM


class UDPServer:
    def __init__(self):
        self.server_socket = socket(family=AF_INET, type=SOCK_DGRAM)

        self.server_address = ('127.0.0.1', 8000)
        self.server_socket.bind(self.server_address)

    def udp_server(self):
        print("Waiting for Client Data!!")
        while True:
            data, client_address = self.server_socket.recvfrom(4096)

            print(f"Data Received from {client_address}")

            if not data or data.decode('utf-8') == 'END':
                break
            print(f'Received data from Client: {str(data.decode("utf-8"))} \n')

            try:
                message = 'Hello I am UDP Server'.encode('utf-8')
                self.server_socket.sendto(message, client_address)

            except OSError as e:
                print(f"\nExited by user, Error: {e}")
                break

    def close_server(self):
        self.server_socket.close()


if __name__ == '__main__':
    app = UDPServer()

    try:
        app.udp_server()
    except KeyboardInterrupt:
        pass
    finally:
        app.close_server()
