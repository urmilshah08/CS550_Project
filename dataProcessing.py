import pandas as pd, numpy as np
# from surprise import SVD
# from surprise import Dataset
ratings = pd.read_csv('ratings.csv')
movies = pd.read_csv('movies.csv')

pivotRatings = pd.pivot_table(ratings, values='rating', index='movieId', columns='userId')

pivotRatings.to_csv('userVsMovie.csv')
