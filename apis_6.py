'''
Create an application that interfaces with the user via the CLI - prompt the user with a menu such as:
Please select from the following options (enter the number of the action you'd like to take):
1) Create a new account (POST)
2) View all your tasks (GET)
3) View your completed tasks (GET)
4) View only your incomplete tasks (GET)
5) Create a new task (POST)
6) Update an existing task (PATCH/PUT)
7) Delete a task (DELETE)
It is your responsibility to build out the application to handle all menu options above.
'''

import requests

my_url = "URL"

print("Welcome to this service portal.")
my_str = "(0) Exit service\n"
my_str += "(1) Create a new account\n"
my_str += "(2) View all your tasks\n"
my_str += "(3) View your completed tasks\n"
my_str += "(4) View only your incomplete tasks\n"
my_str += "(5) Create a new task\n"
my_str += "(6) Update an existing task\n"
my_str += "(7) Delete a task"

while True:
    print(my_str)
    user_input = input("Please choose a service by entering the corresponding number: ")
    if user_input.isdigit():
        user_input = int(user_input)
        if user_input not in [0, 1, 2, 3, 4, 5, 6, 7]:
            print("Please enter a valid number.")
            continue
    else:
        print("You did not enter a number.")
        continue
    
    if user_input == 0:
        print("Exiting...")
        break
    elif user_input == 1:
        user_input = input("Enter your name: ")
        body = {"name": user_input}
        response = requests.post(my_url, body)
    elif user_input == 2:
        user_input = int(input("Enter your account number: "))
        response = requests.get(my_url)
        body = response.json()
        print(body['data'][user_input]['tasks'])
    elif user_input == 3:
        user_input = int(input("Enter your account number: "))
        response = requests.get(my_url)
        body = response.json()
        print(body['data'][user_input]['comptasks'])
    elif user_input == 4:
        user_input = int(input("Enter your account number: "))
        response = requests.get(my_url)
        body = response.json()
        print(body['data'][user_input]['incomptasks'])
    elif user_input == 5:
        user_input = int(input("Enter your account number: "))
        new_task = input("Enter your new task: ")
        response = requests.get(my_url)
        body = response.json()
        tasks = body['data'][user_input]['tasks']
        incomptasks = body['data'][user_input]['incomptasks']
        body = {
            "id": user_input,
            "tasks": tasks.append(new_task),
            "incomptasks": incomptasks.append(new_task)
        }
        response = requests.put(my_url, json=body)
    elif user_input == 6:
        user_input = int(input("Enter your account number: "))
        response = requests.get(my_url)
        body = response.json()
        comptasks = body['data'][user_input]['comptasks']
        incomptasks = body['data'][user_input]['incomptasks']
        print(incomptasks)
        task_choice = input("Select the number (counting from 0) of which task you have completed: ")
        newincomptasks = [x for x in incomptasks if x != incomptasks[task_choice]]
        comptasks.append(incomptasks[task_choice])
        body = {
            "id": user_input,
            "comptasks": comptasks,
            "incomptasks": newincomptasks
        }
        response = requests.put(my_url,json=body)
    elif user_input == 7:
        user_input = int(input("Enter your account number: "))
        response = requests.delete(my_url + "/user_input")