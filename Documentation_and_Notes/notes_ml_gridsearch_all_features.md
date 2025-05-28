# Another Parameter Search

Below parameter tables are presented using **no** feature selection before using the model itself.
The model itself might use a feature selection as part of its process.

## Tables
<details>
<summary>Show</summary>


### ElasticNet
<details>
<summary>Show</summary>

|     | params                                                                                         |       r2 |       MAE |       MSE |      RMSE | 
|----:|:-----------------------------------------------------------------------------------------------|---------:|----------:|----------:|----------:|
| 742 | {'alpha': np.float64(0.0071968567300115215), 'l1_ratio': np.float64(0.28), 'random_state': 42} | 0.654281 | -0.397371 | -0.270223 | -0.519796 |
| 700 | {'alpha': np.float64(0.004498432668969444), 'l1_ratio': np.float64(0.48), 'random_state': 42}  | 0.654215 | -0.397361 | -0.270275 | -0.519845 |
| 703 | {'alpha': np.float64(0.004498432668969444), 'l1_ratio': np.float64(0.54), 'random_state': 42}  | 0.654181 | -0.397354 | -0.270302 | -0.519871 |
| 701 | {'alpha': np.float64(0.004498432668969444), 'l1_ratio': np.float64(0.5), 'random_state': 42}   | 0.654215 | -0.397344 | -0.270275 | -0.519845 |
| 789 | {'alpha': np.float64(0.011513953993264481), 'l1_ratio': np.float64(0.18), 'random_state': 42}  |  0.65435 | -0.397344 |  -0.27017 | -0.519745 |
| 702 | {'alpha': np.float64(0.004498432668969444), 'l1_ratio': np.float64(0.52), 'random_state': 42}  | 0.654206 | -0.397341 | -0.270282 | -0.519852 |
| 745 | {'alpha': np.float64(0.0071968567300115215), 'l1_ratio': np.float64(0.34), 'random_state': 42} | 0.654257 |  -0.39734 | -0.270243 | -0.519815 |
| 743 | {'alpha': np.float64(0.0071968567300115215), 'l1_ratio': np.float64(0.3), 'random_state': 42}  | 0.654304 | -0.397331 | -0.270206 | -0.519779 |
| 790 | {'alpha': np.float64(0.011513953993264481), 'l1_ratio': np.float64(0.2), 'random_state': 42}   | 0.654336 |  -0.39733 | -0.270181 | -0.519756 |
| 744 | {'alpha': np.float64(0.0071968567300115215), 'l1_ratio': np.float64(0.32), 'random_state': 42} | 0.654296 |  -0.39732 | -0.270211 | -0.519784 |


|     | params                                                                                                       |       r2 |       MAE |       MSE |      RMSE | 
|----:|:-------------------------------------------------------------------------------------------------------------|---------:|----------:|----------:|----------:|
| 709 | {'alpha': np.float64(0.008700000000000005), 'l1_ratio': np.float64(0.26000000000000006), 'random_state': 42} | 0.654325 | -0.397319 | -0.270189 | -0.519763 |
| 306 | {'alpha': np.float64(0.007700000000000002), 'l1_ratio': np.float64(0.2950000000000001), 'random_state': 42}  |  0.65431 | -0.397319 | -0.270201 | -0.519775 |
| 789 | {'alpha': np.float64(0.008900000000000005), 'l1_ratio': np.float64(0.25000000000000006), 'random_state': 42} | 0.654332 | -0.397319 | -0.270184 | -0.519758 |
| 870 | {'alpha': np.float64(0.009100000000000006), 'l1_ratio': np.float64(0.24500000000000005), 'random_state': 42} | 0.654334 | -0.397319 | -0.270183 | -0.519757 |
| 507 | {'alpha': np.float64(0.008200000000000002), 'l1_ratio': np.float64(0.2750000000000001), 'random_state': 42}  | 0.654319 | -0.397319 | -0.270194 | -0.519768 |
| 830 | {'alpha': np.float64(0.009000000000000005), 'l1_ratio': np.float64(0.25000000000000006), 'random_state': 42} |  0.65433 | -0.397319 | -0.270185 |  -0.51976 |
| 547 | {'alpha': np.float64(0.008300000000000004), 'l1_ratio': np.float64(0.2700000000000001), 'random_state': 42}  | 0.654322 | -0.397319 | -0.270191 | -0.519765 |
| 628 | {'alpha': np.float64(0.008500000000000004), 'l1_ratio': np.float64(0.26500000000000007), 'random_state': 42} | 0.654324 | -0.397319 |  -0.27019 | -0.519764 |
| 668 | {'alpha': np.float64(0.008600000000000003), 'l1_ratio': np.float64(0.26000000000000006), 'random_state': 42} | 0.654327 | -0.397319 | -0.270188 | -0.519762 |
| 749 | {'alpha': np.float64(0.008800000000000006), 'l1_ratio': np.float64(0.25500000000000006), 'random_state': 42} | 0.654329 | -0.397319 | -0.270186 | -0.519761 |


</details>



### RandomForest
<details>
<summary>Show</summary>

|    | params                                                                                                                                                         |       r2 |       MAE |       MSE |      RMSE | 
|---:|:---------------------------------------------------------------------------------------------------------------------------------------------------------------|---------:|----------:|----------:|----------:|
|  9 | {'bootstrap': False, 'criterion': 'squared_error', 'max_depth': 70, 'min_samples_leaf': 14, 'min_samples_split': 75, 'n_estimators': 2000, 'random_state': 42} | 0.652227 | -0.392916 | -0.271818 | -0.521326 |
| 11 | {'bootstrap': False, 'criterion': 'squared_error', 'max_depth': 70, 'min_samples_leaf': 14, 'min_samples_split': 75, 'n_estimators': 5000, 'random_state': 42} | 0.652227 | -0.392916 | -0.271818 | -0.521326 |
| 10 | {'bootstrap': False, 'criterion': 'squared_error', 'max_depth': 70, 'min_samples_leaf': 14, 'min_samples_split': 75, 'n_estimators': 2500, 'random_state': 42} | 0.652227 | -0.392916 | -0.271817 | -0.521326 |
|  6 | {'bootstrap': False, 'criterion': 'squared_error', 'max_depth': 70, 'min_samples_leaf': 14, 'min_samples_split': 75, 'n_estimators': 500, 'random_state': 42}  | 0.652227 | -0.392916 | -0.271818 | -0.521326 |
|  0 | {'bootstrap': True, 'criterion': 'squared_error', 'max_depth': 70, 'min_samples_leaf': 14, 'min_samples_split': 75, 'n_estimators': 500, 'random_state': 42}   | 0.703339 | -0.362841 | -0.231847 | -0.481478 |
|  4 | {'bootstrap': True, 'criterion': 'squared_error', 'max_depth': 70, 'min_samples_leaf': 14, 'min_samples_split': 75, 'n_estimators': 2500, 'random_state': 42}  | 0.703391 | -0.362694 | -0.231807 | -0.481436 |
|  5 | {'bootstrap': True, 'criterion': 'squared_error', 'max_depth': 70, 'min_samples_leaf': 14, 'min_samples_split': 75, 'n_estimators': 5000, 'random_state': 42}  | 0.703382 |  -0.36268 | -0.231814 | -0.481443 |
|  3 | {'bootstrap': True, 'criterion': 'squared_error', 'max_depth': 70, 'min_samples_leaf': 14, 'min_samples_split': 75, 'n_estimators': 2000, 'random_state': 42}  | 0.703446 |  -0.36265 | -0.231764 | -0.481391 |
|  1 | {'bootstrap': True, 'criterion': 'squared_error', 'max_depth': 70, 'min_samples_leaf': 14, 'min_samples_split': 75, 'n_estimators': 1000, 'random_state': 42}  | 0.703531 | -0.362645 | -0.231698 | -0.481324 |
|  2 | {'bootstrap': True, 'criterion': 'squared_error', 'max_depth': 70, 'min_samples_leaf': 14, 'min_samples_split': 75, 'n_estimators': 1500, 'random_state': 42}  | 0.703559 | -0.362621 | -0.231676 |   -0.4813 |


|   | params                                                                                                                                                        |       r2 |       MAE |       MSE |      RMSE | 
|--:|:--------------------------------------------------------------------------------------------------------------------------------------------------------------|---------:|----------:|----------:|----------:|
| 0 | {'bootstrap': True, 'criterion': 'squared_error', 'max_depth': 70, 'min_samples_leaf': 14, 'min_samples_split': 75, 'n_estimators': 1400, 'random_state': 42} | 0.703574 | -0.362642 | -0.231665 | -0.481289 |
| 3 | {'bootstrap': True, 'criterion': 'squared_error', 'max_depth': 70, 'min_samples_leaf': 14, 'min_samples_split': 75, 'n_estimators': 1700, 'random_state': 42} | 0.703521 |  -0.36264 | -0.231706 | -0.481331 |
| 2 | {'bootstrap': True, 'criterion': 'squared_error', 'max_depth': 70, 'min_samples_leaf': 14, 'min_samples_split': 75, 'n_estimators': 1600, 'random_state': 42} | 0.703547 | -0.362634 | -0.231685 | -0.481309 |
| 1 | {'bootstrap': True, 'criterion': 'squared_error', 'max_depth': 70, 'min_samples_leaf': 14, 'min_samples_split': 75, 'n_estimators': 1500, 'random_state': 42} | 0.703559 | -0.362621 | -0.231676 |   -0.4813 |

</details>



### GradientBoosting
<details>
<summary>Show</summary>

|    | params                                                                                                                  |       r2 |       MAE |       MSE |      RMSE | 
|---:|:------------------------------------------------------------------------------------------------------------------------|---------:|----------:|----------:|----------:|
| 23 | {'criterion': 'friedman_mse', 'learning_rate': 0.1, 'loss': 'absolute_error', 'n_estimators': 200, 'random_state': 42}  | 0.723723 | -0.345445 | -0.215933 | -0.464667 |
| 87 | {'criterion': 'squared_error', 'learning_rate': 0.1, 'loss': 'absolute_error', 'n_estimators': 200, 'random_state': 42} | 0.723723 | -0.345445 | -0.215933 | -0.464667 |
| 82 | {'criterion': 'squared_error', 'learning_rate': 0.1, 'loss': 'squared_error', 'n_estimators': 180, 'random_state': 42}  | 0.731969 | -0.345229 | -0.209478 | -0.457655 |
| 18 | {'criterion': 'friedman_mse', 'learning_rate': 0.1, 'loss': 'squared_error', 'n_estimators': 180, 'random_state': 42}   | 0.731969 | -0.345229 | -0.209478 | -0.457655 |
| 26 | {'criterion': 'friedman_mse', 'learning_rate': 0.1, 'loss': 'huber', 'n_estimators': 180, 'random_state': 42}           |  0.73067 | -0.343763 | -0.210494 | -0.458759 |
| 90 | {'criterion': 'squared_error', 'learning_rate': 0.1, 'loss': 'huber', 'n_estimators': 180, 'random_state': 42}          |  0.73067 | -0.343763 | -0.210494 | -0.458759 |
| 83 | {'criterion': 'squared_error', 'learning_rate': 0.1, 'loss': 'squared_error', 'n_estimators': 200, 'random_state': 42}  | 0.734667 | -0.343299 | -0.207369 | -0.455343 |
| 19 | {'criterion': 'friedman_mse', 'learning_rate': 0.1, 'loss': 'squared_error', 'n_estimators': 200, 'random_state': 42}   | 0.734667 | -0.343299 | -0.207369 | -0.455343 |
| 27 | {'criterion': 'friedman_mse', 'learning_rate': 0.1, 'loss': 'huber', 'n_estimators': 200, 'random_state': 42}           | 0.733025 | -0.342181 | -0.208652 | -0.456747 |
| 91 | {'criterion': 'squared_error', 'learning_rate': 0.1, 'loss': 'huber', 'n_estimators': 200, 'random_state': 42}          | 0.733025 | -0.342181 | -0.208652 | -0.456747 |


|    | params                                                                                                           |       r2 |       MAE |       MSE |      RMSE | 
|---:|:-----------------------------------------------------------------------------------------------------------------|---------:|----------:|----------:|----------:|
|  7 | {'criterion': 'friedman_mse', 'learning_rate': 0.07, 'loss': 'huber', 'n_estimators': 1000, 'random_state': 42}  | 0.753199 |  -0.32901 | -0.192871 |  -0.43912 |
| 23 | {'criterion': 'squared_error', 'learning_rate': 0.07, 'loss': 'huber', 'n_estimators': 1000, 'random_state': 42} | 0.753199 |  -0.32901 | -0.192871 |  -0.43912 |
| 26 | {'criterion': 'squared_error', 'learning_rate': 0.1, 'loss': 'huber', 'n_estimators': 750, 'random_state': 42}   | 0.753413 | -0.328381 | -0.192699 | -0.438909 |
| 10 | {'criterion': 'friedman_mse', 'learning_rate': 0.1, 'loss': 'huber', 'n_estimators': 750, 'random_state': 42}    | 0.753413 | -0.328381 | -0.192699 | -0.438909 |
| 11 | {'criterion': 'friedman_mse', 'learning_rate': 0.1, 'loss': 'huber', 'n_estimators': 1000, 'random_state': 42}   | 0.756977 | -0.325705 | -0.189913 | -0.435726 |
| 27 | {'criterion': 'squared_error', 'learning_rate': 0.1, 'loss': 'huber', 'n_estimators': 1000, 'random_state': 42}  | 0.756977 | -0.325705 | -0.189913 | -0.435726 |
| 30 | {'criterion': 'squared_error', 'learning_rate': 0.13, 'loss': 'huber', 'n_estimators': 750, 'random_state': 42}  | 0.757405 | -0.325679 | -0.189582 | -0.435352 |
| 14 | {'criterion': 'friedman_mse', 'learning_rate': 0.13, 'loss': 'huber', 'n_estimators': 750, 'random_state': 42}   | 0.757405 | -0.325679 | -0.189582 | -0.435352 |
| 15 | {'criterion': 'friedman_mse', 'learning_rate': 0.13, 'loss': 'huber', 'n_estimators': 1000, 'random_state': 42}  | 0.760983 | -0.322617 |  -0.18679 | -0.432139 |
| 31 | {'criterion': 'squared_error', 'learning_rate': 0.13, 'loss': 'huber', 'n_estimators': 1000, 'random_state': 42} | 0.760983 | -0.322617 |  -0.18679 | -0.432139 |

</details>



### MLPR
<details>
<summary>Show</summary>

|    | params                                                                                                               |       r2 |       MAE |       MSE |      RMSE | 
|---:|:---------------------------------------------------------------------------------------------------------------------|---------:|----------:|----------:|----------:|
| 13 | {'activation': 'logistic', 'hidden_layer_sizes': (75, 75), 'max_iter': 1000, 'random_state': 42, 'solver': 'sgd'}    | 0.642962 | -0.402087 | -0.279042 | -0.528198 |
| 16 | {'activation': 'logistic', 'hidden_layer_sizes': (75, 75), 'max_iter': 1500, 'random_state': 42, 'solver': 'sgd'}    | 0.642962 | -0.402087 | -0.279042 | -0.528198 |
| 25 | {'activation': 'logistic', 'hidden_layer_sizes': (100, 100), 'max_iter': 1500, 'random_state': 42, 'solver': 'sgd'}  |  0.64307 | -0.402052 | -0.278958 | -0.528113 |
| 22 | {'activation': 'logistic', 'hidden_layer_sizes': (100, 100), 'max_iter': 1000, 'random_state': 42, 'solver': 'sgd'}  |  0.64307 | -0.402052 | -0.278958 | -0.528113 |
|  7 | {'activation': 'logistic', 'hidden_layer_sizes': (50, 50), 'max_iter': 1500, 'random_state': 42, 'solver': 'sgd'}    | 0.643929 | -0.401329 | -0.278287 | -0.527497 |
|  4 | {'activation': 'logistic', 'hidden_layer_sizes': (50, 50), 'max_iter': 1000, 'random_state': 42, 'solver': 'sgd'}    | 0.643929 | -0.401329 | -0.278287 | -0.527497 |
| 27 | {'activation': 'logistic', 'hidden_layer_sizes': (200, 200), 'max_iter': 100, 'random_state': 42, 'solver': 'lbfgs'} | 0.672242 | -0.382485 | -0.256114 | -0.505993 |
|  0 | {'activation': 'logistic', 'hidden_layer_sizes': (50, 50), 'max_iter': 100, 'random_state': 42, 'solver': 'lbfgs'}   | 0.677243 | -0.374854 | -0.252176 | -0.502027 |
| 18 | {'activation': 'logistic', 'hidden_layer_sizes': (100, 100), 'max_iter': 100, 'random_state': 42, 'solver': 'lbfgs'} | 0.685863 | -0.370638 | -0.245452 |  -0.49519 |
|  9 | {'activation': 'logistic', 'hidden_layer_sizes': (75, 75), 'max_iter': 100, 'random_state': 42, 'solver': 'lbfgs'}   | 0.694034 | -0.365579 | -0.239094 | -0.488823 |


|    | params                                                                                                                     |       r2 |       MAE |       MSE |      RMSE | 
|---:|:---------------------------------------------------------------------------------------------------------------------------|---------:|----------:|----------:|----------:|
|  6 | {'activation': 'logistic', 'hidden_layer_sizes': (75, 75, 75), 'max_iter': 100, 'random_state': 42, 'solver': 'lbfgs'}     | 0.687864 | -0.373167 | -0.243925 | -0.493679 |
|  2 | {'activation': 'logistic', 'hidden_layer_sizes': (75, 75), 'max_iter': 150, 'random_state': 42, 'solver': 'lbfgs'}         | 0.680791 | -0.371791 | -0.249497 | -0.499481 |
| 14 | {'activation': 'logistic', 'hidden_layer_sizes': (75, 75, 75, 75), 'max_iter': 250, 'random_state': 42, 'solver': 'lbfgs'} | 0.682295 | -0.369681 | -0.248353 | -0.498276 |
|  8 | {'activation': 'logistic', 'hidden_layer_sizes': (75, 75, 75), 'max_iter': 200, 'random_state': 42, 'solver': 'lbfgs'}     | 0.683425 | -0.369112 | -0.247357 | -0.497234 |
| 11 | {'activation': 'logistic', 'hidden_layer_sizes': (75, 75, 75, 75), 'max_iter': 100, 'random_state': 42, 'solver': 'lbfgs'} | 0.697561 | -0.366616 | -0.236353 | -0.486009 |
| 13 | {'activation': 'logistic', 'hidden_layer_sizes': (75, 75, 75, 75), 'max_iter': 200, 'random_state': 42, 'solver': 'lbfgs'} | 0.691506 | -0.365754 | -0.241122 | -0.490993 |
|  1 | {'activation': 'logistic', 'hidden_layer_sizes': (75, 75), 'max_iter': 100, 'random_state': 42, 'solver': 'lbfgs'}         | 0.694034 | -0.365579 | -0.239094 | -0.488823 |
|  0 | {'activation': 'logistic', 'hidden_layer_sizes': (75, 75), 'max_iter': 80, 'random_state': 42, 'solver': 'lbfgs'}          |  0.69697 | -0.364134 | -0.236817 | -0.486517 |
|  7 | {'activation': 'logistic', 'hidden_layer_sizes': (75, 75, 75), 'max_iter': 150, 'random_state': 42, 'solver': 'lbfgs'}     | 0.694621 | -0.364099 | -0.238613 | -0.488364 |
| 12 | {'activation': 'logistic', 'hidden_layer_sizes': (75, 75, 75, 75), 'max_iter': 150, 'random_state': 42, 'solver': 'lbfgs'} | 0.699924 |  -0.36182 | -0.234509 | -0.484156 |

</details>



### SVR
<details>
<summary>Show</summary>

|    | params                                                         |       r2 |       MAE |       MSE |      RMSE | 
|---:|:---------------------------------------------------------------|---------:|----------:|----------:|----------:|
| 25 | {'C': 100, 'epsilon': 0.001, 'gamma': 'auto', 'kernel': 'rbf'} | 0.635724 | -0.395614 | -0.284666 | -0.533466 |
| 27 | {'C': 100, 'epsilon': 0.01, 'gamma': 'auto', 'kernel': 'rbf'}  | 0.637856 | -0.394263 | -0.283001 | -0.531904 |
| 28 | {'C': 100, 'epsilon': 0.1, 'gamma': 'scale', 'kernel': 'rbf'}  | 0.648673 | -0.387545 | -0.274573 |  -0.52392 |
| 29 | {'C': 100, 'epsilon': 0.1, 'gamma': 'auto', 'kernel': 'rbf'}   | 0.653574 | -0.384693 | -0.270736 | -0.520249 |
| 16 | {'C': 10, 'epsilon': 0.001, 'gamma': 'scale', 'kernel': 'rbf'} | 0.666321 | -0.375974 |  -0.26076 | -0.510567 |
| 18 | {'C': 10, 'epsilon': 0.01, 'gamma': 'scale', 'kernel': 'rbf'}  | 0.666802 | -0.375656 | -0.260385 |   -0.5102 |
| 17 | {'C': 10, 'epsilon': 0.001, 'gamma': 'auto', 'kernel': 'rbf'}  | 0.667619 | -0.375252 | -0.259746 | -0.509573 |
| 19 | {'C': 10, 'epsilon': 0.01, 'gamma': 'auto', 'kernel': 'rbf'}   | 0.668019 | -0.375017 | -0.259435 | -0.509267 |
| 20 | {'C': 10, 'epsilon': 0.1, 'gamma': 'scale', 'kernel': 'rbf'}   | 0.670475 | -0.373051 | -0.257518 | -0.507385 |
| 21 | {'C': 10, 'epsilon': 0.1, 'gamma': 'auto', 'kernel': 'rbf'}    | 0.671264 | -0.372839 | -0.256901 | -0.506779 |


|    |                            params                             |       r2 |       MAE |       MSE |      RMSE | 
|---:|:-------------------------------------------------------------:|---------:|----------:|----------:|----------:|
|  5 | {'C': 10, 'epsilon': 0.08, 'gamma': 'auto', 'kernel': 'rbf'}  | 0.670806 |   -0.3731 | -0.257259 | -0.507133 |
|  6 | {'C': 10, 'epsilon': 0.09, 'gamma': 'auto', 'kernel': 'rbf'}  | 0.671103 | -0.372913 | -0.257027 | -0.506904 |
|  7 |  {'C': 10, 'epsilon': 0.1, 'gamma': 'auto', 'kernel': 'rbf'}  | 0.671264 | -0.372839 | -0.256901 | -0.506779 |
|  9 | {'C': 10, 'epsilon': 0.12, 'gamma': 'auto', 'kernel': 'rbf'}  | 0.671498 | -0.372818 | -0.256719 | -0.506602 |
|  8 | {'C': 10, 'epsilon': 0.11, 'gamma': 'auto', 'kernel': 'rbf'}  | 0.671442 | -0.372775 | -0.256762 | -0.506643 |
| 10 | {'C': 20, 'epsilon': 0.08, 'gamma': 'auto', 'kernel': 'rbf'}  |  0.67244 | -0.372202 | -0.255975 | -0.505857 |
| 11 | {'C': 20, 'epsilon': 0.09, 'gamma': 'auto', 'kernel': 'rbf'}  | 0.672959 |  -0.37191 |  -0.25557 | -0.505458 |
| 12 |  {'C': 20, 'epsilon': 0.1, 'gamma': 'auto', 'kernel': 'rbf'}  | 0.673366 | -0.371687 | -0.255253 | -0.505145 |
| 13 | {'C': 20, 'epsilon': 0.11, 'gamma': 'auto', 'kernel': 'rbf'}  | 0.673676 | -0.371572 | -0.255013 |  -0.50491 |
| 14 | {'C': 20, 'epsilon': 0.12, 'gamma': 'auto', 'kernel': 'rbf'}  | 0.674051 | -0.371489 | -0.254721 | -0.504622 |

</details>



### Tree
<details>
<summary>Show</summary>

|     | params                                                                                                                |       r2 |       MAE |       MSE |      RMSE | 
|----:|:----------------------------------------------------------------------------------------------------------------------|---------:|----------:|----------:|----------:|
| 322 | {'criterion': 'friedman_mse', 'max_depth': 90, 'min_samples_leaf': 14, 'min_samples_split': 75, 'random_state': 42}   | 0.652243 | -0.392914 | -0.271806 | -0.521315 |
| 292 | {'criterion': 'friedman_mse', 'max_depth': 80, 'min_samples_leaf': 14, 'min_samples_split': 75, 'random_state': 42}   | 0.652243 | -0.392914 | -0.271806 | -0.521315 |
| 352 | {'criterion': 'friedman_mse', 'max_depth': 100, 'min_samples_leaf': 14, 'min_samples_split': 75, 'random_state': 42}  | 0.652243 | -0.392914 | -0.271806 | -0.521315 |
| 382 | {'criterion': 'friedman_mse', 'max_depth': 110, 'min_samples_leaf': 14, 'min_samples_split': 75, 'random_state': 42}  | 0.652243 | -0.392914 | -0.271806 | -0.521315 |
| 472 | {'criterion': 'friedman_mse', 'max_depth': None, 'min_samples_leaf': 14, 'min_samples_split': 75, 'random_state': 42} | 0.652243 | -0.392914 | -0.271806 | -0.521315 |
| 112 | {'criterion': 'squared_error', 'max_depth': 100, 'min_samples_leaf': 14, 'min_samples_split': 75, 'random_state': 42} | 0.652243 | -0.392914 | -0.271806 | -0.521315 |
| 442 | {'criterion': 'friedman_mse', 'max_depth': 130, 'min_samples_leaf': 14, 'min_samples_split': 75, 'random_state': 42}  | 0.652243 | -0.392914 | -0.271806 | -0.521315 |
|  82 | {'criterion': 'squared_error', 'max_depth': 90, 'min_samples_leaf': 14, 'min_samples_split': 75, 'random_state': 42}  | 0.652243 | -0.392914 | -0.271806 | -0.521315 |
|  52 | {'criterion': 'squared_error', 'max_depth': 80, 'min_samples_leaf': 14, 'min_samples_split': 75, 'random_state': 42}  | 0.652243 | -0.392914 | -0.271806 | -0.521315 |
|  22 | {'criterion': 'squared_error', 'max_depth': 70, 'min_samples_leaf': 14, 'min_samples_split': 75, 'random_state': 42}  | 0.652243 | -0.392914 | -0.271806 | -0.521315 |


|   | params                                                                                                               |       r2 |       MAE |       MSE |      RMSE | 
|--:|:---------------------------------------------------------------------------------------------------------------------|---------:|----------:|----------:|----------:|
| 0 | {'criterion': 'squared_error', 'max_depth': 50, 'min_samples_leaf': 14, 'min_samples_split': 75, 'random_state': 42} | 0.652243 | -0.392914 | -0.271806 | -0.521315 |
| 1 | {'criterion': 'squared_error', 'max_depth': 60, 'min_samples_leaf': 14, 'min_samples_split': 75, 'random_state': 42} | 0.652243 | -0.392914 | -0.271806 | -0.521315 |
| 2 | {'criterion': 'squared_error', 'max_depth': 70, 'min_samples_leaf': 14, 'min_samples_split': 75, 'random_state': 42} | 0.652243 | -0.392914 | -0.271806 | -0.521315 |
| 3 | {'criterion': 'squared_error', 'max_depth': 75, 'min_samples_leaf': 14, 'min_samples_split': 75, 'random_state': 42} | 0.652243 | -0.392914 | -0.271806 | -0.521315 |

</details>



### XGB
<details>
<summary>Show</summary>

|   | params                                                                                                   |       r2 |       MAE |       MSE |      RMSE | 
|--:|:---------------------------------------------------------------------------------------------------------|---------:|----------:|----------:|----------:|
| 3 | {'learning_rate': 0.03, 'max_depth': 7, 'min_child_weight': 2, 'n_estimators': 5000, 'random_state': 42} |  0.77869 | -0.311086 | -0.172977 | -0.415887 |
| 2 | {'learning_rate': 0.03, 'max_depth': 7, 'min_child_weight': 2, 'n_estimators': 4000, 'random_state': 42} | 0.779692 | -0.310367 | -0.172195 | -0.414945 |
| 1 | {'learning_rate': 0.03, 'max_depth': 7, 'min_child_weight': 2, 'n_estimators': 3500, 'random_state': 42} | 0.780002 | -0.310183 | -0.171953 | -0.414653 |
| 0 | {'learning_rate': 0.03, 'max_depth': 7, 'min_child_weight': 2, 'n_estimators': 3000, 'random_state': 42} |  0.78015 | -0.310135 | -0.171836 |  -0.41451 |


|   | params                                                                                                   |       r2 |       MAE |       MSE |      RMSE | 
|--:|:---------------------------------------------------------------------------------------------------------|---------:|----------:|----------:|----------:|
| 0 | {'learning_rate': 0.03, 'max_depth': 7, 'min_child_weight': 2, 'n_estimators': 2000, 'random_state': 42} | 0.779243 | -0.310861 | -0.172544 | -0.415358 |
| 1 | {'learning_rate': 0.03, 'max_depth': 7, 'min_child_weight': 2, 'n_estimators': 2500, 'random_state': 42} | 0.779884 | -0.310379 | -0.172045 | -0.414759 |
| 2 | {'learning_rate': 0.03, 'max_depth': 7, 'min_child_weight': 2, 'n_estimators': 2750, 'random_state': 42} | 0.780013 | -0.310222 | -0.171943 | -0.414637 |
| 3 | {'learning_rate': 0.03, 'max_depth': 7, 'min_child_weight': 2, 'n_estimators': 3000, 'random_state': 42} |  0.78015 | -0.310135 | -0.171836 |  -0.41451 |

</details>



</details>


## Comparison 
<details>
<summary>Show</summary>

### ElasticNet
| FeatureSet | params                                                                                         |       r2 |       MAE |       MSE |      RMSE | 
|-----------:|:-----------------------------------------------------------------------------------------------|---------:|----------:|----------:|----------:|
|    **ALL** | {'alpha': np.float64(0.008800000000000006), 'l1_ratio': np.float64(0.255), 'random_state': 42} | 0.654329 | -0.397319 | -0.270186 | -0.519761 |
|      UNION | {'alpha': np.float64(0.004498432668969444), 'l1_ratio': np.float64(0.42), 'random_state': 42}  |  0.64822 | -0.401242 |  -0.27496 | -0.524342 |


### RandomForest
| FeatureSet   | params                                                                                                                                                        |       r2 |       MAE |       MSE |      RMSE | 
|-------------:|:--------------------------------------------------------------------------------------------------------------------------------------------------------------|---------:|----------:|----------:|----------:|
|          ALL | {'bootstrap': True, 'criterion': 'squared_error', 'max_depth': 70, 'min_samples_leaf': 14, 'min_samples_split': 75, 'n_estimators': 1500, 'random_state': 42} | 0.703559 | -0.362621 | -0.231676 |   -0.4813 |
|        UNION | {'bootstrap': True, 'criterion': 'squared_error', 'max_depth': 70, 'min_samples_leaf': 14, 'min_samples_split': 75, 'n_estimators': 1500, 'random_state': 42} | 0.703559 | -0.362622 | -0.231676 |   -0.4813 |


### GradientBoosting
|   FeatureSet | params                                                                                                           |       r2 |       MAE |       MSE |      RMSE | 
|-------------:|:-----------------------------------------------------------------------------------------------------------------|---------:|----------:|----------:|----------:|
|          ALL | {'criterion': 'squared_error', 'learning_rate': 0.13, 'loss': 'huber', 'n_estimators': 1000, 'random_state': 42} | 0.760983 | -0.322617 |  -0.18679 | -0.432139 |
|    **UNION** | {'criterion': 'squared_error', 'learning_rate': 0.19, 'loss': 'huber', 'n_estimators': 1000, 'random_state': 42} | 0.762397 | -0.321788 | -0.185689 | -0.430871 |


### MLPR
|    FeatureSet | params                                                                                                                     |       r2 |       MAE |       MSE |      RMSE | 
|--------------:|:---------------------------------------------------------------------------------------------------------------------------|---------:|----------:|----------:|----------:|
|           ALL | {'activation': 'logistic', 'hidden_layer_sizes': (75, 75, 75, 75), 'max_iter': 150, 'random_state': 42, 'solver': 'lbfgs'} | 0.699924 |  -0.36182 | -0.234509 | -0.484156 |
|     **UNION** | {'activation': 'logistic', 'hidden_layer_sizes': (110, 110, 110), 'max_iter': 150, 'random_state': 42, 'solver': 'lbfgs'}  | 0.722212 | -0.347741 | -0.217066 | -0.465837 |


### SVR
|   FeatureSet | params                                                       |       r2 |       MAE |       MSE |      RMSE | 
|-------------:|:-------------------------------------------------------------|---------:|----------:|----------:|----------:|
|          ALL | {'C': 20, 'epsilon': 0.12, 'gamma': 'auto', 'kernel': 'rbf'} | 0.674051 | -0.371489 | -0.254721 | -0.504622 |
|    **UNION** | {'C': 5, 'epsilon': 0.09, 'gamma': 0.0015, 'kernel': 'rbf'}  | 0.689032 | -0.362902 | -0.243032 | -0.492941 |


### Tree
| FeatureSet | params                                                                                                               |       r2 |       MAE |       MSE |      RMSE | 
|-----------:|:---------------------------------------------------------------------------------------------------------------------|---------:|----------:|----------:|----------:|
|        ALL | {'criterion': 'squared_error', 'max_depth': 75, 'min_samples_leaf': 14, 'min_samples_split': 75, 'random_state': 42} | 0.652243 | -0.392914 | -0.271806 | -0.521315 |
|      UNION | {'criterion': 'squared_error', 'max_depth': 70, 'min_samples_leaf': 14, 'min_samples_split': 75, 'random_state': 42} | 0.652186 | -0.392955 |  -0.27185 | -0.521356 |


### XGB
|  FeatureSet | params                                                                                                   |       r2 |       MAE |       MSE |      RMSE | 
|------------:|:---------------------------------------------------------------------------------------------------------|---------:|----------:|----------:|----------:|
|     **ALL** | {'learning_rate': 0.03, 'max_depth': 7, 'min_child_weight': 2, 'n_estimators': 3000, 'random_state': 42} |  0.78015 | -0.310135 | -0.171836 |  -0.41451 |
|       UNION | {'learning_rate': 0.03, 'max_depth': 7, 'min_child_weight': 2, 'n_estimators': 1750, 'random_state': 42} | 0.777706 | -0.311622 | -0.173741 | -0.416792 |

</details>

## Conclusion

We might se a slight improvement for some models, it is not a significant on.
Therefore, we will continue to consider [selection_arranged_union.csv](../Workplace/created_files/training_score/selection_arranged_union.csv) for features.
