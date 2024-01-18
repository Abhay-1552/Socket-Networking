from socket import *


class Client:
    def __init__(self):
        self.client_socket = socket()
        self.server_address = ('127.0.0.1', 8000)
        self.client_socket.connect(self.server_address)

    def tcp_client(self):
        payload = "Hey Server"

        try:
            while True:
                self.client_socket.send(payload.encode('utf-8'))

                data = self.client_socket.recv(1024)
                print(f'Received data from Server: {data.decode("utf-8")}')

                more_payload = input("Want to send more data to server (y/n): ")

                if more_payload.lower() == 'y':
                    payload = input("Send data to Server: ")
                else:
                    break

        except KeyboardInterrupt:
            print("\nClient interrupted by user.")

        finally:
            self.client_socket.close()


if __name__ == '__main__':
    app = Client()
    app.tcp_client()
