This is the README file for CSE 3461

Author: Yixuan Huang, Chengyan Wang

To run the server and client applications, follow these steps:
python3 list_manager_server.py 8000

In the second terminal, navigate to the directory where you saved the client script and start the client by running:
python3 list_manager_client.py 127.0.0.1 8000

Interact with the list manager:
Now, you can enter commands in the client terminal to interact with the list manager server. Here's an example interaction:

Create a shopping list:
mathematica
Copy code
Enter a command: create Shopping
Response: List "Shopping" created
Create a to-do list:
mathematica
Copy code
Enter a command: create ToDo
Response: List "ToDo" created
Show the list of lists:
yaml
Copy code
Enter a command: catalog
Response: Shopping ToDo
Add items to the shopping list:
mathematica
Copy code
Enter a command: edit Shopping add "Milk"
Response: Item "Milk" added to list "Shopping"
Enter a command: edit Shopping add "Eggs"
Response: Item "Eggs" added to list "Shopping"
Show the shopping list items:
yaml
Copy code
Enter a command: edit Shopping show
Response: Milk Eggs
Remove an item from the shopping list:
csharp
Copy code
Enter a command: edit Shopping remove 1
Response: Item 1 removed from list "Shopping"
Display the shopping list:
yaml
Copy code
Enter a command: display Shopping
Response: Milk
Delete the to-do list:
mathematica
Copy code
Enter a command: delete ToDo
Response: List "ToDo" deleted
Show the list of lists again:
yaml
Copy code
Enter a command: catalog
Response: Shopping
Exit the list manager:
bash
Copy code
Enter a command: exit
Response: Server shutting down