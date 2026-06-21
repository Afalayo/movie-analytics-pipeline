import pandas as pd

df = pd.read_csv("raw_movies.csv")
df = df[
       [ "id",
         "title",
         "release_date",
         "vote_average",
         "popularity"
       ]
    ]
df["release_year"] = pd.to_datetime(df["release_date"]).dt.year
df = df.drop_duplicates()
df.to_csv("clean_movies.csv", index=False)

print(df.head())