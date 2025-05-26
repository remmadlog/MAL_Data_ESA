# Documentation for [module_ml.py](module_ml.py)

A short documentation for [module_ml.py](module_ml.py) that is mainly used for the machine learning part of the project.

- [Go to functions](#functions)
- [Go to imports](#imports) 


---

## Functions
List of all functions:
- [eval_scor_pred](#eval_scor_pred)
- [fs_chi2](#fs_chi2)
- [fs_correlation](#fs_correlation)
- [fs_f_classif](#fs_f_classif)
- [fs_variance](#fs_variance)
- [get_Elasticnet_reg](#get_Elasticnet_reg)
- [get_SVR_reg](#get_SVR_reg)
- [get_XGB_reg](#get_XGB_reg)
- [get_forest_reg](#get_forest_reg)
- [get_gradboost_reg](#get_gradboost_reg)
- [get_logreg_reg](#get_logreg_reg)
- [get_scores](#get_scores)
- [gs_MLP_reg](#gs_MLP_reg)
- [gs_tree_reg](#gs_tree_reg)
- [print_scores](#print_scores)
- [sorting](#sorting)


---

###  eval_scor_pred
> Function to print a table for markdown of
>     ``MAE``, ``r2``, ``MSE``, ``RMSE``, ``Median``, ``abs_median``, ``abs_min``, ``abs_max``, ``%error<0.1``, ``%error<0.2``, ``%error<0.3``, ``%error>0.5``
> for the predicted vs. the actual data.
> 
> df_predictions columns:
>     ``anime_id``, ``og_score``, ``LinReg_score``, ``MLP_score``, ``Tree_score``, ``Forest_score``, ``GradBoost_score``, ``ElNet_score``, ``SVR_score``, ``XGB_score``
> 
> r2_scores in order:
>     ``LinReg_score``, ``MLP_score``, ``Tree_score``, ``Forest_score``, ``GradBoost_score``, ``ElNet_score``, ``SVR_score``, ``XGB_score``
> - `df_predictions` (DataFrame): prediction data obtained in ``ml_RegModel_prediction.py``
> - `r2_scores` (list): r2 scores obtained in CrossValidation in Gridsearch
> - returns: None (prints table)
> 

---

###  fs_chi2
> Feature selection using ``chi2`` from sklearn
> - `df_data`: All data not including the target column
> - `df_target`: Data only including the target column
> - `k_best_features`: Amount of features returned, length of returned object
> - returns:  list of the ``k_best_features`` features
> 

---

###  fs_correlation
> Feature selection using ``correlation values``
> - `df_data`: All data not including the target column|
> - `df_target`: Data only including the target column
> - `k_best_features`: Amount of features returned, length of returned object
> - returns:  list of the ``k_best_features`` features
> 

---

###  fs_f_classif
> Feature selection using ``f_classif`` from sklearn
> - `df_data`: All data not including the target column
> - `df_target`: Data only including the target column
> - `k_best_features`: Amount of features returned, length of returned object
> - returns:  list of the ``k_best_features`` features
> 

---

###  fs_variance
> Feature selection using ``VarianceThresholding`` from sklearn
> - `df_data`: All data not including the target column
> - `threshold`: Threshold that must be overcome to be considered
> 

---

###  get_Elasticnet_reg
> Gridsearch for the ``ElasticNet``.
> 
> Saves results as a ``.csv`` file under ``dir_path``.
> - `param_dict`: parameter as dictionary
> - `X`: data not including ``target``
> - `y`: data only including ``target``
> - `folds`: number of folds used in the cross validation
> - `jobs`: number of cpu cores used. ``Default=1``
> - `dir_path`: directory path for saving, ``Default=""``
> - returns: None
> 

---

###  get_SVR_reg
> Gridsearch for the ``SVR``.
> 
> Saves results as a ``.csv`` file under ``dir_path``.
> - `param_dict`: parameter as dictionary
> - `X`: data not including ``target``
> - `y`: data only including ``target``
> - `folds`: number of folds used in the cross validation
> - `jobs`: number of cpu cores used. ``Default=1``
> - `dir_path`: directory path for saving, ``Default=""``
> - returns: None
> 

---

###  get_XGB_reg
> Gridsearch for the ``XGBRegressor``.
> 
> Saves results as a ``.csv`` file under ``dir_path``.
> - `param_dict`: parameter as dictionary
> - `X`: data not including ``target``
> - `y`: data only including ``target``
> - `folds`: number of folds used in the cross validation
> - `jobs`: number of cpu cores used. ``Default=1``
> - `dir_path`: directory path for saving, ``Default=""``
> - returns: None
> 

---

###  get_forest_reg
> Gridsearch for the ``RandomForestRegressor``.
> 
> Saves results as a ``.csv`` file under ``dir_path``.
> - `param_dict`: parameter as dictionary
> - `X`: data not including ``target``
> - `y`: data only including ``target``
> - `folds`: number of folds used in the cross validation
> - `jobs`: number of cpu cores used. ``Default=-1``: using all cores
> - `dir_path`: directory path for saving, ``Default=""``
> - returns: None
> 

---

###  get_gradboost_reg
> Gridsearch for the ``GradientBoostingRegressor``.
> 
> Saves results as a ``.csv`` file under ``dir_path``.
> - `param_dict`: parameter as dictionary
> - `X`: data not including ``target``
> - `y`: data only including ``target``
> - `folds`: number of folds used in the cross validation
> - `jobs`: number of cpu cores used. ``Default=1``
> - `dir_path`: directory path for saving, ``Default=""``
> - returns: None
> 

---

###  get_logreg_reg
> Gridsearch for the ``LogisticRegression``.
> 
> Saves results as a ``.csv`` file under ``dir_path``.
> - `param_dict`: parameter as dictionary
> - `X`: data not including ``target``
> - `y`: data only including ``target``
> - `folds`: number of folds used in the cross validation
> - `jobs`: number of cpu cores used. ``Default=-1``: using all cores
> - `dir_path`: directory path for saving, ``Default=""``
> - returns: None
> 

---

###  get_scores
> Scoring the original target against the predicted one.
> - `y_test`: original target data (as list)
> - `y_pred`: predicted target data (as list)
> - returns: list containing ``r2, mae, mse, rmse``
> 

---

###  gs_MLP_reg
> Gridsearch for the ``MLPRegressor``.
> 
> Saves results as a ``.csv`` file under ``dir_path``.
> - `param_dict`: parameter as dictionary
> - `X`: data not including ``target``
> - `y`: data only including ``target``
> - `folds`: number of folds used in the cross validation
> - `jobs`: number of cpu cores used. ``Default=-1``: using all cores
> - `dir_path`: directory path for saving, ``Default=""``
> - returns: None
> 

---

###  gs_tree_reg
> Gridsearch for the ``DecisionTreeRegressor``.
> 
> Saves results as a ``.csv`` file under ``dir_path``.
> - `param_dict`: parameter as dictionary
> - `X`: data not including ``target``
> - `y`: data only including ``target``
> - `folds`: number of folds used in the cross validation
> - `jobs`: number of cpu cores used. ``Default=-1``: using all cores
> - `dir_path`: directory path for saving, ``Default=""``
> - returns: None
> 

---

###  print_scores
> Scoring the original target against the predicted one; prints the results.
> - `y_test`: original target data (as list)
> - `y_pred`: predicted target data (as list)
> - returns: None
> 

---

###  sorting
> Sort ``features`` by ``selected_scores``.
> - `features`: List containing all features
> - `selected_indices`: same as ``selector.get_support(indices=True)``
> - `selected_scores`: same as ``selector.scores_``
> - returns: sorted list of features
> 

---

## Imports

This module features a lot of imports, mostly some kind of `sklearn` functions.

```python
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
```
