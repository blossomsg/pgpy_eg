"""Inserting data directly from csv file to db.
Inserting single column from csv to db with the
help of temporary table."""
import psycopg2

connection = psycopg2.connect(host="localhost", dbname="postgres", user="postgres", password="123456789", port="5432")

cursor = connection.cursor()

cursor.execute("DROP TABLE IF EXISTS movies2_temp")
cursor.execute("CREATE TEMPORARY TABLE movies2_temp(movies_id SERIAL PRIMARY KEY, name VARCHAR(250) NOT NULL, col_01 TEXT NOT NULL, col_02 TEXT NOT NULL, col_03 TEXT NOT NULL, col_04 TEXT NOT NULL, col_05 TEXT NOT NULL, col_06 TEXT NOT NULL, col_07 TEXT NOT NULL, col_08 TEXT NOT NULL, col_09 TEXT NOT NULL, col_10 TEXT)")
cursor.execute("COPY movies2_temp(name,col_01,col_02,col_03,col_04,col_05,col_06,col_07,col_08,col_09) FROM 'F:\\All_Projs\\Python_Proj\\code_practise\\db_grow\\1_movies_per_genre\\Action.csv' WITH (FORMAT CSV, HEADER)")
cursor.execute("DROP TABLE IF EXISTS movies2")
cursor.execute("CREATE TABLE movies2(movies_id SERIAL PRIMARY KEY, name VARCHAR(250) NOT NULL)")
cursor.execute("INSERT INTO movies2(name) SELECT name FROM movies2_temp")

connection.commit()
cursor.close()
connection.close()
