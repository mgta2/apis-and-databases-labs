'''
Write the necessary code to make a POST request to:
    http://demo.codingnomads.co:8080/tasks_api/users
and create a user with your information.
Make a GET request to confirm that your user information has been saved.
'''

import requests # Note (venv) must be activate

my_url = "http://demo.codingnomads.co:8080/tasks_api/users"

body = {
    "first_name": "A",
    "last_name": "B",
    "email": "C@email"
}

response = requests.post(my_url, json=body)

print(response.status_code)

check = requests.get(my_url)
given_data = check.json()
print(given_data["data"][-1])
