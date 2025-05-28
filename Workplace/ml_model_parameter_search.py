"""
In this file we gather the ML methods we want to use and try to find suitable parameters for the respected models.
Models for which we want to find "good" parameters:


# Regression:
- Linear Regression
- Neuronal Network
- Logistic Regression
- Decision Tree
- Elastic Net
- Assembled Learning
    - Random Forest
    - Gradient Boosting
    - X Gradient Boosting


# Scoring:
- r2
- mae
- mse
- rmse
"""

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
"""Import"""
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# importing our ml module
from module_ml import *


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
"""Loading data obtained by our feature selection"""
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# df = pd.read_csv("created_files/training_score/selection_arranged_comb.csv").fillna(0)
# df = pd.read_csv("created_files/training_score/selection_arranged_comb2.csv").fillna(0)
# df = pd.read_csv("created_files/training_score/selection_arranged_comb4.csv").fillna(0)
# df = pd.read_csv("created_files/training_score/selection_arranged_intersection.csv").fillna(0)
df = pd.read_csv("created_files/training_score/selection_arranged_union.csv").fillna(0)
# df = pd.read_csv("created_files/training_score/selection_arranged_union2.csv").fillna(0)
# df = pd.read_csv("created_files/training_score/selection_arranged_union4.csv").fillna(0)
# df = pd.read_csv("created_files/training_score/selection_pure_anova.csv").fillna(0)
# df = pd.read_csv("created_files/training_score/selection_pure_chi2.csv").fillna(0)
# df = pd.read_csv("created_files/training_score/selection_pure_corval.csv").fillna(0)
# df = pd.read_csv("created_files/training_score/selection_pure_rrelieff.csv").fillna(0)
# df = pd.read_csv("created_files/training_score/selection_pure_tree.csv").fillna(0)
# df = pd.read_csv("created_files/training_score/selection_pure_univar.csv").fillna(0)
# df = pd.read_csv("created_files/training_score/selection_pure_var.csv").fillna(0)


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
"""Splitting and scaling data"""
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
df_temp = df.copy()

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
"""Regression Models"""
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
# gs_MLP_reg(param_dict,X_train_scaled,y_train,3,10,"created_files/training_score/")


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
# gs_tree_reg(param_dict,X_train,y_train,3,10,"created_files/training_score/")


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
# get_forest_reg(param_dict,X_train,y_train,3,10,"created_files/training_score/")


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
# # uncomment to use
# get_logreg_reg(param_dict,X_train_scaled,y_train,3,10,"created_files/training_score/")


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
}

# uncomment to use
# get_gradboost_reg(param_dict,X_train_scaled,y_train,3,5,"created_files/training_score/")


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
# get_Elasticnet_reg(param_dict,X_train_scaled,y_train,3,5,"created_files/training_score/")


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
# get_SVR_reg(param_dict,X_train_scaled,y_train,3,5,"created_files/training_score/")


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
# get_XGB_reg(param_dict,X_train_scaled,y_train,3,3,"created_files/training_score/")

