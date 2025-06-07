# Clustering

## Approach

- Considering `KMeans` from `sklearn.cluster`
- Considering `DBSCAN` from `sklearn.cluster`



## KMeans

After a few approaches with mixed results:

> Use [selection_arranged_union.csv](../Workplace/created_files/training_score/selection_arranged_union.csv):  
> > **Very weak** silhouette score for KMeans: `n_cluster = 2, score = 0.17`


> Use [selection_arranged_intersection.csv](../Workplace/created_files/training_score/selection_arranged_intersection.csv):  
> > **Okay** silhouette score for KMeans: `n_cluster = 2, score = 0.31`


> Using the new created [training_full_set.csv](../Workplace/created_files/training_full_set.csv):  
> Information: Contains all `anime_type`, dropped `on_list` related information
> > **Okay** silhouette score for KMeans: `n_cluster = 2, score = 0.41`


> Using the new created [training_full_set.csv](../Workplace/created_files/training_full_set.csv) but selecting only a few features **by hand**
> General bad results:  
> 
> ```python
> Features = ["anime_id", "season_fall", "season_spring", "season_summer", "season_winter", "year", "score", "rank", "episodes", "duration"]
> ```
>
> > **Okay** silhouette score for KMeans: `n_cluster = 6, score = 0.39`
> 
> ```python
> Features = ["anime_id", "season_fall", "season_spring", "season_summer", "season_winter", "year", "score", "rank", "episodes", "duration"]
> + ["anime_type_0","anime_type_CM","anime_type_Movie","anime_type_Music","anime_type_ONA","anime_type_OVA","anime_type_PV","anime_type_Special","anime_type_TV","anime_type_TV Special"]
> + ["source_4-koma manga","source_Book","source_Card game","source_Game","source_Light novel","source_Manga","source_Mixed media","source_Music","source_Novel","source_Original","source_Other","source_Picture book","source_Radio","source_Unknown","source_Visual novel","source_Web manga","source_Web novel"]
> + ["rating_G - All Ages","rating_PG - Children","rating_PG-13 - Teens 13 or older","rating_R - 17+ (violence & profanity)","rating_R+ - Mild Nudity","rating_Rx - Hentai"]
> ```
> > **Weak** silhouette score for KMeans: `n_cluster = 22, score = 0.20`


### Failed approach
We went and improved my feature selection, see [notes_ml_UnsupervisedFS.md](notes_ml_UnsupervisedFS.md).

Using several starting points and different feature selection methods, We tested all sets in [ml_KMeans_search.py](../Workplace/ml_KMeans_search.py).
The table below shows all outcomes with a **silhouette score larger than 3**.

| cluster |    score | set             |
|--------:|---------:|:----------------|
|       2 |   0.3181 | X_ByHand_25_ica |
|       2 |   0.3181 | X_ByHand_25_pca |
|       3 |   0.3223 | X_ByHand_25_ica |
|       3 |   0.3223 | X_ByHand_25_pca |
|       5 |   0.4242 | X_Full_pca      |
|       5 |   0.4242 | X_Full_ica      |
|       2 |   0.5480 | X_ByHand_10_ica |
|       2 |   0.5480 | X_ByHand_10_pca |
|       2 |   0.6545 | X_Full_pca      |
|       2 |   0.6545 | X_Full_ica      |
|       3 |   0.8578 | X_Full_ica      |
|       3 |   0.8578 | X_Full_pca      |

The column names **set** reference to the set of features used (not all sets are provides in this git, but they can be created using the files provides).

**Problem:** The cluster distribution is not good.

| cluster name | element amount |
|-------------:|---------------:|
|            0 |          17549 |
|            1 |             17 |
|              |                |
|            0 |          17559 |
|            1 |              7 |
|              |                |
|            0 |          17564 |
|            1 |              1 |
|            2 |              1 |
|              |                |
|            0 |          17516 |
|            1 |             14 |
|            2 |             25 |
|            3 |              3 |
|            4 |              8 |

**We have to many features that we can not handle properly.**


#### DBSCAN

Using ``DBSCAN`` form `sklearn.cluster`, clustering usually results either in only **one** cluster or in a few clusters with **90%** marked as **outliers**.
