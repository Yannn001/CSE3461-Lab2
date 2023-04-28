

# Simple List Management Server and Client

This project provides a simple list management server and client that allows users to create, edit, display, and delete lists. The server stores lists with an ID number, and users can reference the lists by their ID number for modifications.

### The YouTube link for our demonstration video: https://www.youtube.com/watch?v=HcqFoWCsGdw

## Requirements

- Python 3.6 or higher

## Server

To start the server, run the following command:

```bash
python server.py <port></port>
```

Replace `<port>` with the desired port number on which you want the server to listen.

### Features

The server supports the following commands:

- `catalog`: List all the lists with their ID and title.
- `create <list title>`: Create a new list with the specified title.
- `edit <list number>`: Edit the list with the specified ID.
- `show`: Show the list items.
- `add <list item text>`: Add an item to the list.
- `remove <list item number>`: Remove an item from the list by item number.
- `quit`: Exit edit mode.
- `display <list number>`: Display the list with the specified ID.
- `delete <list number>`: Delete the list with the specified ID.
- `exit`: Exit the server.

## Client

To start the client, run the following command:

```bash
python client.py <server_ip> <server_port>
```

Replace `<server_ip>` with the IP address of the server and `<server_port>` with the port number on which the server is listening.

Enter the desired commands at the "Enter a command:" prompt. The client will send the command to the server and display the server's response.
