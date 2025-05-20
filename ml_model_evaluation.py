# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
"""Import"""
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
import pandas as pd
import numpy as np

# for splitting a DF into training and testing
from sklearn.model_selection import train_test_split

# for scaling
from sklearn.preprocessing import StandardScaler

# for evaluating
from sklearn.metrics import mean_squared_error, r2_score, mean_absolute_error

# Save and Load models using pickle
import pickle

# for calculating confidence interval
import scipy.stats as stats

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
df_predictions = pd.read_csv("xlsx_tables/training_score/predictions.csv")

# removing index to avoid mismatching
df_id = df_predictions["anime_id"].to_frame().reset_index(drop=True)
df_score = df_predictions["og_score"].to_frame().reset_index(drop=True)
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
"""Evaluating , Scoring and Combining"""
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

# Model combination by considering the average
df_mean = df_predictions["LinReg_score"]
for entry in ["MLP_score", "Tree_score", "Forest_score", "GradBoost_score", "ElNet_score", "SVR_score", "XGB_score"]:
    df_mean = df_mean + df_predictions[entry]
df_mean = df_mean/8


# Model combination by considering the r2 weighted mean
# wights (r2 scores) obtained during CV in gridsearch
df_biased_mean = (0.72*df_predictions["MLP_score"] + 0.65*df_predictions["Tree_score"]
                  + 0.7*df_predictions["Forest_score"] + 0.76*df_predictions["GradBoost_score"]
                  + 0.65*df_predictions["ElNet_score"] + 0.69*df_predictions["SVR_score"]
                  + 0.78*df_predictions["XGB_score"])/(0.72+0.65+0.7+0.76+0.65+0.69+0.78)


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#! col for model errors:
col_model_error = [
    "LinReg_error", "MLP_error", "Tree_error", "Forest_error",
    "GradBoost_error", "ElNet_error", "SVR_error", "XGB_error",
    "CombMean_error", "CombBiased_error"]

# create an error table
df_compare = pd.concat([
    df_id,
    df_score,
    df_predictions["LinReg_score"] - df_predictions["og_score"],
    df_predictions["MLP_score"] - df_predictions["og_score"],
    df_predictions["Tree_score"] - df_predictions["og_score"],
    df_predictions["Forest_score"] - df_predictions["og_score"],
    df_predictions["GradBoost_score"] - df_predictions["og_score"],
    df_predictions["ElNet_score"] - df_predictions["og_score"],
    df_predictions["SVR_score"] - df_predictions["og_score"],
    df_predictions["XGB_score"] - df_predictions["og_score"],
    df_mean - df_predictions["og_score"],
    df_biased_mean - df_predictions["og_score"]
], axis=1, ignore_index=True
)
df_compare.columns = ["anime_id", "og_score"] + col_model_error


# statistic evaluation as lists
col_mae         = round(df_compare[col_model_error].abs().mean(),3).to_list()
col_r2          = [0.64, 0.74, 0.67, 0.71, 0.78, 0.64, 0.71, 0.79] + [0,0]     #! + [0s for every additional comb_model] -- FOR NOW
col_mse         = round((df_compare[col_model_error]*df_compare[col_model_error]).mean(),3).to_list()
col_rmse        = np.around(np.sqrt(col_mse),3).tolist()
col_median      = round(df_compare[col_model_error],3).median().to_list()
col_abs_median  = round(df_compare[col_model_error],3).abs().median().to_list()
col_abs_min     = round(df_compare[col_model_error],3).abs().min().to_list()
col_abs_max     = round(df_compare[col_model_error],3).abs().max().to_list()



# percentage of error smaller/larger than q
col_01 = []
col_02 = []
col_03 = []
col_geq05 = []
for entry in col_model_error:
    dl = df_compare[df_compare[entry].abs() <= 0.1][entry].to_list()
    percentage = len(dl)/len(df_compare[entry])
    col_01.append(round(percentage,3))

    dl = df_compare[df_compare[entry].abs() <= 0.2][entry].to_list()
    percentage = len(dl)/len(df_compare[entry])
    col_02.append(round(percentage,3))

    dl = df_compare[df_compare[entry].abs() <= 0.3][entry].to_list()
    percentage = len(dl)/len(df_compare[entry])
    col_03.append(round(percentage,3))

    dl = df_compare[df_compare[entry].abs() > 0.5][entry].to_list()
    percentage = len(dl)/len(df_compare[entry])
    col_geq05.append(round(percentage,3))



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# creating table with statistic evaluations
df_stats = pd.DataFrame({
    "MAE":col_mae,
    "r2":col_r2,
    "MSE":col_mse,
    "RMSE":col_rmse,
    "Median":col_median,
    "abs median":col_abs_median,
    "abs min":col_abs_min,
    "abs max":col_abs_max,
    "% error < 0.1":col_01,
    "% error < 0.2":col_02,
    "% error < 0.3":col_03,
    "% error > 0.5":col_geq05
})

# just printing the table, so it can be used in notes_ml_model_evaluation.md
print(df_stats.to_markdown(index=False))
