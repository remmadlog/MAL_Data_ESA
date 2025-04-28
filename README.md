# MyAnimeList Data Analysis (via Jikan API)

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

##  Technologies & Tools
- **Python** (pandas, sklearn, matplotlib, etc.)
- **Jikan API** for MAL data



# Analysis  
## Brief MAL Data Analysis Over Time

Below you'll find a **very brief** analysis of some trends in the MAL dataset. With more time and demand, much deeper insights could be extracted, but that’s not the goal here. Not every plot is shown, and not every detail within each plot is discussed.

**This is mainly a learning project. I’m doing this to get more familiar with the tools involved.**

---

### Remarks
- "Engagement by year" refers to engagement **with shows from that year**, not interactions that happened **during** that year.
- The low number of shows in the early years makes it harder to draw solid conclusions.
- For entries before 2004, engagement occurred post-release, since MAL launched in November 2004.

---


### Entry Growth Over Time

It’s no surprise that the number of entries has grown over time, especially in the last decade.

<img src="Plots/overtime/YEAR_Amount_(Shows_TV+_Movie+_Other).png" width="750">

A clear dip appears around 2020 due to COVID-19.  
- **Movies and specials** decreased.  
- **Music-related content** increased noticeably.

---

### TV, OVA, ONA Trends

<img src="Plots/overtime/YEAR_Amount_(TV_OVA_ONA).png" width="750">


- ONAs have exploded in recent years.  
  Titles like *Cyberpunk: Edgerunners* and *Shiguang Dailiren* are standout examples.

---

### Movie & Special Output


<img src="Plots/overtime/YEAR_Amount_(Movie_Special).png" width="750">

A more focused look shows the decline in movie and special releases over time.

---

### Source Material Usage

<img src="Plots/overtime/YEAR_Amount_SOURCE.png" width="750">

- Original works had a notable rise (and possibly a recent fall).
- Manga remains a strong, consistent source.
- Web manga and light novels are rising.
- Visual novels and traditional novels are declining.

Also visualized here:  
<img src="Plots/overtime/Heatmap_TF_Source.png" width="750">

---

### Performance & Score Trends

Just the number of shows doesn't tell the full story. Performance matters too.

<img src="Plots/overtime/Heatmap_average_Score_Source_TF.png" width="750">

- Original works tend to score higher in the last decade.

But scores in general have been rising:

<img src="Plots/overtime/YEAR_SCORE_average.png" width="750">

- The average score rose by ~0.5 points over the past 5 years.
- A 6.5 today might’ve been a 6.0 thirty years ago, but we can’t confirm without knowing when scores were given.
- Still, the score increase appears consistent, not skewed by outliers.

---

### Engagement Trends

<img src="Plots/overtime/YEAR_ScoredBy_average.png" width="750">

- Fewer people are scoring shows since 2015.
- Fewer than half of all shows are scored by more than 5,000 users.

Other engagement metrics follow similar trends:

<img src="Plots/overtime/YEAR_OnList_average.png" width="750">
<img src="Plots/overtime/YEAR_FAVORITES_average.png" width="750">

- Most shows have low engagement.  
- A small number of hits drive the stats up.
- Average engagement per show has dropped since 2015, even though the total number of shows is about the same.

We can’t say overall MAL activity is lower, just that newer shows get less engagement on average.

---

### Other Notable Trends

#### Duration

<img src="Plots/overtime/Heatmap_average_Duration_Type_TF.png" width="750">

- **Movies** are longer than they used to be.
- **TV specials** are now half as long as pre-2000.
- **TV shows** stayed fairly consistent.

#### Episodes

<img src="Plots/overtime/Heatmap_average_Episodes_Type_TF.png" width="750">

- Show lengths (episode count) are down, likely due to seasonal splits.
  - e.g. *The Apothecary Diaries* S1 & S2 = ~50 episodes total, but recorded as two ~25-episode series.
- Some movies are split into multiple parts but counted under one entry.
- OVAs and ONAs resemble TV shows more than ever.

Also illustrated in:  
<img src="Plots/overtime/Heatmap_TF_Type.png" width="750">

---

### Rating Distributions

<img src="Plots/overtime/Heatmap_TF_Rating_T.png" width="750">

- Most content now targets teens or older:
  - 50%+ rated **PG-13**
- A lange amount targets everyone:
  - ~22% have no restriction
- **R+/Rx (NSFW)** is rarer in proportion, but still increased in raw numbers.

See also:  
<img src="Plots/overtime/Heatmap_TF_Rating.png" width="750">

- 60%+ of R+/Rx content was released in the last 25 years, but total releases have also skyrocketed.

---

### Episode Lengths

<img src="Plots/overtime/Heatmap_DF_TF_T.png" width="750">

- Most entries today are either:
  - Under 5 minutes, or  
  - 20–30 minutes long.
- Short-format anime is significantly more common now.

---

## Predictions

I originally wanted to predict scores, but started by analyzing trends over time.

Here’s a **prediction of seasonal averages for 2025**, based on seasonal and yearly groupings.

Grouping by **year and season** instead of just year allowed more granular predictions (e.g. Winter 2025, Spring 2025, etc.).

**Postponed**
- I tried using ARIMA from sklearn
- only got negative r2 values
  - even using a parameter search
- not sure where I went wrong
- needs more investigating, will skip this for now

---

## Conclusion
The MAL dataset provides a depp insight in the development and propularity of anime over the last 25 years and gives a good idea of teh development of the last 55 years.


## Note
There’s still plenty more to explore, especially:
- Genre and theme analysis
- Deeper score prediction models

That’s where I plan to head next!
