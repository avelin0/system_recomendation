import pandas as pd
import numpy as np

r_cols = ['userId', 'movieId', 'rating']
#ratings = pd.read_csv('e:/sundog-consult/udemy/datascience/ml-100k/u.data', sep='\t', names=r_cols, usecols=range(3), encoding="ISO-8859-1")
ratings = pd.read_csv('ml-latest-small/ratings.csv', sep=',', names=r_cols, usecols=range(3), encoding="ISO-8859-1", header=None, skiprows=1)
#ratings = pd.read_csv('ml-1m/ratings.dat', sep='::', names=r_cols, usecols=range(3), encoding="ISO-8859-1", header=None, skiprows=1)
#ratings = pd.read_csv('ml-10M100K/ratings.dat', sep='::', names=r_cols, usecols=range(3), encoding="ISO-8859-1", header=None, skiprows=1)

m_cols = ['movieId', 'title','genres']
#movies = pd.read_csv('e:/sundog-consult/udemy/datascience/ml-100k/u.item', sep='|', names=m_cols, usecols=range(2), encoding="ISO-8859-1")
movies = pd.read_csv('ml-latest-small/movies.csv', sep=',', names=m_cols, usecols=range(3), encoding="ISO-8859-1", header=None, skiprows=1)
#movies = pd.read_csv('ml-1m/movies.dat', sep='::', names=m_cols, usecols=range(3), encoding="ISO-8859-1", header=None, skiprows=1)
#movies = pd.read_csv('ml-10M100K/movies.dat', sep='::', names=m_cols, usecols=range(3), encoding="ISO-8859-1", header=None, skiprows=1)

movies['genres'] = movies['genres'].apply(lambda x: x.split('|'))
ratings = pd.merge(movies, ratings)
#ratings.head()
#print(ratings.head())
ratings['rating'] = ratings['rating'].map(float)
userRatings = ratings.pivot_table(index=['userId'],columns=['title'],values='rating', aggfunc='first',fill_value=float('nan'))

# mostrar o que o usuario escolhido curtiu
myUserRatings = userRatings.loc[643].dropna()
print(myUserRatings);


corrMatrix = userRatings.corr(method='spearman', min_periods=100)
#print(corrMatrix.head())

simCandidates = pd.Series()
for i in range(0, len(myUserRatings.index)):
    #print ("Adding simimlarities for " + userRatings.index[i] + "...")
    # Retrieve similar movies to this one that I rated
    sims = corrMatrix[myUserRatings.index[i]].dropna()
    # Now scale its similarity by how well I rated this movie
    sims = sims.map(lambda x: x * myUserRatings[i])
    # Add the score to the list of similarity candidates
    simCandidates = simCandidates.append(sims)
    
simCandidates.sort_values(inplace = True, ascending = False)
simCandidates = simCandidates.groupby(simCandidates.index).sum()
simCandidates.sort_values(inplace = True, ascending = False)
#print(myUserRatings.index)
filteredSims = simCandidates.drop(myUserRatings.index, errors = 'ignore')

print("Sugestões")
print (filteredSims.head(10))