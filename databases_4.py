# Databases Task 4.
"""
Application which interfaces with the MySQL database - sqlalcdb.
Capable of:
    - inserting 3 tables.
    - inserting data into tables.
    - update data in tables.
    - select data from each table.
    - delete data from each table.
    - use at least one join statement in a select query.
"""

import sqlalchemy
import os
from pprint import pprint

password = os.environ["DATABASEPASSWORD"]
my_url = f"mysql+pymysql://root:{password}@localhost/sqlalcdb"

engine = sqlalchemy.create_engine(my_url)
connection = engine.connect()
metadata = sqlalchemy.MetaData()

my_str = ("Enter following number to interface with the database:\n"
          "Anything other than 0,1,...,6 - exit\n"
          "1 - insert table\n"
          "2 - insert data into table\n"
          "3 - update data in table\n"
          "4 - select data from table\n"
          "5 - delete data from table\n"
          "6 - special select\n"
          "Your selection: "
          )

type_str = ("Three types of table available (1, 2 or 3):\n"
            "1 - Users Table (user_id, username, email)\n"
            "2 - Posts Table (post_id, user_id, post_text)\n"
            "3 - Friends Table (pair_id, userone_id, usertwo_id)"
            )

def make_users():
    users_table = sqlalchemy.Table('users', metadata,
                       sqlalchemy.Column('one', sqlalchemy.Integer()),
                       sqlalchemy.Column('two', sqlalchemy.String(255), nullable=False),
                       sqlalchemy.Column('three', sqlalchemy.String(255), nullable=False),
              )
    metadata.create_all(engine)
    return

def make_friends():
    friends_table = sqlalchemy.Table('friends', metadata,
                       sqlalchemy.Column('one', sqlalchemy.Integer()),
                       sqlalchemy.Column('two', sqlalchemy.Integer()),
                       sqlalchemy.Column('three', sqlalchemy.Integer()),
              )
    metadata.create_all(engine)
    return

def make_posts():
    posts_table = sqlalchemy.Table('posts', metadata,
                       sqlalchemy.Column('one', sqlalchemy.Integer()),
                       sqlalchemy.Column('two', sqlalchemy.Integer()),
                       sqlalchemy.Column('three', sqlalchemy.String(255), nullable=False),
              )
    metadata.create_all(engine)
    return

while True:
    user_input = input(my_str)
    if user_input.isdigit():
        user_input = int(user_input)
    else:
        break
    
    if user_input == 1:
        # Insert Table
        table_type = int(input(type_str))
        if table_type == 1:
            # Users Table
            make_users()
        elif table_type == 2:
            # Posts Table
            make_posts()
        elif table_type == 3:
            # Friends Table
            make_friends()
        
    elif user_input == 2:
        # Insert Data
        table_choice = input("What table? 'users', 'posts' or 'friends': ")
        table_choice = sqlalchemy.Table(table_choice, metadata, autoload=True, autoload_with=engine)
        first_field = input("user/pair/post_id: ")
        second_field = input("username/userone_id/user_id: ")
        third_field = input("email/usertwo_id/post: ")
        query = sqlalchemy.insert(table_choice).values(one=first_field,two=second_field,three=third_field)
        result_proxy = connection.execute(query)
        
    elif user_input == 3:
        # Update Data
        table_choice = input("What table? 'users', 'posts' or 'friends': ")
        table_choice = sqlalchemy.Table(table_choice, metadata, autoload=True, autoload_with=engine)
        first_field = input("user/pair/post_id: ")
        second_field = input("username/userone_id/user_id: ")
        third_field = input("email/usertwo_id/post: ")
        query = sqlalchemy.update(table_choice).values(two=second_field,three=third_field).where(table_choice.columns.one==int(first_field))
        result_proxy = connection.execute(query)
        
    elif user_input == 4:
        # Select Data
        table_choice = input("What table? 'users', 'posts' or 'friends': ")
        table_choice = sqlalchemy.Table(table_choice, metadata, autoload=True, autoload_with=engine)
        first_field = input("user/pair/post_id: ")
        query = sqlalchemy.select([table_choice]).where(table_choice.columns.one == int(first_field))
        result_proxy = connection.execute(query)
        result_set = result_proxy.fetchall()
        pprint(result_set)
        
    elif user_input == 5:
        # Delete Data
        table_choice = input("What table? 'users', 'posts' or 'friends': ")
        table_choice = sqlalchemy.Table(table_choice, metadata, autoload=True, autoload_with=engine)
        first_field = input("user/pair/post_id: ")
        query = sqlalchemy.delete(table_choice).where(table_choice.columns.one == int(first_field))
        results = connection.execute(query)
        
    elif user_input == 6:
        # Special Select
        table_choice_one = input("What table one? 'users', 'posts' or 'friends': ")
        table_choice_one = sqlalchemy.Table(table_choice_one, metadata, autoload=True, autoload_with=engine)
        table_choice_two = input("What table two? 'users', 'posts' or 'friends': ")
        table_choice_two = sqlalchemy.Table(table_choice_two, metadata, autoload=True, autoload_with=engine)
        joiner = table_choice_one.join(table_choice_two, table_choice_two.columns.one == table_choice_one.columns.one)
        query = sqlalchemy.select([joiner])
        result_proxy = connection.execute(query)
        result_set = result_proxy.fetchall()
        pprint(result_set)
        
    else:
        break





