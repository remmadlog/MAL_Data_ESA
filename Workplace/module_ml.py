"""
A collection of ml related function.
"""
import warnings

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
"""IMPORTS"""
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
import numpy as np                                          # Numerical operations on arrays
import pandas as pd                                         # Data manipulation and analysis

from tqdm import tqdm                                   # lodingbar for loops

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
from sklearn.tree import DecisionTreeRegressor          # for Decision Tree
from sklearn.ensemble import RandomForestRegressor      # for the random forest
from sklearn.linear_model import LogisticRegression     # for LogisticRegression
from sklearn.ensemble import GradientBoostingRegressor  # for Gradient Boosting (ensemble)
from sklearn.linear_model import ElasticNet             # for Elastic Net
from sklearn.svm import SVR                             # for Support Vector Regression
from xgboost import XGBRegressor                        # for Extreme Gradient Boosting

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


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#:  including TARGET
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
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



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#:  NOT including TARGET
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #: Returns List of Features
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
        #: General
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
def correlation_selector(X, threshold=0.95):
    """
    Remove highly correlated features.

    Parameters:
        X (pandas.core.frame.DataFrame): Input data
        threshold (float): Correlation Threshold

    Returns:
        List of selected feature
    """
    features = X.columns
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)
    df = pd.DataFrame(X_scaled, columns=features)

    corr_matrix = df.corr().abs()
    upper = corr_matrix.where(np.triu(np.ones(corr_matrix.shape), k=1).astype(bool))
    to_drop = [column for column in upper.columns if any(upper[column] > threshold)]
    return df.drop(columns=to_drop).columns.to_list()


def variance_threshold_selector(X, threshold=0.1):
    """
    Remove features with low variance.

    Parameters:
        X (pandas.core.frame.DataFrame): Input data
        threshold (float): Variance Threshold

    Returns:
        List of selected feature
    """
    features = X.columns
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)
    df = pd.DataFrame(X_scaled, columns=features)

    selector = VarianceThreshold(threshold=threshold)
    selector.fit_transform(df)

    return df.columns[selector.get_support()].to_list()


#! Mistakes were made
def laplacian_score(X, n_features=5, k=5, t=1.0):
    """
    See e.g. https://proceedings.neurips.cc/paper_files/paper/2005/file/b5b03f06271f8917685d14cea7c6c50a-Paper.pdf

    Compute the Laplacian Score for each feature in X.

    Idea:
        Features are good if they preserve local neighborhood structure (manifold learning idea).
    How:
        Computes a score for each feature based on how well it aligns with the data's graph Laplacian.

    Parameters:
        X (pandas.core.frame.DataFrame): Input data
        n_features (int): Amount of features to select
        k (int): Number of nearest neighbors
        t (float): Heat kernel parameter

    Returns:
        List of selected feature
    """
    features = X.columns
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    # Construct the affinity matrix using k-nearest neighbors
    W = kneighbors_graph(X_scaled, n_neighbors=k, mode='connectivity', include_self=True)
    W = np.exp(-W / t)  # Apply heat kernel

    # Compute the degree matrix
    D = np.diag(W.sum(axis=1))

    # Compute the Laplacian matrix
    L = D - W

    # Compute the Laplacian Score for each feature
    scores = np.diagonal(X_scaled.T @ L @ X_scaled) / np.diagonal(X_scaled.T @ D @ X_scaled)
    return features.to_numpy()[np.argsort(scores)[-n_features:]].tolist()



def autoencoder_feature_selector(X, n_features=2, hidden_layer_size=5):
    """
    Use autoencoder to select most informative features.

    Idea:
        Train an autoencoder and measure how important each input feature is to reconstructing the data.
    How:
        Use L1 regularization on the input layer weights.
        Rank features by their learned weights or reconstruction loss when the feature is dropped.

    Parameters:
        X (pandas.core.frame.DataFrame): Input data
        n_features (int): Amount of features to select
        hidden_layer_size (int): Number of nearest neighbors

    Returns:
        List of selected feature
    """

    features = X.columns
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    ae = MLPRegressor(hidden_layer_sizes=(hidden_layer_size,), max_iter=1000, random_state=42)
    ae.fit(X_scaled, X_scaled)
    feature_importances = np.abs(ae.coefs_[0]).sum(axis=1)
    top_indices = np.argsort(feature_importances)[-n_features:]

    return features.to_numpy()[top_indices].tolist()


def tsne_sensitivity_selector(X, n_features=5, perplexity=30, tsne_components=2):
    """
    Select features by measuring their impact on t-SNE embedding (heuristic method).

    This might take some time fir you have a large amount of features to choose from.

    Parameters:
        X (pandas.core.frame.DataFrame): Input data
        n_features (int): Number of features to select
        perplexity (int): t-SNE perplexity parameter
        tsne_components (int): ``n_components`` in ``TSNE`` -- Diemnsion of the embedded space

    Returns:
        List of selected feature indices (those most important)
    """

    features = X.columns
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    # Run t-SNE on full feature set
    tsne_full = TSNE(n_components=tsne_components, perplexity=perplexity, random_state=42)
    full_embedding = tsne_full.fit_transform(X_scaled)

    diffs = []

    for i in tqdm(range(X_scaled.shape[1])):
        X_mod = np.delete(X_scaled, i, axis=1)
        tsne_mod = TSNE(n_components=tsne_components, perplexity=perplexity, random_state=42)
        mod_embedding = tsne_mod.fit_transform(X_mod)

        # Use mean pairwise distance difference as a proxy for change
        diff = np.mean(np.abs(pairwise_distances(full_embedding) - pairwise_distances(mod_embedding)))
        diffs.append(diff)

    # Higher difference → more important feature
    return features.to_numpy()[np.argsort(diffs)[-n_features:]].tolist()


def entropy_feature_selector(X, n_features=5, bins=10):
    """
    Select features with the highest entropy (most unpredictability).

    Parameters:
        X (pandas.core.frame.DataFrame): Input data
        n_features (int): Number of features to select
        bins (int): Number of bins for histogram estimation

    Returns:
        List of selected feature indices
    """
    features = X.columns
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    entropies = []

    for i in tqdm(range(X_scaled.shape[1])):
        hist, _ = np.histogram(X_scaled[:, i], bins=bins, density=True)
        hist += 1e-9  # Avoid log(0)
        entropies.append(entropy(hist))

    return features.to_numpy()[np.argsort(entropies)[-n_features:]].tolist()


def fa_selector(X, n_features=5, show_plot=True, n_selected_factors=0):
    """
    Factor Analysis used for feature selection

    Assumption:
    -----------
        Each observed variable is assumed to be a linear combination of one or more latent factors plus some noise (error).
            ``X=LZ+ε``

        - X: observed variables (e.g., features)
        - L: loadings (relationship between variables and factors)
        - Z: latent factors (lower-dimensional representation)
        - ε: noise


    Objective:
    ----------
        Find a set of factors that explain the shared variance (correlation) among observed variables.
        Unlike PCA, which captures total variance, FA ignores unique (random) variance, focusing only on what's shared.


    Procedure:
    ----------
        - Try FA with 1 to n factors.
        - For each, transform data to lower dimensions, then reconstruct the original.
        - Measure reconstruction error (MSE): the lower, the better.
        - Plot this error vs. number of factors to choose a good number (elbow method).
        - Once you decide (e.g., 2), transform data.
        - ``fa.components_`` shows how each feature loads on each factor.
        - Stronger loading (higher absolute value) means more contribution to that latent structure.
        - You rank features by these scores to decide which ones are most important.

    Regarding ``n_selected_factors``:
    ---------------------------------
    If ``n_selected_factors == 0`` and ``show_plot=True``
        ``n_selected_factors`` is given as input after plot is shown
    If ``n_selected_factors == 0`` and ``show_plot=False``
        ``n_selected_factors`` is given as the index of the minimum error
    If ``n_selected_factors = n > 0``
        ``n_selected_factors`` is given as ``n``

    :param X: Input data
    :type X: pandas.core.frame.DataFrame
    :param n_features: Number of features to select
    :type n_features: int
    :param show_plot: ``1`` to show plot (Default)
    :type show_plot: bool
    :param n_selected_factors: Number of selected factors. Usually determent after considering error plot.
    :type n_selected_factors: int
    :return: list of ``n_features`` features
    """

    features = X.columns

    # Step 1: Standardize the features
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    # Step 2: Determine optimal number of factors using explained variance (optional)
    # Try multiple numbers of factors and evaluate reconstruction error
    feature_amount = X.shape[1]
    errors = []

    for n_factors in tqdm(range(1, feature_amount + 1)):
        fa = FactorAnalysis(n_components=n_factors, random_state=42)
        X_transformed = fa.fit_transform(X_scaled)
        # X_reconstructed = fa.inverse_transform(X_transformed)
        X_reconstructed = np.dot(X_transformed, fa.components_)
        error = np.mean((X_scaled - X_reconstructed) ** 2)
        errors.append(error)

    if show_plot:
        # Plot reconstruction error vs number of factors
        plt.figure()
        plt.plot(range(1, feature_amount + 1), errors, marker='o')
        plt.xlabel('Number of Factors')
        plt.ylabel('Reconstruction Error (MSE)')
        plt.title('Optimal Number of Factors: Choose n_selected_factors')
        plt.grid(True)
        plt.show(block=True)

        #. Choose n_selected_factors based on the plot
        n_selected_factors = int(input("Give ``n_selected_factors``:"))

    #. Choose n_selected_factors
    else:
        if feature_amount > 150:
            print("A plot consideration is recommended for a large number of features, pleas reconsider.")
        #. Choose n_selected_factors based on minimal error if not given as input
        if n_selected_factors == 0:
            index_min = np.argmin(errors)
            n_selected_factors =range(1, feature_amount + 1)[index_min]
            print("Choosing ``n_selected_factors`` based on minimal error: n_selected_factors=", n_selected_factors)

    # Step 3: Perform Factor Analysis with chosen number of factors
    fa = FactorAnalysis(n_components=n_selected_factors, random_state=42)
    X_fa = fa.fit_transform(X_scaled)

    # Step 4: Analyze factor loadings to select features
    loadings = fa.components_.T  # shape: [feature_amount, n_factors]
    feature_importance = np.sum(np.abs(loadings), axis=1)

    # Rank features by their total loading across factors
    feature_ranks = pd.Series(feature_importance, index=features).sort_values(ascending=False)

    # print("Feature rankings based on Factor Analysis loadings:")
    # print(feature_ranks)

    # Select top N important features (e.g., top 2)
    top_features = feature_ranks.head(n_features).index.tolist()
    return top_features


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
        #: Clustering -- Use if you know how many clusters you want
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
def clustering_stability_selector(X, n_features=5, n_clusters=3, n_iter=10, sample_frac=0.8):
    """
    Select features that produce stable clustering across bootstrap samples.

    :param X: Input data
    :type X: pandas.core.frame.DataFrame
    :param n_features: Number of features to select
    :type n_features: int
    :param n_clusters: Number of clusters for KMeans
    :type n_clusters: int
    :param n_iter: Number of bootstrap iterations
    :type n_iter: int
    :param sample_frac: Fraction of samples to resample each iteration
    :type sample_frac: float
    :return: List of selected feature indices
    :rtype: list
    """



    features = X.columns
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    stability_scores = []

    for i in tqdm(range(X_scaled.shape[1])):
        ari_scores = []

        for _ in range(n_iter):
            # Two independent resamples of the first i features in X
            X1 = resample(X_scaled[:, i].reshape(-1, 1), n_samples=int(sample_frac * X_scaled.shape[0]))
            X2 = resample(X_scaled[:, i].reshape(-1, 1), n_samples=int(sample_frac * X_scaled.shape[0]))

            k1 = KMeans(n_clusters=n_clusters, random_state=0).fit_predict(X1)
            k2 = KMeans(n_clusters=n_clusters, random_state=0).fit_predict(X2)

            # Measure clustering agreement
            score = adjusted_rand_score(k1[:len(k2)], k2[:len(k1)])
            ari_scores.append(score)

        # Average ARI across iterations -> stability score
        stability_scores.append(np.mean(ari_scores))

    return features.to_numpy()[np.argsort(stability_scores)[-n_features:]].tolist()


def silhouette_feature_selector(X, n_features=50, n_clusters=3):
    """
    Evaluate each feature independently using silhouette score after clustering.
    Select n_features features with the highest scores.

        Parameters:
        X (pandas.core.frame.DataFrame): Input data
        n_clusters (int): Number of clusters in ``KMeans``
        n_features (int):

    Returns:
        List of selected feature
    """

    features = X.columns
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)


    scores = []
    for i in tqdm(range(X_scaled.shape[1])):
        feature = X_scaled[:, i].reshape(-1, 1)
        km = KMeans(n_clusters=n_clusters, random_state=42, n_init='auto').fit(feature)
        try:
            score = silhouette_score(feature, km.labels_)
        except:
            score = -1  # score undefined if all samples in 1 cluster
        scores.append(score)

    top_indices = np.argsort(scores)[-n_features:]
    return features.to_numpy()[top_indices].tolist()


def greedy_clustering_feature_selection(X, n_features=5, n_clusters=3):
    """
    Select features based on how much they improve clustering quality (silhouette score).

    Idea:
        Iterate over each feature and keep the one that have an impact on ``silhouette_score``

    Parameters:
        X (pandas.core.frame.DataFrame): Input data
        n_features (int): Number of features to select
        n_clusters (int): Number of clusters for KMeans

    Returns:
        List of selected feature
    """

    features = X.columns
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    selected = []
    remaining = list(range(X_scaled.shape[1]))

    for _ in tqdm(range(n_features)):
        best_score = -1
        best_feature = None

        for f in remaining:
            trial_features = selected + [f]
            X_trial = X_scaled[:, trial_features]
            labels = KMeans(n_clusters=n_clusters, random_state=0).fit_predict(X_trial)
            score = silhouette_score(X_trial, labels)

            if score > best_score:
                best_score = score
                best_feature = f

        selected.append(best_feature)
        remaining.remove(best_feature)

    return features.to_numpy()[selected].tolist()


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #: Returns DataFrame
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

def pca_selector(X, n_features=50):
    """
    Use PCA for dimensionality reduction.

    From https://stackoverflow.com/a/14718560
    The components of a primary component analysis are linear combinations of your original variables.
    So there is no one-to-one mapping between components and genes.
    Excepting special cases, every component describes multiple genes.
    Some of them with a positive and some with a negative contribution. Some with large and some with small absolute values.

    See https://stackoverflow.com/questions/36921068/math-domain-error-while-using-pca for changes to ``_pca.py``

    ``n_features`` (``n_components`` in PCA)
        If n_features == 'mle' and svd_solver == 'full',
            Minka’s MLE is used to guess the dimension.
        Use of n_features == 'mle'
            will interpret svd_solver == 'auto' as svd_solver == 'full'.
        If 0 < n_features < 1 and svd_solver == 'full',
            select the number of components such that the amount of variance that needs to be explained is greater than the percentage specified by n_features.
        If svd_solver == 'arpack',
            the number of components must be strictly less than the minimum of features and samples.

    Parameters:
        X (pandas.core.frame.DataFrame): Input data
        n_features (int): Number of features

    Returns:
        (pandas.core.frame.DataFrame) DataFrame with new combined PCA features
    """
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    # keep pca_components
    pca = PCA(n_components=n_features, random_state=42)

    # PCA application
    principalComponents = pca.fit_transform(X_scaled)

    # create df
    df_pca = pd.DataFrame(data = principalComponents)

    return df_pca



def ica_selector(X, n_features=50):
    """
        See
    1) https://medium.com/@ab.jannatpour/independent-component-analysis-ica-with-python-code-e7d1dd290241

    ICA is a method for dividing a multidimensional signal into its components.

    In the context of feature selection, ICA can be used to convert the original feature space into a new space characterized by statistically independent components.
    You may decrease the dimensionality of the dataset while keeping the underlying structure by picking the top k independent components.

    Parameters:
        X (pandas.core.frame.DataFrame): Input data
        n_features (int): Number of features

    Returns:
        (pandas.core.frame.DataFrame) DataFrame with new combined ICA features
    """

    features = X.columns
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    ICA = FastICA(
        n_components=n_features,
        random_state=42,
        whiten='unit-variance'
    )

    # PCA application
    principalComponents =  ICA.fit_transform(X_scaled)

    # create df
    df_ica = pd.DataFrame(data = principalComponents)

    return df_ica


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#: Feature Selection Pipeline
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

# Run everything and evaluate impact on KMeans
def feature_selection_pipeline(X, n_clusters=3, n_features=50,
                                    threshold_cor=0.95, threshold_var=0.1,
                                    lap_k=5, lap_t=1.0,
                                    hidden_layer_size=50,
                                    perplexity=50, tsne_components=2,
                                    bins=10,
                                    show_plot=True, n_selected_factors=0,
                                    n_iter=10, sample_frac=0.8):
    """

    :param X: Input data, no scaling needed, only provide features that can be selected (no ID, no Target)
    :type X: pandas.core.frame.DataFrame
    :param n_clusters: Number of clusters that will be used for ``clustering_stability_selector`` and ``greedy_clustering_feature_selection``
    :type n_clusters: int
    :param n_features: Amount of features we want to get
    :type n_features: int
    :param threshold_cor: Threshold for correlation
    :type threshold_cor: float
    :param threshold_var: Threshold for variation
    :type threshold_var: float
    :param lap_k: k parameter for Laplacian score
    :type lap_k: int
    :param lap_t: t parameter for Laplacian score
    :type lap_t: float
    :param hidden_layer_size: Hidden layer size
    :type hidden_layer_size: int
    :param perplexity: Parameter for ``tsne_sensitivity_selector``
    :type perplexity:
    :param tsne_components: Parameter for ``tsne_sensitivity_selector``
    :type tsne_components: int
    :param bins: Number of bins for histogram estimation
    :type bins: int
    :param show_plot: ``True`` for showing the plot
    :type show_plot: bool
    :param n_selected_factors: Number of selected factors. Usually determent after considering error plot.
    :type n_selected_factors: int
    :param n_iter: Number of bootstrap iterations
    :type n_iter: int
    :param sample_frac: Fraction of samples to resample each iteration
    :type sample_frac: float
    :return:
    :rtype: list
    """

    # scaling for later:
    features = X.columns
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    # give X, it will be scaled in the function -- todo: maybe change this
    features_cor        = correlation_selector(X, threshold=threshold_cor)
    features_var        = variance_threshold_selector(X, threshold=threshold_var)
    features_lap        = laplacian_score(X, n_features=n_features, k=lap_k, t=lap_t)
    features_encoder    = autoencoder_feature_selector(X, n_features=n_features, hidden_layer_size=hidden_layer_size)
    features_tsne       = tsne_sensitivity_selector(X, n_features=n_features, perplexity=perplexity, tsne_components=tsne_components)
    features_entropy    = entropy_feature_selector(X, n_features=n_features, bins=bins)
    features_fa         = fa_selector(X, n_features=n_features, show_plot=show_plot, n_selected_factors=n_selected_factors)
    features_cluststab  = clustering_stability_selector(X, n_features=n_features, n_clusters=n_clusters, n_iter=n_iter, sample_frac=sample_frac)
    features_greedy     = greedy_clustering_feature_selection(X, n_features=n_features, n_clusters=n_clusters)

    # Make DataFarmes
    df_cor          = pd.DataFrame(data=X_scaled, columns= features_cor)
    df_var          = pd.DataFrame(data=X_scaled, columns= features_var)
    df_lap          = pd.DataFrame(data=X_scaled, columns= features_lap)
    df_encoder      = pd.DataFrame(data=X_scaled, columns= features_encoder)
    df_tsne         = pd.DataFrame(data=X_scaled, columns= features_tsne)
    df_entropy      = pd.DataFrame(data=X_scaled, columns= features_entropy)
    df_fa           = pd.DataFrame(data=X_scaled, columns= features_fa)
    df_cluststab    = pd.DataFrame(data=X_scaled, columns= features_cluststab)
    df_greedy       = pd.DataFrame(data=X_scaled, columns= features_greedy)

    # Get DataFrame as return
    df_pca              = pca_selector(X, n_features=n_features)
    df_ica              = ica_selector(X, n_features=n_features)



    return [df_cor, df_var, df_lap, df_encoder, df_tsne, df_entropy, df_fa, df_cluststab, df_greedy, df_pca, df_ica]


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



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
"""Clustering"""
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
def kmeans_best(X,range):
    """
    Use ``kmeans_best(X,range)`` to obtain the best possible KMEANS clustering of ``X`` for ``n_cluster`` in ``range``.

    Returns the best model for the given ``range`` as well as the ``silhouette_score`` and ``n_cluster``

    :param X: Dataset, only contains columns that are features (e.g. no id-column)
    :type X: pandas.core.frame.DataFrame
    :param range: range for ``n_clusters`` to test the amounts of clusters
    :type range: range
    :return: top_model, silhouette_score, n_clusters
    """
    # Instantiate StandardScaler
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    fits = []
    scores = []

    for k in range:
        # using KMeans for `k` clusters
        model = KMeans(n_clusters = k, random_state = 42, n_init='auto')
        model.fit(X_scaled)

        # append the model to fits
        fits.append(model)

        # evaluate using silhouette_score
        scores.append(silhouette_score(X_scaled, model.labels_, metric='euclidean'))

    top_score = max(scores)
    top_model = fits[(scores.index(top_score))]

    return top_model, top_score, range[scores.index(top_score)]


def kmeans_search(X,range):
    """
    Use ``kmeans_search(X,range)`` to obtain a list of lists containing ``n_cluster`` and ``silhouette_score`` for ``KMeans``, for every element in ``range``.

    Uses ``KMeans`` as well as ``silhouette_score``

    :param X: Dataset, only contains columns that are features (e.g. no id-column)
    :type X: pandas.core.frame.DataFrame
    :param range: range for ``n_clusters`` to test the amounts of clusters
    :type range: range
    :return: list of list: ``data=[["n_clusters","score"]]``
    :rtype: list
    """
    # Instantiate StandardScaler
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    data = [["n_clusters", "score"]]

    for k in range:
        # using KMeans for `k` clusters
        model = KMeans(n_clusters = k, random_state = 42, n_init=10, max_iter=500)
        model.fit(X_scaled)

        # appending data
        data.append([k,silhouette_score(X_scaled, model.labels_, metric='euclidean')])
    return data


def plot_k_distance_graph(X, k):
    """
    Plots a graph of the distance for the ``k`` nearest neighbors, using ``NearestNeighbors´´

    :param X: Dataset without id-column
    :type X: pandas.core.frame.DataFrame
    :param k: number of nearest neighbors to consider
    :type k: int
    :return: None
    """
    neigh = NearestNeighbors(n_neighbors=k)
    neigh.fit(X)
    distances, _ = neigh.kneighbors(X)
    distances = np.sort(distances[:, k - 1])
    plt.figure(figsize=(10, 6))
    plt.plot(distances)
    plt.xlabel('Points')
    plt.ylabel(f'{k}-th nearest neighbor distance')
    plt.title('K-distance Graph')
    plt.show(block=True)


def cluster_KMeans(X, n_cluster=5, n_init=10, max_iter=500):
    """

    :param X: Dataset without id-column
    :type X: pandas.core.frame.DataFrame
    :param n_cluster: Number of clusters to be build
    :type n_cluster: int
    :param n_init: number of start iterations for ``KMeans``
    :type n_init: int
    :param max_iter: Number of max itertaions for ``KMeans``
    :type max_iter: int
    :return: Dataset with labe column added
    :rtype: pandas.core.frame.DataFrame
    """
    df = X.copy()
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    #: clustering
    model = KMeans(n_clusters=n_cluster, random_state=42, n_init=10, max_iter=500)
    clustering_labels = model.fit_predict(X_scaled)
    df["labels"] = clustering_labels

    #: scoring
    score = silhouette_score(X_scaled, clustering_labels, metric='euclidean')
    print("Score: ", score)

    #: amount of elem per cluster
    clust = []
    n_elem = []
    for i in clustering_labels:
        if i not in clust:
            clust.append(i)
            n_elem.append(list(clustering_labels).count(i))

    for i, j in zip(clust, n_elem):
        print(str(i) + ": " + str(j))

    return df


def cluster_DBSCAN(X, n_neighbors=5, min_samples=50, epsilon=0.0):
    """
    If ``epsilon=0``:
        a plot is given and ``epsilon`` will be given as input after viewing the plot.

    :param X: Dataset without id-column
    :type X: pandas.core.frame.DataFrame
    :param n_neighbors: Number of Nearest Neighbors to consider
    :type n_neighbors: int
    :param min_samples: minimal size of a cluster
    :type min_samples: int
    :param epsilon: eps obtained by considering the plot and using the elbow method
    :type epsilon: float
    :return: Dataset with labe column added
    :rtype: pandas.core.frame.DataFrame
    """
    df = X.copy()
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    if epsilon == 0:
        #: plotting distance
        plot_k_distance_graph(X_scaled, k=n_neighbors)
        epsilon = float(input("Give ``eps`` in (0.0, inf):"))

    #: clustering
    # epsilon = 10  # Chosen based on k-distance graph
    model = DBSCAN(eps=epsilon, min_samples=min_samples)
    clustering_labels = model.fit_predict(X_scaled)
    df['labels'] = clustering_labels

    #: scoring
    score = silhouette_score(X_scaled, clustering_labels, metric='euclidean')
    print("Score: ", score)

    #: amount of elem per cluster
    clust = []
    n_elem = []
    for i in clustering_labels:
        if i not in clust:
            clust.append(i)
            n_elem.append(list(clustering_labels).count(i))

    for i, j in zip(clust, n_elem):
        print(str(i) + ": " + str(j))

    return df

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
