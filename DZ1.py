import pandas as pd

# Чтение датасета
df = pd.read_csv('/workspaces/Introduction_Python_MGIMO/netflix_titles.csv')

# 1) Чего больше, фильмов или ТВ шоу
movie_count = len(df[df['type'] == 'Movie'])
show_count = len(df[df['type'] == 'TV Show'])
if movie_count > show_count:
  print("Больше фильмов")
else:
  print("Больше ТВ шоу")

# 2) Фильмов какого года больше всего
year_counts = df['release_year'].value_counts()
print("Фильмов больше всего в году: ", year_counts.idxmax())

# 3) Проверить есть ли в датасете фильмы России и Германии
russia_movies = df[df['country'] == 'Russia']
germany_movies = df[df['country'] == 'Germany']
print("Есть ли фильмы России: ", not russia_movies.empty)
print("Есть ли фильмы Германии: ", not germany_movies.empty)
