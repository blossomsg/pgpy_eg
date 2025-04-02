"""Creating new db altogether - movies3"""
import psycopg2


connection = psycopg2.connect(host="localhost", dbname="movies3", user="postgres", password="123456789", port="5432")

cursor = connection.cursor()

cursor.execute("DROP TABLE IF EXISTS movies3")
cursor.execute("CREATE TABLE movies3(movies_id SERIAL PRIMARY KEY, movies_name VARCHAR(50) NOT NULL)")

connection.commit()
cursor.close()
connection.close()