# SQLAlchemy Tasks

import sqlalchemy
import os
from pprint import pprint

password = os.environ["DATABASEPASSWORD"]
my_url = f"mysql+pymysql://root:{password}@localhost/sakila"

engine = sqlalchemy.create_engine(my_url)
connection = engine.connect()
metadata = sqlalchemy.MetaData()

# Query 1: Select all actors with a first name of your choice.

actor = sqlalchemy.Table('actor', metadata, autoload=True, autoload_with=engine)

query_one = sqlalchemy.select([actor]).where(actor.columns.first_name=="PENELOPE")
result_one = connection.execute(query_one).fetchall()
pprint(result_one)

# Query 2: Select all actors and the films they have been in.

film = sqlalchemy.Table('film', metadata, autoload=True, autoload_with=engine)
film_actor = sqlalchemy.Table('film_actor', metadata, autoload=True, autoload_with=engine)

join_statement = actor.join(film_actor, film_actor.columns.actor_id == actor.columns.actor_id).join(film, film.columns.film_id == film_actor.columns.film_id)
query_two = sqlalchemy.select([actor.columns.first_name, actor.columns.last_name, film.columns.title]).select_from(join_statement)
result_two = connection.execute(query_two).fetchmany(10)
pprint(result_two)
# Only print 10 values else too much info for the CLI.

# Query 3: Select all actors that have appeared in a category of your choice.

category = sqlalchemy.Table('category', metadata, autoload=True, autoload_with=engine)
film_category = sqlalchemy.Table('film_category', metadata, autoload=True, autoload_with=engine)
bigger_join = join_statement.join(film_category, film_category.columns.film_id == film.columns.film_id).join(category, category.columns.category_id == film_category.columns.category_id)
query_three = sqlalchemy.select(actor.columns.first_name, actor.columns.last_name).where(category.columns.name == "Comedy")
result_three = connection.execute(query_three).fetchall()
pprint(result_three)

# Query 4: Select all comedy films and sort them by rental rate.
# Note: ORDER BY statement is here.

query_four = sqlalchemy.select(film.columns.title, film.columns.rental_rate).where(category.columns.name == "Comedy").order_by(sqlalchemy.asc(film.columns.rental_rate))
my_result = connection.execute(query_four).fetchall()
pprint(my_result)

# Asks for GROUP BY statement but those have to come with aggregates like SUM, COUNT etc.
# None of the above queries use these.