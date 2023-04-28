import socket
import sys
import datetime
import threading

is_edit = False
list_id = None

# Specify the log file name
log_file = 'server_log.txt'

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
    log_entry = f'{timestamp} REQUEST INFO from {address}: {request}'
    print(log_entry)
    # Write the log entry to the log file
    with open(log_file, 'a') as f:
        f.write(log_entry + '\n')

def log_response(response):
    timestamp = datetime.datetime.now().strftime('%a %b %d %H:%M:%S %Y')
    log_entry = f'{timestamp} RESPONSE INFO: {response}'
    print(log_entry)
    # Write the log entry to the log file
    with open(log_file, 'a') as f:
        f.write(log_entry + '\n')

def handle_request(request):
    global is_edit, list_id, lists
    commands = request.split(' ')
    cmd = commands[0].lower()

    def invalid_command():
        error_msg = f'Invalid command: {cmd}\n'
        error_msg += 'Valid commands are:\n'
        if is_edit:
            error_msg += '1. show\n2. add <list item text>\n3. remove <list item number>\n4. quit\n'
        else:
            error_msg += 'i. catalog\nii. create <list title>\niii. edit <list number>\n'
            error_msg += 'iv. display <list number>\nv. delete <list number>\nvi. exit\n'
        return error_msg

    if is_edit:
        if cmd == 'show':
            response = ' '.join(lists[list_id])
        elif cmd == 'add':
            if len(commands) < 2:
                response = 'Missing element: add usage: add <list item text>'
            else:
                lists[list_id].append(commands[1])
                response = f'Item "{commands[1]}" added to list with ID {list_id}'
        elif cmd == 'remove':
            if len(commands) < 2:
                response = 'Missing element: remove usage: remove <list item number>'
            else:
                item_num = int(commands[1])
                lists[list_id].pop(item_num)
                response = f'Item {item_num} removed from list with ID {list_id}'
        elif cmd == 'quit':
            response = 'Edit mode exited'
            is_edit = False
        else:
            response = invalid_command()
    else:
        if cmd == 'catalog':
            response = ', '.join([f'{k}: {v[0]}' for k, v in lists.items()])
            if response == '':
                response = 'No lists created yet'
        elif cmd == 'create':
            if len(commands) < 2:
                response = 'Missing element: create usage: create <list title>'
            else:
                list_id = max(lists.keys(), default=0) + 1
                lists[list_id] = [commands[1]]
                response = f'List "{commands[1]}" created with ID {list_id}'
        elif cmd == 'edit':
            if len(commands) < 2:
                response = 'Missing element: edit usage: edit <list number>'
            else:
                list_id = int(commands[1])
                is_edit = True
                response = "You are now in edit mode. Enter 'quit' to exit edit mode\n"
        elif cmd == 'display':
            if len(commands) < 2:
                response = 'Missing element: display usage: display <list number>'
            else:
                list_id = int(commands[1])
                response = ' '.join(lists[list_id][1:])
                if response == '':
                    response = 'No items in list'
        elif cmd == 'delete':
            if len(commands) < 2:
                response = 'Missing element: delete usage: delete <list number>'
            else:
                list_id = int(commands[1])
                del lists[list_id]
                response = f'List with ID {list_id} deleted'
        elif cmd == 'exit':
            response = 'Bye!'
        else:
            response = invalid_command()
    return response

def start_server(port):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('0.0.0.0', port))
    server_socket.listen(5)

    timestamp = datetime.datetime.now().strftime('%a %b %d %H:%M:%S %Y')
    print(f'{timestamp} Starting on port {port}')

    while True:
        connection, address = server_socket.accept()
        threading.Thread(target=handle_client, args=(connection, address)).start()

if __name__ == '__main__':
    lists = {}
    port = int(sys.argv[1])
    start_server(port)
