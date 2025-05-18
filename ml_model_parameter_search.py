"""
In this file we gather the ML methods we want to use and try to find suitable parameters for the respected models.
Models for which we need to find "good" parameter:
- Linear Regression
- Neuronal Network
- Decision Tree
- Elastic Net
- Assembled Learning

Scoring:
- r2
- mae
- mse
- rmse

Problems and learnings:
- parameter search as the gridsearch or the randomsearch can help find parameter.
- parameter search is NOT valuable when testing to many.
- - scaling is not as good (multiplicative).
- - for MLPR and RandomForest this turns out to be a huge problem even with 16 cores in parallel.
- - reduced parameters way sooner.
- the intersection feature selection might be too small, consider union.

"""


# note for myself regarding comment colors in pycharm using better comments
# ? blue
# ! red
# - purple
# # # orange
# ## (ugly) green

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

# for parameter search
from sklearn.model_selection import GridSearchCV
from sklearn.model_selection import RandomizedSearchCV

# for LinearRegression
from sklearn.linear_model import LinearRegression

# for LogisticRegression
from sklearn.linear_model import LogisticRegression

# for the Neuronal Network
from sklearn.neural_network import MLPRegressor

# for Decision Tree
from sklearn.tree import DecisionTreeRegressor

# for the random forest (ensemble)
from sklearn.ensemble import RandomForestRegressor

# for Gradient Boosting (ensemble)
from sklearn.ensemble import GradientBoostingRegressor

# for Elastic Net
from sklearn.linear_model import ElasticNet

# for Support Vector Regression
from sklearn.svm import SVR

# for Extream Gradient Boosting
from xgboost import XGBRegressor
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
"""Defining Gridsearch for ML Models"""
"""     Model Introductions"""
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
"""         Neuronal Network"""
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
def gs_MLP(param_dict,X,y,cv,jobs):
    # model = Neuronal Network
    model = MLPRegressor()

    # # sklearn gridsearch initiation
    gs = GridSearchCV(
        model,          # DecisionTreeRegressor
        param_dict,     # parameters to vary and find good ones
        cv = cv,         # fold for the cross validation
        scoring=["r2", "neg_mean_absolute_error", "neg_mean_squared_error", "neg_root_mean_squared_error"],   # scoring method(s)
        refit = "neg_mean_absolute_error",    # main scoring to get .best_params_
        n_jobs=jobs,       # parallel computing (-1: all cores)
        verbose=3
    )

    # # starting the gridsearch
    gs_result = gs.fit(X,y)

    # # getting ALL the information from the gridsearch and saving them as dataframe
    df_result = pd.DataFrame.from_dict(gs_result.cv_results_)

    # # reducing the df to the information we want
    df_result = df_result[["params", "mean_test_r2", "mean_test_neg_mean_absolute_error", "mean_test_neg_mean_squared_error", "mean_test_neg_root_mean_squared_error"]]

    # # saving the information as csv
    df_result.to_csv("xlsx_tables/training_score/parameter_scoring_MLPR.csv", index=False)


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
"""         Decision Tree"""
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
def gs_tree(param_dict,X,y,cv,jobs):
    # model = Decision Tree
    model = DecisionTreeRegressor()

    # # sklearn gridsearch initiation
    gs = GridSearchCV(
        model,          # DecisionTreeRegressor
        param_dict,     # parameters to vary and find good ones
        cv = cv,         # fold for the cross validation
        scoring=["r2", "neg_mean_absolute_error", "neg_mean_squared_error", "neg_root_mean_squared_error"],   # scoring method(s)
        refit = "neg_mean_absolute_error",   # main scoring to get .best_params_
        n_jobs=jobs,      # parallel computing (-1: all cores)
        verbose=3
    )

    # # starting the gridsearch
    gs_result = gs.fit(X,y)

    # # getting ALL the information from the gridsearch and saving them as dataframe
    df_result = pd.DataFrame.from_dict(gs_result.cv_results_)

    # # reducing the df to the information we want
    df_result = df_result[["params", "mean_test_r2", "mean_test_neg_mean_absolute_error", "mean_test_neg_mean_squared_error", "mean_test_neg_root_mean_squared_error"]]

    # # saving the information as csv
    df_result.to_csv("xlsx_tables/training_score/parameter_scoring_TREE.csv", index=False)


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
"""         Random Forest"""
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
def get_forest(param_dict,X,y,cv,jobs):
    # # model = Decision Tree
    model = RandomForestRegressor()

    # # sklearn gridsearch initiation
    gs = GridSearchCV(
        model,          # DecisionTreeRegressor
        param_dict,     # parameters to vary and find good ones
        cv = cv,         # fold for the cross validation
        scoring=["r2", "neg_mean_absolute_error", "neg_mean_squared_error", "neg_root_mean_squared_error"],   # scoring method(s)
        refit = "neg_mean_absolute_error",    # main scoring to get .best_params_
        n_jobs=jobs,       # parallel computing (-1: all cores)
        verbose=3
    )

    # # starting the gridsearch
    gs_result = gs.fit(X,y)

    # # getting ALL the information from the gridsearch and saving them as dataframe
    df_result = pd.DataFrame.from_dict(gs_result.cv_results_)

    # # reducing the df to the information we want
    df_result = df_result[["params", "mean_test_r2", "mean_test_neg_mean_absolute_error", "mean_test_neg_mean_squared_error", "mean_test_neg_root_mean_squared_error"]]

    # # saving the information as csv
    df_result.to_csv("xlsx_tables/training_score/parameter_scoring_FOREST.csv", index=False)


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
"""         Logistic Regression"""
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
def get_logreg(param_dict,X,y,cv,jobs):
    # # model = Linear Regressor
    model = LogisticRegression()

    # # sklearn gridsearch initiation
    gs = GridSearchCV(
        model,          # DecisionTreeRegressor
        param_dict,     # parameters to vary and find good ones
        cv = cv,         # fold for the cross validation
        scoring=["r2", "neg_mean_absolute_error", "neg_mean_squared_error", "neg_root_mean_squared_error"],   # scoring method(s)
        refit = "neg_mean_absolute_error",    # main scoring to get .best_params_
        n_jobs=jobs,       # parallel computing (-1: all cores)
        verbose=3
    )

    # # starting the gridsearch
    gs_result = gs.fit(X,y)

    # # getting ALL the information from the gridsearch and saving them as dataframe
    df_result = pd.DataFrame.from_dict(gs_result.cv_results_)

    # # reducing the df to the information we want
    df_result = df_result[["params", "mean_test_r2", "mean_test_neg_mean_absolute_error", "mean_test_neg_mean_squared_error", "mean_test_neg_root_mean_squared_error"]]

    # # saving the information as csv
    df_result.to_csv("xlsx_tables/training_score/parameter_scoring_LogReg.csv", index=False)



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
"""         Gradient Boosting"""
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
def get_gradboost(param_dict,X,y,cv,jobs):
    # # model = Gradient Boosting
    model = GradientBoostingRegressor()

    # # sklearn gridsearch initiation
    gs = GridSearchCV(
        model,          # DecisionTreeRegressor
        param_dict,     # parameters to vary and find good ones
        cv = cv,         # fold for the cross validation
        scoring=["r2", "neg_mean_absolute_error", "neg_mean_squared_error", "neg_root_mean_squared_error"],   # scoring method(s)
        refit = "neg_mean_absolute_error",    # main scoring to get .best_params_
        n_jobs=jobs,       # parallel computing (-1: all cores)
        verbose=3
    )

    # # starting the gridsearch
    gs_result = gs.fit(X,y)

    # # getting ALL the information from the gridsearch and saving them as dataframe
    df_result = pd.DataFrame.from_dict(gs_result.cv_results_)

    # # reducing the df to the information we want
    df_result = df_result[["params", "mean_test_r2", "mean_test_neg_mean_absolute_error", "mean_test_neg_mean_squared_error", "mean_test_neg_root_mean_squared_error"]]

    # # saving the information as csv
    df_result.to_csv("xlsx_tables/training_score/parameter_scoring_GradBoost.csv", index=False)


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
"""         Elastic Net"""
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
def get_Elasticnet(param_dict,X,y,cv,jobs):
    # # model = Elastic Net
    model = ElasticNet()

    # # sklearn gridsearch initiation
    gs = GridSearchCV(
        model,          # DecisionTreeRegressor
        param_dict,     # parameters to vary and find good ones
        cv = cv,         # fold for the cross validation
        scoring=["r2", "neg_mean_absolute_error", "neg_mean_squared_error", "neg_root_mean_squared_error"],   # scoring method(s)
        refit = "neg_mean_absolute_error",    # main scoring to get .best_params_
        n_jobs=jobs,       # parallel computing (-1: all cores)
        verbose=3
    )

    # # starting the gridsearch
    gs_result = gs.fit(X,y)

    # # getting ALL the information from the gridsearch and saving them as dataframe
    df_result = pd.DataFrame.from_dict(gs_result.cv_results_)

    # # reducing the df to the information we want
    df_result = df_result[["params", "mean_test_r2", "mean_test_neg_mean_absolute_error", "mean_test_neg_mean_squared_error", "mean_test_neg_root_mean_squared_error"]]

    # # saving the information as csv
    df_result.to_csv("xlsx_tables/training_score/parameter_scoring_ElasticNet.csv", index=False)


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
"""         Support Vector Regression"""
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
def get_SVR(param_dict,X,y,cv,jobs):
    # # model = SVR
    model = SVR()

    # # sklearn gridsearch initiation
    gs = GridSearchCV(
        model,          # DecisionTreeRegressor
        param_dict,     # parameters to vary and find good ones
        cv = cv,         # fold for the cross validation
        scoring=["r2", "neg_mean_absolute_error", "neg_mean_squared_error", "neg_root_mean_squared_error"],   # scoring method(s)
        refit = "neg_mean_absolute_error",    # main scoring to get .best_params_
        n_jobs=jobs,       # parallel computing (-1: all cores)
        verbose=3
    )

    # # starting the gridsearch
    gs_result = gs.fit(X,y)

    # # getting ALL the information from the gridsearch and saving them as dataframe
    df_result = pd.DataFrame.from_dict(gs_result.cv_results_)

    # # reducing the df to the information we want
    df_result = df_result[["params", "mean_test_r2", "mean_test_neg_mean_absolute_error", "mean_test_neg_mean_squared_error", "mean_test_neg_root_mean_squared_error"]]

    # # saving the information as csv
    df_result.to_csv("xlsx_tables/training_score/parameter_scoring_SVR.csv", index=False)


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
"""         XGBoost Regression"""
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
def get_XGB(param_dict,X,y,cv,jobs):
    # # model = XGBRegressor
    model = XGBRegressor()

    # # sklearn gridsearch initiation
    gs = GridSearchCV(
        model,          # DecisionTreeRegressor
        param_dict,     # parameters to vary and find good ones
        cv = cv,         # fold for the cross validation
        scoring=["r2", "neg_mean_absolute_error", "neg_mean_squared_error", "neg_root_mean_squared_error"],   # scoring method(s)
        refit = "neg_mean_absolute_error",    # main scoring to get .best_params_
        n_jobs=jobs,       # parallel computing (-1: all cores)
        verbose=3
    )

    # # starting the gridsearch
    gs_result = gs.fit(X,y)

    # # getting ALL the information from the gridsearch and saving them as dataframe
    df_result = pd.DataFrame.from_dict(gs_result.cv_results_)

    # # reducing the df to the information we want
    df_result = df_result[["params", "mean_test_r2", "mean_test_neg_mean_absolute_error", "mean_test_neg_mean_squared_error", "mean_test_neg_root_mean_squared_error"]]

    # # saving the information as csv
    df_result.to_csv("xlsx_tables/training_score/parameter_scoring_XGB.csv", index=False)
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
"""Preparations"""
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
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
"""     Neuronal Network"""
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# parameters for testing
param_dict = {
        "hidden_layer_sizes":[(110, 110, 110),(110,110, 110, 110)], # one hidden layer with 100 neurons
        "activation":["logistic"],                                  # activation function
        "solver":["lbfgs"],                                         # solver for weight optimization
        "max_iter":[150],                                           # set the number of iterations
        "random_state":[42]                                         # for reproducibility
            }

# # uncomment to use
# scaling needed
# gs_MLP(param_dict,X_train_scaled,y_train,3,10)


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
"""     Decision Tree"""
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# parameters for testing
param_dict = {
        "criterion":['squared_error','friedman_mse'],       # criterion for spitting
        "max_depth":[70,80,90,100,110,120,130,None],        # max depth of tree
        "min_samples_split":[55,60,65,70,75,80],            # minimum number of samples required to split
        "min_samples_leaf":[11,12,13,14,15],                # minimum number of samples required to be at a leaf node
        "random_state":[42]                                 # for reproducibility
    }

# # uncomment to use
# scaling not needed
# gs_tree(param_dict,X_train,y_train,3,10)


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
"""         Random Forest""" # parallel trees
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# parameters for testing
param_dict = {
    "criterion":['squared_error'],                # criterion for spitting
    "n_estimators":[1200,1250,1300,1350,1400,1450,1500],    # number of trees
    "bootstrap":[True],                           # Whether bootstrap samples are used when building trees. If False, the whole dataset is used to build each tree.
    "max_depth":[70],                             # max depth of tree
    "min_samples_split":[75],                     # minimum number of samples required to split
    "min_samples_leaf":[14],                      # minimum number of samples required to be at a leaf node
    "random_state":[42]                           # for reproducibility
}

# uncomment to use
# # scaling not needed
# get_forest(param_dict,X_train,y_train,3,10)

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
"""         Logistic Regression"""
# todo: not working atm
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # parameters for testing
# param_dict = {
#     'penalty' : ['l2', None],
#     'C' : [100],#[100, 10, 1.0, 0.1, 0.01],
#     'solver' : ['lbfgs','newton-cg','sag','saga'],
#     'max_iter' : [100],#[100, 1000,2500, 5000],
#     'random_state': [42]                       # for reproducibility
# }
#
# # solve:liblinear not with penalty:None
# # penalty:elasticnet needs l1_ratio:____
# # solver:sag, newton-cg only penalty:l2 or None
#
# # # uncomment to use
# get_logreg(param_dict,X_train_scaled,y_train,3,10)

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
"""         Gradient Boosting""" # sequentially trees
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# parameters for testing
param_dict = {
    'loss': ["huber"],
    'criterion': ["squared_error"],
    'learning_rate': [0.19],
    'n_estimators': [900,1000,1100],
    'random_state': [42]
                          # for reproducibility
}

# uncomment to use
# get_gradboost(param_dict,X_train_scaled,y_train,3,5)


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
"""         Elastic Net"""
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# parameters for testing
param_dict = {
    'alpha': np.logspace(-5, 5, 50, endpoint=True),       # values between e^-5 and e^5
    'l1_ratio': np.append(np.arange(0, 1.01, 0.02), 1.0),  # values between 0 and 1, including 1.0
    'random_state': [42]                                   # for reproducibility
}

# # uncomment to use
# get_Elasticnet(param_dict,X_train_scaled,y_train,3,5)

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
"""         Support Vector Regression"""
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# parameters for testing
"""
if gamma='scale' (default) is passed then it uses 1 / (n_features * X.var()) as value of gamma,
if gamma=‘auto’, uses 1 / n_features
"""
param_dict = {
    'C': [0.1, 1, 10, 100],
    'gamma':["scale", "auto"],        #'gamma':[0.01, 0.1, 1, "scale", "auto"],
    'epsilon': [0.001, 0.01, 0.1, 0.5],
    'kernel': ["rbf"],         # 'kernel': ["linear", "poly", "rbf"]
            }

# # uncomment to use
# get_SVR(param_dict,X_train_scaled,y_train,3,5)


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
"""         XGBoost Regression"""
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# parameters for testing
param_dict = {
    'n_estimators': [1650,1700,1750,1800],
    'max_depth': [7],
    'learning_rate': [0.02,0.025,0.03],
    'min_child_weight': [2,3],
    'random_state': [42]                       # for reproducibility
            }

# uncomment to use
# jobs = cv, since XGB runs parallel
get_XGB(param_dict,X_train_scaled,y_train,3,3)

