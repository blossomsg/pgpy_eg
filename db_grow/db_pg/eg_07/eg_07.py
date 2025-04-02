"""https://medium.com/@patrikstrausz17/part3-postgresql-relationships-creating-and-managing-database-relationships-5e1eaea769d8
many to many relationships
"""

import psycopg2

connection = psycopg2.connect(host="localhost", dbname="postgres", user="postgres", password="123456789", port="5432")

cursor = connection.cursor()

cursor.execute("DROP TABLE IF EXISTS movies7, actors3, movies7_actors3")
cursor.execute("CREATE TABLE actors3(id SERIAL PRIMARY KEY, name VARCHAR(100) UNIQUE NOT NULL)")
cursor.execute(
    "INSERT INTO actors3(name) VALUES ('Keanu Reeves'), ('Cillian Murphy'), ('Christian Bale'), ('Jennifer Lawrence')")

cursor.execute(
    "CREATE TABLE movies7(movie7_id SERIAL PRIMARY KEY, name VARCHAR(250), date INTEGER)")
cursor.execute(
    "INSERT INTO movies7(name, date) VALUES ('The Matrix', '1999'), ('Batman Begins', '2005'), ('Blade Runner','1982'), ('The Dark Knight','2008'), ('The Dark Knight Rises', '2012'), ('The Hunger Games','2012')")

cursor.execute(
    "CREATE TABLE movies7_actors3(id SERIAL PRIMARY KEY, movie_id INTEGER , actor_id INTEGER, CONSTRAINT fk_movie FOREIGN KEY(movie_id) REFERENCES movies7(movie7_id), CONSTRAINT fk_actor FOREIGN KEY(actor_id) REFERENCES actors3(id))")
cursor.execute("INSERT INTO movies7_actors3(movie_id, actor_id) VALUES (1, 1), (2, 2), (2, 3), (3, Null), (4, 3), (5, 2), (5, 3), (6, 4)")
cursor.execute("SELECT * FROM movies7_actors3 JOIN movies7 ON movies7_actors3.movie_id = movies7.movie7_id JOIN actors3 ON movies7_actors3.actor_id = actors3.id ORDER BY movies7.name")
print(cursor.fetchall())
cursor.execute("SELECT * FROM movies7_actors3 JOIN movies7 ON movies7_actors3.movie_id = movies7.movie7_id JOIN actors3 ON movies7_actors3.actor_id = actors3.id WHERE movies7.name = 'Batman Begins'")
print(cursor.fetchall())

connection.commit()
cursor.close()
connection.close()