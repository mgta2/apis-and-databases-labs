'''
Building on the previous example, create a list of all of the emails of the users and print
the list to the console.
'''

import requests # Note (venv) must be activate

url = "http://demo.codingnomads.co:8080/tasks_api/users"

response = requests.get(url)
body = response.json()

emails_list = []

for my_dict in body['data']:
    emails_list.append(my_dict['email'])

print(emails_list)
