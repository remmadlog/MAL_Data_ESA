"""
A collection of ml related function.
todo: documentation needed
"""



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
"""IMPORTS"""
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
import pandas as pd
import numpy as np

# for sorting list of lists
from operator import itemgetter

# Save and Load models using pickle
import pickle

# for splitting a DF into training and testing
from sklearn.model_selection import train_test_split

# for scaling
from sklearn.preprocessing import StandardScaler

# will be used for feature selection
from sklearn.feature_selection import SelectKBest
from sklearn.feature_selection import VarianceThreshold
from sklearn.feature_selection import f_classif
from sklearn.feature_selection import chi2

# for evaluating/scoring
from sklearn.metrics import mean_squared_error, r2_score, mean_absolute_error

# Gridsearch for better parameter tuning
from sklearn.model_selection import GridSearchCV

# Regression models
from sklearn.linear_model import LinearRegression       # for LinearRegression
from sklearn.neural_network import MLPRegressor         # for the Neuronal Network
from sklearn.tree import DecisionTreeRegressor          # for Decision Tree
from sklearn.ensemble import RandomForestRegressor      # for the random forest
from sklearn.linear_model import LogisticRegression     # for LogisticRegression
from sklearn.ensemble import GradientBoostingRegressor  # for Gradient Boosting (ensemble)
from sklearn.linear_model import ElasticNet             # for Elastic Net
from sklearn.svm import SVR                             # for Support Vector Regression
from xgboost import XGBRegressor                        # for Extreme Gradient Boosting


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
"""Defining usefully, but non-essential Functions"""
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

# get evaluations a list
def get_scores(y_test, y_pred):
    """
    Scoring the original target against the predicted one.

    :param y_test: original target data (as list)
    :param y_pred: predicted target data (as list)
    :return: list containing ``r2, mae, mse, rmse``
    """
    # # r^2
    r2 = r2_score(y_test, y_pred)

    # # mean absolut error (MAE)
    mae = mean_absolute_error(y_test, y_pred)

    # # mean squared error (MSE)
    mse = mean_squared_error(y_test, y_pred)

    # # root mean squared error (RMSE)
    rmse = mse ** 0.5
    return [r2,mae,mse,rmse]


# print evaluations
def print_scores(y_test, y_pred):
    """
    Scoring the original target against the predicted one; prints the results.

    :param y_test: original target data (as list)
    :param y_pred: predicted target data (as list)
    :return: None
    """
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
"""FEATURE SELECTION"""
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
def sorting(features, selected_indices,selected_scores):
    """
    Sort ``features`` by ``selected_scores``.

    :param features: List containing all features
    :param selected_indices: same as ``selector.get_support(indices=True)``
    :param selected_scores: same as ``selector.scores_``
    :return: sorted list of features
    """
    unsorted_list = []
    for i in selected_indices:
        unsorted_list.append([features[i],selected_scores[i]])

    # soring by score
    sorted_list = sorted(unsorted_list, key=itemgetter(1))
    # reverse order so the highest score is first entry
    sorted_list.reverse()
    return sorted_list


#,,,,,,,,,,,,,,,,,,,,,Univariate Feature Selection,,,,,,,,,,,,,,,,,,,,,
def fs_chi2(df_data,df_target,k_best_features):
    """
    Feature selection using ``chi2`` from sklearn

    :param df_data: All data not including the target column
    :param df_target: Data only including the target column
    :param k_best_features: Amount of features returned, length of returned object
    :return:  list of the ``k_best_features`` features
    """
    selector = SelectKBest(score_func=chi2, k=k_best_features)

    # since chi2 is for categorical target
    selector.fit_transform(df_data, df_target.astype("str"))

    # ids of chosen features
    selected_indices = selector.get_support(indices=True)

    # scores as array
    selected_scores = selector.scores_
    help_list = sorting(df_data.columns.to_list(),selected_indices,selected_scores)

    # get features as list
    features_chi2 = []
    for entry in help_list:
        features_chi2.append(entry[0])

    return features_chi2

#,,,,,,,,,,,,,,,,,,,,,Feature selection using f_classif,,,,,,,,,,,,,,,,,,,,,
def fs_f_classif(df_data,df_target,k_best_features):
    """
    Feature selection using ``f_classif`` from sklearn

    :param df_data: All data not including the target column
    :param df_target: Data only including the target column
    :param k_best_features: Amount of features returned, length of returned object
    :return:  list of the ``k_best_features`` features
    """
    selector = SelectKBest(score_func=f_classif, k=k_best_features)
    selector.fit_transform(df_data, df_target)

    # ids of chosen features
    selected_indices = selector.get_support(indices=True)

    # scores as array
    selected_scores = selector.scores_

    help_list = sorting(df_data.columns.to_list(),selected_indices,selected_scores)

    # get features as list
    features_anova = []
    for entry in help_list:
        features_anova.append(entry[0])

    return features_anova

#,,,,,,,,,,,,,,,,,,,,,Correlation-based Feature Selection,,,,,,,,,,,,,,,,,,,,,
def fs_correlation(df_data,df_target,k_best_features):
    """
    Feature selection using ``correlation values``

    :param df_data: All data not including the target column|
    :param df_target: Data only including the target column
    :param k_best_features: Amount of features returned, length of returned object
    :return:  list of the ``k_best_features`` features
    """
    # calculating correlation values
    cor_val = df_data.apply(lambda feature: np.abs(np.corrcoef(feature, df_target)[0, 1]))

    # getting some NaN || replace them with zero
    cor_val = cor_val.fillna(0)

    # sorting the values and extracting the top 100 features
    # # sorting
    cor_val = cor_val.sort_values(ascending=False)
    # # extracting the features
    features_cor_val = cor_val.index
    # # only getting the top k_best_features
    features_cor_val = features_cor_val[:k_best_features].to_list()

    return features_cor_val

#,,,,,,,,,,,,,,,,,,,,,Variance Thresholding,,,,,,,,,,,,,,,,,,,,,
def fs_variance(df_data,threshold = 0.05):
    """
    Feature selection using ``VarianceThresholding`` from sklearn

    :param df_data: All data not including the target column
    :param threshold: Threshold that must be overcome to be considered
    """
    # performing variance thresholding using VarianceThreshold from sklearn.feature_selection
    selector = VarianceThreshold(threshold=threshold)
    selector.fit_transform(df_data)

    # get features as list
    features_variance = df_data.columns[selector.get_support()].to_list()

    return features_variance





# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
"""Defining Gridsearch for ML Models"""
"""     Model Introductions"""
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
"""         Neuronal Network"""
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
def gs_MLP_reg(param_dict,X,y,folds,jobs=-1,dir_path=""):
    """
    Gridsearch for the ``MLPRegressor``.

    Saves results as a ``.csv`` file under ``dir_path``.

    :param param_dict: parameter as dictionary
    :param X: data not including ``target``
    :param y: data only including ``target``
    :param folds: number of folds used in the cross validation
    :param jobs: number of cpu cores used. ``Default=-1``: using all cores
    :param dir_path: directory path for saving, ``Default=""``
    :return: None
    """
    # model = Neuronal Network
    model = MLPRegressor()

    # # sklearn gridsearch initiation
    gs = GridSearchCV(
        model,          # DecisionTreeRegressor
        param_dict,     # parameters to vary and find good ones
        cv = folds,         # fold for the cross validation
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
    df_result.to_csv(dir_path + "parameter_scoring_MLPR.csv", index=False)


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
"""         Decision Tree"""
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
def gs_tree_reg(param_dict,X,y,folds,jobs=-1,dir_path=""):
    """
    Gridsearch for the ``DecisionTreeRegressor``.

    Saves results as a ``.csv`` file under ``dir_path``.

    :param param_dict: parameter as dictionary
    :param X: data not including ``target``
    :param y: data only including ``target``
    :param folds: number of folds used in the cross validation
    :param jobs: number of cpu cores used. ``Default=-1``: using all cores
    :param dir_path: directory path for saving, ``Default=""``
    :return: None
    """
    # model = Decision Tree
    model = DecisionTreeRegressor()

    # # sklearn gridsearch initiation
    gs = GridSearchCV(
        model,          # DecisionTreeRegressor
        param_dict,     # parameters to vary and find good ones
        cv = folds,         # fold for the cross validation
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
    df_result.to_csv(dir_path + "parameter_scoring_TREE.csv", index=False)


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
"""         Random Forest"""
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
def get_forest_reg(param_dict,X,y,folds,jobs=-1,dir_path=""):
    """
    Gridsearch for the ``RandomForestRegressor``.

    Saves results as a ``.csv`` file under ``dir_path``.

    :param param_dict: parameter as dictionary
    :param X: data not including ``target``
    :param y: data only including ``target``
    :param folds: number of folds used in the cross validation
    :param jobs: number of cpu cores used. ``Default=-1``: using all cores
    :param dir_path: directory path for saving, ``Default=""``
    :return: None
    """
    # # model = Decision Tree
    model = RandomForestRegressor()

    # # sklearn gridsearch initiation
    gs = GridSearchCV(
        model,          # DecisionTreeRegressor
        param_dict,     # parameters to vary and find good ones
        cv = folds,         # fold for the cross validation
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
    df_result.to_csv(dir_path + "parameter_scoring_FOREST.csv", index=False)


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
"""         Logistic Regression"""
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
def get_logreg_reg(param_dict,X,y,folds,jobs=-1,dir_path=""):
    """
    Gridsearch for the ``LogisticRegression``.

    Saves results as a ``.csv`` file under ``dir_path``.

    :param param_dict: parameter as dictionary
    :param X: data not including ``target``
    :param y: data only including ``target``
    :param folds: number of folds used in the cross validation
    :param jobs: number of cpu cores used. ``Default=-1``: using all cores
    :param dir_path: directory path for saving, ``Default=""``
    :return: None
    """
    # # model = Linear Regressor
    model = LogisticRegression()

    # # sklearn gridsearch initiation
    gs = GridSearchCV(
        model,          # DecisionTreeRegressor
        param_dict,     # parameters to vary and find good ones
        cv = folds,         # fold for the cross validation
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
    df_result.to_csv(dir_path + "parameter_scoring_LogReg.csv", index=False)



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
"""         Gradient Boosting"""
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
def get_gradboost_reg(param_dict,X,y,folds,jobs=1,dir_path=""):
    """
    Gridsearch for the ``GradientBoostingRegressor``.

    Saves results as a ``.csv`` file under ``dir_path``.

    :param param_dict: parameter as dictionary
    :param X: data not including ``target``
    :param y: data only including ``target``
    :param folds: number of folds used in the cross validation
    :param jobs: number of cpu cores used. ``Default=1``
    :param dir_path: directory path for saving, ``Default=""``
    :return: None
    """
    # # model = Gradient Boosting
    model = GradientBoostingRegressor()

    # # sklearn gridsearch initiation
    gs = GridSearchCV(
        model,          # DecisionTreeRegressor
        param_dict,     # parameters to vary and find good ones
        cv = folds,         # fold for the cross validation
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
    df_result.to_csv(dir_path + "parameter_scoring_GradBoost.csv", index=False)


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
"""         Elastic Net"""
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
def get_Elasticnet_reg(param_dict,X,y,folds,jobs=1,dir_path=""):
    """
    Gridsearch for the ``ElasticNet``.

    Saves results as a ``.csv`` file under ``dir_path``.

    :param param_dict: parameter as dictionary
    :param X: data not including ``target``
    :param y: data only including ``target``
    :param folds: number of folds used in the cross validation
    :param jobs: number of cpu cores used. ``Default=1``
    :param dir_path: directory path for saving, ``Default=""``
    :return: None
    """
    # # model = Elastic Net
    model = ElasticNet()

    # # sklearn gridsearch initiation
    gs = GridSearchCV(
        model,          # DecisionTreeRegressor
        param_dict,     # parameters to vary and find good ones
        cv = folds,         # fold for the cross validation
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
    df_result.to_csv(dir_path + "parameter_scoring_ElasticNet.csv", index=False)


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
"""         Support Vector Regression"""
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
def get_SVR_reg(param_dict,X,y,folds,jobs=1,dir_path=""):
    """
    Gridsearch for the ``SVR``.

    Saves results as a ``.csv`` file under ``dir_path``.

    :param param_dict: parameter as dictionary
    :param X: data not including ``target``
    :param y: data only including ``target``
    :param folds: number of folds used in the cross validation
    :param jobs: number of cpu cores used. ``Default=1``
    :param dir_path: directory path for saving, ``Default=""``
    :return: None
    """
    # # model = SVR
    model = SVR()

    # # sklearn gridsearch initiation
    gs = GridSearchCV(
        model,          # DecisionTreeRegressor
        param_dict,     # parameters to vary and find good ones
        cv = folds,         # fold for the cross validation
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
    df_result.to_csv(dir_path + "parameter_scoring_SVR.csv", index=False)


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
"""         XGBoost Regression"""
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
def get_XGB_reg(param_dict,X,y,folds,jobs=1,dir_path=""):
    """
    Gridsearch for the ``XGBRegressor``.

    Saves results as a ``.csv`` file under ``dir_path``.

    :param param_dict: parameter as dictionary
    :param X: data not including ``target``
    :param y: data only including ``target``
    :param folds: number of folds used in the cross validation
    :param jobs: number of cpu cores used. ``Default=1``
    :param dir_path: directory path for saving, ``Default=""``
    :return: None
    """
    # # model = XGBRegressor
    model = XGBRegressor()

    # # sklearn gridsearch initiation
    gs = GridSearchCV(
        model,          # DecisionTreeRegressor
        param_dict,     # parameters to vary and find good ones
        cv = folds,         # fold for the cross validation
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
    df_result.to_csv(dir_path + "parameter_scoring_XGB.csv", index=False)




# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
"""Model Evaluations"""
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
def eval_scor_pred(df_predictions, r2_scores):
    """
    Function to print a table for markdown of
        ``MAE``, ``r2``, ``MSE``, ``RMSE``, ``Median``, ``abs_median``, ``abs_min``, ``abs_max``, ``%error<0.1``, ``%error<0.2``, ``%error<0.3``, ``%error>0.5``
    for the predicted vs. the actual data.

    df_predictions columns:
        ``anime_id``, ``og_score``, ``LinReg_score``, ``MLP_score``, ``Tree_score``, ``Forest_score``, ``GradBoost_score``, ``ElNet_score``, ``SVR_score``, ``XGB_score``

    r2_scores in order:
        ``LinReg_score``, ``MLP_score``, ``Tree_score``, ``Forest_score``, ``GradBoost_score``, ``ElNet_score``, ``SVR_score``, ``XGB_score``

    :param df_predictions: prediction data obtained in ``ml_RegModel_prediction.py``
    :type df_predictions: DataFrame
    :param r2_scores: r2 scores obtained in CrossValidation in Gridsearch
    :type r2_scores: list
    :return: None (prints table)
    """

    #" removing index to avoid mismatching # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    df_id = df_predictions["anime_id"].to_frame().reset_index(drop=True)
    df_score = df_predictions["og_score"].to_frame().reset_index(drop=True)


    #" Averaging model predictions # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # Model combination by considering the average
    df_mean = df_predictions["LinReg_score"]
    for entry in ["MLP_score", "Tree_score", "Forest_score", "GradBoost_score", "ElNet_score", "SVR_score", "XGB_score"]:
        df_mean = df_mean + df_predictions[entry]
    df_mean = df_mean/8

    # Model combination by considering the r2 weighted mean
    # wights (r2 scores) obtained during CV in gridsearch
    i = 0
    df_biased_mean = df_predictions["LinReg_score"] * r2_scores[i]
    for entry in ["MLP_score", "Tree_score", "Forest_score", "GradBoost_score", "ElNet_score", "SVR_score", "XGB_score"]:
        i = i +1
        df_biased_mean = df_biased_mean + df_predictions[entry] * r2_scores[i]
    df_biased_mean = df_biased_mean/sum(r2_scores)


    #" Error calculation # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
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


    #" statistic evaluation as lists # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    col_mae         = round(df_compare[col_model_error].abs().mean(),3).to_list()
    col_r2          = r2_scores + [0,0]     #! + [0,0] for df_mean and df_biased_mean, no crossval -> no r2 from crossval
    col_mse         = round((df_compare[col_model_error]*df_compare[col_model_error]).mean(),3).to_list()
    col_rmse        = np.around(np.sqrt(col_mse),3).tolist()
    col_median      = round(df_compare[col_model_error],3).median().to_list()
    col_abs_median  = round(df_compare[col_model_error],3).abs().median().to_list()
    col_abs_min     = round(df_compare[col_model_error],3).abs().min().to_list()
    col_abs_max     = round(df_compare[col_model_error],3).abs().max().to_list()


    #" percentage of error smaller/larger than q # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
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


    #" creating table with statistic evaluations # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
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

    #" printing the table, so it can be used in notes_ml_model_evaluation.md # # # # # # # # # # # # # # # # # # # # # #
    print(df_stats.to_markdown(index=False))





