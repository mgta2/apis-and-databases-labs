'''
Write a program that makes a DELETE request to remove the user your create in a previous example.
Again, make a GET request to confirm that information has been deleted.
'''

import requests # Note (venv) must be activate

my_url = "http://demo.codingnomads.co:8080/tasks_api/users"

response = requests.delete(my_url + '/501')

print(response.status_code)

check = requests.get(my_url)
given_data = check.json()
print(given_data["data"][-1])