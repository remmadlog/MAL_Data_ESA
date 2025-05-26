# Updates

A probably not compleat list of updates.


<details>
<summary>26.05.2025</summary>


> created:
> - [module_ml.py](module_ml.py)
>   - See regarding `module_ml.py` for more information.
> - [Documentation_module_ml.md](Documentation_module_ml.md)


> regarding [README.md](README.md):
> - Added subsection about documentations.


> regarding [module_ml.py](module_ml.py)
> - Collection of functions needed all over the ml part.
> - Managing imports and streamlining files respectively.
> - See 


> regarding [ml_fs_score_prediction.py](ml_fs_score_prediction.py)
> - Streamlined, using `module_ml.py`.
> - Should be more adaptable for **slightly** different data.


> regarding [ml_model_evaluation.py](ml_model_evaluation.py)
> - Streamlined, using `module_ml.py`.


> regarding [ml_model_parameter_search.py](ml_model_parameter_search.py)
> - Moved functions to `module_ml.py`.
> - Reduced imports.


> regarding [ml_RegModel_training.py](ml_RegModel_training.py)
> - Reduced imports using `from module_ml import *`.
> - Changing file from `ml_fs_score_prediction.py` is now cleaner.
>   - Only loading one file, change file name if needed.
> - Changing saving path for trained models is now easier.
>   - Just change `path = "xlsx_tables/training_score/trained_models/"` in upper part.


> regarding [ml_RegModel_prediction.py](ml_RegModel_prediction.py)
> - Reduced imports using `from module_ml import *`.
> - Changing file from `ml_fs_score_prediction.py` is now cleaner.
>   - Only loading one file, change file name if needed.
> - Loading models and saving predictions can now be adjusted by changing their corresponding paths.
>   - loading: `path_model = "xlsx_tables/training_score/trained_models/"`.
>   - saving: `path_pred = "xlsx_tables/training_score/"`.


</details>

---

<details>
<summary>23.05.2025</summary>

> This one might be a bit to detailed

> created:
> - [ml_clustering.py](ml_clustering.py)
>   - use `sklearn` for clustering
> - [section_updates.md](section_updates.md)
>   - For keeping track of larger changes and updates
> - [notes_ml_clustering.md](notes_ml_clustering.md)
>   - To take notes for `ml_clustering.py`
> - [training_full_set.csv](xlsx_tables/training_full_set.csv)
>   - Created using [ml_table_creation.py](ml_table_creation.py)
>   - Contains **the whole data set**, but **no feature related to `on_list`**
> - Added: [predictions.csv](xlsx_tables/training_score/predictions.csv)


> regarding [training_partial_set_OnList.csv](xlsx_tables/training_partial_set_OnList.csv):
> - name change of `training_score.csv` to `training_partial_set_OnList.csv`
> - moved location from `xlsx_tables/training_score` to `xlsx_tables`
> - influence on
>   - `ml_feature_selection.py`


> regarding [ml_feature_selection.py](ml_fs_score_prediction.py):
> - changes due to name changes of `training_partial_set_OnList.csv`


> reading [ml_RegModel_prediction.py](ml_RegModel_prediction.py) and [ml_RegModel_training.py](ml_RegModel_training.py):
> - name change


> regarding [ml_table_creation.py](ml_table_creation.py):
> - saving of additional table: `training_full_set.csv`


</details>

