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
from module_ml import *


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#. Decisions to make # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#" Loading data obtained by our feature selection
df = pd.read_csv("created_files/training_score/selection_arranged_union.csv").fillna(0)


#" Chose a path for saving
# Change path if you want to load different models
path_model = "created_files/training_score/trained_models/"
# path to save predictions
path_pred = "created_files/training_score/"
#. # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
"""Splitting and scaling data"""
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
df_temp = df.copy()

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
with open(path_model + 'LinearRegression.pkl', 'rb') as f:
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
with open(path_model + 'MLPRegressor.pkl', 'rb') as f:
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
with open(path_model + 'DecisionTreeRegressor.pkl', 'rb') as f:
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
with open(path_model + 'RandomForestRegressor.pkl', 'rb') as f:
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
with open(path_model + 'GradientBoostingRegressor.pkl', 'rb') as f:
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
with open(path_model + 'ElasticNet.pkl', 'rb') as f:
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
with open(path_model + 'SVR.pkl', 'rb') as f:
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
with open(path_model + 'XGB.pkl', 'rb') as f:
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

df_predictions.to_csv(path_pred + "predictions.csv", index=False)
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
