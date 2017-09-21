import pandas as pd
import numpy as np

r_cols = ['userId', 'movieId', 'rating']
#ratings = pd.read_csv('e:/sundog-consult/udemy/datascience/ml-100k/u.data', sep='\t', names=r_cols, usecols=range(3), encoding="ISO-8859-1")
#ratings = pd.read_csv('ml-latest-small/ratings.csv', sep=',', names=r_cols, usecols=range(3), encoding="ISO-8859-1", header=None, skiprows=1)
ratings = pd.read_csv('ml-1m/ratings.dat', sep='::', names=r_cols, usecols=range(3), encoding="ISO-8859-1", header=None, skiprows=1)
#ratings = pd.read_csv('ml-10M100K/ratings.dat', sep='::', names=r_cols, usecols=range(3), encoding="ISO-8859-1", header=None, skiprows=1)

m_cols = ['movieId', 'title','genres']
#movies = pd.read_csv('e:/sundog-consult/udemy/datascience/ml-100k/u.item', sep='|', names=m_cols, usecols=range(2), encoding="ISO-8859-1")
#movies = pd.read_csv('ml-latest-small/movies.csv', sep=',', names=m_cols, usecols=range(3), encoding="ISO-8859-1", header=None, skiprows=1)
movies = pd.read_csv('ml-1m/movies.dat', sep='::', names=m_cols, usecols=range(3), encoding="ISO-8859-1", header=None, skiprows=1)
#movies = pd.read_csv('ml-10M100K/movies.dat', sep='::', names=m_cols, usecols=range(3), encoding="ISO-8859-1", header=None, skiprows=1)

movies['genres'] = movies['genres'].apply(lambda x: x.split('|'))
ratings = pd.merge(movies, ratings)
#ratings.head()
#print(ratings.head())
ratings['rating'] = ratings['rating'].map(float)
#print(ratings.applymap(type).drop_duplicates())
#movieRatings = ratings.pivot_table(index=['userId'],columns=['title'],values='rating', aggfunc='first',fill_value=float('nan'))
movieRatings = ratings.pivot_table(index=['userId'],columns=['title'],values='rating', aggfunc='first',fill_value=float('nan'))
#movieRatings = ratings.pivot_table(index=['movieId'],columns=['title'],values=['rating', 'genres'], aggfunc='first')
#movieRatings.head()
#print(movieRatings.head())
#print(movieRatings.map(type).unique())

starWarsRatings = movieRatings['Star Wars: Episode IV - A New Hope (1977)'].map(float)
#starWarsRatings = movieRatings['Star Wars: Episode VII - The Force Awakens (2015)'].map(float)
#starWarsRatings = movieRatings['Iron Man (2008)'].map(float)

similarMovies = movieRatings.corrwith(starWarsRatings)
similarMovies = similarMovies.dropna()
similarMovies = similarMovies.sort_values(ascending=False)

df = pd.DataFrame(similarMovies)
#print(df.head(100))

movieStats = ratings.groupby('title').agg({'rating': [np.size, np.mean]})
#movieStats.head()
popularMovies = movieStats['rating']['size'] >= 500
movieStats[popularMovies].sort_values([('rating', 'mean')], ascending=False)[:15]
df = movieStats[popularMovies].join(pd.DataFrame(similarMovies, columns=['similarity']))
df = df.sort_values(['similarity'], ascending=False)
print(df.head(15))