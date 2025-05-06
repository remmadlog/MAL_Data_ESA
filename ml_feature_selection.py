"""
In ml_table_creation.py we created a csv that shell be used for score prediction
The problem:
- we have way to many features
The solution:
- consider feature selection
- - I have never done this before so this might end badly

Idea:
- RreliefF Feature Scoring
- -
- Univariate Feature Selection
- - chi2
- - anova
- Correlation-based Feature Selection
- - influence on target
- Variance Thresholding
- - feature variance check (a constant feature is not a good feature)
- Random Forest + Feature Importance
"""

# importing
import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest   # importing additional libraries below

# open csv
dfml = pd.read_csv('xlsx_tables/training_score/training_score.csv').fillna(0)

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
"""
Columns:
- ['anime_id', 'theme_Adult Cast', 'theme_Anthropomorphic', 'theme_CGDCT', 'theme_Childcare', 'theme_Combat Sports', 'theme_Crossdressing', 'theme_Delinquents', 'theme_Detective', 'theme_Educational',
       ...
       'year', 'score', 'rank', 'episodes', 'duration', 'watching', 'completed', 'on_hold', 'dropped', 'plan_to_watch']
Target:
- score
Redundant
- rank, year
Additional removal
- remove("completed") 
- - since airing shows have 0 completions
"""

# getting features as list
# # no need for anime_id, year, rank, score
features = dfml.columns.to_list()
features.remove("anime_id")
features.remove("year")
features.remove("rank")
features.remove("score")
features.remove("completed")

# defining target column name
target = ["score"]

# defining feature date
dfml_data = dfml[features].astype("float").fillna(0)
#defining target data
dfml_target = dfml[target].astype("float").fillna(0)
# target data unknown value error -> transform to int
dfml_target = dfml_target["score"].astype("int")


# len of created features lists
# # NOT INCLUDED: features_variance (this is given by a threshold, not by length)
q = 200
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
"""Univariate Feature Selection"""
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
from sklearn.feature_selection import chi2

# get the 100 best features provided by chi2
k_best_features = q
selector = SelectKBest(score_func=chi2, k=k_best_features)
X_new = selector.fit_transform(dfml_data, dfml_target)

# ids of chosen features
selected_indices = selector.get_support(indices=True)

# get features as list
features_chi2 = []
for i in selected_indices:
    features_chi2.append(features[i])

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
from sklearn.feature_selection import f_classif

# get the 100 best features provided by ANOVA
k_best_features = q
selector = SelectKBest(score_func=f_classif, k=k_best_features)
X_new = selector.fit_transform(dfml_data, dfml_target)

# ids of chosen features
selected_indices = selector.get_support(indices=True)

# get features as list
features_anova = []
for i in selected_indices:
    features_anova.append(features[i])

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
"""Correlation-based Feature Selection"""
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# calculating corralation values
cor_val = dfml_data.apply(lambda feature: np.abs(np.corrcoef(feature, dfml_target)[0, 1]))

# getting some NaN || replace them with zero
cor_val = cor_val.fillna(0)

# sorting the values and extracting the top 100 features
# # sorting
cor_val = cor_val.sort_values(ascending=False)
# # extracting the features
features_cor_val = cor_val.index
# # only getting the top 100
features_cor_val = features_cor_val[:q].to_list()


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
"""Variance Thresholding"""
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
from sklearn.feature_selection import VarianceThreshold

# calculate variance for features
variance = dfml_data.var()

# set variation threshold || wanted to get as many features as we consider above
threshold = 0.0025

# performing variance thresholding using VarianceThreshold from sklearn.feature_selection
selector = VarianceThreshold(threshold=threshold)
dfml_data_selected = selector.fit_transform(dfml_data)

# get features as list
features_variance = dfml_data.columns[selector.get_support()].to_list()

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
"""presenting results obtained in orange"""
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
"""
ml_feature_selection.ows
- Load csv
- Deselect features as described above
- - Use Rank to get
- - - RreliefF score
- - - Univariate regression score
- - Save in ml_orange_feature_rank.xlsx
- - Use Random Forest (50 trees || R2 = 0.774 || MAE = 0.31)
- - - Consider Feature Importance
- - Save in ml_orange_feature_score_RandromTree.xlsx

Consider ml_orange_feature_rank.xlsx
- columns = 'Feature', 'Univar. reg.', 'RReliefF'
- first two rows:
- - 0 | string |    continuous |  continuous
- - 1 | meta   |    0          |  0

Consider ml_orange_feature_score_RandromTree.xlsx
- 
"""
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# open Rank file
df_rank = pd.read_excel('xlsx_tables/ml_orange_feature_rank.xlsx').fillna(0)
# cleaning first two rows
df_rank = df_rank.drop([0, 1])
# convert string_number to number
df_rank["Univar. reg."] = df_rank["Univar. reg."].astype("float")
df_rank["RReliefF"] = df_rank["RReliefF"].astype("float")


# get top 100 features by Univar. reg.
features_univar = df_rank.sort_values("Univar. reg.", ascending=False)[:q]["Feature"].to_list()
# get top 100 features by 'RReliefF'
features_rrelieff = df_rank.sort_values("RReliefF", ascending=False)[:q]["Feature"].to_list()

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# open Random Tree file
df_rt = pd.read_excel('xlsx_tables/ml_orange_feature_score_RandromTree.xlsx').fillna(0)
# convert string_number to number
df_rt["Mean"] = df_rt["Mean"].astype("float")
df_rt["Std"] = df_rt["Std"].astype("float")

# get top 100 features by R2 Mean
features_tree_r2_mean = df_rt.sort_values("Mean", ascending=False)["Feature"][:q].to_list()

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
"""
All feature lists
- features_chi2
- features_anova
- features_cor_val
- features_variance
- features_univar
- features_rrelieff
- features_tree_r2_mean
"""
# print(features_chi2)
# print(features_anova)
# print(features_cor_val)
# print(features_variance)
# print(features_univar)
# print(features_rrelieff)
# print(features_tree_r2_mean)
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

"""
Since I have not much experience regarding this, I do not know how many features are to many.
Therefore, I will consider different approaches. 
- Intersection of all feature selections
- Union of all feature selections
- Reduced union of all feature selections
- Combination of the above
Maybe I also go with:
- Usage of each feature selection separately?
"""
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

# take an intersection
features_intersection = set(features_chi2) & set(features_anova) & set(features_cor_val) & set(features_variance) & set(features_univar) & set(features_rrelieff) & set(features_tree_r2_mean)
features_intersection = list(features_intersection)
print("Feature Amount Intersection:      ", len(features_intersection))

# take all of each and combine them
features_union_full = list(set(features_chi2+features_anova+features_cor_val+features_variance+features_univar+features_rrelieff+features_tree_r2_mean))
print("Feature Amount Union:      ", len(features_union_full))

# take half
k = int(round(q/2,0))
features_union_half = list(set(features_chi2[:k]+features_anova[:k]+features_cor_val[:k]+features_variance[:k]+features_univar[:k]+features_rrelieff[:k]+features_tree_r2_mean[:k]))
print("Feature Amount Union Half:      ", len(features_union_half))

# take quarter
k = int(round(q/4,0))
features_union_quarter = list(set(features_chi2[:k]+features_anova[:k]+features_cor_val[:k]+features_variance[:k]+features_univar[:k]+features_rrelieff[:k]+features_tree_r2_mean[:k]))
print("Feature Amount Union Quarter:      ", len(features_union_quarter))

# combination: intersection \cap union_full
features_comb_full = list(set(features_intersection)&set(features_union_full))
print("Feature Amount Combination:      ", len(features_comb_full))

# combination: intersection \cap union_half
features_comb_half = list(set(features_intersection)&set(features_union_half))
print("Feature Amount Combination Half:      ", len(features_comb_half))

# combination: intersection \cap union_quarter
features_comb_quarter = list(set(features_intersection)&set(features_union_quarter))
print("Feature Amount Combination Quarter:      ", len(features_comb_quarter))

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# creating tables using the established features
training_score_features_intersection = dfml[["anime_id"] + features_intersection + ["score"]]
training_score_features_union_full = dfml[["anime_id"] + features_union_full + ["score"]]
training_score_features_union_half = dfml[["anime_id"] + features_union_half + ["score"]]
training_score_features_union_quarter = dfml[["anime_id"] + features_union_quarter + ["score"]]
training_score_features_combination_full = dfml[["anime_id"] + features_comb_full + ["score"]]
training_score_features_combination_half = dfml[["anime_id"] + features_comb_half + ["score"]]
training_score_features_combination_quarter = dfml[["anime_id"] + features_comb_quarter + ["score"]]

training_score_features_chi2 = dfml[["anime_id"] + features_chi2 + ["score"]]
training_score_features_anova = dfml[["anime_id"] + features_anova + ["score"]]
training_score_features_cor_val = dfml[["anime_id"] + features_cor_val + ["score"]]
training_score_features_variance = dfml[["anime_id"] + features_variance + ["score"]]
training_score_features_univar = dfml[["anime_id"] + features_univar + ["score"]]
training_score_features_rrelieff = dfml[["anime_id"] + features_rrelieff + ["score"]]
training_score_features_tree_r2_mean = dfml[["anime_id"] + features_tree_r2_mean + ["score"]]


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# saving everything as CSV (it is faster this way and good enough)
training_score_features_chi2.to_csv("xlsx_tables/training_score/selection_pure_chi2.csv", index=False)
training_score_features_anova.to_csv("xlsx_tables/training_score/selection_pure_anova.csv", index=False)
training_score_features_cor_val.to_csv("xlsx_tables/training_score/selection_pure_corval.csv", index=False)
training_score_features_variance.to_csv("xlsx_tables/training_score/selection_pure_var.csv", index=False)
training_score_features_univar.to_csv("xlsx_tables/training_score/selection_pure_univar.csv", index=False)
training_score_features_rrelieff.to_csv("xlsx_tables/training_score/selection_pure_rrelieff.csv", index=False)
training_score_features_tree_r2_mean.to_csv("xlsx_tables/training_score/selection_pure_tree.csv", index=False)

training_score_features_intersection.to_csv("xlsx_tables/training_score/selection_arranged_intersection.csv", index=False)
training_score_features_union_full.to_csv("xlsx_tables/training_score/selection_arranged_union.csv", index=False)
training_score_features_union_half.to_csv("xlsx_tables/training_score/selection_arranged_union2.csv", index=False)
training_score_features_union_quarter.to_csv("xlsx_tables/training_score/selection_arranged_union4.csv", index=False)
training_score_features_combination_full.to_csv("xlsx_tables/training_score/selection_arranged_comb.csv", index=False)
training_score_features_combination_half.to_csv("xlsx_tables/training_score/selection_arranged_comb2.csv", index=False)
training_score_features_combination_quarter.to_csv("xlsx_tables/training_score/selection_arranged_comb4.csv", index=False)

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

