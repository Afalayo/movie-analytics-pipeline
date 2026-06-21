import pandas as pd
import sqlite3 

print("TOP RATED MOVIES")

conn = sqlite3.connect("movies.db")

query = """
SELECT
    title,
    release_year,
    vote_average
FROM movies
ORDER BY vote_average DESC
LIMIT 10
"""

df = pd.read_sql(query, conn)

print(df)






print("MOST POPULAR MOVIES")

conn = sqlite3.connect("movies.db")

query = """
SELECT
    title,
    popularity
FROM movies
ORDER BY popularity DESC
LIMIT 10
"""

df = pd.read_sql(query, conn)

print(df)




print("YEARLY MOVIE TREND")

conn = sqlite3.connect("movies.db")

query = """
SELECT
    release_year,
    COUNT(*) AS movie_count
FROM movies
GROUP BY release_year
ORDER BY release_year DESC
LIMIT 10
"""

df = pd.read_sql(query, conn)

print(df)
