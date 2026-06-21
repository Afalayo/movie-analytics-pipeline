import pandas as pd
from sqlalchemy import create_engine 

engine = create_engine("sqlite:///movies.db")
df = pd.read_csv("clean_movies.csv")

df.to_sql("movies",
	       engine,
	       if_exists="replace",
	       index=False
	       )

print("Loaded!")