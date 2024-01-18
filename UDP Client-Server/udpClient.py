from socket import socket, AF_INET, SOCK_DGRAM

class UDPClient:
    def __init__(self):
        self.client_socket = socket(family=AF_INET, type=SOCK_DGRAM)
        self.server_address = ('127.0.0.1', 8000)

    def udp_client(self):
        payload = "Hey Server"

        try:
            while True:
                self.client_socket.sendto(payload.encode('utf-8'), self.server_address)

                data, addr = self.client_socket.recvfrom(4096)
                print(f"Received data from Server: {str(data.decode('utf-8'))}")

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
    app = UDPClient()
    app.udp_client()
