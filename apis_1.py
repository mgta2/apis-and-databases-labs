'''
Using the requests package, make a GET request to the api behind this endpoint:
    http://demo.codingnomads.co:8080/tasks_api/users
Print out:
    - the status code
    - the encoding of the response
    - the text of the response body
'''

import requests # Note (venv) must be activate

url = "http://demo.codingnomads.co:8080/tasks_api/users"

response = requests.get(url)

print(response.status_code)
print(response.encoding)
print(response.text)