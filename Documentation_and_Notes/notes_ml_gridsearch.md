# Parameter Search

Here I present my findings and challenges finding suitable parameters.

The main focus is on scoring using the MAE.
The results obtained there will be used in the next steps.

## General Approach

- Used [selection_arranged_intersection.csv](../Workplace/created_files/training_score/selection_arranged_intersection.csv) in order to not have to many features early on.
  - The idea was to use a small feature set and find good parameters and apply them to a larger feature set.
  - Not sure if that was a good idea.
    - Overall not a great r2 score.
- Forgot to fix the **random_state**.
  - Results are not reproducible, need to start over.
  - Used the opportunity to change the dataset to [selection_arranged_union2.csv](../Workplace/created_files/training_score/selection_arranged_union2.csv) in hope of better results.
- Used [selection_arranged_union2.csv](../Workplace/created_files/training_score/selection_arranged_union2.csv).
  - Still hoping that the same parameter are giving good results for the larger feature set.
    - I do not think that this can work. 
      - The DecisionTreeRegressor gets very different parameters using [selection_arranged_union.csv](../Workplace/created_files/training_score/selection_arranged_union.csv).
      - Thought that it might give an indication, this seems not to be the case.
- Using [selection_arranged_union.csv](../Workplace/created_files/training_score/selection_arranged_union.csv).
  - Noticed huge deference in parameter choice.
  - Overall better r2 score, still bad though (<0.8)
  - Forgot scaling for a minute, using scaled data works much better...
  - Considered **MAE** as scoring lead, since I have a better feeling for the real impact.

> [!NOTE]
> One may also consider [notes_ml_gridsearch_all_features](notes_ml_gridsearch_all_features.md) for a brief look into the possibility of using **all** features.
---

---

# Scoring using r2
<details>
<summary>Show Details and Results for r2</summary>

Using 
- [selection_arranged_union.csv](../Workplace/created_files/training_score/selection_arranged_union.csv) and [selection_arranged_union2.csv](../Workplace/created_files/training_score/selection_arranged_union2.csv)
- r2 for scoring
- 3 to 5 foldings in the cross validation

---

<details>
<summary>Show Results</summary>


## Results

Using [selection_arranged_union.csv](../Workplace/created_files/training_score/selection_arranged_union.csv)

[DecisionTreeRegressor](#decisiontreeregressor):
```python
model = DecisionTreeRegressor(
    criterion = "friedman_mse",           # criterion for spitting
    max_depth = 75,                       # max depth of tree
    min_samples_split = 56,               # minimum number of samples required to split
    min_samples_leaf = 12,                # minimum number of samples required to be at a leaf node
    random_state = 42                     # for reproducibility
)
```

[RandomForestRegressor](#randomforestregressor):
```python
model = RandomForestRegressor(
    criterion= "squared_error",     # criterion for spitting
    n_estimators= 1300,             # number of trees
    bootstrap= True,                # Whether bootstrap samples are used when building trees. If False, the whole dataset is used to build each tree.
    max_depth= 75,                  # max depth of tree
    min_samples_leaf= 12,           # minimum number of samples required to be at a leaf node
    min_samples_split= 56,          # minimum number of samples required to split
    random_state = 42               # for reproducibility
)
```


[MLPRegressor](#mlpregressor):
```python
model = MLPRegressor(
    hidden_layer_sizes = (100,100),     # one hidden layer with 100 neurons
    activation = "logistic",            # 'relu' activation function
    solver = "lbfgs",                   # 'adam' solver for weight optimization
    max_iter = 120,                     # set the number of iterations
    random_state = 42                   # for reproducibility
)
```

</details>

---

<details>
<summary>Show more Details</summary>



## DecisionTreeRegressor

<details>
<summary>Show DecisionTreeRegressor</summary>

>Starting with the following parameters:
>```python
>param_dict = {
>        "criterion":['squared_error','friedman_mse','poisson','absolute_error'],    # criterion for spitting
>        "max_depth":[5,10,25,75,None],                                              # max depth of tree
>        "min_samples_split":[2,5,15,50,100],                                        # minimum number of samples required to split
>        "min_samples_leaf":[2,5,15,50,100],                                         # minimum number of samples required to be at a leaf node
>        "random_state":[42]                                                         # for reproducibility
>              }
>```
>
>Obtaining the table below:
><details>
><summary>Show Table</summary>
>
>|     | params                                                                                                                 |       r2 |       MAE |       MSE |      RMSE |
>|----:|:-----------------------------------------------------------------------------------------------------------------------|---------:|----------:|----------:|----------:|
>|  85 | {'criterion': 'squared_error', 'max_depth': 75, 'min_samples_leaf': 15, 'min_samples_split': 2, 'random_state': 42}    | 0.655983 | -0.393176 |  -0.26873 | -0.518381 |
>|  86 | {'criterion': 'squared_error', 'max_depth': 75, 'min_samples_leaf': 15, 'min_samples_split': 5, 'random_state': 42}    | 0.655983 | -0.393176 |  -0.26873 | -0.518381 |
>|  87 | {'criterion': 'squared_error', 'max_depth': 75, 'min_samples_leaf': 15, 'min_samples_split': 15, 'random_state': 42}   | 0.655983 | -0.393176 |  -0.26873 | -0.518381 |
>| 110 | {'criterion': 'squared_error', 'max_depth': None, 'min_samples_leaf': 15, 'min_samples_split': 2, 'random_state': 42}  | 0.655983 | -0.393176 |  -0.26873 | -0.518381 |
>| 111 | {'criterion': 'squared_error', 'max_depth': None, 'min_samples_leaf': 15, 'min_samples_split': 5, 'random_state': 42}  | 0.655983 | -0.393176 |  -0.26873 | -0.518381 |
>|  61 | {'criterion': 'squared_error', 'max_depth': 25, 'min_samples_leaf': 15, 'min_samples_split': 5, 'random_state': 42}    | 0.655983 | -0.393176 |  -0.26873 | -0.518381 |
>|  60 | {'criterion': 'squared_error', 'max_depth': 25, 'min_samples_leaf': 15, 'min_samples_split': 2, 'random_state': 42}    | 0.655983 | -0.393176 |  -0.26873 | -0.518381 |
>| 112 | {'criterion': 'squared_error', 'max_depth': None, 'min_samples_leaf': 15, 'min_samples_split': 15, 'random_state': 42} | 0.655983 | -0.393176 |  -0.26873 | -0.518381 |
>|  62 | {'criterion': 'squared_error', 'max_depth': 25, 'min_samples_leaf': 15, 'min_samples_split': 15, 'random_state': 42}   | 0.655983 | -0.393176 |  -0.26873 | -0.518381 |
>|  88 | {'criterion': 'squared_error', 'max_depth': 75, 'min_samples_leaf': 15, 'min_samples_split': 50, 'random_state': 42}   | 0.658694 | -0.390515 | -0.266636 | -0.516359 |
>|  63 | {'criterion': 'squared_error', 'max_depth': 25, 'min_samples_leaf': 15, 'min_samples_split': 50, 'random_state': 42}   | 0.658694 | -0.390515 | -0.266636 | -0.516359 |
>| 113 | {'criterion': 'squared_error', 'max_depth': None, 'min_samples_leaf': 15, 'min_samples_split': 50, 'random_state': 42} | 0.658694 | -0.390515 | -0.266636 | -0.516359 |
>| 188 | {'criterion': 'friedman_mse', 'max_depth': 25, 'min_samples_leaf': 15, 'min_samples_split': 50, 'random_state': 42}    | 0.658694 | -0.390515 | -0.266636 | -0.516359 |
>| 238 | {'criterion': 'friedman_mse', 'max_depth': None, 'min_samples_leaf': 15, 'min_samples_split': 50, 'random_state': 42}  | 0.658694 | -0.390515 | -0.266636 | -0.516359 |
>| 213 | {'criterion': 'friedman_mse', 'max_depth': 75, 'min_samples_leaf': 15, 'min_samples_split': 50, 'random_state': 42}    | 0.658694 | -0.390515 | -0.266636 | -0.516359 |
></details>


>With the parameters:
>```python
>param_dict = {
>        "criterion":['squared_error','friedman_mse'],    # criterion for spitting
>        "max_depth":[25,50,75,100,150,None],             # max depth of tree
>        "min_samples_split":[45,50,55],                  # minimum number of samples required to split
>        "min_samples_leaf":[12,13,14,15,16,17],          # minimum number of samples required to be at a leaf node
>        "random_state":[42]                              # for reproducibility
>              }
>```
>We obtain:
><details>
><summary>Show Table</summary>
>
>|     | params                                                                                                                 |       r2 |       MAE |       MSE |      RMSE |
>|----:|:-----------------------------------------------------------------------------------------------------------------------|---------:|----------:|----------:|----------:|
>| 146 | {'criterion': 'friedman_mse', 'max_depth': 75, 'min_samples_leaf': 12, 'min_samples_split': 55, 'random_state': 42}    | 0.659818 | -0.389828 | -0.265734 | -0.515467 |
>| 182 | {'criterion': 'friedman_mse', 'max_depth': 150, 'min_samples_leaf': 12, 'min_samples_split': 55, 'random_state': 42}   | 0.659818 | -0.389828 | -0.265734 | -0.515467 |
>| 164 | {'criterion': 'friedman_mse', 'max_depth': 100, 'min_samples_leaf': 12, 'min_samples_split': 55, 'random_state': 42}   | 0.659818 | -0.389828 | -0.265734 | -0.515467 |
>| 128 | {'criterion': 'friedman_mse', 'max_depth': 50, 'min_samples_leaf': 12, 'min_samples_split': 55, 'random_state': 42}    | 0.659818 | -0.389828 | -0.265734 | -0.515467 |
>| 200 | {'criterion': 'friedman_mse', 'max_depth': None, 'min_samples_leaf': 12, 'min_samples_split': 55, 'random_state': 42}  | 0.659818 | -0.389828 | -0.265734 | -0.515467 |
>
></details>


>Considering the parameters given below:
>```python
>param_dict = {
>        "criterion":['friedman_mse'],    # criterion for spitting
>        "max_depth":[75,100,150,200,250,300,None],             # max depth of tree
>        "min_samples_split":[54,55,56],                  # minimum number of samples required to split
>        "min_samples_leaf":[11,12,13],          # minimum number of samples required to be at a leaf node
>        "random_state":[42]                              # for reproducibility
>              }
>```
>
>Obtaining the following table:
><details>
><summary>Show Table</summary>
>
>|    | params                                                                                                                |       r2 |        MAE |       MSE |      RMSE |
>|---:|:----------------------------------------------------------------------------------------------------------------------|---------:|-----------:|----------:|----------:|
>|  5 | {'criterion': 'friedman_mse', 'max_depth': 75, 'min_samples_leaf': 12, 'min_samples_split': 56, 'random_state': 42}   | 0.659838 |  -0.389733 | -0.265714 | -0.515446 |
>| 32 | {'criterion': 'friedman_mse', 'max_depth': 200, 'min_samples_leaf': 12, 'min_samples_split': 56, 'random_state': 42}  | 0.659838 |  -0.389733 | -0.265714 | -0.515446 |
>| 41 | {'criterion': 'friedman_mse', 'max_depth': 250, 'min_samples_leaf': 12, 'min_samples_split': 56, 'random_state': 42}  | 0.659838 |  -0.389733 | -0.265714 | -0.515446 |
>| 50 | {'criterion': 'friedman_mse', 'max_depth': 300, 'min_samples_leaf': 12, 'min_samples_split': 56, 'random_state': 42}  | 0.659838 |  -0.389733 | -0.265714 | -0.515446 |
>| 59 | {'criterion': 'friedman_mse', 'max_depth': None, 'min_samples_leaf': 12, 'min_samples_split': 56, 'random_state': 42} | 0.659838 |  -0.389733 | -0.265714 | -0.515446 |
></details>



The parameters to chose are given by

```python
model = DecisionTreeRegressor(
    criterion = "friedman_mse",           # criterion for spitting
    max_depth = 75,                       # max depth of tree
    min_samples_split = 56,               # minimum number of samples required to split
    min_samples_leaf = 12,                # minimum number of samples required to be at a leaf node
    random_state = 42                     # for reproducibility
)
```

</details>

---

## RandomForestRegressor

<details>
<summary>Show RandomForestRegressor</summary>


### Using [selection_arranged_union.csv](../Workplace/created_files/training_score/selection_arranged_union.csv)

>Using only DecisionTreeRegressor for the cross validation and the previous obtained parameters for the **decision tree regressor**, we consider the following parameters:
>
>```python
>param_dict = {
>    "criterion":['squared_error'],                # criterion for spitting
>    "n_estimators":[500,1000,2000,2500,5000],     # number of trees
>    "bootstrap":[True,False],                     # Whether bootstrap samples are used when building trees. If False, the whole dataset is used to build each tree.
>    "max_depth":[75],                             # max depth of tree
>    "min_samples_split":[56],                     # minimum number of samples required to split
>    "min_samples_leaf":[12],                      # minimum number of samples required to be at a leaf node
>    "random_state":[42]                           # for reproducibility
>}
>```
>
>Resulting in the table below:
>
><details>
><summary>Show Table</summary>
>
>|    | params                                                                                                                                                         |       r2 |       MAE |       MSE |      RMSE |
>|---:|:---------------------------------------------------------------------------------------------------------------------------------------------------------------|---------:|----------:|----------:|----------:|
>|  7 | {'bootstrap': False, 'criterion': 'squared_error', 'max_depth': 75, 'min_samples_leaf': 12, 'min_samples_split': 56, 'n_estimators': 2000, 'random_state': 42} | 0.649381 | -0.394114 | -0.274034 | -0.523443 |
>|  8 | {'bootstrap': False, 'criterion': 'squared_error', 'max_depth': 75, 'min_samples_leaf': 12, 'min_samples_split': 56, 'n_estimators': 2500, 'random_state': 42} | 0.649381 | -0.394114 | -0.274034 | -0.523443 |
>|  9 | {'bootstrap': False, 'criterion': 'squared_error', 'max_depth': 75, 'min_samples_leaf': 12, 'min_samples_split': 56, 'n_estimators': 5000, 'random_state': 42} | 0.649382 | -0.394114 | -0.274034 | -0.523442 |
>|  5 | {'bootstrap': False, 'criterion': 'squared_error', 'max_depth': 75, 'min_samples_leaf': 12, 'min_samples_split': 56, 'n_estimators': 500, 'random_state': 42}  | 0.649382 | -0.394114 | -0.274034 | -0.523442 |
>|  6 | {'bootstrap': False, 'criterion': 'squared_error', 'max_depth': 75, 'min_samples_leaf': 12, 'min_samples_split': 56, 'n_estimators': 1000, 'random_state': 42} | 0.649382 | -0.394114 | -0.274034 | -0.523442 |
>|  4 | {'bootstrap': True, 'criterion': 'squared_error', 'max_depth': 75, 'min_samples_leaf': 12, 'min_samples_split': 56, 'n_estimators': 5000, 'random_state': 42}  |  0.71121 | -0.357628 | -0.225697 | -0.475052 |
>|  3 | {'bootstrap': True, 'criterion': 'squared_error', 'max_depth': 75, 'min_samples_leaf': 12, 'min_samples_split': 56, 'n_estimators': 2500, 'random_state': 42}  | 0.711225 | -0.357617 | -0.225686 |  -0.47504 |
>|  0 | {'bootstrap': True, 'criterion': 'squared_error', 'max_depth': 75, 'min_samples_leaf': 12, 'min_samples_split': 56, 'n_estimators': 500, 'random_state': 42}   | 0.711291 | -0.357698 | -0.225633 | -0.474984 |
>|  2 | {'bootstrap': True, 'criterion': 'squared_error', 'max_depth': 75, 'min_samples_leaf': 12, 'min_samples_split': 56, 'n_estimators': 2000, 'random_state': 42}  | 0.711313 | -0.357564 | -0.225617 | -0.474967 |
>|  1 | {'bootstrap': True, 'criterion': 'squared_error', 'max_depth': 75, 'min_samples_leaf': 12, 'min_samples_split': 56, 'n_estimators': 1000, 'random_state': 42}  | 0.711444 | -0.357542 | -0.225515 | -0.474861 |
></details>


>Considering the following parameters:
>```python
>param_dict = {
>    "criterion":['squared_error'],                          # criterion for spitting
>    "n_estimators":[1700,1800,1900,1000,1100,1200,1300],    # number of trees
>    "bootstrap":[True],                                     # Whether bootstrap samples are used when building trees. If False, the whole dataset is used to build each tree.
>    "max_depth":[75],                                       # max depth of tree
>    "min_samples_split":[56],                               # minimum number of samples required to split
>    "min_samples_leaf":[12],                                # minimum number of samples required to be at a leaf node
>    "random_state":[42]                                     # for reproducibility
>}
>```
>
>Resulting in the table below:
>
><details>
><summary>Show Table</summary>
>
>|   | params                                                                                                                                                        |       r2 |       MAE |       MSE |      RMSE |
>|--:|:--------------------------------------------------------------------------------------------------------------------------------------------------------------|---------:|----------:|----------:|----------:|
>| 2 | {'bootstrap': True, 'criterion': 'squared_error', 'max_depth': 75, 'min_samples_leaf': 12, 'min_samples_split': 56, 'n_estimators': 1900, 'random_state': 42} | 0.711341 | -0.357563 | -0.225595 | -0.474945 |
>| 1 | {'bootstrap': True, 'criterion': 'squared_error', 'max_depth': 75, 'min_samples_leaf': 12, 'min_samples_split': 56, 'n_estimators': 1800, 'random_state': 42} | 0.711349 | -0.357555 | -0.225589 | -0.474939 |
>| 0 | {'bootstrap': True, 'criterion': 'squared_error', 'max_depth': 75, 'min_samples_leaf': 12, 'min_samples_split': 56, 'n_estimators': 1700, 'random_state': 42} | 0.711379 | -0.357559 | -0.225565 | -0.474913 |
>| 4 | {'bootstrap': True, 'criterion': 'squared_error', 'max_depth': 75, 'min_samples_leaf': 12, 'min_samples_split': 56, 'n_estimators': 1100, 'random_state': 42} | 0.711417 | -0.357582 | -0.225536 | -0.474884 |
>| 5 | {'bootstrap': True, 'criterion': 'squared_error', 'max_depth': 75, 'min_samples_leaf': 12, 'min_samples_split': 56, 'n_estimators': 1200, 'random_state': 42} | 0.711423 | -0.357573 | -0.225531 | -0.474878 |
>| 3 | {'bootstrap': True, 'criterion': 'squared_error', 'max_depth': 75, 'min_samples_leaf': 12, 'min_samples_split': 56, 'n_estimators': 1000, 'random_state': 42} | 0.711444 | -0.357542 | -0.225515 | -0.474861 |
>| 6 | {'bootstrap': True, 'criterion': 'squared_error', 'max_depth': 75, 'min_samples_leaf': 12, 'min_samples_split': 56, 'n_estimators': 1300, 'random_state': 42} | 0.711446 | -0.357565 | -0.225513 | -0.474858 |
></details>



We finally end up using the following:


```python
model = RandomForestRegressor(
    criterion= "squared_error",     # criterion for spitting
    n_estimators= 1300,             # number of trees
    bootstrap= True,                # Whether bootstrap samples are used when building trees. If False, the whole dataset is used to build each tree.
    max_depth= 75,                  # max depth of tree
    min_samples_leaf= 12,           # minimum number of samples required to be at a leaf node
    min_samples_split= 56,          # minimum number of samples required to split
    random_state = 42               # for reproducibility
)
```

</details>

---

## MLPRegressor

<details>
<summary>Show MLPRegressor</summary>

### Using [selection_arranged_union.csv](../Workplace/created_files/training_score/selection_arranged_union.csv)

>Starting with the following set of parameters:
>```python
>param_dict = {
>        "hidden_layer_sizes":[(50,50),(75,75),(100,100),(200,200)], # one hidden layer with 100 neurons
>        "activation":["logistic", "tanh","relu"],                   # activation function
>        "solver":["lbfgs", "sgd", "adam"],                          # solver for weight optimization
>        "max_iter":[100,1000,1500],                                 # set the number of iterations
>        "random_state":[42]                                         # for reproducibility
>            }
>```
>
>Obtaining very good results in the first round:
><details>
><summary>Show Table</summary>
>
>|    | params                                                                                                               |       r2 |       MAE |       MSE |      RMSE |
>|---:|:---------------------------------------------------------------------------------------------------------------------|---------:|----------:|----------:|----------:|
>| 36 | {'activation': 'tanh', 'hidden_layer_sizes': (50, 50), 'max_iter': 100, 'random_state': 42, 'solver': 'lbfgs'}       |  0.62515 | -0.404913 | -0.292996 |  -0.54129 |
>| 63 | {'activation': 'tanh', 'hidden_layer_sizes': (200, 200), 'max_iter': 100, 'random_state': 42, 'solver': 'lbfgs'}     | 0.632735 | -0.396114 | -0.287009 |  -0.53564 |
>|  2 | {'activation': 'logistic', 'hidden_layer_sizes': (50, 50), 'max_iter': 100, 'random_state': 42, 'solver': 'adam'}    | 0.633275 | -0.366213 | -0.286627 | -0.535372 |
>|  7 | {'activation': 'logistic', 'hidden_layer_sizes': (50, 50), 'max_iter': 1500, 'random_state': 42, 'solver': 'sgd'}    | 0.636657 | -0.406267 | -0.283966 |  -0.53284 |
>|  4 | {'activation': 'logistic', 'hidden_layer_sizes': (50, 50), 'max_iter': 1000, 'random_state': 42, 'solver': 'sgd'}    | 0.636657 | -0.406267 | -0.283966 |  -0.53284 |
>| 34 | {'activation': 'logistic', 'hidden_layer_sizes': (200, 200), 'max_iter': 1500, 'random_state': 42, 'solver': 'sgd'}  | 0.638411 | -0.404442 | -0.282596 |  -0.53156 |
>| 31 | {'activation': 'logistic', 'hidden_layer_sizes': (200, 200), 'max_iter': 1000, 'random_state': 42, 'solver': 'sgd'}  | 0.638411 | -0.404442 | -0.282596 |  -0.53156 |
>| 13 | {'activation': 'logistic', 'hidden_layer_sizes': (75, 75), 'max_iter': 1000, 'random_state': 42, 'solver': 'sgd'}    | 0.638741 | -0.404858 | -0.282365 | -0.531372 |
>| 16 | {'activation': 'logistic', 'hidden_layer_sizes': (75, 75), 'max_iter': 1500, 'random_state': 42, 'solver': 'sgd'}    | 0.638741 | -0.404858 | -0.282365 | -0.531372 |
>| 25 | {'activation': 'logistic', 'hidden_layer_sizes': (100, 100), 'max_iter': 1500, 'random_state': 42, 'solver': 'sgd'}  |  0.64206 | -0.403477 | -0.279766 | -0.528892 |
>| 22 | {'activation': 'logistic', 'hidden_layer_sizes': (100, 100), 'max_iter': 1000, 'random_state': 42, 'solver': 'sgd'}  |  0.64206 | -0.403477 | -0.279766 | -0.528892 |
>| 27 | {'activation': 'logistic', 'hidden_layer_sizes': (200, 200), 'max_iter': 100, 'random_state': 42, 'solver': 'lbfgs'} | 0.688858 |   -0.3689 | -0.243165 | -0.493084 |
>|  0 | {'activation': 'logistic', 'hidden_layer_sizes': (50, 50), 'max_iter': 100, 'random_state': 42, 'solver': 'lbfgs'}   | 0.691842 | -0.364427 | -0.240811 |  -0.49067 |
>|  9 | {'activation': 'logistic', 'hidden_layer_sizes': (75, 75), 'max_iter': 100, 'random_state': 42, 'solver': 'lbfgs'}   | 0.696994 | -0.363153 | -0.236802 | -0.486604 |
>| 18 | {'activation': 'logistic', 'hidden_layer_sizes': (100, 100), 'max_iter': 100, 'random_state': 42, 'solver': 'lbfgs'} | 0.704031 | -0.361691 | -0.231282 | -0.480858 |
></details>


>Using the following parameters:
>```python
>param_dict = {
>        "hidden_layer_sizes":[(50,50),(60,60),(75,75),(90,90),(100,100),(110,110),(120,120)],  # one hidden layer with 100 neurons
>        "activation":["logistic"],                                                             # activation function
>        "solver":["lbfgs"],                                                                    # solver for weight optimization
>        "max_iter":[50,100,150,2000,2500],                                                     # set the number of iterations
>        "random_state":[42]                                                                    # for reproducibility
>            }
>```
>
>Obtaining very good results in the first round:
>
><details>
><summary>Show Table</summary>
>
>|    | params                                                                                                               |       r2 |       MAE |       MSE |      RMSE |
>|---:|:---------------------------------------------------------------------------------------------------------------------|---------:|----------:|----------:|----------:|
>| 26 | {'activation': 'logistic', 'hidden_layer_sizes': (110, 110), 'max_iter': 100, 'random_state': 42, 'solver': 'lbfgs'} | 0.689566 |  -0.36483 |  -0.24259 | -0.492487 |
>| 27 | {'activation': 'logistic', 'hidden_layer_sizes': (110, 110), 'max_iter': 150, 'random_state': 42, 'solver': 'lbfgs'} |  0.69152 | -0.362914 | -0.241067 | -0.490948 |
>|  1 | {'activation': 'logistic', 'hidden_layer_sizes': (50, 50), 'max_iter': 100, 'random_state': 42, 'solver': 'lbfgs'}   | 0.691842 | -0.364427 | -0.240811 |  -0.49067 |
>| 31 | {'activation': 'logistic', 'hidden_layer_sizes': (120, 120), 'max_iter': 100, 'random_state': 42, 'solver': 'lbfgs'} |   0.6927 | -0.366355 | -0.240169 | -0.490046 |
>|  7 | {'activation': 'logistic', 'hidden_layer_sizes': (60, 60), 'max_iter': 150, 'random_state': 42, 'solver': 'lbfgs'}   | 0.695079 | -0.364698 | -0.238322 | -0.488169 |
>| 11 | {'activation': 'logistic', 'hidden_layer_sizes': (75, 75), 'max_iter': 100, 'random_state': 42, 'solver': 'lbfgs'}   | 0.696994 | -0.363153 | -0.236802 | -0.486604 |
>| 21 | {'activation': 'logistic', 'hidden_layer_sizes': (100, 100), 'max_iter': 100, 'random_state': 42, 'solver': 'lbfgs'} | 0.704031 | -0.361691 | -0.231282 | -0.480858 |
>| 32 | {'activation': 'logistic', 'hidden_layer_sizes': (120, 120), 'max_iter': 150, 'random_state': 42, 'solver': 'lbfgs'} | 0.705433 |  -0.35866 |  -0.23023 | -0.479814 |
>|  6 | {'activation': 'logistic', 'hidden_layer_sizes': (60, 60), 'max_iter': 100, 'random_state': 42, 'solver': 'lbfgs'}   | 0.706246 | -0.358376 | -0.229557 | -0.479077 |
>| 22 | {'activation': 'logistic', 'hidden_layer_sizes': (100, 100), 'max_iter': 150, 'random_state': 42, 'solver': 'lbfgs'} | 0.709168 | -0.356207 | -0.227244 | -0.476586 |
></details>


>Using the following parameters:
>```python
>param_dict = {
>        "hidden_layer_sizes":[(90,90),(100,100),(110,110),(120,120)],  # one hidden layer
>        "activation":["logistic"],                                     # activation function
>        "solver":["lbfgs"],                                            # solver for weight optimization
>        "max_iter":[90,100,110,120],                                   # set the number of iterations
>        "random_state":[42]                                            # for reproducibility
>            }
>```
>
>Obtaining very good results in the first round:
><details>
><summary>Show Table</summary>
>
>|   | params                                                                                                                    |       r2 |       MAE |       MSE |      RMSE |
>|--:|:--------------------------------------------------------------------------------------------------------------------------|---------:|----------:|----------:|----------:|
>| 1 | {'activation': 'logistic', 'hidden_layer_sizes': (100, 100), 'max_iter': 100, 'random_state': 42, 'solver': 'lbfgs'}      | 0.704031 | -0.361691 | -0.231282 | -0.480858 |
>| 6 | {'activation': 'logistic', 'hidden_layer_sizes': (100, 100, 100), 'max_iter': 110, 'random_state': 42, 'solver': 'lbfgs'} | 0.705036 | -0.358979 |  -0.23051 | -0.480065 |
>| 2 | {'activation': 'logistic', 'hidden_layer_sizes': (100, 100), 'max_iter': 110, 'random_state': 42, 'solver': 'lbfgs'}      | 0.708728 | -0.357777 | -0.227622 | -0.477028 |
>| 7 | {'activation': 'logistic', 'hidden_layer_sizes': (100, 100, 100), 'max_iter': 120, 'random_state': 42, 'solver': 'lbfgs'} |  0.70889 | -0.356398 | -0.227501 |  -0.47691 |
>| 3 | {'activation': 'logistic', 'hidden_layer_sizes': (100, 100), 'max_iter': 120, 'random_state': 42, 'solver': 'lbfgs'}      | 0.712401 | -0.356235 | -0.224729 |  -0.47395 |
></details>


Thus, resulting in the final chose of parameters:

```python
model = MLPRegressor(
    hidden_layer_sizes = (100,100),     # one hidden layer with 100 neurons
    activation = "logistic",            # 'relu' activation function
    solver = "lbfgs",                   # 'adam' solver for weight optimization
    max_iter = 120,                     # set the number of iterations
    random_state = 42                   # for reproducibility
)
```

</details>

</details>

</details>

---

---





# Scoring using MAE
<details>
<summary>Show Details and Results for MAE</summary>

Using 
- [selection_arranged_union.csv](../Workplace/created_files/training_score/selection_arranged_union.csv)
- MAE for scoring
- 3 foldings in the cross validation

---

<details>
<summary>Show Results</summary>


## Results

[DecisionTreeRegressor](#decisiontreeregressor-1):
```python
model = DecisionTreeRegressor(
    criterion = "squared_error",          # criterion for spitting
    max_depth = 70,                       # max depth of tree
    min_samples_split = 75,               # minimum number of samples required to split
    min_samples_leaf = 14,                # minimum number of samples required to be at a leaf node
    random_state = 42                     # for reproducibility
)
```

[RandomForestRegressor](#randomforestregressor-1):
```python
model = RandomForestRegressor(
    criterion= "squared_error",     # criterion for spitting
    n_estimators= 1500,             # number of trees
    bootstrap= True,                # Whether bootstrap samples are used when building trees. If False, the whole dataset is used to build each tree.
    max_depth= 70,                  # max depth of tree
    min_samples_leaf= 14,           # minimum number of samples required to be at a leaf node
    min_samples_split= 75,          # minimum number of samples required to split
    random_state = 42               # for reproducibility
)
```


[MLPRegressor](#mlpregressor-1):
```python
model = MLPRegressor(
    hidden_layer_sizes = (110,110,110),     # one hidden layer with 100 neurons
    activation = "logistic",                # 'relu' activation function
    solver = "lbfgs",                       # 'adam' solver for weight optimization
    max_iter = 150,                         # set the number of iterations
    random_state = 42                       # for reproducibility
)
```


[GradientBoostingRegressor](#gradientboostingregressor):
```python
model = GradientBoostingRegressor(
    loss = "huber",                         # loss function to be optimized
    criterion = "squared_error",            # function to measure the quality of a split
    learning_rate = 0.19,                   # shrinks the contribution of each tree by learning_rate
    n_estimators = 1800,                    # number of boosting stages to perform
    random_state = 42                       # for reproducibility
)
```


[ElasticNet](#elasticnet):
```python
model = ElasticNet(
    alpha = 0.00449,      # multiplies the penalty terms
    l1_ratio = 0.42,      # mixing parameter, with 0 <= l1_ratio <= 1
    random_state = 42     # for reproducibility
)
```


[SVR](#svr):
```python
model = SVR(
    C = 5,                  # regularization parameter
    gamma = 0.0015,         # Kernel coefficient for ‘rbf’, ‘poly’ and ‘sigmoid’. 
                            # # if gamma='scale' (default) is passed then it uses 1 / (n_features * X.var()) as value of gamma,
                            # # if ‘auto’, uses 1 / n_features
                            # # if float, must be non-negative.
    epsilon = 0.09,         # pecifies the epsilon-tube within which no penalty is associated
    kernel = "rbf",         #  kernel type to be used in the algorithm
)
```


[XGBoost](#xgboost):
```python
model = XGBRegressor(    
    n_estimators = 1750,                # number of trees in the ensemble increased until no further improvements
    max_depth = 7,                      # maximum depth of each tree, usually between 1 and 10
    learning_rate = 0.03,               # earning rate used to weight each model, often set to small values such as 0.3, 0.1, 0.01, or smaller
    min_child_weight = 2,               # minimum sum of instance weight
    random_state = 42                   # for reproducibility
)
```
</details>


---
<details>
<summary>Show more Details</summary>

## DecisionTreeRegressor

<details>
<summary>Show DecisionTreeRegressor</summary>

>Using the following parameters:
>```python
>param_dict = {
>        "criterion":['squared_error','friedman_mse','poisson','absolute_error'],    # criterion for spitting
>        "max_depth":[5,10,25,75,None],                                              # max depth of tree
>        "min_samples_split":[2,5,15,50,100],                                        # minimum number of samples required to split
>        "min_samples_leaf":[2,5,15,50,100],                                         # minimum number of samples required to be at a leaf node
>        "random_state":[42]                                                         # for reproducibility
>              }
>```
>
>Obtaining the table presented below:
><details>
><summary>Show Table</summary>
>
>|     | params                                                                                                                 |       r2 |       MAE |       MSE |      RMSE |
>|----:|:-----------------------------------------------------------------------------------------------------------------------|---------:|----------:|----------:|----------:|
>| 188 | {'criterion': 'friedman_mse', 'max_depth': 10, 'min_samples_leaf': 15, 'min_samples_split': 50, 'random_state': 42}    | 0.655549 | -0.392436 | -0.269117 | -0.518759 |
>|  38 | {'criterion': 'squared_error', 'max_depth': 10, 'min_samples_leaf': 15, 'min_samples_split': 50, 'random_state': 42}   | 0.655549 | -0.392436 | -0.269117 | -0.518759 |
>| 288 | {'criterion': 'friedman_mse', 'max_depth': None, 'min_samples_leaf': 15, 'min_samples_split': 50, 'random_state': 42}  | 0.658694 | -0.390515 | -0.266636 | -0.516359 |
>| 138 | {'criterion': 'squared_error', 'max_depth': None, 'min_samples_leaf': 15, 'min_samples_split': 50, 'random_state': 42} | 0.658694 | -0.390515 | -0.266636 | -0.516359 |
>| 113 | {'criterion': 'squared_error', 'max_depth': 100, 'min_samples_leaf': 15, 'min_samples_split': 50, 'random_state': 42}  | 0.658694 | -0.390515 | -0.266636 | -0.516359 |
>| 238 | {'criterion': 'friedman_mse', 'max_depth': 75, 'min_samples_leaf': 15, 'min_samples_split': 50, 'random_state': 42}    | 0.658694 | -0.390515 | -0.266636 | -0.516359 |
>|  63 | {'criterion': 'squared_error', 'max_depth': 25, 'min_samples_leaf': 15, 'min_samples_split': 50, 'random_state': 42}   | 0.658694 | -0.390515 | -0.266636 | -0.516359 |
>|  88 | {'criterion': 'squared_error', 'max_depth': 75, 'min_samples_leaf': 15, 'min_samples_split': 50, 'random_state': 42}   | 0.658694 | -0.390515 | -0.266636 | -0.516359 |
>| 213 | {'criterion': 'friedman_mse', 'max_depth': 25, 'min_samples_leaf': 15, 'min_samples_split': 50, 'random_state': 42}    | 0.658694 | -0.390515 | -0.266636 | -0.516359 |
>| 263 | {'criterion': 'friedman_mse', 'max_depth': 100, 'min_samples_leaf': 15, 'min_samples_split': 50, 'random_state': 42}   | 0.658694 | -0.390515 | -0.266636 | -0.516359 |
></details>

>Using the following parameters:
>```python
>param_dict = {
>        "criterion":['squared_error','friedman_mse'],    # criterion for spitting
>        "max_depth":[25,50,75,100,150,None],             # max depth of tree
>        "min_samples_split":[45,50,55],                  # minimum number of samples required to split
>        "min_samples_leaf":[12,13,14,15,16,17],          # minimum number of samples required to be at a leaf node
>        "random_state":[42]                              # for reproducibility
>              }
>```
>
>Obtaining the table presented below:
><details>
><summary>Show Table</summary>
>
>|     | params                                                                                                                 |       r2 |       MAE |       MSE |      RMSE |
>|----:|:-----------------------------------------------------------------------------------------------------------------------|---------:|----------:|----------:|----------:|
>| 113 | {'criterion': 'friedman_mse', 'max_depth': 25, 'min_samples_leaf': 13, 'min_samples_split': 55, 'random_state': 42}    | 0.651092 | -0.393541 | -0.272705 | -0.522173 |
>| 149 | {'criterion': 'friedman_mse', 'max_depth': 75, 'min_samples_leaf': 13, 'min_samples_split': 55, 'random_state': 42}    | 0.651092 | -0.393541 | -0.272705 | -0.522173 |
>| 131 | {'criterion': 'friedman_mse', 'max_depth': 50, 'min_samples_leaf': 13, 'min_samples_split': 55, 'random_state': 42}    | 0.651092 | -0.393541 | -0.272705 | -0.522173 |
>| 203 | {'criterion': 'friedman_mse', 'max_depth': None, 'min_samples_leaf': 13, 'min_samples_split': 55, 'random_state': 42}  | 0.651092 | -0.393541 | -0.272705 | -0.522173 |
>|  77 | {'criterion': 'squared_error', 'max_depth': 150, 'min_samples_leaf': 13, 'min_samples_split': 55, 'random_state': 42}  | 0.651097 | -0.393531 | -0.272701 | -0.522169 |
>|  95 | {'criterion': 'squared_error', 'max_depth': None, 'min_samples_leaf': 13, 'min_samples_split': 55, 'random_state': 42} | 0.651097 | -0.393531 | -0.272701 | -0.522169 |
>|  23 | {'criterion': 'squared_error', 'max_depth': 50, 'min_samples_leaf': 13, 'min_samples_split': 55, 'random_state': 42}   | 0.651097 | -0.393531 | -0.272701 | -0.522169 |
>|   5 | {'criterion': 'squared_error', 'max_depth': 25, 'min_samples_leaf': 13, 'min_samples_split': 55, 'random_state': 42}   | 0.651097 | -0.393531 | -0.272701 | -0.522169 |
>|  41 | {'criterion': 'squared_error', 'max_depth': 75, 'min_samples_leaf': 13, 'min_samples_split': 55, 'random_state': 42}   | 0.651097 | -0.393531 | -0.272701 | -0.522169 |
>|  59 | {'criterion': 'squared_error', 'max_depth': 100, 'min_samples_leaf': 13, 'min_samples_split': 55, 'random_state': 42}  | 0.651097 | -0.393531 | -0.272701 | -0.522169 |
></details>


>Using the following parameters:
>```python
>param_dict = {
>        "criterion":['squared_error','friedman_mse'],    # criterion for spitting
>        "max_depth":[70,80,90,100,110,120,130,None],     # max depth of tree
>        "min_samples_split":[55,60,65,70,75,80],         # minimum number of samples required to split
>        "min_samples_leaf":[11,12,13,14,15],             # minimum number of samples required to be at a leaf node
>        "random_state":[42]                              # for reproducibility
>              }
>```
>
>Obtaining the table presented below:
><details>
><summary>Show Table</summary>
>
>|     | params                                                                                                                |       r2 |       MAE |        MSE |      RMSE |
>|----:|:----------------------------------------------------------------------------------------------------------------------|---------:|----------:|-----------:|----------:|
>| 142 | {'criterion': 'squared_error', 'max_depth': 110, 'min_samples_leaf': 14, 'min_samples_split': 75, 'random_state': 42} | 0.652186 | -0.392955 |   -0.27185 | -0.521356 |
>| 442 | {'criterion': 'friedman_mse', 'max_depth': 130, 'min_samples_leaf': 14, 'min_samples_split': 75, 'random_state': 42}  | 0.652186 | -0.392955 |   -0.27185 | -0.521356 |
>|  82 | {'criterion': 'squared_error', 'max_depth': 90, 'min_samples_leaf': 14, 'min_samples_split': 75, 'random_state': 42}  | 0.652186 | -0.392955 |   -0.27185 | -0.521356 |
>|  52 | {'criterion': 'squared_error', 'max_depth': 80, 'min_samples_leaf': 14, 'min_samples_split': 75, 'random_state': 42}  | 0.652186 | -0.392955 |   -0.27185 | -0.521356 |
>|  22 | {'criterion': 'squared_error', 'max_depth': 70, 'min_samples_leaf': 14, 'min_samples_split': 75, 'random_state': 42}  | 0.652186 | -0.392955 |   -0.27185 | -0.521356 |
></details>


The parameters to chose are given by

```python
model = DecisionTreeRegressor(
    criterion = "squared_error",          # criterion for spitting
    max_depth = 70,                       # max depth of tree
    min_samples_split = 75,               # minimum number of samples required to split
    min_samples_leaf = 14,                # minimum number of samples required to be at a leaf node
    random_state = 42                     # for reproducibility
)
```

</details>

---

## RandomForestRegressor

<details>
<summary>Show RandomForestRegressor</summary>

>Using the previous obtained parameters for the **decision tree regressor**, we consider the following parameters:
>```python
>param_dict = {
>    "criterion":['squared_error'],                # criterion for spitting
>    "n_estimators":[500,1000,2000,2500,5000],     # number of trees
>    "bootstrap":[True,False],                     # Whether bootstrap samples are used when building trees. If False, the whole dataset is used to build each tree.
>    "max_depth":[70],                             # max depth of tree
>    "min_samples_split":[75],                     # minimum number of samples required to split
>    "min_samples_leaf":[14],                      # minimum number of samples required to be at a leaf node
>    "random_state":[42]                           # for reproducibility
>}
>```
>
>Resulting in the table below:
>
><details>
><summary>Show Table</summary>
>
>|    | params                                                                                                                                                         |       r2 |       MAE |       MSE |      RMSE |
>|---:|:---------------------------------------------------------------------------------------------------------------------------------------------------------------|---------:|----------:|----------:|----------:|
>|  5 | {'bootstrap': False, 'criterion': 'squared_error', 'max_depth': 70, 'min_samples_leaf': 14, 'min_samples_split': 75, 'n_estimators': 500, 'random_state': 42}  | 0.652226 | -0.392917 | -0.271819 | -0.521327 |
>|  6 | {'bootstrap': False, 'criterion': 'squared_error', 'max_depth': 70, 'min_samples_leaf': 14, 'min_samples_split': 75, 'n_estimators': 1000, 'random_state': 42} | 0.652227 | -0.392916 | -0.271818 | -0.521326 |
>|  7 | {'bootstrap': False, 'criterion': 'squared_error', 'max_depth': 70, 'min_samples_leaf': 14, 'min_samples_split': 75, 'n_estimators': 2000, 'random_state': 42} | 0.652227 | -0.392916 | -0.271818 | -0.521326 |
>|  8 | {'bootstrap': False, 'criterion': 'squared_error', 'max_depth': 70, 'min_samples_leaf': 14, 'min_samples_split': 75, 'n_estimators': 2500, 'random_state': 42} | 0.652227 | -0.392916 | -0.271818 | -0.521326 |
>|  9 | {'bootstrap': False, 'criterion': 'squared_error', 'max_depth': 70, 'min_samples_leaf': 14, 'min_samples_split': 75, 'n_estimators': 5000, 'random_state': 42} | 0.652227 | -0.392916 | -0.271818 | -0.521326 |
>|  0 | {'bootstrap': True, 'criterion': 'squared_error', 'max_depth': 70, 'min_samples_leaf': 14, 'min_samples_split': 75, 'n_estimators': 500, 'random_state': 42}   | 0.703338 | -0.362841 | -0.231848 | -0.481479 |
>|  3 | {'bootstrap': True, 'criterion': 'squared_error', 'max_depth': 70, 'min_samples_leaf': 14, 'min_samples_split': 75, 'n_estimators': 2500, 'random_state': 42}  |  0.70339 | -0.362694 | -0.231808 | -0.481437 |
>|  4 | {'bootstrap': True, 'criterion': 'squared_error', 'max_depth': 70, 'min_samples_leaf': 14, 'min_samples_split': 75, 'n_estimators': 5000, 'random_state': 42}  | 0.703382 |  -0.36268 | -0.231814 | -0.481443 |
>|  2 | {'bootstrap': True, 'criterion': 'squared_error', 'max_depth': 70, 'min_samples_leaf': 14, 'min_samples_split': 75, 'n_estimators': 2000, 'random_state': 42}  | 0.703445 |  -0.36265 | -0.231765 | -0.481392 |
>|  1 | {'bootstrap': True, 'criterion': 'squared_error', 'max_depth': 70, 'min_samples_leaf': 14, 'min_samples_split': 75, 'n_estimators': 1000, 'random_state': 42}  | 0.703531 | -0.362645 | -0.231699 | -0.481324 |
></details>


>Using the following parameters:
>```python
>param_dict = {
>    "criterion":['squared_error'],                # criterion for spitting
>    "n_estimators":[1000,1250,1500,1750,2000],    # number of trees
>    "bootstrap":[True],                           # Whether bootstrap samples are used when building trees. If False, the whole dataset is used to build each tree.
>    "max_depth":[70],                             # max depth of tree
>    "min_samples_split":[75],                     # minimum number of samples required to split
>    "min_samples_leaf":[14],                      # minimum number of samples required to be at a leaf node
>    "random_state":[42]                           # for reproducibility
>}
>```
>
>Resulting in the table below:
>
><details>
><summary>Show Table</summary>
>
>|    | params                                                                                                                                                        |       r2 |       MAE |        MSE |      RMSE |
>|---:|:--------------------------------------------------------------------------------------------------------------------------------------------------------------|---------:|----------:|-----------:|----------:|
>|  4 | {'bootstrap': True, 'criterion': 'squared_error', 'max_depth': 70, 'min_samples_leaf': 14, 'min_samples_split': 75, 'n_estimators': 2000, 'random_state': 42} | 0.703445 |  -0.36265 |  -0.231765 | -0.481392 |
>|  0 | {'bootstrap': True, 'criterion': 'squared_error', 'max_depth': 70, 'min_samples_leaf': 14, 'min_samples_split': 75, 'n_estimators': 1000, 'random_state': 42} | 0.703531 | -0.362645 |  -0.231699 | -0.481324 |
>|  3 | {'bootstrap': True, 'criterion': 'squared_error', 'max_depth': 70, 'min_samples_leaf': 14, 'min_samples_split': 75, 'n_estimators': 1750, 'random_state': 42} | 0.703515 | -0.362637 |  -0.231711 | -0.481336 |
>|  1 | {'bootstrap': True, 'criterion': 'squared_error', 'max_depth': 70, 'min_samples_leaf': 14, 'min_samples_split': 75, 'n_estimators': 1250, 'random_state': 42} | 0.703574 | -0.362635 |  -0.231665 | -0.481288 |
>|  2 | {'bootstrap': True, 'criterion': 'squared_error', 'max_depth': 70, 'min_samples_leaf': 14, 'min_samples_split': 75, 'n_estimators': 1500, 'random_state': 42} | 0.703559 | -0.362622 |  -0.231676 |   -0.4813 |
></details>


>Using the following parameters:
>```python
>param_dict = {
>    "criterion":['squared_error'],                          # criterion for spitting
>    "n_estimators":[1200,1250,1300,1350,1400,1450,1500],    # number of trees
>    "bootstrap":[True],                                     # Whether bootstrap samples are used when building trees. If False, the whole dataset is used to build each tree.
>    "max_depth":[70],                                       # max depth of tree
>    "min_samples_split":[75],                               # minimum number of samples required to split
>    "min_samples_leaf":[14],                                # minimum number of samples required to be at a leaf node
>    "random_state":[42]                                     # for reproducibility
>}
>```
>
>Resulting in the table below:
>
><details>
><summary>Show Table</summary>
>
>|    | params                                                                                                                                                        |       r2 |       MAE |       MSE |      RMSE |
>|---:|:--------------------------------------------------------------------------------------------------------------------------------------------------------------|---------:|----------:|----------:|----------:|
>|  0 | {'bootstrap': True, 'criterion': 'squared_error', 'max_depth': 70, 'min_samples_leaf': 14, 'min_samples_split': 75, 'n_estimators': 1200, 'random_state': 42} | 0.703549 | -0.362657 | -0.231684 | -0.481309 |
>|  2 | {'bootstrap': True, 'criterion': 'squared_error', 'max_depth': 70, 'min_samples_leaf': 14, 'min_samples_split': 75, 'n_estimators': 1300, 'random_state': 42} | 0.703572 | -0.362648 | -0.231666 | -0.481289 |
>|  3 | {'bootstrap': True, 'criterion': 'squared_error', 'max_depth': 70, 'min_samples_leaf': 14, 'min_samples_split': 75, 'n_estimators': 1350, 'random_state': 42} | 0.703572 | -0.362643 | -0.231666 |  -0.48129 |
>|  4 | {'bootstrap': True, 'criterion': 'squared_error', 'max_depth': 70, 'min_samples_leaf': 14, 'min_samples_split': 75, 'n_estimators': 1400, 'random_state': 42} | 0.703573 | -0.362642 | -0.231665 | -0.481289 |
>|  1 | {'bootstrap': True, 'criterion': 'squared_error', 'max_depth': 70, 'min_samples_leaf': 14, 'min_samples_split': 75, 'n_estimators': 1250, 'random_state': 42} | 0.703574 | -0.362635 | -0.231665 | -0.481288 |
>|  5 | {'bootstrap': True, 'criterion': 'squared_error', 'max_depth': 70, 'min_samples_leaf': 14, 'min_samples_split': 75, 'n_estimators': 1450, 'random_state': 42} | 0.703576 | -0.362624 | -0.231663 | -0.481286 |
>|  6 | {'bootstrap': True, 'criterion': 'squared_error', 'max_depth': 70, 'min_samples_leaf': 14, 'min_samples_split': 75, 'n_estimators': 1500, 'random_state': 42} | 0.703559 | -0.362622 | -0.231676 |   -0.4813 |
></details>


We finally end up using the following:
```python
model = RandomForestRegressor(
    criterion= "squared_error",     # criterion for spitting
    n_estimators= 1500,             # number of trees
    bootstrap= True,                # Whether bootstrap samples are used when building trees. If False, the whole dataset is used to build each tree.
    max_depth= 70,                  # max depth of tree
    min_samples_leaf= 14,           # minimum number of samples required to be at a leaf node
    min_samples_split= 75,          # minimum number of samples required to split
    random_state = 42               # for reproducibility
)
```

</details>

---

## MLPRegressor

<details>
<summary>Show MLPRegressor</summary>


>Using the following set of parameters:
>
>```python
>param_dict = {
>        "hidden_layer_sizes":[(50,50),(75,75),(100,100),(200,200)], # one hidden layer with 100 neurons
>        "activation":["logistic", "tanh","relu"],                   # activation function
>        "solver":["lbfgs", "sgd", "adam"],                          # solver for weight optimization
>        "max_iter":[100,1000,1500],                                 # set the number of iterations
>        "random_state":[42]                                         # for reproducibility
>            }
>```
>
>Obtaining the following results:
><details>
><summary>Show Table</summary>
>
>|    | params                                                                                                               |       r2 |       MAE |       MSE |      RMSE |
>|---:|:---------------------------------------------------------------------------------------------------------------------|---------:|----------:|----------:|----------:|
>| 25 | {'activation': 'logistic', 'hidden_layer_sizes': (100, 100), 'max_iter': 1500, 'random_state': 42, 'solver': 'sgd'}  |  0.64206 | -0.403477 | -0.279766 | -0.528892 |
>| 63 | {'activation': 'tanh', 'hidden_layer_sizes': (200, 200), 'max_iter': 100, 'random_state': 42, 'solver': 'lbfgs'}     | 0.632735 | -0.396114 | -0.287009 |  -0.53564 |
>| 29 | {'activation': 'logistic', 'hidden_layer_sizes': (200, 200), 'max_iter': 100, 'random_state': 42, 'solver': 'adam'}  | 0.530795 | -0.379914 | -0.366871 | -0.605582 |
>| 20 | {'activation': 'logistic', 'hidden_layer_sizes': (100, 100), 'max_iter': 100, 'random_state': 42, 'solver': 'adam'}  | 0.575421 | -0.369898 | -0.331883 | -0.576078 |
>| 27 | {'activation': 'logistic', 'hidden_layer_sizes': (200, 200), 'max_iter': 100, 'random_state': 42, 'solver': 'lbfgs'} | 0.688858 |   -0.3689 | -0.243165 | -0.493084 |
>|  2 | {'activation': 'logistic', 'hidden_layer_sizes': (50, 50), 'max_iter': 100, 'random_state': 42, 'solver': 'adam'}    | 0.633275 | -0.366213 | -0.286627 | -0.535372 |
>| 11 | {'activation': 'logistic', 'hidden_layer_sizes': (75, 75), 'max_iter': 100, 'random_state': 42, 'solver': 'adam'}    | 0.615354 | -0.365067 | -0.300658 |  -0.54832 |
>|  0 | {'activation': 'logistic', 'hidden_layer_sizes': (50, 50), 'max_iter': 100, 'random_state': 42, 'solver': 'lbfgs'}   | 0.691842 | -0.364427 | -0.240811 |  -0.49067 |
>|  9 | {'activation': 'logistic', 'hidden_layer_sizes': (75, 75), 'max_iter': 100, 'random_state': 42, 'solver': 'lbfgs'}   | 0.696994 | -0.363153 | -0.236802 | -0.486604 |
>| 18 | {'activation': 'logistic', 'hidden_layer_sizes': (100, 100), 'max_iter': 100, 'random_state': 42, 'solver': 'lbfgs'} | 0.704031 | -0.361691 | -0.231282 | -0.480858 |
></details>


>Using the following set of parameters:
>```python
>param_dict = {
>        "hidden_layer_sizes":[(90,90),(100,100),(110,110),(90,90,90),(100,100,100),(110,110,110),], # one hidden layer with 100 neurons
>        "activation":["logistic"],                                                                  # activation function
>        "solver":["lbfgs", "adam"],                                                                 # solver for weight optimization
>        "max_iter":[70,80,90,100,110,120,130,1400,1500,1600],                                       # set the number of iterations
>        "random_state":[42]                                                                         # for reproducibility
>            }
>```
>
>Obtaining the following results:
><details>
><summary>Show Table</summary>
>
>|     | params                                                                                                                    |       r2 |       MAE |       MSE |      RMSE |
>|----:|:--------------------------------------------------------------------------------------------------------------------------|---------:|----------:|----------:|----------:|
>|  88 | {'activation': 'logistic', 'hidden_layer_sizes': (100, 100, 100), 'max_iter': 110, 'random_state': 42, 'solver': 'lbfgs'} | 0.705036 | -0.358979 |  -0.23051 | -0.480065 |
>|  28 | {'activation': 'logistic', 'hidden_layer_sizes': (100, 100), 'max_iter': 110, 'random_state': 42, 'solver': 'lbfgs'}      | 0.708728 | -0.357777 | -0.227622 | -0.477028 |
>| 108 | {'activation': 'logistic', 'hidden_layer_sizes': (110, 110, 110), 'max_iter': 110, 'random_state': 42, 'solver': 'lbfgs'} | 0.707896 | -0.357739 | -0.228271 | -0.477726 |
>|  72 | {'activation': 'logistic', 'hidden_layer_sizes': (90, 90, 90), 'max_iter': 130, 'random_state': 42, 'solver': 'lbfgs'}    | 0.709149 | -0.357227 | -0.227259 | -0.476614 |
>|  90 | {'activation': 'logistic', 'hidden_layer_sizes': (100, 100, 100), 'max_iter': 120, 'random_state': 42, 'solver': 'lbfgs'} |  0.70889 | -0.356398 | -0.227501 |  -0.47691 |
>|  30 | {'activation': 'logistic', 'hidden_layer_sizes': (100, 100), 'max_iter': 120, 'random_state': 42, 'solver': 'lbfgs'}      | 0.712401 | -0.356235 | -0.224729 |  -0.47395 |
>|  32 | {'activation': 'logistic', 'hidden_layer_sizes': (100, 100), 'max_iter': 130, 'random_state': 42, 'solver': 'lbfgs'}      | 0.713022 | -0.355285 |  -0.22422 | -0.473362 |
>|  92 | {'activation': 'logistic', 'hidden_layer_sizes': (100, 100, 100), 'max_iter': 130, 'random_state': 42, 'solver': 'lbfgs'} | 0.712112 | -0.354012 |  -0.22498 | -0.474289 |
>| 110 | {'activation': 'logistic', 'hidden_layer_sizes': (110, 110, 110), 'max_iter': 120, 'random_state': 42, 'solver': 'lbfgs'} | 0.714326 | -0.353656 | -0.223261 | -0.472479 |
>| 112 | {'activation': 'logistic', 'hidden_layer_sizes': (110, 110, 110), 'max_iter': 130, 'random_state': 42, 'solver': 'lbfgs'} | 0.718692 | -0.351547 | -0.219844 | -0.468837 |
></details>


>Using the following set of parameters:
>```python
>param_dict = {
>        "hidden_layer_sizes":[(110, 110, 110),(120, 120, 120),(130, 130, 130)], # one hidden layer with 100 neurons
>        "activation":["logistic"],                                              # activation function
>        "solver":["lbfgs"],                                                     # solver for weight optimization
>        "max_iter":[130,140,150],                                               # set the number of iterations
>        "random_state":[42]                                                     # for reproducibility
>            }
>```
>
>Obtaining the following results:
><details>
><summary>Show Table</summary>
>
>|   | params                                                                                                                    |       r2 |       MAE |       MSE |      RMSE |
>|--:|:--------------------------------------------------------------------------------------------------------------------------|---------:|----------:|----------:|----------:|
>| 4 | {'activation': 'logistic', 'hidden_layer_sizes': (120, 120, 120), 'max_iter': 140, 'random_state': 42, 'solver': 'lbfgs'} | 0.713832 | -0.353402 | -0.223595 | -0.472744 |
>| 8 | {'activation': 'logistic', 'hidden_layer_sizes': (130, 130, 130), 'max_iter': 150, 'random_state': 42, 'solver': 'lbfgs'} | 0.714898 | -0.352251 | -0.222782 | -0.471933 |
>| 0 | {'activation': 'logistic', 'hidden_layer_sizes': (110, 110, 110), 'max_iter': 130, 'random_state': 42, 'solver': 'lbfgs'} | 0.718692 | -0.351547 | -0.219844 | -0.468837 |
>| 1 | {'activation': 'logistic', 'hidden_layer_sizes': (110, 110, 110), 'max_iter': 140, 'random_state': 42, 'solver': 'lbfgs'} | 0.720179 | -0.349739 | -0.218662 | -0.467562 |
>| 2 | {'activation': 'logistic', 'hidden_layer_sizes': (110, 110, 110), 'max_iter': 150, 'random_state': 42, 'solver': 'lbfgs'} | 0.722212 | -0.347741 | -0.217066 | -0.465837 |
></details>


>Using the following set of parameters:
>```python
>param_dict = {
>        "hidden_layer_sizes":[(110, 110, 110),(110,110)], # one hidden layer with 100 neurons
>        "activation":["logistic"],                                              # activation function
>        "solver":["lbfgs"],                                                     # solver for weight optimization
>        "max_iter":[150,155,160,165,170,175],                                   # set the number of iterations
>        "random_state":[42]                                                     # for reproducibility
>            }
>```
>
>Obtaining the following results:
><details>
><summary>Show Table</summary>
>
>|     | params                                                                                                                    |       r2 |       MAE |       MSE |      RMSE |
>|----:|:--------------------------------------------------------------------------------------------------------------------------|---------:|----------:|----------:|----------:|
>|   7 | {'activation': 'logistic', 'hidden_layer_sizes': (110, 110), 'max_iter': 155, 'random_state': 42, 'solver': 'lbfgs'}      | 0.690572 | -0.363376 | -0.241803 | -0.491683 |
>| ... | ...                                                                                                                       |      ... |       ... |       ... |       ... |
>|   5 | {'activation': 'logistic', 'hidden_layer_sizes': (110, 110, 110), 'max_iter': 175, 'random_state': 42, 'solver': 'lbfgs'} | 0.721297 | -0.348775 | -0.217773 | -0.466567 |
>|   2 | {'activation': 'logistic', 'hidden_layer_sizes': (110, 110, 110), 'max_iter': 160, 'random_state': 42, 'solver': 'lbfgs'} |  0.72101 | -0.348451 | -0.217994 | -0.466807 |
>|   1 | {'activation': 'logistic', 'hidden_layer_sizes': (110, 110, 110), 'max_iter': 155, 'random_state': 42, 'solver': 'lbfgs'} | 0.721307 | -0.348232 | -0.217772 | -0.466596 |
>|   0 | {'activation': 'logistic', 'hidden_layer_sizes': (110, 110, 110), 'max_iter': 150, 'random_state': 42, 'solver': 'lbfgs'} | 0.722212 | -0.347741 | -0.217066 | -0.465837 |
></details>


>Using the following set of parameters:
>```python
>param_dict = {
>        "hidden_layer_sizes":[(110, 110, 110),(110,110, 110, 110)], # one hidden layer with 100 neurons
>        "activation":["logistic"],                                  # activation function
>        "solver":["lbfgs"],                                         # solver for weight optimization
>        "max_iter":[150],                                           # set the number of iterations
>        "random_state":[42]                                         # for reproducibility
>            }
>```
>
>Obtaining the following results:
><details>
><summary>Show Table</summary>
>
>|   | params                                                                                                                         |       r2 |       MAE |       MSE |      RMSE |
>|--:|:-------------------------------------------------------------------------------------------------------------------------------|---------:|----------:|----------:|----------:|
>| 1 | {'activation': 'logistic', 'hidden_layer_sizes': (110, 110, 110, 110), 'max_iter': 150, 'random_state': 42, 'solver': 'lbfgs'} | 0.703878 | -0.361468 | -0.231462 | -0.481105 |
>| 0 | {'activation': 'logistic', 'hidden_layer_sizes': (110, 110, 110), 'max_iter': 150, 'random_state': 42, 'solver': 'lbfgs'}      | 0.722212 | -0.347741 | -0.217066 | -0.465837 |
></details>

Thus, resulting in the final chose of parameters:
```python
model = MLPRegressor(
    hidden_layer_sizes = (110,110,110),     # one hidden layer with 100 neurons
    activation = "logistic",                # 'relu' activation function
    solver = "lbfgs",                       # 'adam' solver for weight optimization
    max_iter = 150,                         # set the number of iterations
    random_state = 42                       # for reproducibility
)
```

</details>


---

## GradientBoostingRegressor

<details>
<summary>Show GradientBoostingRegressor</summary>

  >Considering the following set of parameters:
  >```python
  >param_dict = {
  >    'loss': ["squared_error", "absolute_error", "huber", "quantile"],
  >    'criterion': ["friedman_mse", "squared_error"],
  >    'learning_rate': [0.001, 0.1, 1, 10],
  >    'n_estimators': [100, 150, 180, 200],
  >    'random_state': [42]                       # for reproducibility
  >            }
  >```
  >
  >Obtaining the following results:
  ><details>
  ><summary>Show</summary>
  >
  >|    | params                                                                                                                  |       r2 |       MAE |       MSE |      RMSE |
  >|---:|:------------------------------------------------------------------------------------------------------------------------|---------:|----------:|----------:|----------:|
  >| 12 | {'criterion': 'friedman_mse', 'learning_rate': 0.1, 'loss': 'squared_error', 'n_estimators': 100, 'random_state': 42}   | 0.715294 | -0.356997 | -0.222515 | -0.471684 |
  >| 66 | {'criterion': 'squared_error', 'learning_rate': 0.1, 'loss': 'huber', 'n_estimators': 100, 'random_state': 42}          | 0.712859 | -0.356073 | -0.224417 | -0.473703 |
  >| 18 | {'criterion': 'friedman_mse', 'learning_rate': 0.1, 'loss': 'huber', 'n_estimators': 100, 'random_state': 42}           | 0.712864 | -0.356065 | -0.224413 | -0.473698 |
  >| 16 | {'criterion': 'friedman_mse', 'learning_rate': 0.1, 'loss': 'absolute_error', 'n_estimators': 150, 'random_state': 42}  | 0.718284 | -0.349204 | -0.220186 | -0.469228 |
  >| 64 | {'criterion': 'squared_error', 'learning_rate': 0.1, 'loss': 'absolute_error', 'n_estimators': 150, 'random_state': 42} | 0.718328 | -0.349112 | -0.220152 | -0.469192 |
  >| 13 | {'criterion': 'friedman_mse', 'learning_rate': 0.1, 'loss': 'squared_error', 'n_estimators': 150, 'random_state': 42}   | 0.728845 | -0.347635 | -0.211924 | -0.460314 |
  >| 61 | {'criterion': 'squared_error', 'learning_rate': 0.1, 'loss': 'squared_error', 'n_estimators': 150, 'random_state': 42}  | 0.728845 | -0.347635 | -0.211924 | -0.460314 |
  >| 67 | {'criterion': 'squared_error', 'learning_rate': 0.1, 'loss': 'huber', 'n_estimators': 150, 'random_state': 42}          | 0.726679 | -0.346321 |  -0.21361 | -0.462141 |
  >| 19 | {'criterion': 'friedman_mse', 'learning_rate': 0.1, 'loss': 'huber', 'n_estimators': 150, 'random_state': 42}           | 0.726684 | -0.346312 | -0.213606 | -0.462137 |
  >| 65 | {'criterion': 'squared_error', 'learning_rate': 0.1, 'loss': 'absolute_error', 'n_estimators': 200, 'random_state': 42} | 0.724747 | -0.344731 | -0.215133 | -0.463808 |
  >| 17 | {'criterion': 'friedman_mse', 'learning_rate': 0.1, 'loss': 'absolute_error', 'n_estimators': 200, 'random_state': 42}  | 0.724852 | -0.344713 | -0.215051 |  -0.46372 |
  >| 14 | {'criterion': 'friedman_mse', 'learning_rate': 0.1, 'loss': 'squared_error', 'n_estimators': 200, 'random_state': 42}   | 0.735761 | -0.342585 | -0.206516 | -0.454396 |
  >| 62 | {'criterion': 'squared_error', 'learning_rate': 0.1, 'loss': 'squared_error', 'n_estimators': 200, 'random_state': 42}  | 0.735761 | -0.342585 | -0.206516 | -0.454396 |
  >| 68 | {'criterion': 'squared_error', 'learning_rate': 0.1, 'loss': 'huber', 'n_estimators': 200, 'random_state': 42}          | 0.733816 |  -0.34163 | -0.208032 |  -0.45607 |
  >| 20 | {'criterion': 'friedman_mse', 'learning_rate': 0.1, 'loss': 'huber', 'n_estimators': 200, 'random_state': 42}           | 0.733819 | -0.341622 | -0.208029 | -0.456066 |
  ></details>
  
  
  >Considering the following set of parameters:
  >```python
  >param_dict = {
  >    'loss': ["squared_error", "huber"],
  >    'criterion': ["squared_error"],
  >    'learning_rate': [0.05, 0.1, 0.15],
  >    'n_estimators': [100,150,200],
  >    'random_state': [42]                       # for reproducibility
  >            }
  >```
  >
  >Obtaining the following results:
  ><details>
  ><summary>Show</summary>
  >
  >|    | params                                                                                                                  |       r2 |       MAE |       MSE |      RMSE |
  >|---:|:------------------------------------------------------------------------------------------------------------------------|---------:|----------:|----------:|----------:|
  >| 12 | {'criterion': 'squared_error', 'learning_rate': 0.15, 'loss': 'squared_error', 'n_estimators': 100, 'random_state': 42} | 0.728236 | -0.348348 | -0.212394 | -0.460815 |
  >|  7 | {'criterion': 'squared_error', 'learning_rate': 0.1, 'loss': 'squared_error', 'n_estimators': 150, 'random_state': 42}  | 0.728845 | -0.347635 | -0.211924 | -0.460314 |
  >| 15 | {'criterion': 'squared_error', 'learning_rate': 0.15, 'loss': 'huber', 'n_estimators': 100, 'random_state': 42}         | 0.726755 | -0.346715 | -0.213566 | -0.462104 |
  >| 10 | {'criterion': 'squared_error', 'learning_rate': 0.1, 'loss': 'huber', 'n_estimators': 150, 'random_state': 42}          | 0.726679 | -0.346321 |  -0.21361 | -0.462141 |
  >|  8 | {'criterion': 'squared_error', 'learning_rate': 0.1, 'loss': 'squared_error', 'n_estimators': 200, 'random_state': 42}  | 0.735761 | -0.342585 | -0.206516 | -0.454396 |
  >| 11 | {'criterion': 'squared_error', 'learning_rate': 0.1, 'loss': 'huber', 'n_estimators': 200, 'random_state': 42}          | 0.733816 |  -0.34163 | -0.208032 |  -0.45607 |
  >| 13 | {'criterion': 'squared_error', 'learning_rate': 0.15, 'loss': 'squared_error', 'n_estimators': 150, 'random_state': 42} | 0.738497 | -0.341278 | -0.204378 | -0.452048 |
  >| 16 | {'criterion': 'squared_error', 'learning_rate': 0.15, 'loss': 'huber', 'n_estimators': 150, 'random_state': 42}         | 0.736048 |  -0.34029 | -0.206291 | -0.454156 |
  >| 14 | {'criterion': 'squared_error', 'learning_rate': 0.15, 'loss': 'squared_error', 'n_estimators': 200, 'random_state': 42} | 0.744032 | -0.337558 | -0.200048 |  -0.44723 |
  >| 17 | {'criterion': 'squared_error', 'learning_rate': 0.15, 'loss': 'huber', 'n_estimators': 200, 'random_state': 42}         | 0.742745 | -0.335803 | -0.201052 | -0.448343 |
  ></details>
  
  
  >Considering the following set of parameters:
  >```python
  >param_dict = {
  >    'loss': ["huber"],
  >    'criterion': ["squared_error"],
  >    'learning_rate': [0.125,0.15, 0.175,0.2],
  >    'n_estimators': [190,200,210,220],
  >    'random_state': [42]                       # for reproducibility
  >            }
  >```
  >
  >Obtaining the following results:
  ><details>
  ><summary>Show</summary>
  >
  >|    | params                                                                                                           |       r2 |       MAE |       MSE |      RMSE |
  >|---:|:-----------------------------------------------------------------------------------------------------------------|---------:|----------:|----------:|----------:|
  >| 12 | {'criterion': 'squared_error', 'learning_rate': 0.2, 'loss': 'huber', 'n_estimators': 190, 'random_state': 42}   | 0.745233 | -0.334489 | -0.199108 | -0.446171 |
  >| 10 | {'criterion': 'squared_error', 'learning_rate': 0.175, 'loss': 'huber', 'n_estimators': 210, 'random_state': 42} | 0.745105 | -0.334474 |  -0.19921 | -0.446297 |
  >| 14 | {'criterion': 'squared_error', 'learning_rate': 0.2, 'loss': 'huber', 'n_estimators': 210, 'random_state': 42}   | 0.745406 |  -0.33439 | -0.198972 | -0.446018 |
  >| 11 | {'criterion': 'squared_error', 'learning_rate': 0.175, 'loss': 'huber', 'n_estimators': 220, 'random_state': 42} | 0.745385 | -0.334275 | -0.198993 | -0.446055 |
  >| 15 | {'criterion': 'squared_error', 'learning_rate': 0.2, 'loss': 'huber', 'n_estimators': 220, 'random_state': 42}   | 0.746034 | -0.333895 | -0.198483 | -0.445468 |
  ></details>
  
  
  >Considering the following set of parameters:
  >```python
  >param_dict = {
  >    'loss': ["huber"],
  >    'criterion': ["squared_error"],
  >    'learning_rate': [0.175,0.18,0.185,0.19,0.195,0.2,0.25,0.3],
  >    'n_estimators': [220,230,240,250,300,500],
  >    'random_state': [42]                       # for reproducibility
  >            }
  >```
  >
  >Obtaining the following results:
  ><details>
  ><summary>Show</summary>
  >
  >|    | params                                                                                                           |       r2 |       MAE |       MSE |      RMSE |
  >|---:|:-----------------------------------------------------------------------------------------------------------------|---------:|----------:|----------:|----------:|
  >|  5 | {'criterion': 'squared_error', 'learning_rate': 0.175, 'loss': 'huber', 'n_estimators': 500, 'random_state': 42} | 0.756745 | -0.325946 | -0.190109 |  -0.43598 |
  >| 35 | {'criterion': 'squared_error', 'learning_rate': 0.2, 'loss': 'huber', 'n_estimators': 500, 'random_state': 42}   | 0.757643 | -0.325644 | -0.189407 | -0.435166 |
  >| 17 | {'criterion': 'squared_error', 'learning_rate': 0.185, 'loss': 'huber', 'n_estimators': 500, 'random_state': 42} | 0.758042 | -0.325253 | -0.189093 | -0.434801 |
  >| 23 | {'criterion': 'squared_error', 'learning_rate': 0.19, 'loss': 'huber', 'n_estimators': 500, 'random_state': 42}  | 0.758687 | -0.325022 | -0.188582 | -0.434202 |
  >| 41 | {'criterion': 'squared_error', 'learning_rate': 0.25, 'loss': 'huber', 'n_estimators': 500, 'random_state': 42}  |  0.75788 |   -0.3248 | -0.189219 | -0.434952 |
  ></details>
  
  
  >Considering the following set of parameters:
  >```python
  >param_dict = {
  >    'loss': ["huber"],
  >    'criterion': ["squared_error"],
  >    'learning_rate': [0.25,0.19],
  >    'n_estimators': [500,750,1000,1500,2000],
  >    'random_state': [42]                       # for reproducibility
  >            }
  >```
  >
  >Obtaining the following results:
  ><details>
  ><summary>Show</summary>
  >
  >|    | params                                                                                                           |       r2 |       MAE |       MSE |      RMSE |
  >|---:|:-----------------------------------------------------------------------------------------------------------------|---------:|----------:|----------:|----------:|
  >|  0 | {'criterion': 'squared_error', 'learning_rate': 0.25, 'loss': 'huber', 'n_estimators': 500, 'random_state': 42}  |  0.75788 |   -0.3248 | -0.189219 | -0.434952 |
  >|  1 | {'criterion': 'squared_error', 'learning_rate': 0.25, 'loss': 'huber', 'n_estimators': 750, 'random_state': 42}  | 0.758392 | -0.324526 | -0.188813 | -0.434484 |
  >|  8 | {'criterion': 'squared_error', 'learning_rate': 0.19, 'loss': 'huber', 'n_estimators': 1500, 'random_state': 42} | 0.760524 | -0.323543 | -0.187152 | -0.432569 |
  >|  6 | {'criterion': 'squared_error', 'learning_rate': 0.19, 'loss': 'huber', 'n_estimators': 750, 'random_state': 42}  | 0.762126 | -0.322156 | -0.185903 | -0.431113 |
  >|  7 | {'criterion': 'squared_error', 'learning_rate': 0.19, 'loss': 'huber', 'n_estimators': 1000, 'random_state': 42} | 0.762397 | -0.321788 | -0.185689 | -0.430871 |
  ></details>


Thus, resulting in the final chose of parameters:

```python
model = GradientBoostingRegressor(
    loss = "huber",
    criterion = "squared_error",
    learning_rate = 0.19,
    n_estimators = 1800,
    random_state = 42                       # for reproducibility
)
```
</details>



---

## ElasticNet

<details>
<summary>Show ElasticNet</summary>

  >Considering the following set of parameters:
  >```python
  >param_dict = {
  >    'alpha': np.logspace(-5, 5, 50, endpoint=True),       # values between e^-5 and e^5
  >    'l1_ratio': np.append(np.arange(0, 1.01, 0.02), 1.0),  # values between 0 and 1, including 1.0
  >    'random_state': [42]                                   # for reproducibility
  >}
  >```
  >
  >Obtaining the following results:
  ><details>
  ><summary>Show</summary>
  >
  >|     | params                                                                                         |        r2 |       MAE |       MSE |      RMSE |
  >|----:|:-----------------------------------------------------------------------------------------------|----------:|----------:|----------:|----------:|
  >| 701 | {'alpha': np.float64(0.004498432668969444), 'l1_ratio': np.float64(0.5), 'random_state': 42}   |  0.648044 | -0.401255 | -0.275097 | -0.524472 |
  >| 742 | {'alpha': np.float64(0.0071968567300115215), 'l1_ratio': np.float64(0.28), 'random_state': 42} |  0.648166 | -0.401251 | -0.275002 | -0.524381 |
  >| 740 | {'alpha': np.float64(0.0071968567300115215), 'l1_ratio': np.float64(0.24), 'random_state': 42} |  0.648291 |  -0.40125 | -0.274904 | -0.524288 |
  >| 695 | {'alpha': np.float64(0.004498432668969444), 'l1_ratio': np.float64(0.38), 'random_state': 42}  |  0.648293 | -0.401249 | -0.274903 | -0.524287 |
  >| 700 | {'alpha': np.float64(0.004498432668969444), 'l1_ratio': np.float64(0.48), 'random_state': 42}  |  0.648092 | -0.401248 | -0.275059 | -0.524436 |
  >| 699 | {'alpha': np.float64(0.004498432668969444), 'l1_ratio': np.float64(0.46), 'random_state': 42}  |  0.648133 | -0.401246 | -0.275028 | -0.524406 |
  >| 741 | {'alpha': np.float64(0.0071968567300115215), 'l1_ratio': np.float64(0.26), 'random_state': 42} |  0.648234 | -0.401245 | -0.274949 | -0.524331 |
  >| 698 | {'alpha': np.float64(0.004498432668969444), 'l1_ratio': np.float64(0.44), 'random_state': 42}  |  0.648178 | -0.401243 | -0.274993 | -0.524373 |
  >| 696 | {'alpha': np.float64(0.004498432668969444), 'l1_ratio': np.float64(0.4), 'random_state': 42}   |  0.648262 | -0.401243 | -0.274927 |  -0.52431 |
  >| 697 | {'alpha': np.float64(0.004498432668969444), 'l1_ratio': np.float64(0.42), 'random_state': 42}  |   0.64822 | -0.401242 |  -0.27496 | -0.524342 |
  ></details>

> [!WARNING]  
> No significant improvement.
> Stick with this for now, but the results are quite useless.
>
>```python
>model = ElasticNet(
>    alpha = 0.00449,
>    l1_ratio = 0.42,
>    random_state = 42                       # for reproducibility
>)
>```

</details>



---

## SVR

<details>
<summary>Show SVR</summary>

  >Considering the following set of parameters:
  >```python
  >param_dict = {
  >    'C': [0.1, 1, 10, 100],
  >    'gamma':[0.01, 0.1, 1],
  >    'epsilon': [0.01, 0.1, 0.5],
  >    'kernel': ["rbf"]
  >            }
  >```
  >
  >Obtaining the following results (after a long time):
  ><details>
  ><summary>Show</summary>
  >
  >|    | params                                     |       r2 |       MAE |       MSE |      RMSE |
  >|---:|:-------------------------------------------|---------:|----------:|----------:|----------:|
  >| 10 | {'C': 1, 'epsilon': 0.01, 'gamma': 0.1}    | 0.297747 | -0.570147 | -0.548993 | -0.740909 |
  >| 22 | {'C': 10, 'epsilon': 0.1, 'gamma': 0.1}    | 0.306368 |  -0.56836 | -0.542254 | -0.736347 |
  >| 19 | {'C': 10, 'epsilon': 0.01, 'gamma': 0.1}   | 0.309437 | -0.566268 | -0.539856 | -0.734716 |
  >|  6 | {'C': 0.1, 'epsilon': 0.5, 'gamma': 0.01}  | 0.415707 | -0.519722 | -0.456746 | -0.675818 |
  >|  3 | {'C': 0.1, 'epsilon': 0.1, 'gamma': 0.01}  | 0.445166 | -0.498947 | -0.433713 |  -0.65855 |
  >|  0 | {'C': 0.1, 'epsilon': 0.01, 'gamma': 0.01} | 0.446551 | -0.497752 | -0.432634 | -0.657729 |
  >| 33 | {'C': 100, 'epsilon': 0.5, 'gamma': 0.01}  | 0.550859 | -0.452786 | -0.351109 | -0.592524 |
  >| 15 | {'C': 1, 'epsilon': 0.5, 'gamma': 0.01}    | 0.556398 | -0.448548 | -0.346773 | -0.588848 |
  >| 24 | {'C': 10, 'epsilon': 0.5, 'gamma': 0.01}   |  0.56227 | -0.445975 | -0.342189 | -0.584947 |
  >| 27 | {'C': 100, 'epsilon': 0.01, 'gamma': 0.01} | 0.551051 | -0.439327 | -0.350962 | -0.592392 |
  >| 30 | {'C': 100, 'epsilon': 0.1, 'gamma': 0.01}  | 0.567326 | -0.431066 | -0.338236 | -0.581559 |
  >| 18 | {'C': 10, 'epsilon': 0.01, 'gamma': 0.01}  | 0.593579 |  -0.41445 | -0.317734 | -0.563611 |
  >| 21 | {'C': 10, 'epsilon': 0.1, 'gamma': 0.01}   |  0.59835 | -0.412571 | -0.314004 | -0.560301 |
  >| 12 | {'C': 1, 'epsilon': 0.1, 'gamma': 0.01}    | 0.598456 | -0.411196 | -0.313871 | -0.560214 |
  >|  9 | {'C': 1, 'epsilon': 0.01, 'gamma': 0.01}   | 0.598927 | -0.409783 | -0.313494 | -0.559877 |
  ></details>
      

  >Considering the following set of parameters:
  >```python
  >param_dict = {
  >    'C': [0.1, 1, 10, 100],
  >    'gamma':["scale", "auto"],        #'gamma':[0.01, 0.1, 1, "scale", "auto"],
  >    'epsilon': [0.001, 0.01, 0.1, 0.5],
  >    'kernel': ["rbf"]         # 'kernel': ["linear", "poly", "rbf"]
  >}
  >```
  >
  >Obtaining the following results:
  ><details>
  ><summary>Show</summary>
  >
  >|    | params                                                         |       r2 |       MAE |       MSE |      RMSE |
  >|---:|:---------------------------------------------------------------|---------:|----------:|----------:|----------:|
  >|  1 | {'C': 1, 'epsilon': 0.005, 'gamma': 'auto', 'kernel': 'rbf'}   | 0.653202 | -0.384458 | -0.271047 | -0.520576 |
  >|  2 | {'C': 1, 'epsilon': 0.008, 'gamma': 'scale', 'kernel': 'rbf'}  | 0.653076 | -0.384429 | -0.271146 | -0.520672 |
  >|  3 | {'C': 1, 'epsilon': 0.008, 'gamma': 'auto', 'kernel': 'rbf'}   | 0.653245 | -0.384413 | -0.271014 | -0.520545 |
  >|  4 | {'C': 1, 'epsilon': 0.01, 'gamma': 'scale', 'kernel': 'rbf'}   | 0.653098 | -0.384404 | -0.271129 | -0.520655 |
  >|  5 | {'C': 1, 'epsilon': 0.01, 'gamma': 'auto', 'kernel': 'rbf'}    | 0.653259 |  -0.38439 | -0.271003 | -0.520535 |
  >|  6 | {'C': 1, 'epsilon': 0.02, 'gamma': 'scale', 'kernel': 'rbf'}   | 0.653282 | -0.384224 | -0.270986 | -0.520519 |
  >|  7 | {'C': 1, 'epsilon': 0.02, 'gamma': 'auto', 'kernel': 'rbf'}    | 0.653442 | -0.384212 | -0.270861 | -0.520399 |
  >|  8 | {'C': 10, 'epsilon': 0.005, 'gamma': 'scale', 'kernel': 'rbf'} | 0.666899 | -0.374239 |  -0.26033 |  -0.51017 |
  >| 10 | {'C': 10, 'epsilon': 0.008, 'gamma': 'scale', 'kernel': 'rbf'} | 0.667245 | -0.374006 |  -0.26006 | -0.509906 |
  >|  9 | {'C': 10, 'epsilon': 0.005, 'gamma': 'auto', 'kernel': 'rbf'}  |  0.66751 | -0.373939 | -0.259851 | -0.509702 |
  >| 12 | {'C': 10, 'epsilon': 0.01, 'gamma': 'scale', 'kernel': 'rbf'}  | 0.667466 |  -0.37385 | -0.259888 | -0.509737 |
  >| 11 | {'C': 10, 'epsilon': 0.008, 'gamma': 'auto', 'kernel': 'rbf'}  | 0.667855 | -0.373705 | -0.259583 | -0.509439 |
  >| 13 | {'C': 10, 'epsilon': 0.01, 'gamma': 'auto', 'kernel': 'rbf'}   | 0.668085 | -0.373545 | -0.259403 | -0.509263 |
  >| 14 | {'C': 10, 'epsilon': 0.02, 'gamma': 'scale', 'kernel': 'rbf'}  | 0.668469 | -0.373166 | -0.259106 |  -0.50897 |
  >| 15 | {'C': 10, 'epsilon': 0.02, 'gamma': 'auto', 'kernel': 'rbf'}   | 0.669079 | -0.372857 | -0.258628 | -0.508501 |
  ></details>
  
  
  >Considering the following set of parameters:
  >```python
  >param_dict = {
  >    'C': [10,25,50],
  >    'gamma':["scale", "auto"],        #'gamma':[0.01, 0.1, 1, "scale", "auto"],
  >    'epsilon': [0.01, 0.02, 0.04, 0.06],
  >    'kernel': ["rbf"]         # 'kernel': ["linear", "poly", "rbf"]
  >            }
  >```
  >
  >Obtaining the following results:
  ><details>
  ><summary>Show</summary>
  >
  >|      | params                                                        |       r2 |       MAE |       MSE |      RMSE |
  >|-----:|:--------------------------------------------------------------|---------:|----------:|----------:|----------:|
  >|    3 | {'C': 10, 'epsilon': 0.02, 'gamma': 'auto', 'kernel': 'rbf'}  | 0.669079 | -0.372857 | -0.258628 | -0.508501 |
  >|    4 | {'C': 10, 'epsilon': 0.04, 'gamma': 'scale', 'kernel': 'rbf'} | 0.670218 | -0.372073 | -0.257744 | -0.507631 |
  >|    5 | {'C': 10, 'epsilon': 0.04, 'gamma': 'auto', 'kernel': 'rbf'}  | 0.670813 | -0.371763 | -0.257278 | -0.507173 |
  >|    6 | {'C': 10, 'epsilon': 0.06, 'gamma': 'scale', 'kernel': 'rbf'} | 0.671574 | -0.371334 | -0.256687 | -0.506586 |
  >|    7 | {'C': 10, 'epsilon': 0.06, 'gamma': 'auto', 'kernel': 'rbf'}  | 0.672133 | -0.371029 | -0.256249 | -0.506155 |
  ></details>
  
  
  >Considering the following set of parameters:
  >```python
  >param_dict = {
  >    'C': [9,10,11],
  >    'gamma':["auto"],        #'gamma':[0.01, 0.1, 1, "scale", "auto"],
  >    'epsilon': [0.06, 0.08, 0.1, 0.15, 0.2],
  >    'kernel': ["rbf"]         # 'kernel': ["linear", "poly", "rbf"]
  >            }
  >```
  >
  >Obtaining the following results:
  ><details>
  ><summary>Show</summary>
  >
  >|   | params                                                      |       r2 |       MAE |       MSE |      RMSE |
  >|--:|:------------------------------------------------------------|---------:|----------:|----------:|----------:|
  >| 7 | {'C': 10, 'epsilon': 0.1, 'gamma': 'auto', 'kernel': 'rbf'} | 0.674444 | -0.370199 | -0.254449 |  -0.50437 |
  >| 0 | {'C': 9, 'epsilon': 0.06, 'gamma': 'auto', 'kernel': 'rbf'} | 0.673394 | -0.370181 | -0.255262 |  -0.50518 |
  >| 1 | {'C': 9, 'epsilon': 0.08, 'gamma': 'auto', 'kernel': 'rbf'} | 0.674563 | -0.369677 |  -0.25435 | -0.504274 |
  >| 3 | {'C': 9, 'epsilon': 0.15, 'gamma': 'auto', 'kernel': 'rbf'} | 0.676519 | -0.369583 | -0.252832 | -0.502766 |
  >| 2 | {'C': 9, 'epsilon': 0.1, 'gamma': 'auto', 'kernel': 'rbf'}  | 0.675401 | -0.369486 | -0.253699 | -0.503627 |
  ></details>
  
  
  >Considering the following set of parameters:
  >```python
  >param_dict = {
  >    'C': [7,8,9],
  >    'gamma':["auto"],        #'gamma':[0.01, 0.1, 1, "scale", "auto"],
  >    'epsilon': [0.1, 0.12, 0.13, 0.15],
  >    'kernel': ["rbf", "poly"]         # 'kernel': ["linear", "poly", "rbf"]
  >            }
  >```
  >
  >Obtaining the following results:
  ><details>
  ><summary>Show</summary>
  >
  >|    | params                                                      |       r2 |       MAE |       MSE |      RMSE |
  >|---:|:------------------------------------------------------------|---------:|----------:|----------:|----------:|
  >| 10 | {'C': 8, 'epsilon': 0.12, 'gamma': 'auto', 'kernel': 'rbf'} | 0.677006 | -0.368669 | -0.252445 | -0.502381 |
  >|  6 | {'C': 7, 'epsilon': 0.15, 'gamma': 'auto', 'kernel': 'rbf'} | 0.677958 | -0.368549 | -0.251704 | -0.501647 |
  >|  4 | {'C': 7, 'epsilon': 0.13, 'gamma': 'auto', 'kernel': 'rbf'} | 0.677781 | -0.368324 | -0.251839 | -0.501781 |
  >|  2 | {'C': 7, 'epsilon': 0.12, 'gamma': 'auto', 'kernel': 'rbf'} | 0.677672 | -0.368245 | -0.251923 | -0.501864 |
  >|  0 | {'C': 7, 'epsilon': 0.1, 'gamma': 'auto', 'kernel': 'rbf'}  | 0.677308 | -0.368073 | -0.252204 | -0.502143 |
  ></details>
  
  
  >Considering the following set of parameters:
  >```python
  >param_dict = {
  >    'C': [4,5,6,7],
  >    'gamma':["auto"],        #'gamma':[0.01, 0.1, 1, "scale", "auto"],
  >    'epsilon': [0.09,0.1,0.11],
  >    'kernel': ["rbf"]         # 'kernel': ["linear", "poly", "rbf"]
  >            }
  >```
  >
  >Obtaining the following results:
  ><details>
  ><summary>Show</summary>
  >
  >|    | params                                                      |       r2 |       MAE |       MSE |      RMSE |
  >|---:|:------------------------------------------------------------|---------:|----------:|----------:|----------:|
  >|  6 | {'C': 6, 'epsilon': 0.09, 'gamma': 'auto', 'kernel': 'rbf'} |  0.67809 | -0.367422 | -0.251591 | -0.501537 |
  >|  0 | {'C': 4, 'epsilon': 0.09, 'gamma': 'auto', 'kernel': 'rbf'} | 0.678641 | -0.367398 |  -0.25116 | -0.501119 |
  >|  5 | {'C': 5, 'epsilon': 0.11, 'gamma': 'auto', 'kernel': 'rbf'} | 0.678833 | -0.367341 |  -0.25101 | -0.500962 |
  >|  4 | {'C': 5, 'epsilon': 0.1, 'gamma': 'auto', 'kernel': 'rbf'}  | 0.678777 | -0.367213 | -0.251054 | -0.501006 |
  >|  3 | {'C': 5, 'epsilon': 0.09, 'gamma': 'auto', 'kernel': 'rbf'} | 0.678719 | -0.367152 | -0.251099 | -0.501051 |
  ></details>
  
  
  >Considering the following set of parameters:
  >```python
  >param_dict = {
  >    'C': [5],
  >    'gamma':["auto", 0.001,0.00001,0.000001, "scale"],        #'gamma':[0.01, 0.1, 1, "scale", "auto"],
  >    'epsilon': [0.09],
  >    'kernel': ["rbf"]         # 'kernel': ["linear", "poly", "rbf"]
  >            }
  >```
  >
  >Obtaining the following results:
  ><details>
  ><summary>Show</summary>
  >
  >|    | params                                                       |       r2 |       MAE |       MSE |      RMSE |
  >|---:|:-------------------------------------------------------------|---------:|----------:|----------:|----------:|
  >|  3 | {'C': 5, 'epsilon': 0.09, 'gamma': 1e-06, 'kernel': 'rbf'}   | 0.205469 |  -0.62215 | -0.621079 | -0.788078 |
  >|  2 | {'C': 5, 'epsilon': 0.09, 'gamma': 1e-05, 'kernel': 'rbf'}   | 0.571467 | -0.442974 | -0.334979 | -0.578741 |
  >|  4 | {'C': 5, 'epsilon': 0.09, 'gamma': 'scale', 'kernel': 'rbf'} | 0.678239 | -0.367377 | -0.251474 | -0.501423 |
  >|  0 | {'C': 5, 'epsilon': 0.09, 'gamma': 'auto', 'kernel': 'rbf'}  | 0.678719 | -0.367152 | -0.251099 | -0.501051 |
  >|  1 | {'C': 5, 'epsilon': 0.09, 'gamma': 0.001, 'kernel': 'rbf'}   | 0.686324 | -0.366278 | -0.245143 | -0.495073 |
  ></details>
  
  
  >Considering the following set of parameters:
  >```python
  >param_dict = {
  >    'C': [5],
  >    'gamma':[0.0005,0.001,0.0015,0.002,0.0025],        #'gamma':[0.01, 0.1, 1, "scale", "auto"],
  >    'epsilon': [0.09],
  >    'kernel': ["rbf"]         # 'kernel': ["linear", "poly", "rbf"]
  >            }
  >```
  >
  >Obtaining the following results:
  ><details>
  ><summary>Show</summary>
  >
  >|    | params                                                      |       r2 |       MAE |       MSE |      RMSE |
  >|---:|:------------------------------------------------------------|---------:|----------:|----------:|----------:|
  >|  0 | {'C': 5, 'epsilon': 0.09, 'gamma': 0.0005, 'kernel': 'rbf'} | 0.670657 | -0.379656 | -0.257383 | -0.507286 |
  >|  4 | {'C': 5, 'epsilon': 0.09, 'gamma': 0.0025, 'kernel': 'rbf'} | 0.679771 | -0.366659 | -0.250276 | -0.500231 |
  >|  1 | {'C': 5, 'epsilon': 0.09, 'gamma': 0.001, 'kernel': 'rbf'}  | 0.686324 | -0.366278 | -0.245143 | -0.495073 |
  >|  3 | {'C': 5, 'epsilon': 0.09, 'gamma': 0.002, 'kernel': 'rbf'}  | 0.685726 | -0.363967 | -0.245619 | -0.495562 |
  >|  2 | {'C': 5, 'epsilon': 0.09, 'gamma': 0.0015, 'kernel': 'rbf'} | 0.689032 | -0.362902 | -0.243032 | -0.492941 |
  ></details>


Thus, we use the following parameter:
```python
model = SVR(
    C = 5,
    gamma = 0.0015,
    epsilon = 0.09,
    kernel = "rbf"
)
```
</details>


---

## XGBoost

<details>
<summary>Show XGBoost</summary>

  >Considering the following set of parameters:
  >```python
  >param_dict = {
  >    'n_estimators': [100, 400, 800],
  >    'max_depth': [3, 6, 9],
  >    'learning_rate': [0.05, 0.1, 0.20],
  >    'min_child_weight': [1, 10, 100],
  >    'random_state': [42]                       # for reproducibility
  >            }
  >```
  >
  >Obtaining the following results:
  ><details>
  ><summary>Show</summary>
  >
  >|    | params                                                                                                   |       r2 |       MAE |       MSE |      RMSE |
  >|---:|:---------------------------------------------------------------------------------------------------------|---------:|----------:|----------:|----------:|
  >| 47 | {'learning_rate': 0.1, 'max_depth': 9, 'min_child_weight': 1, 'n_estimators': 800, 'random_state': 42}   | 0.771364 | -0.316816 | -0.178693 | -0.422705 |
  >| 22 | {'learning_rate': 0.05, 'max_depth': 9, 'min_child_weight': 10, 'n_estimators': 400, 'random_state': 42} |  0.77138 | -0.316689 | -0.178692 | -0.422705 |
  >| 23 | {'learning_rate': 0.05, 'max_depth': 9, 'min_child_weight': 10, 'n_estimators': 800, 'random_state': 42} | 0.771534 | -0.316614 | -0.178571 | -0.422564 |
  >| 19 | {'learning_rate': 0.05, 'max_depth': 9, 'min_child_weight': 1, 'n_estimators': 400, 'random_state': 42}  | 0.771743 | -0.316607 | -0.178394 | -0.422331 |
  >| 37 | {'learning_rate': 0.1, 'max_depth': 6, 'min_child_weight': 1, 'n_estimators': 400, 'random_state': 42}   | 0.772419 | -0.316148 | -0.177867 |  -0.42169 |
  >| 46 | {'learning_rate': 0.1, 'max_depth': 9, 'min_child_weight': 1, 'n_estimators': 400, 'random_state': 42}   | 0.772233 | -0.315857 | -0.178013 | -0.421898 |
  >| 11 | {'learning_rate': 0.05, 'max_depth': 6, 'min_child_weight': 1, 'n_estimators': 800, 'random_state': 42}  | 0.773699 | -0.315214 | -0.176866 | -0.420509 |
  >| 14 | {'learning_rate': 0.05, 'max_depth': 6, 'min_child_weight': 10, 'n_estimators': 800, 'random_state': 42} | 0.773306 | -0.315135 | -0.177181 | -0.420904 |
  >| 20 | {'learning_rate': 0.05, 'max_depth': 9, 'min_child_weight': 1, 'n_estimators': 800, 'random_state': 42}  | 0.774637 | -0.314057 | -0.176129 | -0.419643 |
  >| 38 | {'learning_rate': 0.1, 'max_depth': 6, 'min_child_weight': 1, 'n_estimators': 800, 'random_state': 42}   | 0.775236 | -0.313642 | -0.175671 | -0.419086 |
  ></details>
  
  
  >Considering the following set of parameters:
  >```python
  >param_dict = {
  >    'n_estimators': [700,800,900,1000,1500],
  >    'max_depth': [5,6,7],
  >    'learning_rate': [0.04, 0.05, 0.06, 0.07, 0.08, 0.09, 0.1, 0.11],
  >    'min_child_weight': [1,3,5,7,9],
  >    'random_state': [42]                       # for reproducibility
  >            }
  >```
  >
  >Obtaining the following results:
  ><details>
  ><summary>Show</summary>
  >
  >|     | params                                                                                                   |       r2 |       MAE |       MSE |      RMSE |
  >|----:|:---------------------------------------------------------------------------------------------------------|---------:|----------:|----------:|----------:|
  >| 127 | {'learning_rate': 0.05, 'max_depth': 7, 'min_child_weight': 1, 'n_estimators': 900, 'random_state': 42}  | 0.776719 | -0.312362 | -0.174517 | -0.417717 |
  >|  57 | {'learning_rate': 0.04, 'max_depth': 7, 'min_child_weight': 3, 'n_estimators': 900, 'random_state': 42}  | 0.776782 | -0.312291 | -0.174461 | -0.417665 |
  >| 353 | {'learning_rate': 0.08, 'max_depth': 7, 'min_child_weight': 1, 'n_estimators': 1000, 'random_state': 42} | 0.776919 | -0.312259 | -0.174366 | -0.417544 |
  >| 350 | {'learning_rate': 0.08, 'max_depth': 7, 'min_child_weight': 1, 'n_estimators': 700, 'random_state': 42}  | 0.777295 | -0.312203 | -0.174069 | -0.417185 |
  >| 351 | {'learning_rate': 0.08, 'max_depth': 7, 'min_child_weight': 1, 'n_estimators': 800, 'random_state': 42}  |  0.77732 | -0.312174 | -0.174051 | -0.417163 |
  >| 128 | {'learning_rate': 0.05, 'max_depth': 7, 'min_child_weight': 1, 'n_estimators': 1000, 'random_state': 42} | 0.776968 | -0.312141 | -0.174323 | -0.417485 |
  >| 352 | {'learning_rate': 0.08, 'max_depth': 7, 'min_child_weight': 1, 'n_estimators': 900, 'random_state': 42}  | 0.777235 | -0.312121 | -0.174119 | -0.417246 |
  >|  54 | {'learning_rate': 0.04, 'max_depth': 7, 'min_child_weight': 1, 'n_estimators': 1500, 'random_state': 42} | 0.777056 | -0.312064 | -0.174248 | -0.417397 |
  >|  58 | {'learning_rate': 0.04, 'max_depth': 7, 'min_child_weight': 3, 'n_estimators': 1000, 'random_state': 42} | 0.777125 | -0.312006 | -0.174193 | -0.417344 |
  >|  59 | {'learning_rate': 0.04, 'max_depth': 7, 'min_child_weight': 3, 'n_estimators': 1500, 'random_state': 42} | 0.777246 | -0.311816 | -0.174099 | -0.417227 |
  ></details>


  >Considering the following set of parameters:
  >```python
  >param_dict = {
  >    'n_estimators': [1500,1600,1750,2000],
  >    'max_depth': [6,7,8],
  >    'learning_rate': [0.03,0.04,0.05],
  >    'min_child_weight': [2,3,4],
  >    'random_state': [42]                       # for reproducibility
  >            }
  >```
  >
  >Obtaining the following results:
  ><details>
  ><summary>Show</summary>
  >
  >|    | params                                                                                                   |       r2 |       MAE |        MSE |      RMSE |
  >|---:|:---------------------------------------------------------------------------------------------------------|---------:|----------:|-----------:|----------:|
  >| 53 | {'learning_rate': 0.04, 'max_depth': 7, 'min_child_weight': 3, 'n_estimators': 1600, 'random_state': 42} | 0.777136 | -0.311821 |  -0.174185 | -0.417331 |
  >| 15 | {'learning_rate': 0.03, 'max_depth': 7, 'min_child_weight': 2, 'n_estimators': 2000, 'random_state': 42} | 0.777502 | -0.311817 |  -0.173901 | -0.416984 |
  >| 52 | {'learning_rate': 0.04, 'max_depth': 7, 'min_child_weight': 3, 'n_estimators': 1500, 'random_state': 42} | 0.777246 | -0.311816 |  -0.174099 | -0.417227 |
  >| 13 | {'learning_rate': 0.03, 'max_depth': 7, 'min_child_weight': 2, 'n_estimators': 1600, 'random_state': 42} | 0.777527 | -0.311744 |  -0.173881 | -0.416961 |
  >| 14 | {'learning_rate': 0.03, 'max_depth': 7, 'min_child_weight': 2, 'n_estimators': 1750, 'random_state': 42} | 0.777706 | -0.311622 |  -0.173741 | -0.416792 |
  ></details>


  >Considering the following set of parameters:
  >```python
  >param_dict = {
  >    'n_estimators': [1650,1700,1750,1800],
  >    'max_depth': [7],
  >    'learning_rate': [0.02,0.025,0.03],
  >    'min_child_weight': [2,3],
  >    'random_state': [42]                       # for reproducibility
  >            }
  >```
  >
  >Obtaining the following results:
  ><details>
  ><summary>Show</summary>
  >
  >|    | params                                                                                                   |       r2 |       MAE |       MSE |      RMSE |
  >|---:|:---------------------------------------------------------------------------------------------------------|---------:|----------:|----------:|----------:|
  >| 20 | {'learning_rate': 0.03, 'max_depth': 7, 'min_child_weight': 3, 'n_estimators': 1650, 'random_state': 42} | 0.777946 |  -0.31203 | -0.173557 | -0.416579 |
  >| 16 | {'learning_rate': 0.03, 'max_depth': 7, 'min_child_weight': 2, 'n_estimators': 1650, 'random_state': 42} | 0.777601 | -0.311688 | -0.173823 | -0.416892 |
  >| 19 | {'learning_rate': 0.03, 'max_depth': 7, 'min_child_weight': 2, 'n_estimators': 1800, 'random_state': 42} | 0.777693 | -0.311661 | -0.173751 | -0.416804 |
  >| 17 | {'learning_rate': 0.03, 'max_depth': 7, 'min_child_weight': 2, 'n_estimators': 1700, 'random_state': 42} | 0.777657 | -0.311654 | -0.173779 | -0.416839 |
  >| 18 | {'learning_rate': 0.03, 'max_depth': 7, 'min_child_weight': 2, 'n_estimators': 1750, 'random_state': 42} | 0.777706 | -0.311622 | -0.173741 | -0.416792 |
  ></details>

Obtaining the final parameters:
```python
model = XGBRegressor(
    n_estimators = 1750,
    max_depth = 7,
    learning_rate = 0.03,
    min_child_weight = 2,
    random_state = 42                       # for reproducibility
)
```
</details>



</details>




</details>

---

---