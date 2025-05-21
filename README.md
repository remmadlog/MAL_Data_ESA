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
4. [Machine Learning](#machine-learning)
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

- Fetching anime/manga data using the Jikan API
- Cleaning and transforming raw data
- Exploring relationships between different features
- Applying clustering techniques
- Performing predictive analysis


##  Note
This is a **learning project**, not intended for production or perfection. The goal is to practice real-world data workflows and apply analytical thinking in a practical context.


##  Technologies and Tools
- **Python** (pandas, sklearn, matplotlib, etc.)
- **Jikan API** for MAL data
- **Orange**


## Todos
This is a very brief list of some task I want to do at some point.

- General documentation
- Mentioning and explain the Jikan API usage
- Cleaner and more focused version of most python files


<div style="text-align: right"> 

(
[Section start](#myanimelist-data-analysis) | 
[Top](#table-of-contents)
)
</div>



---

# Data Analysis
> See [section_DataAnalysis.md](section_DataAnalysis.md) for full information.

## Summary: Brief MAL Data Analysis Over Time
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

> This summary is part of a broader, ongoing exploration of the MAL dataset as a data science learning project.
> For more details see [Data Analysis](section_DataAnalysis.md).

<div style="text-align: right"> 

(
[Section start](#data-analysis) | 
[Top](#table-of-contents)
)
</div>


## Summary: Genre, Theme, and Studio Analysis (MAL Dataset)

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
> See [section_MachineLearning.md](section_MachineLearning.md) for full information.

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

> Detailed results and notes in:  
> [notes_ml_featureselection.md](notes_ml_featureselection.md)  
> [notes_ml_gridsearch.md](notes_ml_gridsearch.md)  
> [notes_ml_gridsearch_all_features.md](notes_ml_gridsearch_all_features.md)
> [notes_ml_model_evaluation.md](notes_ml_model_evaluation.md)



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

- **General learnings:**
  - Keep things short and clear.
  - Things take more time than you think they do.
    - This is especially true if you are learning while doing.
  - It is okay to make mistakes.
    - They are part of the process.
  - Managing a solo learning project takes effort and time.
    - Planing ahead can have an enormous impact on workflow.
    - Keeping track of todos and priories what to handle and if it should be handled at all (at the moment).
- **Data collecting and cleaning:**
  - Collecting takes time.
  - Organizing is a huge part and needs to be taken in consideration.
    - Tracking collected data, as well as warnings and errors.
  - Using an API and handling occurring problems.
- **Data analysis:**
  - Ratios and totals are both important and should both considered before making assumptions.
  - A Plot can be overwhelming when it provides to much information.
  - Creating plots while analysing to avoid to many corrections later on. 
- **Programming:**
  - Gathering data using request.
  - Using logging if things get overwhelming.
  - A feeling for pandas:
    - What can I do, where to find help, how to identify helpful advice.
    - Using pandas in general.
  - Using seaborn for heat plots.
    - Using matplotlib for plotting in general.
    - Efficiency is not the most important part if your data set is not overwhelmingly large.
    - It is okay to do things why to complicate if you are learning.
  - Using markdowns for e.g. a Git README.
    - Using Git to back up und publish a project.
    - Clear commit comments are quit useful.
- **Machine learning:**
  - Feature selection
    - Different methods can provide vastly different results.
    - Different feature sizes can make a significant differance.
  - Choosing parameters
    - A gridsearch takes time, chose the candidates wisely.
    - Parameters for a smaller feature set do not necessarily provide an indication for the larger feature set.



<div style="text-align: right"> 

(
[Section start](#learnings) | 
[Top](#table-of-contents)
)
</div>

---