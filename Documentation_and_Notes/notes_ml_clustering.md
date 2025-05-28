# Clustering

## Approach

- Considering `KMeans` from `sklearn.cluster`


### KMeans n_cluster search

> Use [selection_arranged_union.csv](../Workplace/created_files/training_score/selection_arranged_union.csv):  
> > **Very weak** silhouette score for KMeans: `n_cluster = 2, score = 0.17`


> Use [selection_arranged_intersection.csv](../Workplace/created_files/training_score/selection_arranged_intersection.csv):  
> > **Weak** silhouette score for KMeans: `n_cluster = 2, score = 0.31`


> Using the new created [training_full_set.csv](../Workplace/created_files/training_full_set.csv):  
> Information: Contains all `anime_type`, dropped `on_list` related information
> > **Weak** silhouette score for KMeans: `n_cluster = 2, score = 0.41`


> Using the new created [training_full_set.csv](../Workplace/created_files/training_full_set.csv) but selecting only a few features **by hand**
> General bad results:  
> 
> ```python
> Features = ["anime_id", "season_fall", "season_spring", "season_summer", "season_winter", "year", "score", "rank", "episodes", "duration"]
> ```
> 
> > **Weak** silhouette score for KMeans: `n_cluster = 6, score = 0.39`
> 
> ```python
> Features = ["anime_id", "season_fall", "season_spring", "season_summer", "season_winter", "year", "score", "rank", "episodes", "duration"]
> + ["anime_type_0","anime_type_CM","anime_type_Movie","anime_type_Music","anime_type_ONA","anime_type_OVA","anime_type_PV","anime_type_Special","anime_type_TV","anime_type_TV Special"]
> + ["source_4-koma manga","source_Book","source_Card game","source_Game","source_Light novel","source_Manga","source_Mixed media","source_Music","source_Novel","source_Original","source_Other","source_Picture book","source_Radio","source_Unknown","source_Visual novel","source_Web manga","source_Web novel"]
> + ["rating_G - All Ages","rating_PG - Children","rating_PG-13 - Teens 13 or older","rating_R - 17+ (violence & profanity)","rating_R+ - Mild Nudity","rating_Rx - Hentai"]
> ```
> > **Weak** silhouette score for KMeans: `n_cluster = 22, score = 0.20`


