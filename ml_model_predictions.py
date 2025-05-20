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
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
"""Import"""
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
import pandas as pd

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
X = df_temp.drop(["score"], axis=1).astype("float").fillna(0)
# y target
y = df_temp[["anime_id","score"]].astype("float").fillna(0)

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

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
"""Model loading and application"""
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
"""         Linear Regression"""
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# load model
with open('xlsx_tables/training_score/trained_models/LinearRegression.pkl', 'rb') as f:
    model = pickle.load(f)

# print name and scores
print("LinearRegression")
# making predictions
y_pred_LR = model.predict(X_test_scaled)
# print scores
print_scores(y_test, y_pred_LR)


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
"""         Neuronal Network"""
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# load model
with open('xlsx_tables/training_score/trained_models/MLPRegressor.pkl', 'rb') as f:
    model = pickle.load(f)

# print name and scores
print("MLPRegressor")
# making predictions
y_pred_MLP = model.predict(X_test_scaled)
# print scores
print_scores(y_test, y_pred_MLP)


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
"""         Decision Tree"""
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# load model
with open('xlsx_tables/training_score/trained_models/DecisionTreeRegressor.pkl', 'rb') as f:
    model = pickle.load(f)

# print name and scores
print("DecisionTreeRegressor")
# making predictions
y_pred_tree = model.predict(X_test)
# print scores
print_scores(y_test, y_pred_tree)


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
"""         Random Forest"""
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# load model
with open('xlsx_tables/training_score/trained_models/RandomForestRegressor.pkl', 'rb') as f:
    model = pickle.load(f)

# print name and scores
print("RandomForestRegressor")
# making predictions
y_pred_forest = model.predict(X_test)
# print scores
print_scores(y_test, y_pred_forest)


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
"""         Gradient Boosting"""
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# load model
with open('xlsx_tables/training_score/trained_models/GradientBoostingRegressor.pkl', 'rb') as f:
    model = pickle.load(f)

# print name and scores
print("GradientBoostingRegressor")
# making predictions
y_pred_gradboost = model.predict(X_test_scaled)
# print scores
print_scores(y_test, y_pred_gradboost)


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
"""         Elastic Net"""
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# load model
with open('xlsx_tables/training_score/trained_models/ElasticNet.pkl', 'rb') as f:
    model = pickle.load(f)

# print name and scores
print("ElasticNet")
# making predictions
y_pred_elnet = model.predict(X_test_scaled)
# print scores
print_scores(y_test, y_pred_elnet)


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
"""         Support Vector Regression"""
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# load model
with open('xlsx_tables/training_score/trained_models/SVR.pkl', 'rb') as f:
    model = pickle.load(f)

# print name and scores
print("SVR")
# making predictions
y_pred_svr = model.predict(X_test_scaled)
# print scores
print_scores(y_test, y_pred_svr)


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
"""         XGB"""
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# load model
with open('xlsx_tables/training_score/trained_models/XGB.pkl', 'rb') as f:
    model = pickle.load(f)

# print name and scores
print("XGB")
# making predictions
y_pred_xgb = model.predict(X_test_scaled)
# print scores
print_scores(y_test, y_pred_xgb)


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
"""Creating a table"""
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# define anime_id col
df_id = y_test_id["anime_id"].astype("int")
df_id = df_id.astype("str").reset_index(drop=True)

# reset the index so concat works probably
df_score = y_test_id["score"].reset_index(drop=True)


df_predictions = pd.concat([
    df_id,
    df_score,
    pd.DataFrame(y_pred_LR),
    pd.DataFrame(y_pred_MLP),
    pd.DataFrame(y_pred_tree),
    pd.DataFrame(y_pred_forest),
    pd.DataFrame(y_pred_gradboost),
    pd.DataFrame(y_pred_elnet),
    pd.DataFrame(y_pred_svr),
    pd.DataFrame(y_pred_xgb)
], axis=1, ignore_index=True
)

df_predictions.columns = [
    "anime_id", "og_score",
    "LinReg_score", "MLP_score", "Tree_score", "Forest_score", "GradBoost_score", "ElNet_score", "SVR_score", "XGB_score"
    ]

df_predictions.to_csv("xlsx_tables/training_score/predictions.csv", index=False)
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
