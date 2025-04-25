"""
Creating table using the main tables obtained by the __module_creation__
"""
from itertools import groupby

from module_creation import *
from warnings import simplefilter

# since the way we create the table below is probably not the best way, receiving the warning:
    # "PerformanceWarning: DataFrame is highly fragmented.  This is usually the result of calling `frame.insert` many times,
    # which has poor performance.  Consider joining all columns at once using pd.concat(axis=1) instead. To get a de-fragmented frame,
    # use `newframe = frame.copy()` table_full_studios.loc[str(id),item] = 1"
simplefilter(action="ignore", category=pd.errors.PerformanceWarning)

    # FutureWarning: The behavior of DataFrame concatenation with empty or all-NA entries is deprecated. In a future version,
    # this will no longer exclude empty or all-NA columns when determining the result dtypes. To retain the old behavior, exclude
    # the relevant entries before the concat operation.
warnings.filterwarnings("ignore", category=FutureWarning)


pd.options.display.width= None
pd.options.display.max_columns= None
pd.set_option('display.max_rows', 3000)
pd.set_option('display.max_columns', 3000)






# loading tables created by using the module_creation
table = pd.read_excel('Season_1970_2024_SGT.xlsx')
table_main = pd.read_excel('Season_1970_2024_main.xlsx')



"""
Procedure:
    We going to create several tables and combine them. This provides a better overview and makes it easier to change and fix things.

What are interesting relations?
    -- per year:
        -- amount of anime_type (TV, Movie....)
        -- average, min, max score
            -- consider all, TV, and Movie
        -- score distribution of tv shows
"""

#todo: Special == TV Special

# Create a table that gives the amount of anime_type by year
#   table_main[table_main["anime_type"] == "TV"].groupby("year").size()
#       -- In table_main where anime_type == "TV" count (no nan entries) per year
tab_year_type = pd.concat([
    table_main.groupby("year").size(),
    table_main[(table_main["anime_type"] == "TV")
               | (table_main["anime_type"] == "Movie")
               | (table_main["anime_type"] == "OVA")
               | (table_main["anime_type"] == "Special")
               | (table_main["anime_type"] == "TV Special")
               | (table_main["anime_type"] == "ONA")].groupby("year").size(),
    table_main[(table_main["anime_type"] == "TV")
               | (table_main["anime_type"] == "OVA")
               | (table_main["anime_type"] == "ONA")].groupby("year").size(),
    table_main[(table_main["anime_type"] == "Movie")
               | (table_main["anime_type"] == "Special")
               | (table_main["anime_type"] == "TV Special")].groupby("year").size(),
    table_main[(table_main["anime_type"] == "Music")
               | (table_main["anime_type"] == "CM")
               | (table_main["anime_type"] == "PV")].groupby("year").size(),
    table_main[table_main["anime_type"] == "TV"].groupby("year").size(),
    table_main[table_main["anime_type"] == "OVA"].groupby("year").size(),
    table_main[table_main["anime_type"] == "ONA"].groupby("year").size(),
    table_main[table_main["anime_type"] == "Movie"].groupby("year").size(),
    table_main[(table_main["anime_type"] == "Special")
               | (table_main["anime_type"] == "TV Special")].groupby("year").size(),
    table_main[table_main["anime_type"] == "Music"].groupby("year").size(),
    table_main[table_main["anime_type"] == "CM"].groupby("year").size(),
    table_main[table_main["anime_type"] == "PV"].groupby("year").size(),
    table_main[(table_main["anime_type"] != "TV")
               & (table_main["anime_type"] != "Movie")
               & (table_main["anime_type"] != "OVA")
               & (table_main["anime_type"] != "Special")
               & (table_main["anime_type"] != "TV Special")
               & (table_main["anime_type"] != "ONA")
               & (table_main["anime_type"] != "Music")
               & (table_main["anime_type"] != "CM")
               & (table_main["anime_type"] != "PV")].groupby("year").size()

],
axis =1)
tab_year_type.columns = ["#shows", "#TV_Movie_OVA_Special_ONA", "#TV_OVA_ONA", "#Movie_Special", "#Music_CM_PV",  "#TV_shows", "#OVA_shows", "#ONA_shows", "#Movie_shows", "#Special_shows", "#Music_shows", "#CM_shows", "PV_shows", "#Other_shows"]





# Create a table that gives the mean, max and min of score per year
#   table_main.groupby(["year"])["score"].mean()
#       -- In table_main get the mean score for each year
tab_year_score = pd.concat([
    table_main.groupby(["year"])["score"].mean(),
    table_main.groupby(["year"])["score"].min(),
    table_main.groupby(["year"])["score"].max(),
    table_main[(table_main["anime_type"] == "TV")
               | (table_main["anime_type"] == "Movie")
               | (table_main["anime_type"] == "OVA")
               | (table_main["anime_type"] == "Special")
               | (table_main["anime_type"] == "TV Special")
               | (table_main["anime_type"] == "ONA")].groupby("year")["score"].mean(),
    table_main[(table_main["anime_type"] == "TV")
               | (table_main["anime_type"] == "OVA")
               | (table_main["anime_type"] == "ONA")].groupby("year")["score"].mean(),
    table_main[(table_main["anime_type"] == "Movie")
               | (table_main["anime_type"] == "Special")
               | (table_main["anime_type"] == "TV Special")].groupby("year")["score"].mean(),
    table_main[(table_main["anime_type"] == "Music")
               | (table_main["anime_type"] == "CM")
               | (table_main["anime_type"] == "PV")].groupby("year")["score"].mean(),
    table_main[(table_main["anime_type"] == "TV")
               | (table_main["anime_type"] == "Movie")
               | (table_main["anime_type"] == "OVA")
               | (table_main["anime_type"] == "Special")
               | (table_main["anime_type"] == "TV Special")
               | (table_main["anime_type"] == "ONA")].groupby("year")["score"].min(),
    table_main[(table_main["anime_type"] == "TV")
               | (table_main["anime_type"] == "OVA")
               | (table_main["anime_type"] == "ONA")].groupby("year")["score"].min(),
    table_main[(table_main["anime_type"] == "Movie")
               | (table_main["anime_type"] == "Special")
               | (table_main["anime_type"] == "TV Special")].groupby("year")["score"].min(),
    table_main[(table_main["anime_type"] == "Music")
               | (table_main["anime_type"] == "CM")
               | (table_main["anime_type"] == "PV")].groupby("year")["score"].min(),
    table_main[(table_main["anime_type"] == "TV")
               | (table_main["anime_type"] == "Movie")
               | (table_main["anime_type"] == "OVA")
               | (table_main["anime_type"] == "Special")
               | (table_main["anime_type"] == "TV Special")
               | (table_main["anime_type"] == "ONA")].groupby("year")["score"].max(),
    table_main[(table_main["anime_type"] == "TV")
               | (table_main["anime_type"] == "OVA")
               | (table_main["anime_type"] == "ONA")].groupby("year")["score"].max(),
    table_main[(table_main["anime_type"] == "Movie")
               | (table_main["anime_type"] == "Special")
               | (table_main["anime_type"] == "TV Special")].groupby("year")["score"].max(),
    table_main[(table_main["anime_type"] == "Music")
               | (table_main["anime_type"] == "CM")
               | (table_main["anime_type"] == "PV")].groupby("year")["score"].max(),
    table_main[table_main["anime_type"] == "TV"].groupby(["year"])["score"].mean(),
    table_main[table_main["anime_type"] == "OVA"].groupby(["year"])["score"].mean(),
    table_main[table_main["anime_type"] == "ONA"].groupby(["year"])["score"].mean(),
    table_main[table_main["anime_type"] == "Movie"].groupby(["year"])["score"].mean(),
    table_main[(table_main["anime_type"] == "Special")
               | (table_main["anime_type"] == "TV Special")].groupby(["year"])["score"].mean(),
    table_main[table_main["anime_type"] == "TV"].groupby(["year"])["score"].min(),
    table_main[table_main["anime_type"] == "OVA"].groupby(["year"])["score"].min(),
    table_main[table_main["anime_type"] == "ONA"].groupby(["year"])["score"].min(),
    table_main[(table_main["anime_type"] == "Special")
               | (table_main["anime_type"] == "TV Special")].groupby(["year"])["score"].min(),
    table_main[table_main["anime_type"] == "Movie"].groupby(["year"])["score"].min(),
    table_main[table_main["anime_type"] == "TV"].groupby(["year"])["score"].max(),
    table_main[table_main["anime_type"] == "OVA"].groupby(["year"])["score"].max(),
    table_main[table_main["anime_type"] == "ONA"].groupby(["year"])["score"].max(),
    table_main[(table_main["anime_type"] == "Special")
               | (table_main["anime_type"] == "TV Special")].groupby(["year"])["score"].max(),
    table_main[table_main["anime_type"] == "Movie"].groupby(["year"])["score"].max()
],
axis =1)

tab_year_score.columns = ["score_mean","score_min", "score_max",
                          "TV_Movie_OVA_Special_ONA_score_mean","TV_OVA_ONA_score_mean", "Movie_Special_score_mean", "Music_CM_PV_score_mean",
                          "TV_Movie_OVA_Special_ONA_score_min","TV_OVA_ONA_score_min", "Movie_Special_score_min", "Music_CM_PV_score_min",
                          "TV_Movie_OVA_Special_ONA_score_max","TV_OVA_ONA_score_max", "Movie_Special_score_max", "Music_CM_PV_score_max",
                          "TV_score_mean", "OVA_score_mean", "ONA_score_mean", "Movie_score_mean", "Special_score_mean",
                          "TV_score_min", "OVA_score_min", "ONA_score_min", "Movie_score_min", "Special_score_min",
                          "TV_score_max", "OVA_score_max", "ONA_score_max", "Movie_score_max", "Special_score_max"
                          ]





# Create a table that gives the amount of source material XZY per year
"""
consideration of 
    pd.concat([table_main[(table_main["score"] > 0)].groupby("source").size().sort_values()],axis=1)
gives
    Radio              9
    Card game         71
    Picture book      73
    Book              96
    Web novel        125
    Mixed media      185
    Music            208
    4-koma manga     299
    Web manga        430
    Novel            612
    Other            654
    Light novel     1039
    Unknown         1134
    Visual novel    1143
    Game            1162
    Manga           4762
    Original        5778
we reduce this to
    Web manga        430
    Novel            612
    Light novel     1039
    Unknown         1134
    Visual novel    1143
    Game            1162
    Other           1711
    Manga           4762
    Original        5778
"""

tab_year_source = pd.concat([
    table_main[(table_main["source"] == "Manga") & (table_main["score"] > 0)].groupby("year").size(),
    table_main[(table_main["source"] == "Original") & (table_main["score"] > 0)].groupby("year").size(),
    table_main[(table_main["source"] == "Game") & (table_main["score"] > 0)].groupby("year").size(),
    table_main[(table_main["source"] == "Visual novel") & (table_main["score"] > 0)].groupby("year").size(),
    table_main[(table_main["source"] == "Web manga") & (table_main["score"] > 0)].groupby("year").size(),
    table_main[(table_main["source"] == "Light novel") & (table_main["score"] > 0)].groupby("year").size(),
    table_main[(table_main["source"] == "Novel") & (table_main["score"] > 0)].groupby("year").size(),
    table_main[(table_main["source"] == "Unknown") & (table_main["score"] > 0)].groupby("year").size(),

    table_main[((table_main["source"] == "Other")
        |(table_main["source"] == "4-koma manga")
        |(table_main["source"] == "Picture book")
        |(table_main["source"] == "Music")
        |(table_main["source"] == "Book")
        |(table_main["source"] == "Radio")
        |(table_main["source"] == "Mixed media")
        |(table_main["source"] == "Card game")
        |(table_main["source"] == "Web novel"))
    & (table_main["score"] > 0)].groupby("year").size(),
],
axis =1)

tab_year_source.columns =  ['#Manga', '#Original', '#Game', '#Visual novel', '#Web manga', '#Light novel', '#Novel', '#Unknown', '#Other']








#
#
#
#
#
# # Create a table that gives the mean, max and min of score per year
# #   table_main[(table_main["anime_type"] == "TV") & (table_main["score"] > 0)].groupby(["year"])["episodes"].mean(),
# #       -- In table_main where anime_type == "TV" and score >0 (has an entry) get the average amount of episodes for each year
# tab_year_stuff = pd.concat([
#     table_main[(table_main["anime_type"] == "TV") & (table_main["score"] > 0)].groupby(["year"])["episodes"].mean(),
#     table_main[(table_main["anime_type"] == "TV") & (table_main["score"] > 0)].groupby(["year"])["duration"].mean(),
#     table_main[(table_main["anime_type"] == "TV") & (table_main["score"] > 0)].groupby(["year"])["scored_by"].mean(),
#     table_main[(table_main["anime_type"] == "TV") & (table_main["score"] > 0)].groupby(["year"])["on_list"].mean(),
#     table_main[(table_main["anime_type"] == "TV") & (table_main["score"] > 0)].groupby(["year"])["favorites"].mean(),
#     table_main[(table_main["anime_type"] == "Movie") & (table_main["score"] > 0)].groupby(["year"])["duration"].mean(),
#     table_main[(table_main["anime_type"] == "Movie") & (table_main["score"] > 0)].groupby(["year"])["scored_by"].mean(),
#     table_main[(table_main["anime_type"] == "Movie") & (table_main["score"] > 0)].groupby(["year"])["on_list"].mean(),
#     table_main[(table_main["anime_type"] == "Movie") & (table_main["score"] > 0)].groupby(["year"])["favorites"].mean(),
# ],
# axis =1)
#
# tab_year_stuff.columns =  ["tv_episode_mean", "tv_duration_mean", "tv_scored_by_mean", "tv_on_list_mean", "tv_favorites_mean", "movie_duration_mean", "movie_scored_by_mean", "movie_on_list_mean", "movie_favorites_mean"]
#
#
# # Create a table that gives the mean, max and min of score per year
# #   table_main[(round(table_main["score"]) == 2) & (table_main["anime_type"] == "TV")].groupby(["year"]).size(),
# #       -- In table_main get the amount of TV shows that are rated 2 (rounded) for each year
# tab_year_score_distr = pd.concat([
#     table_main[(round(table_main["score"]) == 2) & (table_main["anime_type"] == "TV")].groupby(["year"]).size(),
#     table_main[(round(table_main["score"]) == 3) & (table_main["anime_type"] == "TV")].groupby(["year"]).size(),
#     table_main[(round(table_main["score"]) == 4) & (table_main["anime_type"] == "TV")].groupby(["year"]).size(),
#     table_main[(round(table_main["score"]) == 5) & (table_main["anime_type"] == "TV")].groupby(["year"]).size(),
#     table_main[(round(table_main["score"]) == 6) & (table_main["anime_type"] == "TV")].groupby(["year"]).size(),
#     table_main[(round(table_main["score"]) == 7) & (table_main["anime_type"] == "TV")].groupby(["year"]).size(),
#     table_main[(round(table_main["score"]) == 8) & (table_main["anime_type"] == "TV")].groupby(["year"]).size(),
#     table_main[(round(table_main["score"]) == 9) & (table_main["anime_type"] == "TV")].groupby(["year"]).size()
# ],
# axis =1)
#
# tab_year_score_distr.columns =  ["rating=2", "rating=3", "rating=4", "rating=5", "rating=6", "rating=7", "rating=8", "rating=9"]




# Combing above created tables:
table_year = pd.concat([
    tab_year_type, tab_year_score,tab_year_source
],
axis =1)


# saving table as xlsx
table_year.to_excel("xlsx_tables/S_1970_2024_information_by_year.xlsx")

# open table, SINCE the index before was YEAR, but we do not want that.
# reopening the table from file gives us a nw indes column that is independent of the file
table_year = pd.read_excel('S_1970_2024_information_by_year.xlsx')

# normalize data to [0,1] so plots are more comparable
df = table_year
normalized = (df-df.min())/(df.max()-df.min())

# we normalized the column with "year" too. let's fix that
normalized["year"] = table_year["year"]

#save the normalized file as xlsx
normalized.to_excel("xlsx_tables/S_1970_2024_information_by_year_normalized.xlsx")























