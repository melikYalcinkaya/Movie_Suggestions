import pandas as pd
import numpy as np
from main import movies_df, ratings_df
from mlxtend.frequent_patterns import fpgrowth
from mlxtend.frequent_patterns import association_rules


# making user-movie matrix
user_movie_matrix = ratings_df[ratings_df['movieId'].isin(movies_df['movieId'])] \
                    .pivot_table(index='userId', columns='movieId', values='rating', fill_value=0)

# I marked True for movies watched and False for movies not watched
user_movie_matrix = user_movie_matrix.apply(lambda col: col.map(lambda x: True if x > 0 else False))
user_movie_matrix.to_csv("user_movie_matrix.csv")

# user-movie matrix
user_movie_matrix = pd.read_csv("user_movie_matrix.csv", index_col=0)

#minimum support value
minsupport = 0.10

#I use the FP growth algorithm to find frequent itemsets.
frequent_itemsets = fpgrowth(user_movie_matrix, min_support=minsupport, use_colnames=True)

#minimum confidence
min_confidence = 0.10

#association rules
rules = association_rules(frequent_itemsets, metric="confidence", min_threshold=min_confidence)
