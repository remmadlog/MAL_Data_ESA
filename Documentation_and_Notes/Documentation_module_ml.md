# Documentation for [module_ml.py](../Workplace/module_ml.py)

A short documentation for [module_ml.py](../Workplace/module_ml.py) that is mainly used for the machine learning part of the project.

- [Go to functions](#functions)
- [Go to imports](#imports) 


---

## Functions
List of all functions:
- [autoencoder_feature_selector](#autoencoder_feature_selector)
- [cluster_DBSCAN](#cluster_DBSCAN)
- [cluster_KMeans](#cluster_KMeans)
- [clustering_stability_selector](#clustering_stability_selector)
- [correlation_selector](#correlation_selector)
- [entropy_feature_selector](#entropy_feature_selector)
- [eval_scor_pred](#eval_scor_pred)
- [fa_selector](#fa_selector)
- [feature_selection_pipeline](#feature_selection_pipeline)
- [fs_chi2](#fs_chi2)
- [fs_f_classif](#fs_f_classif)
- [get_Elasticnet_reg](#get_Elasticnet_reg)
- [get_SVR_reg](#get_SVR_reg)
- [get_XGB_reg](#get_XGB_reg)
- [get_forest_reg](#get_forest_reg)
- [get_gradboost_reg](#get_gradboost_reg)
- [get_logreg_reg](#get_logreg_reg)
- [get_scores](#get_scores)
- [greedy_clustering_feature_selection](#greedy_clustering_feature_selection)
- [gs_MLP_reg](#gs_MLP_reg)
- [gs_tree_reg](#gs_tree_reg)
- [ica_selector](#ica_selector)
- [kmeans_best](#kmeans_best)
- [kmeans_search](#kmeans_search)
- [laplacian_score](#laplacian_score)
- [pca_selector](#pca_selector)
- [plot_k_distance_graph](#plot_k_distance_graph)
- [print_scores](#print_scores)
- [silhouette_feature_selector](#silhouette_feature_selector)
- [sorting](#sorting)
- [tsne_sensitivity_selector](#tsne_sensitivity_selector)
- [variance_threshold_selector](#variance_threshold_selector)


---

###  autoencoder_feature_selector
> Use autoencoder to select most informative features.
> 
> Idea:
>     Train an autoencoder and measure how important each input feature is to reconstructing the data.
> How:
>     Use L1 regularization on the input layer weights.
>     Rank features by their learned weights or reconstruction loss when the feature is dropped.
> 
> Parameters:
>     X (pandas.core.frame.DataFrame): Input data
>     n_features (int): Amount of features to select
>     hidden_layer_size (int): Number of nearest neighbors
> 
> #### Returns
> 
> - List of selected feature
> 

---

###  cluster_DBSCAN
> If ``epsilon=0``:
>     a plot is given and ``epsilon`` will be given as input after viewing the plot.
> - `X` (pandas.core.frame.DataFrame): Dataset without id-column
> - `n_neighbors` (int): Number of Nearest Neighbors to consider
> - `min_samples` (int): minimal size of a cluster
> - `epsilon` (float): eps obtained by considering the plot and using the elbow method
> - returns: Dataset with labe column added
> - return type: `pandas.core.frame.DataFrame`
> 

---

###  cluster_KMeans- `X` (pandas.core.frame.DataFrame): Dataset without id-column
> - `n_cluster` (int): Number of clusters to be build
> - `n_init` (int): number of start iterations for ``KMeans``
> - `max_iter` (int): Number of max itertaions for ``KMeans``
> - returns: Dataset with labe column added
> - return type: `pandas.core.frame.DataFrame`
> 

---

###  clustering_stability_selector
> Select features that produce stable clustering across bootstrap samples.
> - `X` (pandas.core.frame.DataFrame): Input data
> - `n_features` (int): Number of features to select
> - `n_clusters` (int): Number of clusters for KMeans
> - `n_iter` (int): Number of bootstrap iterations
> - `sample_frac` (float): Fraction of samples to resample each iteration
> - returns: List of selected feature indices
> - return type: `list`
> 

---

###  correlation_selector
> Remove highly correlated features.
> 
> Parameters:
>     X (pandas.core.frame.DataFrame): Input data
>     threshold (float): Correlation Threshold
> 
> #### Returns
> 
> - List of selected feature
> 

---

###  entropy_feature_selector
> Select features with the highest entropy (most unpredictability).
> 
> Parameters:
>     X (pandas.core.frame.DataFrame): Input data
>     n_features (int): Number of features to select
>     bins (int): Number of bins for histogram estimation
> 
> #### Returns
> 
> - List of selected feature indices
> 

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

###  fa_selector
> Factor Analysis used for feature selection
> 
> Assumption:
> -----------
>     Each observed variable is assumed to be a linear combination of one or more latent factors plus some noise (error).
>         ``X=LZ+ε``
> 
>     - X: observed variables (e.g., features)
>     - L: loadings (relationship between variables and factors)
>     - Z: latent factors (lower-dimensional representation)
>     - ε: noise
> 
> 
> Objective:
> ----------
>     Find a set of factors that explain the shared variance (correlation) among observed variables.
>     Unlike PCA, which captures total variance, FA ignores unique (random) variance, focusing only on what's shared.
> 
> 
> Procedure:
> ----------
>     - Try FA with 1 to n factors.
>     - For each, transform data to lower dimensions, then reconstruct the original.
>     - Measure reconstruction error (MSE): the lower, the better.
>     - Plot this error vs. number of factors to choose a good number (elbow method).
>     - Once you decide (e.g., 2), transform data.
>     - ``fa.components_`` shows how each feature loads on each factor.
>     - Stronger loading (higher absolute value) means more contribution to that latent structure.
>     - You rank features by these scores to decide which ones are most important.
> 
> Regarding ``n_selected_factors``:
> ---------------------------------
> If ``n_selected_factors == 0`` and ``show_plot=True``
>     ``n_selected_factors`` is given as input after plot is shown
> If ``n_selected_factors == 0`` and ``show_plot=False``
>     ``n_selected_factors`` is given as the index of the minimum error
> If ``n_selected_factors = n > 0``
>     ``n_selected_factors`` is given as ``n``
> - `X` (pandas.core.frame.DataFrame): Input data
> - `n_features` (int): Number of features to select
> - `show_plot` (bool): ``1`` to show plot (Default)
> - `n_selected_factors` (int): Number of selected factors. Usually determent after considering error plot.
> - returns: list of ``n_features`` features
> 

---

###  feature_selection_pipeline- `X` (pandas.core.frame.DataFrame): Input data, no scaling needed, only provide features that can be selected (no ID, no Target)
> - `n_clusters` (int): Number of clusters that will be used for ``clustering_stability_selector`` and ``greedy_clustering_feature_selection``
> - `n_features` (int): Amount of features we want to get
> - `threshold_cor` (float): Threshold for correlation
> - `threshold_var` (float): Threshold for variation
> - `lap_k` (int): k parameter for Laplacian score
> - `lap_t` (float): t parameter for Laplacian score
> - `hidden_layer_size` (int): Hidden layer size
> - `perplexity`: Parameter for ``tsne_sensitivity_selector``
>   . Type: `perplexity`:
> - `tsne_components` (int): Parameter for ``tsne_sensitivity_selector``
> - `bins` (int): Number of bins for histogram estimation
> - `show_plot` (bool): ``True`` for showing the plot
> - `n_selected_factors` (int): Number of selected factors. Usually determent after considering error plot.
> - `n_iter` (int): Number of bootstrap iterations
> - `sample_frac` (float): Fraction of samples to resample each iteration
> - returns:
> - return type: `list`
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

###  fs_f_classif
> Feature selection using ``f_classif`` from sklearn
> - `df_data`: All data not including the target column
> - `df_target`: Data only including the target column
> - `k_best_features`: Amount of features returned, length of returned object
> - returns:  list of the ``k_best_features`` features
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

###  greedy_clustering_feature_selection
> Select features based on how much they improve clustering quality (silhouette score).
> 
> Idea:
>     Iterate over each feature and keep the one that have an impact on ``silhouette_score``
> 
> Parameters:
>     X (pandas.core.frame.DataFrame): Input data
>     n_features (int): Number of features to select
>     n_clusters (int): Number of clusters for KMeans
> 
> #### Returns
> 
> - List of selected feature
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

###  ica_selector
>     See
> 1) https://medium.com/@ab.jannatpour/independent-component-analysis-ica-with-python-code-e7d1dd290241
> 
> ICA is a method for dividing a multidimensional signal into its components.
> 
> In the context of feature selection, ICA can be used to convert the original feature space into a new space characterized by statistically independent components.
> You may decrease the dimensionality of the dataset while keeping the underlying structure by picking the top k independent components.
> 
> Parameters:
>     X (pandas.core.frame.DataFrame): Input data
>     n_features (int): Number of features
> 
> #### Returns
> 
> - (pandas.core.frame.DataFrame) DataFrame with new combined ICA features
> 

---

###  kmeans_best
> Use ``kmeans_best(X,range)`` to obtain the best possible KMEANS clustering of ``X`` for ``n_cluster`` in ``range``.
> 
> Returns the best model for the given ``range`` as well as the ``silhouette_score`` and ``n_cluster``
> - `X` (pandas.core.frame.DataFrame): Dataset, only contains columns that are features (e.g. no id-column)
> - `range` (range): range for ``n_clusters`` to test the amounts of clusters
> - returns: top_model, silhouette_score, n_clusters
> 

---

###  kmeans_search
> Use ``kmeans_search(X,range)`` to obtain a list of lists containing ``n_cluster`` and ``silhouette_score`` for ``KMeans``, for every element in ``range``.
> 
> Uses ``KMeans`` as well as ``silhouette_score``
> - `X` (pandas.core.frame.DataFrame): Dataset, only contains columns that are features (e.g. no id-column)
> - `range` (range): range for ``n_clusters`` to test the amounts of clusters
> - returns: list of list: ``data=[["n_clusters","score"]]``
> - return type: `list`
> 

---

###  laplacian_score
> See e.g. https://proceedings.neurips.cc/paper_files/paper/2005/file/b5b03f06271f8917685d14cea7c6c50a-Paper.pdf
> 
> Compute the Laplacian Score for each feature in X.
> 
> Idea:
>     Features are good if they preserve local neighborhood structure (manifold learning idea).
> How:
>     Computes a score for each feature based on how well it aligns with the data's graph Laplacian.
> 
> Parameters:
>     X (pandas.core.frame.DataFrame): Input data
>     n_features (int): Amount of features to select
>     k (int): Number of nearest neighbors
>     t (float): Heat kernel parameter
> 
> #### Returns
> 
> - List of selected feature
> 

---

###  pca_selector
> Use PCA for dimensionality reduction.
> 
> From https://stackoverflow.com/a/14718560
> The components of a primary component analysis are linear combinations of your original variables.
> So there is no one-to-one mapping between components and genes.
> Excepting special cases, every component describes multiple genes.
> Some of them with a positive and some with a negative contribution. Some with large and some with small absolute values.
> 
> See https://stackoverflow.com/questions/36921068/math-domain-error-while-using-pca for changes to ``_pca.py``
> 
> ``n_features`` (``n_components`` in PCA)
>     If n_features == 'mle' and svd_solver == 'full',
>         Minka’s MLE is used to guess the dimension.
>     Use of n_features == 'mle'
>         will interpret svd_solver == 'auto' as svd_solver == 'full'.
>     If 0 < n_features < 1 and svd_solver == 'full',
>         select the number of components such that the amount of variance that needs to be explained is greater than the percentage specified by n_features.
>     If svd_solver == 'arpack',
>         the number of components must be strictly less than the minimum of features and samples.
> 
> Parameters:
>     X (pandas.core.frame.DataFrame): Input data
>     n_features (int): Number of features
> 
> #### Returns
> 
> - (pandas.core.frame.DataFrame) DataFrame with new combined PCA features
> 

---

###  plot_k_distance_graph
> Plots a graph of the distance for the ``k`` nearest neighbors, using ``NearestNeighbors´´
> - `X` (pandas.core.frame.DataFrame): Dataset without id-column
> - `k` (int): number of nearest neighbors to consider
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

###  silhouette_feature_selector
> Evaluate each feature independently using silhouette score after clustering.
> Select n_features features with the highest scores.
> 
>     Parameters:
>     X (pandas.core.frame.DataFrame): Input data
>     n_clusters (int): Number of clusters in ``KMeans``
>     n_features (int):
> 
> #### Returns
> 
> - List of selected feature
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

###  tsne_sensitivity_selector
> Select features by measuring their impact on t-SNE embedding (heuristic method).
> 
> This might take some time fir you have a large amount of features to choose from.
> 
> Parameters:
>     X (pandas.core.frame.DataFrame): Input data
>     n_features (int): Number of features to select
>     perplexity (int): t-SNE perplexity parameter
>     tsne_components (int): ``n_components`` in ``TSNE`` -- Diemnsion of the embedded space
> 
> #### Returns
> 
> - List of selected feature indices (those most important)
> 

---

###  variance_threshold_selector
> Remove features with low variance.
> 
> Parameters:
>     X (pandas.core.frame.DataFrame): Input data
>     threshold (float): Variance Threshold
> 
> #### Returns
> 
> - List of selected feature
> 

---

## Imports

This module features a lot of imports, mostly some kind of `sklearn` functions.

```python
import numpy as np                                          # Numerical operations on arrays
import pandas as pd                                         # Data manipulation and analysis
    
from tqdm import tqdm                                       # lodingbar for loops

# for sorting list of lists
from operator import itemgetter

# will be used for feature selection
from sklearn.feature_selection import SelectKBest
from sklearn.feature_selection import f_classif
from sklearn.feature_selection import chi2

# for evaluating/scoring
from sklearn.metrics import mean_squared_error, r2_score, mean_absolute_error

# Gridsearch for better parameter tuning
from sklearn.model_selection import GridSearchCV

# Regression models
from sklearn.tree import DecisionTreeRegressor              # for Decision Tree
from sklearn.ensemble import RandomForestRegressor          # for the random forest
from sklearn.linear_model import LogisticRegression         # for LogisticRegression
from sklearn.ensemble import GradientBoostingRegressor      # for Gradient Boosting (ensemble)
from sklearn.linear_model import ElasticNet                 # for Elastic Net
from sklearn.svm import SVR                                 # for Support Vector Regression
from xgboost import XGBRegressor                            # for Extreme Gradient Boosting

import matplotlib.pyplot as plt                             # For creating visualizations

from scipy.stats import entropy                             # To compute entropy of distributions


from sklearn.cluster import KMeans                          # K-means clustering algorithm
from sklearn.cluster import DBSCAN                          # DBSCAN clustering algorithm
from sklearn.decomposition import (                         # Dimensionality reduction techniques
    FastICA,
    FactorAnalysis,
    PCA
)
from sklearn.feature_selection import VarianceThreshold     # Removes low-variance features
from sklearn.manifold import TSNE                           # t-SNE for dimensionality reduction and visualization
from sklearn.metrics import (                               # Evaluation metrics
    adjusted_rand_score,
    pairwise_distances,
    silhouette_score
)
from sklearn.neighbors import kneighbors_graph              # Graph-based nearest neighbors
from sklearn.neural_network import MLPRegressor             # Multilayer perceptron regressor
from sklearn.preprocessing import StandardScaler            # Standardize features
from sklearn.utils import resample                          # Bootstrap resampling

from sklearn.neighbors import NearestNeighbors              # Nearest neighbors algorithm
```
