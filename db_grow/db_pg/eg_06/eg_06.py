"""https://medium.com/@patrikstrausz17/part3-postgresql-relationships-creating-and-managing-database-relationships-5e1eaea769d8
one to many relationship
"""

import psycopg2

connection = psycopg2.connect(host="localhost", dbname="postgres", user="postgres", password="123456789", port="5432")

cursor = connection.cursor()

cursor.execute("DROP TABLE IF EXISTS actors2, movies6")
cursor.execute("CREATE TABLE actors2(id SERIAL PRIMARY KEY, name VARCHAR(100) UNIQUE NOT NULL)")
cursor.execute("INSERT INTO actors2(name) VALUES ('Keanu Reeves'), ('Cillian Murphy'), ('Christian Bale'), ('Jennifer Lawrence')")

cursor.execute("CREATE TABLE movies6(movie6_id SERIAL PRIMARY KEY, name VARCHAR(250), date INTEGER, actor_id INTEGER, CONSTRAINT fk_actor FOREIGN KEY(actor_id) REFERENCES actors2(id))")
cursor.execute("INSERT INTO movies6(name, date, actor_id) VALUES ('The Matrix', '1999', '1'), ('Batman Begins', '2005', '3'), ('Blade Runner','1982', Null), ('The Dark Knight','2008', '3'), ('The Dark Knight Rises', '2012', '3'), ('The Hunger Games','2012', '4')")
cursor.execute("SELECT * FROM movies6 JOIN actors2 ON movies6.actor_id = actors2.id")
print(cursor.fetchall())


connection.commit()
cursor.close()
connection.close()