# Feature Selection

Here I present a short overview of my feature selection methods used in [ml_feature_selection.py](ml_fs_score_prediction.py).

## General Approach

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
     - Only for classes &#8594; made targets to strings
   - anova
   - Correlation-based Feature Selection
   - Variance Thresholding
     - could not sort the outcome
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

## Feature Appearance

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




## Results

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