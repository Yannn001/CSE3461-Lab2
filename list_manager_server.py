import socket
import sys
import datetime
import threading

def handle_client(connection, address):
    while True:
        request = connection.recv(1024).decode()
        log_request(request, address)
        if not request:
            break
        response = handle_request(request)
        log_response(response)
        connection.sendall(response.encode())

def log_request(request, address):
    timestamp = datetime.datetime.now().strftime('%a %b %d %H:%M:%S %Y')
    print(f'{timestamp} REQUEST INFO from {address}: {request}')

def log_response(response):
    timestamp = datetime.datetime.now().strftime('%a %b %d %H:%M:%S %Y')
    print(f'{timestamp} RESPONSE INFO: {response}')

def handle_request(request):
    commands = request.split(' ')
    cmd = commands[0].lower()
    if cmd == 'catalog':
        response = ' '.join(lists.keys())
    elif cmd == 'create':
        lists[commands[1]] = []
        response = f'List "{commands[1]}" created'
    elif cmd == 'edit':
        list_num = int(commands[1])
        sub_cmd = commands[2].lower()
        if sub_cmd == 'show':
            response = ' '.join(lists[list_num])
        elif sub_cmd == 'add':
            lists[list_num].append(commands[3])
            response = f'Item "{commands[3]}" added to list "{list_num}"'
        elif sub_cmd == 'remove':
            item_num = int(commands[3])
            lists[list_num].pop(item_num)
            response = f'Item {item_num} removed from list "{list_num}"'
        elif sub_cmd == 'quit':
            response = 'Edit mode exited'
    elif cmd == 'display':
        list_num = int(commands[1])
        response = ' '.join(lists[list_num])
    elif cmd == 'delete':
        list_num = int(commands[1])
        del lists[list_num]
        response = f'List "{list_num}" deleted'
    elif cmd == 'exit':
        response = 'Server shutting down'
    else:
        response = 'Invalid command'
    return response

def start_server(port):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('0.0.0.0', port))
    server_socket.listen(5)

    print(f'Starting on port {port}')
    while True:
        connection, address = server_socket.accept()
        threading.Thread(target=handle_client, args=(connection, address)).start()

if __name__ == '__main__':
    lists = {}
    port = int(sys.argv[1])
    start_server(port)