"""ALTER and UPDATE to modify table"""
import psycopg2

connection = psycopg2.connect(host="localhost", dbname="postgres", user="postgres", password="123456789", port="5432")

cursor = connection.cursor()
# cursor.execute("DROP TABLE IF EXISTS movies4")
# cursor.execute("CREATE TABLE movies4(movies_id SERIAL PRIMARY KEY, movies_name VARCHAR(100) NOT NULL, release_year INTEGER NOT NULL)")
# cursor.execute("INSERT INTO movies4(movies_name, release_year) VALUES ('The Dark Knight', '2008'), ('Mad Max: Fury Road', '2015');")
# modifying a single row in column
# cursor.execute("UPDATE movies4 SET movies_name='Iron Man' WHERE movies_name='The Dark Knight'")
# adding a single column
# cursor.execute("ALTER TABLE movies4 ADD COLUMN rating FLOAT")
# setting values in a row
cursor.execute("UPDATE movies4 SET rating=8.5 WHERE movies_name='Mad Max: Fury Road'")

connection.commit()
cursor.close()
connection.commit()
