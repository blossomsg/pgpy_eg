"""https://medium.com/@patrikstrausz17/part3-postgresql-relationships-creating-and-managing-database-relationships-5e1eaea769d8
One to One relationship
"""

import psycopg2

connection = psycopg2.connect(host="localhost", dbname="postgres", user="postgres", password="123456789", port="5432")

cursor = connection.cursor()

cursor.execute("DROP TABLE IF EXISTS movies5, movies5_budgets")
cursor.execute("CREATE TABLE movies5(id SERIAL PRIMARY KEY, name VARCHAR(250) NOT NULL, date INTEGER)")
cursor.execute("INSERT INTO movies5(name, date) VALUES ('The Matrix', '1999'), ('Batman Begins', '2005'), ('Blade Runner','1982'), ('The Dark Knight','2008'), ('The Dark Knight Rises','2012'), ('The Hunger Games','2012')")

cursor.execute("CREATE TABLE movies5_budgets(movie_budget_id SERIAL, movie_budget_in_usd INTEGER, movie_id INTEGER UNIQUE, CONSTRAINT fk_movie_id FOREIGN KEY(movie_id) REFERENCES movies5(id))")
cursor.execute("INSERT INTO movies5_budgets(movie_budget_in_usd, movie_id) VALUES ('63000000', '1'), ('150000000', '2'), ('28000000', '3'), ('185000000', '4'), ('250000000', '5'), ('78000000', '6')")
cursor.execute("SELECT * FROM movies5 JOIN movies5_budgets ON movies5.id = movies5_budgets.movie_id WHERE movies5_budgets.movie_budget_in_usd = (SELECT MAX(movies5_budgets.movie_budget_in_usd) FROM movies5_budgets)")
print(cursor.fetchone())

connection.commit()
cursor.close()
connection.close()