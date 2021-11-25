'''
Write a program that makes a PUT request to update your user information to a new first_name, last_name and email.
Again make a GET request to confirm that your information has been updated.
'''

import requests # Note (venv) must be activate

my_url = "http://demo.codingnomads.co:8080/tasks_api/users"

body = {
    "id": 505,
    "first_name": "Aupdate",
    "last_name": "Bupdate",
    "email": "Cupdate@email"
}

response = requests.put(my_url, json=body)

print(response.status_code)

check = requests.get(my_url)
given_data = check.json()
print(given_data["data"][-1])
