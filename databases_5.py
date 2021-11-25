# Databases Task 5
"""
Using the API from the APIs section, write a program to get user data and
all of their tasks. Create tables in a new database to model this data.

The previous API only lists user information - no tasks. Code below gets this
data and puts it in a database. If we have additional data on tasks then this
would be a many-one relationship: each task has a unique user attached to it.
"""

import requests
import sqlalchemy
import os

password = os.environ["DATABASEPASSWORD"]
my_url = f"mysql+pymysql://root:{password}@localhost/apidb"

engine = sqlalchemy.create_engine(my_url)
connection = engine.connect()
metadata = sqlalchemy.MetaData()

users = sqlalchemy.Table('users', metadata, autoload=True, autoload_with=engine)

api_url = "http://demo.codingnomads.co:8080/tasks_api/users"

response = requests.get(api_url)
body = response.json()
api_data = body['data']

# body['data'] is a list of dictionaries with keys: 'id', 'first_name',
# 'last_name', 'email', 'createdAt', 'updatedAt'.

select_query = sqlalchemy.select([users])
select_result = connection.execute(select_query).fetchall()

# select_result is a collection of mappings with keys given by columns of 'users'.

db_ids = []
for mapping in select_result:
    db_ids.append(mapping['id'])

site_ids = []
for my_dict in api_data:
    site_ids.append(my_dict['id'])

new_records = []
for i in range(0,len(site_ids)):
    if site_ids[i] not in db_ids:
        new_records.append(api_data[i])

# new_records is the list of new data to enter into the database.

if len(new_records) == 0:
    print("No new records to add.")
else:
    insert_query = sqlalchemy.insert(users)
    result_proxy = connection.execute(insert_query, new_records)
