# WIP
"""
In this file we want to start with the modeling and figuring out what model or model combinations works well and what feature set is suitable.
Models I want to use
- Linear Regression
- Neuronal Network
- Decision Tree
- Random Forest
- Assembled Learning
Maybe use Classification modules too (target classification needed for that)
- Multinomial Logistic Regression (MLR)
- KNN
- Support Vector Machine (SVM)
- Assembled Learning
"""

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
"""Import"""
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
import pandas as pd
import csv

# for splitting a DF into training and testing
from sklearn.model_selection import train_test_split

# for scaling
from sklearn.preprocessing import StandardScaler

# for evaluating
from sklearn.metrics import mean_squared_error, r2_score, mean_absolute_error


# Save and Load models using pickle
import pickle
"""
# save
with open('model.pkl','wb') as f:
    pickle.dump(model,f)
# load
with open('model.pkl', 'rb') as f:
    model = pickle.load(f)
# using
model.predict(X[0:1])
"""
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
"""Defining usefully, but non-essential Functions"""
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

# get evaluations a list
def get_scores(y_test, y_pred):
    # # r^2
    r2 = r2_score(y_test, y_pred)

    # # mean absolut error (MAE)
    mae = mean_absolute_error(y_test, y_pred)

    # # mean squared error (MSE)
    mse = mean_squared_error(y_test, y_pred)

    # # root mean squared error (RMSE)
    rmse = mse ** 0.5

    # print("     r2  : ", r2)
    # print("     mae : ", mae)
    # print("     mse : ", mse)
    # print("     rmse: ", rmse)
    return [r2,mae,mse,rmse]


# print evaluations
def print_scores(y_test, y_pred):
    # # r^2
    r2 = r2_score(y_test, y_pred)

    # # mean absolut error (MAE)
    mae = mean_absolute_error(y_test, y_pred)

    # # mean squared error (MSE)
    mse = mean_squared_error(y_test, y_pred)

    # # root mean squared error (RMSE)
    rmse = mse ** 0.5

    print("     r2  : ", r2)
    print("     mae : ", mae)
    print("     mse : ", mse)
    print("     rmse: ", rmse)



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
"""Loading Data"""
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# df_comb = pd.read_csv("xlsx_tables/training_score/selection_arranged_comb.csv").fillna(0)
# df_comb2 = pd.read_csv("xlsx_tables/training_score/selection_arranged_comb2.csv").fillna(0)
# df_comb4 = pd.read_csv("xlsx_tables/training_score/selection_arranged_comb4.csv").fillna(0)
# df_inter = pd.read_csv("xlsx_tables/training_score/selection_arranged_intersection.csv").fillna(0)
df_union = pd.read_csv("xlsx_tables/training_score/selection_arranged_union.csv").fillna(0)
# df_union2 = pd.read_csv("xlsx_tables/training_score/selection_arranged_union2.csv").fillna(0)
# df_union4 = pd.read_csv("xlsx_tables/training_score/selection_arranged_union4.csv").fillna(0)
# df_anova = pd.read_csv("xlsx_tables/training_score/selection_pure_anova.csv").fillna(0)
# df_chiw = pd.read_csv("xlsx_tables/training_score/selection_pure_chi2.csv").fillna(0)
# df_corval = pd.read_csv("xlsx_tables/training_score/selection_pure_corval.csv").fillna(0)
# df_rrff = pd.read_csv("xlsx_tables/training_score/selection_pure_rrelieff.csv").fillna(0)
# df_tree = pd.read_csv("xlsx_tables/training_score/selection_pure_tree.csv").fillna(0)
# df_univar = pd.read_csv("xlsx_tables/training_score/selection_pure_univar.csv").fillna(0)
# df_var = pd.read_csv("xlsx_tables/training_score/selection_pure_var.csv").fillna(0)

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
"""Preparations"""
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# We start with a smaller dataset
df_temp = df_union.copy()

# X features
X = df_temp.drop(["anime_id", "score"], axis=1).astype("float").fillna(0)
# y target
y = df_temp["score"].astype("float").fillna(0)

# splitting in test and trainings data (10% test data)
X_train, X_test, y_train, y_test, = train_test_split(
    X,          # split the feature set
    y,                 # split the target set
    test_size=0.1,     # get 10% as text data
    random_state=42    # split random but repeatable
)

# Instantiate StandardScaler
scaler = StandardScaler()

# scale training data.
X_train_scaled = scaler.fit_transform(X_train)

# scale test data.
X_test_scaled = scaler.transform(X_test)

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
"""Model Introductions"""
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
"""     Classify the target data"""
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# the target data y_ contains floats, just changing it to strings would probably not give good results
# we will round the target value and convert it to string afterward
y_test = y_test.round({"score": 1})
y_test = y_test.astype("str")

y_train = y_train.round({"score": 1})
y_train = y_train.astype("str")
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
"""         Multinomial Logistic Regression"""
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #




# # save
# with open('xlsx_tables/training_score/trained_models/NAME.pkl','wb') as f:
#     pickle.dump(model,f)
#
#
# print("NAME")
# # making predictions
# y_pred = model.predict(X_test)
# # print scores
# print_scores(y_test, y_pred)
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
"""         KNN"""
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
"""         Support Vector Machine (SVM)"""
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #