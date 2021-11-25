# Print information about the film and category tables.
import sqlalchemy
import os
from pprint import pprint

password = os.environ["DATABASEPASSWORD"]
my_url = f"mysql+pymysql://root:{password}@localhost/sakila"

engine = sqlalchemy.create_engine(my_url)
connection = engine.connect()
metadata = sqlalchemy.MetaData()
category = sqlalchemy.Table('category', metadata, autoload=True, autoload_with=engine)
film = sqlalchemy.Table('film', metadata, autoload=True, autoload_with=engine)

query_one = sqlalchemy.select([category])
query_two = sqlalchemy.select([film])

result_one = connection.execute(query_one).fetchall()
result_two = connection.execute(query_two).fetchall()

pprint(result_one)
print()
pprint(result_two)