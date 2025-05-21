# Table of Contents

<details open>
<summary>Show table of contents</summary>

1. [Table of Contents](#table-of-contents)
2. [MyAnimeList Data Analysis](#myanimelist-data-analysis)
   - [Project Goal](#project-goal)
   - [Note](#note)
   - [Technologies & Tools](#technologies-and-tools)
   - [Todos](#todos)
3. [Data Analysis](#data-analysis)
   - [Summary: Brief Data Analysis Over Time](#summary-brief-data-analysis-over-time)
   - [Full Entry: Brief Data Analysis Over Time](section_DataAnalysis.md#1-brief-mal-data-analysis-over-time)
   - [Summary: Brief Analysis of Genre and Themes as well as Studios](#summary-brief-analysis-of-genre-and-themes-as-well-as-studios)
   - [Full Entry: Brief Analysis of Genre and Themes as well as Studios](section_DataAnalysis.md#2-brief-analysis-of-genre-and-themes-as-well-as-studios-of-the-mal-dataset)
   - [Summary: Brief Score-Oriented Analysis](#summary-brief-score-oriented-analysis)
   - [Full Entry: Brief Score-Oriented Analysis](section_DataAnalysis.md#3-brief-score-oriented-analysis-of-the-mal-dataset)
4. [Machine Learning](#machine-learning)
   - [Summary](#machine-learning)
   - [Full Entry](section_MachineLearning.md#machine-learning)
5. [Learnings](#learnings)

</details>




<div style="text-align: right"> 

(
[Section start](#table-of-contents) | 
[Top](#table-of-contents)
)
</div>

---

# MyAnimeList Data Analysis

This project explores data from [MyAnimeList (MAL)](https://myanimelist.net/) using the [Jikan API](https://jikan.moe/#). MAL is a social cataloging platform for anime and manga fans, offering a wide range of metadata and user-generated content.



## Project Goal
This repository serves as a **learning-by-doing** project focused on:

1. [x] Fetching anime/manga data using the Jikan API.
2. [x] Cleaning and transforming raw data.
   - [x] Create an easy-to-excess file containing the main data. 
     - [S_1970_2024_merged.xlsx](xlsx_tables/S_1970_2024_merged.xlsx) and [S_1970_2024_merged_unique.xlsx](xlsx_tables/S_1970_2024_merged_unique.xlsx).
3. [x] Exploring relationships between different features and categories.
4. [ ] Applying clustering techniques.
   - [ ] Performe a feature selection.
   - [ ] Train several models.
   - [ ] Evaluate the trained models.
5. [x] Performing predictive analysis using multiple ml models.
   - [x] Performe a feature selection.
   - [x] Train several models.
   - [x] Evaluate the trained models.


##  Note
This is a **learning project**, not intended for production or perfection. The goal is to practice real-world data workflows and apply analytical thinking in a practical context.


##  Technologies and Tools
- **Python** (pandas, sklearn, matplotlib, etc.)
- **Jikan API** for MAL data
- **Orange**
- **Git** (repo, markdowns)


## Todos
This is a very brief list of some task I want to do at some point.
In general, they don't take priority over the main project goals.
> Maybe not doing any of them, maybe I will do all of them.
> No promises were made.

- [ ] Move from `.xlsx` to `.csv`.
- [ ] Highlight the combined dataset.
- [ ] Documentation for the following files:
  - [ ] [module_supply.py](module_supply.py)
  - [ ] [module_creation.py](module_creation.py)
- [ ] Mentioning and explaining the Jikan API.
- [ ] Cleaner and more focused version of:
  - [ ] [module_supply.py](module_supply.py)
  - [ ] [module_creation.py](module_creation.py)
- [ ] Creating (cleaner) modules for
    - [ ] Automate/easy analysis
    - [ ] Gridsearch
    - [ ] Training and evaluation


<div style="text-align: right"> 

(
[Section start](#myanimelist-data-analysis) | 
[Top](#table-of-contents)
)
</div>



---

# Data Analysis
> See [section_DataAnalysis](section_DataAnalysis.md) for full information.

## Summary: Brief Data Analysis Over Time
This is a high-level summary of trends in the MAL dataset, focusing on anime production, scoring, and engagement over time.

### Key Insights

- **Anime Production** has grown steadily, with a COVID-19 dip around 2020.
- **ONAs** (Original Net Animations) surged recently, while **movies and specials** declined.
- **Source Materials**: Manga remains dominant; light/web novels are rising; visual novels declining.
- **Scores** have increased over time — possibly due to shifting rating behavior.
- **Engagement** (user scores, favorites, lists) has dropped per title since ~2015.
- **Episode Counts** have fallen due to split-season shows.
- **Short-form anime** (under 5 min) is more common now.
- **Ratings**: Most content now targets teens (PG-13+), with R+/Rx growing in count but not proportion.

> [!IMPORTANT]  
> This summary is part of a broader, ongoing exploration of the MAL dataset as a data science learning project.  
> For more details see [Data Analysis](section_DataAnalysis.md).

<div style="text-align: right"> 

(
[Section start](#data-analysis) | 
[Top](#table-of-contents)
)
</div>


## Summary: Brief Analysis of Genre and Themes as well as Studios

This analysis focuses on the distribution and average scores of **genres**, **themes**, and to a lesser extent, **studios**, based on completed and rated anime entries from the MyAnimeList (MAL) dataset.

### Key Insights

- **Data Filters**: Only completed entries with non-zero scores were analyzed.
- **Genre Trends**:
  - Most common: **Comedy**, **Action**, **Fantasy** (3,000+ entries each).
  - Least common: **Erotica**, **Girls Love**, **Gourmet** (<250 entries).
- **Theme Trends**:
  - Most common: **Music**, followed by **School**.
  - Least common: **Villainess**.
  - Many entries lack themes (~6,200), fewer lack genres (~2,300).
- **Average Scores**:
  - Highest scoring genres: **Award Winning**, **Suspense**, **Mystery**, **Drama**, **Romance**.
  - Lowest scoring genre: **Avant Garde** (<5.5 avg score).
  - Highest scoring themes (less common): **Love Polygon**, **Childcare**, **Iyashikei**.
- **Studios**: Considered but not deeply analyzed in this overview.

> [!IMPORTANT]  
> This summary is part of a broader, ongoing exploration of the MAL dataset as a data science learning project.  
> For more details see [Data Analysis](section_DataAnalysis.md).

<div style="text-align: right"> 

(
[Section start](#data-analysis) | 
[Top](#table-of-contents)
)
</div>


## Summary: Brief Score-Oriented Analysis

This section explores how various features relate to **anime scores** in the MAL dataset, focusing on completed and scored entries only.

### Key Insights

- **Higher scores** are linked to:
  - More **user ratings**, **favorites**, and **list adds**
  - **Longer durations** (especially movies and full-length episodes)
- **High episode counts** do *not* correlate with higher scores — most top entries have **<13 episodes**.
- **Top 100 shows** are mostly:
  - **TV series** (70%), sourced from **Manga**, rated **PG-13**, and air in **Fall**.
  - Dominated by studios like **Madhouse**, **MAPPA**, and **Sunrise**.
- **Drama** and **Action** are leading genres; **Historical** is the top theme.
- **Recent entries (past 4 years)** make up a large portion of high-scoring anime.

### Trends Over Time

- **Scores rose** for most types, especially **Movies**, **OVAs**, and **Music**.
- **Originals** and **books** also gained in average score.
- **Rx-rated** shows have the highest recent scores.
- Entries with **short durations** or **extreme episode counts** are harder to assess due to sample size issues.

> [!IMPORTANT]  
> This summary is part of a broader, ongoing exploration of the MAL dataset as a data science learning project.  
> For more details see [Data Analysis](section_DataAnalysis.md).

<div style="text-align: right"> 

(
[Section start](#data-analysis) | 
[Top](#table-of-contents)
)
</div>

--- 



# Machine Learning
> See [section_MachineLearning](section_MachineLearning.md) for full information.

## A Summary

This section explores predicting anime scores using various **machine learning models** and **feature selection techniques**.

### Data & Preprocessing
- Based on cleaned MAL data with only scored, finished entries.
- Uses `anime_id_statistics.json` and `S_1970_2024_merged.xlsx`.
- Ratios (e.g. watching/on_list) are used over raw counts.
- Features expanded using `pd.get_dummies`, leading to **1000+ features**.

### Feature Selection
- Multiple techniques applied:
  - **RreliefF**, **chi²**, **ANOVA**, **correlation**, **variance thresholding**
  - **Random Forest** and **ranking via Orange**
- Results saved across 14 feature files for later model testing.

### Models & Parameter Search
- Models used:
  - **Linear Regression**, **Neural Network**, **Decision Tree**, **Random Forest**, **Gradient Boosting**, **Elastic Net**, **XGBoost**
- **r²** and **MAE** are primary evaluation metrics.
- Emphasis on experimentation due to uncertainty about what features will perform well.

> [!IMPORTANT]  
> Detailed results and notes in:  
> [notes_ml_featureselection](notes_ml_featureselection.md)  
> [notes_ml_gridsearch](notes_ml_gridsearch.md)  
> [notes_ml_gridsearch_all_features](notes_ml_gridsearch_all_features.md)  
> [notes_ml_model_evaluation](notes_ml_model_evaluation.md)



<div style="text-align: right"> 

(
[Section start](#machine-learning) | 
[Top](#table-of-contents)
)
</div>



# Learnings

**(May 2025)**

Let me present my, probably incomplete, list of learnings so far.

(Keep track on what you learned so you see your progress and can present them without looking at everything you did. The later case will take way more time...)

- **General Learnings**
  - Be clear and concise.
  - Learning takes time -- plan ahead.
  - Mistakes are part of progress.
  - Prioritize and track tasks.

- **Data Collection & Cleaning**
  - Collecting and organizing data takes time.
  - Track data, warnings, and errors.
  - Handle API issues as they come.

- **Data Analysis**
  - Use both ratios and totals.
  - Avoid overcrowded plots.
  - Plot during analysis to reduce rework.

- **Programming**
  - Use `requests` to gather data.
  - Logging helps manage complexity.
  - Learn here to get help.
  - Efficiency matters less for small datasets.
  - Use Markdown and Git (with clear commits).

- **Machine Learning**
  - Feature selection methods vary in impact.
  - Feature size affects outcomes.
  - Choose grid search params carefully.
  - Parameters for small sets may not generalize.


<div style="text-align: right"> 

(
[Section start](#learnings) | 
[Top](#table-of-contents)
)
</div>

---