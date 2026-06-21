import requests
import pandas as pd

API_KEY = "1af066d05f482c3934b943db1ab6ffaa"
url = f"https://api.themoviedb.org/3/movie/popular?api_key={API_KEY}"
respond = requests.get(url)
movie = respond.json()["results"]
df = pd.DataFrame(movie)
print(df.head())
df.to_csv("raw_movies.csv", index=False)
