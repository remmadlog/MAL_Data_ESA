# Feature Selection

## First steps
Presenting feature selection methods used in [ml_feature_selection.py](../Workplace/ml_fs_score_prediction.py).

Thees are marly baby steps and first tries, They are more advanced later on.

<details>
<summary>ml_feature_selection.py</summary>

### General Approach

My idea was to rank the **1175** features (after removing) in different ways and use the intersection or the union or some kind of combination to obtain a reasonable sized feature set.

1. Removing of not needed information like
    - anime_id (meta)
    - year
    - rank
    - completed
    - score (target)
2. Creating target set
3. Use different methods for the selection
   - chi2
     - Only for classification
   - anova
   - Correlation-based Feature Selection
   - Variance Thresholding
   - Feature Ranking in Orange
     - univar
     - rrelieff
   - Random Forest top Features in Orange
4. Processing
   - Creating different feature sets based on the selection before.
     - union
     - intersection
     - combination of both while only considering top **k** features in each set.
       - Not done for features_variance, since it's not sorted.
5. Saving files as CSV

### Feature Appearance

The features come in different groups:
1. Categorial
   - Themes
   - Genres
   - Studios
     - This is the reason for so many features.
   - Rating
   - Source
   - Anime Type
   - Season
2. Other
    - Epidotes (total)
    - Duration (total in minutes)
    - On List (ratio)
      - **Split** in: watching, on_hold, dropped, plan_to_watch
        - "Completed" was **removed**, since for **new** shows this is always **zero**

### Results

We end up with 7 lists of features:
- features_chi2
- features_anova
- features_cor_val
- features_variance
- features_univar
- features_rrelieff
- features_tree_r2_mean

Considering the union and the intersection as a start:
- union length: 
- intersection length: 

Creating sets by only taking the top 50 and top 100 features (all but features_variance -- it is not sorted):
- union_half 
  - union of the top 100
- union_quarter           
  - union of the top 50
- combination_half        
  - union of the top 100 intersected with intersection of all lists
- combination_quarter     
-   union of the top 50 intersected with intersection of all lists

</details>














## More complicated approaches

Presenting feature selection methods used in [ml_unsupervised_fs.py](../Workplace/ml_unsupervised_fs.py)

Here we present more techniques, more understanding, more structure.

<details>
<summary>ml_unsupervised_fs.py</summary>

Considering the application in [ml_KMeans_search.py](../Workplace/ml_KMeans_search.py) as well as the feature selection functions in [module_ml.py](../Workplace/module_ml.py):


### Unsupervised feature selection methods

- autoencoder_feature_selector
- clustering_stability_selector
- correlation_selector
- entropy_feature_selector
- eval_scor_pred
- fa_selector
- feature_selection_pipeline
- fs_f_classif
- greedy_clustering_feature_selection
- ica_selector
- laplacian_score
- pca_selector
- silhouette_feature_selector
- tsne_sensitivity_selector
- variance_threshold_selector


- By Hand: Selecting, or rather **not** selecting features by hand.
  - remove every feature that has less than ``n`` entries (if entries are ``1`` or ``0``)

Several of thees methods are used in [ml_unsupervised_fs.py](../Workplace/ml_unsupervised_fs.py) to finde good features for clustering.
The resulting features are than used in [ml_KMeans_search.py](../Workplace/ml_KMeans_search.py) to see wich set of features provides the best results.
An application is than done in [ml_clustering.py](../Workplace/ml_clustering.py).

For more details on each method see [Documentation_module_ml.md](Documentation_module_ml.md).
For more details on how they were used see [notes_ml_UnsupervisedFS.md](notes_ml_UnsupervisedFS.md).



</details>