"""
File for modul evaluation:
    Using ``eval_scor_pred`` from ``module_ml`` to evaluate score predictions
        Evaluation is presented in console as table formatted for markdown
"""

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#" Import
from module_ml import *

#. # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#" Loading and declaring necessary files and objects
df_predictions = pd.read_csv("xlsx_tables/training_score/predictions.csv")

# ``LinReg_score``, ``MLP_score``, ``Tree_score``, ``Forest_score``, ``GradBoost_score``, ``ElNet_score``, ``SVR_score``, ``XGB_score``
r2_scores = [0.64, 0.74, 0.67, 0.71, 0.78, 0.64, 0.71, 0.79]
#. # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#" Evaluation by using ``eval_scor_pred``
eval_scor_pred(df_predictions, r2_scores)
