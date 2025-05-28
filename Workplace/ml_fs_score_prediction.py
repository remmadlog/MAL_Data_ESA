"""
In ml_table_creation.py we created a csv that shell be used for score prediction
The problem:
- we have way to many features
The solution:
- consider feature selection
- - I have never done this before so this might end badly

Idea:
- RreliefF Feature Scoring
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
from module_ml import *


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
"""Loading and preparing"""
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# open csv
df = pd.read_csv('created_files/training_partial_set_OnList.csv').fillna(0)

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
# # no need for anime_id, year, rank, score, or completed
features = df.columns.to_list()
features.remove("anime_id")
features.remove("year")
features.remove("rank")
features.remove("score")
features.remove("completed")

# defining target column name
target = ["score"]

# defining feature date
df_data = df[features].astype("float").fillna(0)
#defining target data
df_target = df[target].astype("float").fillna(0)
df_target = df_target["score"].astype("float")


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
"""Feature selection of loaded and prepared data.csv"""
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# set the amount of features to be considered (if possible)
k_best_features = 200

features_chi2 = fs_chi2(df_data,df_target,k_best_features)

features_anova = fs_f_classif(df_data,df_target,k_best_features)

features_cor_val = fs_correlation(df_data,df_target,k_best_features)

features_variance = fs_variance(df_data,threshold = 0.0025)


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#" presenting results obtained in orange
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

# open Rank file
df_rank = pd.read_excel('created_files/ml_orange_feature_rank.xlsx').fillna(0)
# cleaning first two rows
df_rank = df_rank.drop([0, 1])
# convert string_number to number
df_rank["Univar. reg."] = df_rank["Univar. reg."].astype("float")
df_rank["RReliefF"] = df_rank["RReliefF"].astype("float")


# get top features by Univar. reg.
features_univar = df_rank.sort_values("Univar. reg.", ascending=False)[:k_best_features]["Feature"].to_list()
# get top features by 'RReliefF'
features_rrelieff = df_rank.sort_values("RReliefF", ascending=False)[:k_best_features]["Feature"].to_list()


# open Random Tree file
df_rt = pd.read_excel('created_files/ml_orange_feature_score_RandromTree.xlsx').fillna(0)
# convert string_number to number
df_rt["Mean"] = df_rt["Mean"].astype("float")
df_rt["Std"] = df_rt["Std"].astype("float")

# get top 100 features by R2 Mean
features_tree_r2_mean = df_rt.sort_values("Mean", ascending=False)["Feature"][:k_best_features].to_list()


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
"""Processing lists by combining and or intersecting"""
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


Since I have not much experience regarding this, I do not know how many features are to many.
Therefore, I will consider different approaches. 
- Intersection of all feature selections
- Union of all feature selections
- Reduced union of all feature selections
- Combination of the above
Maybe I also go with:
- Usage of each feature selection separately
"""
# take an intersection
features_intersection = set(features_chi2) & set(features_anova) & set(features_cor_val) & set(features_variance) & set(features_univar) & set(features_rrelieff) & set(features_tree_r2_mean)
features_intersection = list(features_intersection)
print("Feature Amount Intersection:      ", len(features_intersection))

# take all of each and combine them
features_union_full = list(set(features_chi2+features_anova+features_cor_val+features_variance+features_univar+features_rrelieff+features_tree_r2_mean))
print("Feature Amount Union:      ", len(features_union_full))

# take half
k = int(round(k_best_features/2,0))
features_union_half = list(set(features_chi2[:k]+features_anova[:k]+features_cor_val[:k]+features_univar[:k]+features_rrelieff[:k]+features_tree_r2_mean[:k]))
print("Feature Amount Union Half:      ", len(features_union_half))

# take quarter
k = int(round(k_best_features/4,0))
features_union_quarter = list(set(features_chi2[:k]+features_anova[:k]+features_cor_val[:k]+features_univar[:k]+features_rrelieff[:k]+features_tree_r2_mean[:k]))
print("Feature Amount Union Quarter:      ", len(features_union_quarter))

# combination: intersection \cap union_full
features_comb_full = list(set(features_intersection)&set(features_union_full))
print("Feature Amount Combination:      ", len(features_comb_full))

# combination: intersection \cap union_half
features_comb_half = list(set(features_intersection)&set(features_union_half)&set(features_variance))
print("Feature Amount Combination Half:      ", len(features_comb_half))

# combination: intersection \cap union_quarter
features_comb_quarter = list(set(features_intersection)&set(features_union_quarter)&set(features_variance))
print("Feature Amount Combination Quarter:      ", len(features_comb_quarter))

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# creating tables using the established features
training_score_features_intersection = df[["anime_id"] + features_intersection + ["score"]]
training_score_features_union_full = df[["anime_id"] + features_union_full + ["score"]]
training_score_features_union_half = df[["anime_id"] + features_union_half + ["score"]]
training_score_features_union_quarter = df[["anime_id"] + features_union_quarter + ["score"]]
training_score_features_combination_full = df[["anime_id"] + features_comb_full + ["score"]]
training_score_features_combination_half = df[["anime_id"] + features_comb_half + ["score"]]
training_score_features_combination_quarter = df[["anime_id"] + features_comb_quarter + ["score"]]

training_score_features_chi2 = df[["anime_id"] + features_chi2 + ["score"]]
training_score_features_anova = df[["anime_id"] + features_anova + ["score"]]
training_score_features_cor_val = df[["anime_id"] + features_cor_val + ["score"]]
training_score_features_variance = df[["anime_id"] + features_variance + ["score"]]
training_score_features_univar = df[["anime_id"] + features_univar + ["score"]]
training_score_features_rrelieff = df[["anime_id"] + features_rrelieff + ["score"]]
training_score_features_tree_r2_mean = df[["anime_id"] + features_tree_r2_mean + ["score"]]

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# saving everything as CSV (it is faster this way and good enough)
training_score_features_chi2.to_csv("created_files/training_score/selection_pure_chi2.csv", index=False)
training_score_features_anova.to_csv("created_files/training_score/selection_pure_anova.csv", index=False)
training_score_features_cor_val.to_csv("created_files/training_score/selection_pure_corval.csv", index=False)
training_score_features_variance.to_csv("created_files/training_score/selection_pure_var.csv", index=False)
training_score_features_univar.to_csv("created_files/training_score/selection_pure_univar.csv", index=False)
training_score_features_rrelieff.to_csv("created_files/training_score/selection_pure_rrelieff.csv", index=False)
training_score_features_tree_r2_mean.to_csv("created_files/training_score/selection_pure_tree.csv", index=False)

training_score_features_intersection.to_csv("created_files/training_score/selection_arranged_intersection.csv", index=False)
training_score_features_union_full.to_csv("created_files/training_score/selection_arranged_union.csv", index=False)
training_score_features_union_half.to_csv("created_files/training_score/selection_arranged_union2.csv", index=False)
training_score_features_union_quarter.to_csv("created_files/training_score/selection_arranged_union4.csv", index=False)
training_score_features_combination_full.to_csv("created_files/training_score/selection_arranged_comb.csv", index=False)
training_score_features_combination_half.to_csv("created_files/training_score/selection_arranged_comb2.csv", index=False)
training_score_features_combination_quarter.to_csv("created_files/training_score/selection_arranged_comb4.csv", index=False)

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

