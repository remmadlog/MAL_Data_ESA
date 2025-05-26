"""
In this file we will investigate the MAL dataset using clustering methods.

Plan and deviation:
- Use 'selection_arranged_union.csv'
    - VERY WEAK silhouette score for KMeans (n_cluster = 2, score = 0.17)
- Use 'selection_arranged_intersection.csv'
    - WEAK silhouette score for KMeans (n_cluster = 2, score = 0.31)

I intend to consider the whole data set too, but will probably drop `on_list` for that.
    - After changing 'ml_table_creation.py' we now can use 'training_full_set.csv'
        - Still a WEAK silhouette score for KMeans (n_cluster = 2, score = 0.41)
"""
# note for myself regarding comment colors in pycharm using better comments
# # # orange
#? blue
#! red
#. purple
#: green
#, blueish
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
"""Import"""
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
import pandas as pd
import numpy as np

# for splitting a DF into training and testing
from sklearn.model_selection import train_test_split

# for scaling
from sklearn.preprocessing import StandardScaler

# for clustering
from sklearn.cluster import KMeans

# for scoring
from sklearn.metrics import silhouette_score


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
"""Loading"""
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# Loading file with selected features (fs)
# df_fs = pd.read_csv("xlsx_tables/training_score/selection_arranged_intersection.csv").fillna(0)
df_partial_fs = pd.read_csv("xlsx_tables/training_score/selection_arranged_union.csv").fillna(0)


# considering the main table
df_full_no_fs = pd.read_csv("xlsx_tables/training_full_set.csv").fillna(0)

# reduce features in df_full_no_fs
# ! feature selection by hand -- maybe do smth. similar as in 'ml_fs_score_prediction.py' -> model training, clustering....
df_full_fs = df_full_no_fs[
    ["anime_id", "season_fall", "season_spring", "season_summer", "season_winter", "year", "score", "rank", "episodes", "duration"]
    + ["anime_type_0","anime_type_CM","anime_type_Movie","anime_type_Music","anime_type_ONA","anime_type_OVA","anime_type_PV","anime_type_Special","anime_type_TV","anime_type_TV Special"]
    + ["source_4-koma manga","source_Book","source_Card game","source_Game","source_Light novel","source_Manga","source_Mixed media","source_Music","source_Novel","source_Original","source_Other","source_Picture book","source_Radio","source_Unknown","source_Visual novel","source_Web manga","source_Web novel"]
    + ["rating_G - All Ages","rating_PG - Children","rating_PG-13 - Teens 13 or older","rating_R - 17+ (violence & profanity)","rating_R+ - Mild Nudity","rating_Rx - Hentai"]
]

# considered dataset
df = df_full_fs.copy()
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
"""Preparations"""
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
def data_preparation(df):
    # We start with a smaller dataset
    df_temp = df.copy()

    # X features
    X = df_temp
    #: We do not need y, we do NOT have a TARGET
    y = X

    # splitting in test and trainings data (10% test data)
    X_train_id, X_test_id, y_train_id, y_test_id, = train_test_split(
        X,          # split the feature set
        y,                 # split the target set
        test_size=0.1,     # get 10% as text data
        random_state=42    # split random but repeatable
    )

    # kept anime_id till now, needs to be removed!
    X_train = X_train_id.drop(["anime_id"], axis=1)
    X_test = X_test_id.drop(["anime_id"], axis=1)
    y_train = y_train_id.drop(["anime_id"], axis=1)
    y_test = y_test_id.drop(["anime_id"], axis=1)


    # Instantiate StandardScaler
    scaler = StandardScaler()

    # scale training data.
    X_train_scaled = scaler.fit_transform(X_train)

    # scale test data.
    X_test_scaled = scaler.transform(X_test)
    return

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
"""Functions"""
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# X: dataset -- as `DataFrame`
# range: range to test for n_clusters -- as `range`, `list`
def kmeans_tuning(X,range):
    fits = []
    scores = []

    for k in range:
        # using KMeans for `k` clusters
        model = KMeans(n_clusters = k, random_state = 42, n_init='auto')
        model.fit(X)

        # append the model to fits
        fits.append(model)

        # evaluate using silhouette_score
        scores.append(silhouette_score(X, model.labels_, metric='euclidean', random_state = 42))

    top_score = max(scores)
    top_model = fits[(scores.index(top_score))]

    return top_model, top_score, range[scores.index(top_score)]

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
"""Using KMeans"""
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

# get best scored model
model , score, n_cluster = kmeans_tuning(X_train_scaled,range(2,25))

print("for ", n_cluster, "clusters, we score: ", score)






#?  Maybe make functions for everything, so we can use them for different files and stuff














