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
# Change path if you want to keep older models
path = "created_files/training_score/trained_models/"
#. # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
"""Splitting and scaling data"""
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# We start with a smaller dataset
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
"""Model Introductions"""
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
"""         Linear Regression"""
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# linear regression model
model = LinearRegression()

# fitting the model on training data
# # X = features || y = target
model.fit(X_train_scaled, y_train)

# save
with open(path + 'LinearRegression.pkl','wb') as f:
    pickle.dump(model,f)

print("LinearRegression")
# making predictions
y_pred = model.predict(X_test_scaled)
# print scores
print_scores(y_test, y_pred)


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
"""         Neuronal Network"""
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# neuronal network
model = MLPRegressor(
    hidden_layer_sizes = (110,110,110),     # one hidden layer with 100 neurons
    activation = "logistic",                # 'relu' activation function
    solver = "lbfgs",                       # 'adam' solver for weight optimization
    max_iter = 150,                         # set the number of iterations
    random_state = 42                       # for reproducibility
)

# fitting the model on training data
# # X = features || y = target
model.fit(X_train_scaled, y_train)

# save
with open(path + 'MLPRegressor.pkl','wb') as f:
    pickle.dump(model,f)

print("MLPRegressor")
# making predictions
y_pred = model.predict(X_test_scaled)
# print scores
print_scores(y_test, y_pred)


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
"""         Decision Tree"""
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# Decision Tree

model = DecisionTreeRegressor(
    criterion = "squared_error",          # criterion for spitting
    max_depth = 70,                       # max depth of tree
    min_samples_split = 75,               # minimum number of samples required to split
    min_samples_leaf = 14,                # minimum number of samples required to be at a leaf node
    random_state = 42                     # for reproducibility
)
# fitting the model on training data
# # X = features || y = target
model.fit(X_train, y_train)

# save
with open(path + 'DecisionTreeRegressor.pkl','wb') as f:
    pickle.dump(model,f)

print("DecisionTreeRegressor")
# making predictions
y_pred = model.predict(X_test)
# print scores
print_scores(y_test, y_pred)


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
"""         Random Forest"""
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# Optimal parameters
model = RandomForestRegressor(
    criterion= "squared_error",     # criterion for spitting
    n_estimators= 1500,             # number of trees
    bootstrap= True,                # Whether bootstrap samples are used when building trees. If False, the whole dataset is used to build each tree.
    max_depth= 70,                  # max depth of tree
    min_samples_leaf= 14,           # minimum number of samples required to be at a leaf node
    min_samples_split= 75,          # minimum number of samples required to split
    random_state = 42               # for reproducibility
)
# fitting the model on training data
# # X = features || y = target
model.fit(X_train, y_train)

# save
with open(path + 'RandomForestRegressor.pkl','wb') as f:
    pickle.dump(model,f)

print("RandomForestRegressor")
# making predictions
y_pred = model.predict(X_test)
# print scores
print_scores(y_test, y_pred)


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
"""         Gradient Boosting"""
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# Optimal parameters
model = GradientBoostingRegressor(
    loss = "huber",                         # loss function to be optimized
    criterion = "squared_error",            # function to measure the quality of a split
    learning_rate = 0.19,                   # shrinks the contribution of each tree by learning_rate
    n_estimators = 1800,                    # number of boosting stages to perform
    random_state = 42                       # for reproducibility
)
# fitting the model on training data
# # X = features || y = target
model.fit(X_train_scaled, y_train)

# save
with open(path + 'GradientBoostingRegressor.pkl','wb') as f:
    pickle.dump(model,f)

print("GradientBoostingRegressor")
# making predictions
y_pred = model.predict(X_test_scaled)
# print scores
print_scores(y_test, y_pred)


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
"""         Elastic Net"""
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# Optimal parameters
model = ElasticNet(
    alpha = 0.00449,      # multiplies the penalty terms
    l1_ratio = 0.42,      # mixing parameter, with 0 <= l1_ratio <= 1
    random_state = 42     # for reproducibility
)
# fitting the model on training data
# # X = features || y = target
model.fit(X_train_scaled, y_train)

# save
with open(path + 'ElasticNet.pkl','wb') as f:
    pickle.dump(model,f)

print("ElasticNet")
# making predictions
y_pred = model.predict(X_test_scaled)
# print scores
print_scores(y_test, y_pred)


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
"""         Support Vector Regression"""
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# Optimal parameters
model = SVR(
    C = 5,                  # regularization parameter
    gamma = 0.0015,         # Kernel coefficient for ‘rbf’, ‘poly’ and ‘sigmoid’.
                            # # if gamma='scale' (default) is passed then it uses 1 / (n_features * X.var()) as value of gamma,
                            # # if ‘auto’, uses 1 / n_features
                            # # if float, must be non-negative.
    epsilon = 0.09,         # pecifies the epsilon-tube within which no penalty is associated
    kernel = "rbf",         #  kernel type to be used in the algorithm
)
# fitting the model on training data
# # X = features || y = target
model.fit(X_train_scaled, y_train)

# save
with open(path + 'SVR.pkl','wb') as f:
    pickle.dump(model,f)

print("SVR")
# making predictions
y_pred = model.predict(X_test_scaled)
# print scores
print_scores(y_test, y_pred)


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
"""         XGB"""
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# Optimal parameters
model = XGBRegressor(
    n_estimators = 1750,                # number of trees in the ensemble increased until no further improvements
    max_depth = 7,                      # maximum depth of each tree, usually between 1 and 10
    learning_rate = 0.03,               # earning rate used to weight each model, often set to small values such as 0.3, 0.1, 0.01, or smaller
    min_child_weight = 2,               # minimum sum of instance weight
    random_state = 42                   # for reproducibility
)
# fitting the model on training data
# # X = features || y = target
model.fit(X_train_scaled, y_train)

# save
with open(path + 'XGB.pkl','wb') as f:
    pickle.dump(model,f)

print("XGB")
# making predictions
y_pred = model.predict(X_test_scaled)
# print scores
print_scores(y_test, y_pred)


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #