# Update all films in the film table to a rental_duration value of 10, if
# the length of the movie is more than 150.

import sqlalchemy
import os

password = os.environ["DATABASEPASSWORD"]
my_url = f"mysql+pymysql://root:{password}@localhost/sakila"

engine = sqlalchemy.create_engine(my_url)
connection = engine.connect()
metadata = sqlalchemy.MetaData()

film = sqlalchemy.Table('film', metadata, autoload=True, autoload_with=engine)

query = sqlalchemy.update(film).values(rental_duration = 10).where(film.columns.length > 150)
result = connection.execute(query)