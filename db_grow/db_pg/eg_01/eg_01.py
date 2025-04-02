"""Inserting data manually in the DB"""

import psycopg2

from db_grow.db_pg.CONSTANTS import HOST, DBNAME, USER, PASSWORD, PORT

connection = psycopg2.connect(host=HOST, dbname=DBNAME, user=USER, password=PASSWORD, port=PORT)

cursor = connection.cursor()

cursor.execute("DROP TABLE IF EXISTS movies")
cursor.execute("CREATE TABLE movies(movies_id SERIAL PRIMARY KEY, movie_name VARCHAR(50) NOT NULL, release_year INTEGER NOT NULL);")
cursor.execute("INSERT INTO movies(movie_name, release_year) VALUES ('The Dark Knight', '2008'), ('Mad Max: Fury Road', '2015');")

connection.commit()
cursor.close()
connection.close()
