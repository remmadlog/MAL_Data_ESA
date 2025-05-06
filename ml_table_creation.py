from download import *
import pandas as pd

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
"""
Planing for dataset creation to use for score prediction and related things 
- mainly using
- - S_1970_2024_merged.xlsx
- - S_1970_2024_merged_unique.xlsx
- Data cleaning
- - score > 0, status == "Finished Airing", episodes > 0
- - only use 'TV', 'Movie', 'Special', 'TV Special', 'OVA', 'ONA'
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
Column planing
- Meta and Features
- - main
- - - anime_id, ,theme, genre, studio, anime_type, source, episodes, duration, rating, scored_by, on_list, favorites, broadcast_day, broadcast_time
- - meta?
- - - season, year, anime_id
- - target
- - - score, rank, 
- - for cleaning
- - - status,
- - for later use?
- - - title, synopsis,
- - From [id]_statistics.json (for this we need to create the table)
- - - watching, completed, on_hold, dropped, plan_to_watch
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
Actual realization || what does change (from planing to application)
- focusing on relation, not on total numbers
- - if we want to predict the score of a shows airing rn, the total number for dropped or watched, will be very very low in comparison
- not considering:  "scored_by", "on_list", "favorites",
- - for the same reason
- dropping tile ans synopsis
- - not needed atm, can be considered later if wanted
"""

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# table creation from [id]_statistics.json -- ON_LIST

# open tracking
with open("tracking_logging/tracking.json", encoding="utf8") as f:
    tracking_date = json.load(f)

# we only consider the anime part
anime_data = tracking_date["anime"]

# this will become a list of list
# elements in here are rows of the table to be
table_list = []

for anime_id in tqdm(anime_data):
    # get anime type
    anime_type = anime_data[anime_id]["anime_type"]

    # define path of file
    path = "data_json/anime/" + anime_type + "/" + anime_id + "/" + anime_id + "_statistics.json"

    # try open
    # # except file not found -> go download it and try again
    try:
        with open(path, encoding="utf8") as f:
            statistics = json.load(f)
    except:
        download_missing_only(anime_id, "full")
        download_missing_only(anime_id, "statistics")
        with open(path, encoding="utf8") as f:
            statistics = json.load(f)

    """
    "data": {
        "watching": 16311,
        "completed": 687102,
        "on_hold": 5942,
        "dropped": 3638,
        "plan_to_watch": 195153,
        "total": 908146,
        "scores": [...]}
    """
    watching = statistics["data"]["watching"]
    completed = statistics["data"]["completed"]
    on_hold = statistics["data"]["on_hold"]
    dropped = statistics["data"]["dropped"]
    plan_to_watch = statistics["data"]["plan_to_watch"]
    # subtract completed so we do not bias it
    total = statistics["data"]["total"] - completed


    # write row
    # going for ratios, not totals
    if total == 0:
        row = [int(anime_id), 0,0,0,0,0]
    else:
        row = [int(anime_id), watching/total, completed/total, on_hold/total, dropped/total, plan_to_watch/total]

    # append table_list
    table_list.append(row)

# column names of the table to be
col_names = ["anime_id", "watching", "completed", "on_hold", "dropped", "plan_to_watch"]

# creating table
df_on_list = pd.DataFrame(table_list, columns = col_names)


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
"""This can be done smarter and with less unnecessary use of data, but it is not a real problem here, cause our data size is moderate"""
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# create the other part of the table using S_1970_2024_merged.xlsx and S_1970_2024_merged_unique.xlsx
# load S_1970_2024_merged.xlsx
dfm = pd.read_excel('xlsx_tables/S_1970_2024_merged.xlsx').fillna(0)
dfmu = pd.read_excel('xlsx_tables/S_1970_2024_merged_unique.xlsx').fillna(0)

# dfm
# # select only the wanted columns
# # dftemp = dfm[["anime_id", "year", "status", "score", "rank", "season", "theme", "genre", "studio", "anime_type", "source", "episodes", "duration", "rating", "scored_by", "on_list", "favorites", "broadcast_day", "broadcast_time", "title", "synopsis"]]
dfmtemp = dfm[["anime_id", "year", "status", "score", "rank", "season", "theme", "genre", "studio", "anime_type", "source", "episodes", "duration", "rating"]]
# # cleaning
dfmtemp = dfmtemp[(dfmtemp["score"]>0) & (dfmtemp["episodes"]>0) & (dfmtemp["status"] == "Finished Airing")]

# dfmu
# # select only the wanted columns
# # dftemp = dfm[["anime_id", "year", "status", "score", "rank", "season", "theme", "genre", "studio", "anime_type", "source", "episodes", "duration", "rating", "scored_by", "on_list", "favorites", "broadcast_day", "broadcast_time", "title", "synopsis"]]
dfmutemp = dfmu[["anime_id", "year", "status", "score", "rank", "season", "theme", "genre", "studio", "anime_type", "source", "episodes", "duration", "rating"]]
# # cleaning
dfmutemp = dfmutemp[(dfmutemp["score"]>0) & (dfmutemp["episodes"]>0) & (dfmutemp["status"] == "Finished Airing")]

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
"""
- I planed on only use get_dummies for gerne and theme and not on studios to reduce feature amount
- - figuring out the "good" features later is an option so we use this
- for "anime_type", "source", "rating","season" i planed on lable encoding, but it is possible the the modle will see a meaning behind those numbers
- - 1<3 || if 1 = "summer" and 3 = "winter" --> "winter" > "summer" || that would be not so good
- here we use get dummies for all the categories
"""
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# encoding / get_dummies for SGT

# only consider what we need
dfsgt = dfmtemp[["anime_id","theme", "genre", "studio"]]
# expand columns so we have features instead of categories
df_encoded_sgt = pd.get_dummies(dfsgt, dtype = int)
# get rid of genre_0, theme_0 and studio_0
df_encoded_sgt = df_encoded_sgt.drop(["theme_0", "genre_0", "studio_0"], axis=1)
# since we have multiple rows per id we group them
# each genre_xyz is unique, we should be able to group by anime_id and sum the cols
df_encoded_sgt = df_encoded_sgt.groupby("anime_id").sum()

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# encoding / get_dummies for "anime_type", "source", "rating","season"

# only consider what we need
dftemp = dfmutemp[["anime_id", "anime_type", "source", "rating","season"]]      # !!! using dfmu NOT dfml -> merge in right order !!!
# expand columns so we have features instead of categories
df_encoded_rest = pd.get_dummies(dftemp, dtype = int)
# get rid of genre_0, theme_0 and studio_0
df_encoded_rest = df_encoded_rest.drop(["rating_0"], axis=1)
# since we have multiple rows per id we group them
# each genre_xyz is unique, we should be able to group by anime_id and sum the cols
df_encoded_rest = df_encoded_rest.groupby("anime_id").sum()

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# full encodes table
df_encoded = pd.merge(df_encoded_sgt, df_encoded_rest, on="anime_id")


# full table
dftemp = pd.merge(df_encoded, dfmu[["anime_id", "year", "score", "rank", "episodes", "duration"]] ,on="anime_id")
dfml = pd.merge(dftemp, df_on_list ,on="anime_id",how='inner')


# saving table as xlsx
dfml.to_csv("xlsx_tables/training_score/training_score.csv", index=False)


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #





















