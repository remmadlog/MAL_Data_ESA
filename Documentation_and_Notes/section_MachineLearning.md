



# Machine Learning

<div style="text-align: right"> 

(
[Back to main](../README.md)
)
</div>

**(May 2025)**

In this section I present my approach to score prediction.
For this I use different machine learning models as well as different features.

In contrast to the section above, this section is an actually  work in progress and will change over time.
I want to write this while working on it at the same time, in oder to see if this kind of notetaking could work for me.

## General Approach

### Data
- Use the data previously used.
- Use `anime_id_statistics.json` to split `on_list`.
  - `on_list` = `plan_to_watch` + `on_hold` + `dropped` + `completed` + `watching`:
    - dropping `completed`, since for new shows it is zero
  - Using ratios instead of totals: `watching` = `watching`/(`on_list` - `completed`).
  - Removing `completed` here as wells, since it would impact the ratio.
- Fiter/clean for:
  - `score` > 0
  - `status` == `Finished Airing`
  - `episodes` > 0
- Convert categories to features using `pd.get_dummies`.
  - As a result the amount of features explodes.
    - There are way to many studios.


### Regarding [ml_table_creation.py](../Workplace/ml_table_creation.py)
- Creating a table from anime_id_statistics.json.
  - Pull all the lokal files and download missing files on the fly.
  - End up with  `anime_id`, `watching`, `completed`, `on_hold`, `dropped`, `plan_to_watch` as columns.
- Load [S_1970_2024_merged.xlsx](../Workplace/created_files/S_1970_2024_merged.xlsx).
  - Use pd.get_dummies to get a column for each genre, theme and studio.
  - Group by anime_id to obtain a table with unique rows (one row per `anime_id`).
- Load [S_1970_2024_merged_unique.xlsx](../Workplace/created_files/S_1970_2024_merged_unique.xlsx).
  - Use pd.get_dummies for `anime_type`, `source`, `rating`,`season`.
  - Group by anime_id to obtain a table with unique rows (one row per `anime_id`).
- Merge all tables suitable.
- End up with a CSV file, since way too many columns for xlsx, that contains all needed information.
  - [training_score.csv](../Workplace/created_files/training_partial_set_OnList.csv)

### Regarding [ml_feature_selection.py](../Workplace/ml_fs_score_prediction.py)
- [training_score.csv](../Workplace/created_files/training_partial_set_OnList.csv) contains more than 1k features.
- 1k features are lot, therefore we do a feature selection.
- Feature selection methods used:
  - RreliefF feature scoring
   - Univariate feature selection:
     - chi2
     - anova
  - Correlation-based feature selection
    - Influence on target
  - Variance thresholding
    - Feature variance check (a constant feature is not a good feature)
  - Feature ranking
    - Using Orange
  - Random forest + feature importance
    - Using Orange
- Application:
  - Last two are obtained using Orange `ml_feature_selection.ows`.
    - Resulting in [ml_orange_feature_rank.xlsx](../Workplace/created_files/ml_orange_feature_rank.xlsx) and [ml_orange_feature_score_RandromTree.xlsx](../Workplace/created_files/ml_orange_feature_score_RandromTree.xlsx).
  - Rest is obtained using sklearn.feature_selection.
- Resting in 7 lists of features.
  - Considering union, intersections as well as partial (only top 50 or top 100 entries) union and intersection.
- Ending with 14 files, see [training_score](../Workplace/created_files/training_score).
  - One for each feature list and one for arranged combinations.
- In order to see which file will be of use, we will use all of them and decide afterward.
  - I have not a good feeling for what will work and what won't work, therefore I will try and see.

> For more information, see [notes_ml_featureselection](notes_ml_feature_selection.md).


### Regarding [ml_model_parameter_search.py](../Workplace/ml_model_parameter_search.py) (WIP)
- Using different ML models on our data to obtain prediction models:
  - Linear Regression
  - Neuronal Network
  - Decision Tree
  - Random Forest
  - Gradient Boosting
  - Elastic Net
  - XGBoosting
- A parameter search is used to find suitable parameters.
  - Note: fixing **random_state** is important and can otherwise result in non-usable parameters.
    - Learned that the hard way. 
- Focused on **r2** and **MAE** for scoring.

> [!IMPORTANT]  
> For more information and results, see [notes_ml_gridsearch_notes](notes_ml_gridsearch.md).\
> For a consideration of **all** features, see [notes_ml_gridsearch_all_features](notes_ml_gridsearch_all_features.md).


## Results

The main findings are presented in [notes_ml_model_evaluation](notes_ml_model_evaluation.md).
In short, the XGBoosting model performed best, but still has an MAE of 0.3.



<div style="text-align: right"> 

(
[Section start](#machine-learning) | 
[Back to main](../README.md)
)
</div>

---
