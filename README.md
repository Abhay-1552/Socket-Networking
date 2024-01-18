# Socket Networking with Python

This GitHub project provides a comprehensive implementation of TCP and UDP client-server socket connections in Python, with added support for multi-threading. These examples serve as a foundation for building networked applications and understanding the fundamentals of socket programming.

## Table of Contents

1. [Introduction](#introduction)
2. [Features](#features)
3. [Requirements](#requirements)
4. [Usage](#usage)
5. [Examples](#examples)
6. [Contributing](#contributing)
7. [License](#license)

## Introduction

Socket programming is a key aspect of network communication, enabling data exchange between devices over a network. This project aims to provide clear and functional examples of both TCP and UDP client-server socket connections using Python. Additionally, multi-threading is incorporated to demonstrate concurrent communication with multiple clients.

## Features

- TCP client-server socket implementation
- UDP client-server socket implementation
- Multi-threading support for handling multiple clients simultaneously
- Clean and modular code for easy understanding and customization

## Requirements

- Python 3.x
- socket
- _thread

## Usage

1. Clone the repository to your local machine:

   ```bash
   git clone https://github.com/Abhay-1552/Socket-Networking.git
   ```

2. Navigate to the project directory:

   ```bash
   cd Socket-Networking
   ```

3. Run the desired Python script:

   ```bash
   python tcpServer.py
   ```

   or

   ```bash
   python udpServer.py
   ```

   This will start the server.

4. Open a new terminal window and run the corresponding client script:

   ```bash
   python tcpClient.py
   ```

   or

   ```bash
   python udpClient.py
   ```

   Follow the prompts to interact with the server.

## Examples

### TCP Example

```python
# Sample TCP client implementation
import socket

host = 'localhost'
port = 12345

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((host, port))

message = input("Enter a message for the server: ")
client_socket.sendall(message.encode())

data = client_socket.recv(1024)
print(f"Received from server: {data.decode()}")

client_socket.close()
```

### UDP Example

```python
# Sample UDP client implementation
import socket

host = 'localhost'
port = 12345

client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

message = input("Enter a message for the server: ")
client_socket.sendto(message.encode(), (host, port))

data, server_address = client_socket.recvfrom(1024)
print(f"Received from server {server_address}: {data.decode()}")

client_socket.close()
```

## Contributing

Contributions are welcome! Feel free to open issues or submit pull requests to enhance the functionality, add features, or fix any bugs.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
