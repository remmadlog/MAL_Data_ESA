# Updates

A probably not compleat list of updates.



<details>
<summary>07.06.2025</summary>

> created:
> - [notes_ml_UnsupervisedFS.md](notes_ml_UnsupervisedFS.md)
>   - Notes on unsupervised features selection.
> - [ml_KMeans_search.py](../Workplace/ml_KMeans_search.py)
>   - Using KMeans for clustering, but finding the right amount of clusters too.
> - [ml_unsupervised_fs.py](../Workplace/ml_unsupervised_fs.py)
>   - Using several FS methods for dimensional reduction and more
>   - Combined and independent use cases

> Updated
> - [Documentation_module_ml.md](Documentation_module_ml.md)
>   - Added information about the new functions.
> - [notes_ml_clustering.md](notes_ml_clustering.md)
>   - Updated results and conclusion.
> - [notes_ml_feature_selection.md](notes_ml_feature_selection.md)
>   - Added information for new functions.
> - [ml_clustering.py](../Workplace/ml_clustering.py)
>   - Change content, now only DBSCAN example.
> - [ml_table_creation.py](../Workplace/ml_table_creation.py)
>   - Creates now additional table:
>     - Without a decomposition of ``on_list``, but containing all data
> - [module_ml.py](../Workplace/module_ml.py)
>   - Added nes functions
>     - Unsupervised feature selection
>       - Variance Selector
>       - Correlation Selector
>       - Entropy Selector
>       - Factor Analysis
>       - Auto Encoder
>       - TSNE Selector
>       - PCA Selector
>       - ICA Selector
>   - Clustering
>     - KMeans
>     - DBSCAN

</details>

---

<details>
<summary>28.05.2025</summary>

> Moved a lot of files for a better **first** impression.
> Tried moving files in a more detailed manner, but had to change to many references in path by hand.

</details>

---

<details>
<summary>26.05.2025</summary>


> created:
> - [module_ml.py](../Workplace/module_ml.py)
>   - See regarding `module_ml.py` for more information.
> - [Documentation_module_ml.md](Documentation_module_ml.md)


> regarding [README.md](../README.md):
> - Added subsection about documentations.


> regarding [module_ml.py](../Workplace/module_ml.py)
> - Collection of functions needed all over the ml part.
> - Managing imports and streamlining files respectively.
> - See 


> regarding [ml_fs_score_prediction.py](../Workplace/ml_fs_score_prediction.py)
> - Streamlined, using `module_ml.py`.
> - Should be more adaptable for **slightly** different data.


> regarding [ml_model_evaluation.py](../Workplace/ml_model_evaluation.py)
> - Streamlined, using `module_ml.py`.


> regarding [ml_model_parameter_search.py](../Workplace/ml_model_parameter_search.py)
> - Moved functions to `module_ml.py`.
> - Reduced imports.


> regarding [ml_RegModel_training.py](../Workplace/ml_RegModel_training.py)
> - Reduced imports using `from module_ml import *`.
> - Changing file from `ml_fs_score_prediction.py` is now cleaner.
>   - Only loading one file, change file name if needed.
> - Changing saving path for trained models is now easier.
>   - Just change `path = "xlsx_tables/training_score/trained_models/"` in upper part.


> regarding [ml_RegModel_prediction.py](../Workplace/ml_RegModel_prediction.py)
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
> - [ml_clustering.py](../Workplace/ml_clustering.py)
>   - use `sklearn` for clustering
> - [section_updates.md](section_updates.md)
>   - For keeping track of larger changes and updates
> - [notes_ml_clustering.md](notes_ml_clustering.md)
>   - To take notes for `ml_clustering.py`
> - [training_full_set.csv](../Workplace/created_files/training_full_set.csv)
>   - Created using [ml_table_creation.py](../Workplace/ml_table_creation.py)
>   - Contains **the whole data set**, but **no feature related to `on_list`**
> - Added: [predictions.csv](../Workplace/created_files/training_score/predictions.csv)


> regarding [training_partial_set_OnList.csv](../Workplace/created_files/training_partial_set_OnList.csv):
> - name change of `training_score.csv` to `training_partial_set_OnList.csv`
> - moved location from `xlsx_tables/training_score` to `xlsx_tables`
> - influence on
>   - `ml_feature_selection.py`


> regarding [ml_feature_selection.py](../Workplace/ml_fs_score_prediction.py):
> - changes due to name changes of `training_partial_set_OnList.csv`


> reading [ml_RegModel_prediction.py](../Workplace/ml_RegModel_prediction.py) and [ml_RegModel_training.py](../Workplace/ml_RegModel_training.py):
> - name change


> regarding [ml_table_creation.py](../Workplace/ml_table_creation.py):
> - saving of additional table: `training_full_set.csv`


</details>

