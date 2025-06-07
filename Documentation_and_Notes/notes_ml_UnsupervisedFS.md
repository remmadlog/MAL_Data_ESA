# Notes on [ml_unsupervised_fs.py](../Workplace/ml_unsupervised_fs.py)

## Main Idea

1. Use different starting points to apply feature selection.
   - Full set with all the features.
     - Reduced set used for score prediction.
     - Selected set, where features were removed by hand.
2. Use quick and easy methods for a fast iterative reduction.
   - Variance Selector
   - Correlation Selector
   - Entropy Selector
3. Save the outcome as our first reduction file. 
   - Use this outcome for more time-consuming and complex feature selection methods.
     - Factor Analysis
     - Auto Encoder
     - TSNE Selector
     - PCA Selector
     - ICA Selector
4. Save each outcome separately.
5. Thus creating several feature sets.

Those can be than tested to see wich set fits best.
This was done in [ml_KMeans_search.py](../Workplace/ml_KMeans_search.py) to obtain a good feature set for clustering.

For more information on this see [notes_ml_clustering.md](notes_ml_clustering.md).

A brief overview of all the feature selection is given in [notes_ml_feature_selection.md](notes_ml_feature_selection.md).

For the documentation see [Documentation_module_ml.md](Documentation_module_ml.md).
