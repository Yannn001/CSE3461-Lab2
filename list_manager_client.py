import socket
import sys

def send_request(server_ip, server_port, request):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((server_ip, server_port))
    client_socket.sendall(request.encode())
    response = client_socket.recv(1024).decode()
    client_socket.close()
    return response

if __name__ == '__main__':
    server_ip = sys.argv[1]
    server_port = int(sys.argv[2])

    while True:
        command = input('Enter a command: ')
        response = send_request(server_ip, server_port, command)
        print('Response:', response)
        if command.lower() == 'exit':
            break