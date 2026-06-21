import pandas as pd
import matplotlib.pyplot as plt
import sqlite3

conn = sqlite3.connect("movies.db")

query = """ 
    SELECT 
       release_year,
       COUNT(*) AS movie_count
    FROM movies 
    GROUP BY release_year
    ORDER BY release_year
    """


df = pd.read_sql(query, conn)

plt.plot(
	df["release_year"],
	df["movie_count"]
	)

plt.xlabel("Year")
plt.ylabel("Number of Movies")
plt.title("Movies Released Each Year")



plt.show()
