#   #   #   #   #   #   #
#   General comment and planing
#   #   #   #   #   #   #
"""
Overview: where do we get what kind of data
    full
        mal_id
        title_english (title)
        type
        source [based on]
        episodes
        ?   duration
        ?   rating
        score (1-10)
        scored_by
        rank
        popularity [https://myanimelist.net/info.php?go=topanime]
        members [#useres who listed the anime]
        favorites
        ?   synopsis
        season
        year
        ?   producers, _number_, name
        studios, _number_, name
        genres, _number_, name
        themes, _number_, name
    characters
        _number_, character, name
        _number_, role
        _number_, favorites
        ?   _number_, voice_actors, _number_, person, name
        ?   _number_, voice_actors, _number_, person, mal_id
        ?   _number_, voice_actors, _number_, language
    staff
        ? _number_, person, name
        ? _number_, person, mal_id
        ? _number_, position, _number_
    episodes
        pagination, has_next_page
        data, _number_, score [score of episode _number_-1 (1-5)]
    forum (only check for existence for engagement measurement, since we get 15 entries at most)
        ~~_number_, comments~~
    statistics
        watching
        completed
        on_hold
        dropped
        plan_to_watch
        total (= members)
        scores, _number_, score [_number_+1 points of 10]
        scores, _number_, votes [for that score]
        scores, _number_, percentage [for that score]
    # ?recommendations
    #     _number_, entry, mal_id
    #     _number_, entry, title
    #     _number_, votes [#votes for recommendation]
    # ?relations
    #     _number_, relation

what do we want
    -- Information of anime (line-brakes just for readability)
        anime_id, title, source, #episodes, duration in min, rating(?), score (1-10), #scored_by, rank, popularity, #on list, #favorites, season, year
        studios_name_1,studios_name_2,studios_name_3,studios_name_4,    (check for max length)
        genres_1, genres_2, genres_3, genres_4,                         (check for max length)
        themes_name_1, themes_name_2, themes_name_3,                    (check for max length)
        #studios involved, #genres, #themes
        #characters, #characters with votes, #all votes for characters, character vote average,highest vote, highest vote in ratio
        #staff,
        average episode score, first episode score, last episode score  (episodes can be empty)!!!
        #of comments, #of threats                                       (forum can be empty)!!!
        #watching, #completed, #on_hold, #dropped, #plan_to_watch, #1point,...,#10point, %of <=5*
        score_mod (ignore 1*), score_mod2 (ignore 1* & 10*)
        -- (measure engagement by demanding "characters", "forum", "episodes" and co. ?)

    -- score ~ synopsis
    -- synopsis wordcloud over time
    -- genre over time
    -- score ~ staff


    -- season
        year, season, #all, #TV, #Movie, #rest, #all_aired, #TV_aired, #Movie_aired, #rest_aired,
        #episodes_average for TV,
        score_average, #votes, score_average if engagement             (measure engagement by demanding "characters", "forum", "episodes" ?)
        #has_characters, #has_episodes, #has_forum, #hast_staff

    -- staff (VA) ~ score
"""


# Deeper look into id_full.json (the other .json work similar)
"""
mal_id = ad["data"]["mal_id"]                               int,
approved = ad["data"]["approved"]                           true/false,
title = ad["data"]["title"]                                 str
title_english = ad["data"]["title_english"]                 str     (can be null)
title_jap = ad["data"]["title_japanese"]                    str
anime_type = ad["data"]["type"]                             str     "TV",
source = ad["data"]["source"]                               str
episodes = ad["data"]["episodes"]                           int,
status = ad["data"]["status"]                               str     "Finished Airing",
airing_1_0 = ad["data"]["airing"]                           true/false,
start = ad["data"]["aired"]["from"]                         str     "1970-11-02T00:00:00+00:00",
end = ad["data"]["aired"]["to"]                             str     "1971-09-27T00:00:00+00:00",
start_day = ad["data"]["aired"]["prop"]["from"]["day"]      int,
start_month = ad["data"]["aired"]["prop"]["from"]["month"]  int,
start_year = ad["data"]["aired"]["prop"]["from"]["year"]    int
end_day = ad["data"]["aired"]["prop"]["to"]["day"]          int,
end_month = ad["data"]["aired"]["prop"]["to"]["month"]      int,
end_year = ad["data"]["aired"]["prop"]["to"]["year"]        int
duration = ad["data"]["duration"]                           str     "23 min per ep",
rating = ad["data"]["rating"]                               str
score = ad["data"]["score"]                                 int,
scored_by = ad["data"]["scored_by"]                         int,
rank = ad["data"]["rank"]                                   int,
popularity = ad["data"]["popularity"]                       int,
on_list = ad["data"]["members"]                             int,
favorites = ad["data"]["favorites"]                         int,
synopsis = ad["data"]["synopsis"]                           str
season = ad["data"]["season"]                               str,
year = ad["data"]["year"]                                   int,
brod_day = ad["data"]["broadcast"]["day"]                   int,
broad_time = ad["data"]["broadcast"]["time"]                int

ad["data"]["studios"][INDEX]["name"]:                       str
...
ad["data"]["studios"][INDEX]["name"]:                       str
ad["data"]["genres"][INDEX]["name"]:                        str
...
ad["data"]["genres"][INDEX]["name"]:                        str
ad["data"]["themes"][INDEX]["name"]:                        str
...
ad["data"]["themes"][INDEX]["name"]:                        str
"""

#   #   #   #   #   #   #
#   Import
#   #   #   #   #   #   #

import time
from pathlib import Path
import json
import logging
import warnings
from module_supply import *
import pandas as pd
import numpy as np
from warnings import simplefilter
import os


#   #   #   #   #   #   #
#   Manage warnings and Co.
#   #   #   #   #   #   #
# since the way we create the table below is probably not the best way, receiving the warning:
# "PerformanceWarning: DataFrame is highly fragmented.  This is usually the result of calling `frame.insert` many times, which has poor performance.  Consider joining all columns at once using pd.concat(axis=1) instead. To get a de-fragmented frame, use `newframe = frame.copy()` table_full_studios.loc[str(id),item] = 1"
# over and over again
simplefilter(action="ignore", category=pd.errors.PerformanceWarning)


# FutureWarning: The behavior of DataFrame concatenation with empty or all-NA entries is deprecated. In a future version,
# this will no longer exclude empty or all-NA columns when determining the result dtypes. To retain the old behavior, exclude
# the relevant entries before the concat operation.
warnings.filterwarnings("ignore", category=FutureWarning)


# Pycharm sometimes cuts the presentation of DataFrames, not a huge fan of that, so I found that on stackoverflow
pd.options.display.width= None
pd.options.display.max_columns= None
pd.set_option('display.max_rows', 3000)
pd.set_option('display.max_columns', 3000)


#   #   #   #   #   #   #
#   logging
#   #   #   #   #   #   #

logger = logging.getLogger("_creation_")
logging.basicConfig(filename='tracking_logging/Logging.log', encoding='utf-8', level=logging.WARNING, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s")


#   #   #   #   #   #   #
#   Useful
#   #   #   #   #   #   #
def split_list(Liste, n):
    k, m = divmod(len(Liste), n)
    return (Liste[i*k+min(i, m):(i+1)*k+min(i+1, m)] for i in range(n))


#   #   #   #   #   #   #
#   open
#   #   #   #   #   #   #

def open_data(Type, year_id, season_reqparam, anime_type = "TV"):
    if Type == "season":
        path_name = "data_json/season/" + str(year_id) + "/" + str(year_id) + "_" + season_reqparam + ".json"
        try:
            with open(path_name, encoding="utf8") as f:
                data = json.load(f)
                return data
        except:
            logger.warning("In open_data -- " + 'No such file: ' + path_name)
            print('No such file: ' + path_name)
    if Type == "anime":
        path_name = "data_json/anime/" + anime_type + "/" + str(year_id) + "/" + str(year_id) + "_" + season_reqparam + ".json"
        try:
            with open(path_name, encoding="utf8") as f:
                data = json.load(f)
                return data
        except:
            logger.warning("In open_data -- " + 'No such file: ' + path_name)
            print('No such file: ' + path_name)

def open_id(anime_id, req_param = "full"):
    with open("tracking_logging/tracking.json", encoding="utf8") as f:
        tracking = json.load(f)
    try:
        anime_type = tracking["anime"][str(anime_id)]["anime_type"]
        if req_param in tracking["anime"][str(anime_id)]["req_param"]:
            path = "data_json/anime/" + anime_type + "/" + str(anime_id) + "/" + str(anime_id) + "_" + str(req_param) + ".json"
            with open(path, encoding="utf8") as f:
                data = json.load(f)
            return data
        else:
            logger.warning("In open_id -- " + 'No such file: -- ' + str(anime_id) + "_" + str(req_param))
            print(anime_id,req_param, " -- no such file exists")
    except:
        logger.warning("In open_id -- " + 'No such file: -- ' + str(anime_id))
        print(anime_id, " -- no such file exists")


def open_season(year, season):
    with open("tracking_logging/tracking.json", encoding="utf8") as f:
        tracking = json.load(f)
    try:
        if season in tracking["season"][str(year)]["season"]:
            path = "data_json/season/" + str(year) + "/" + str(year) + "_" + season + ".json"
            with open(path, encoding="utf8") as f:
                data = json.load(f)
            return data
        else:
            num = 1/0
    except:
        logger.warning("In open_season -- " + 'No such file: -- ' + str(year) + "_" + season)
        print(year,season, " -- no such file exists")




#   #   #   #   #   #   #
#   get
#   #   #   #   #   #   #
# getting all anime_id, by type, on disk
# # -> data for them: data_json/anime/[anime_type]/[anime_id]/[anime_id]_[req_param].json
def get_IDs_downloades(anime_type="all"):
    anime_IDs = []

    Movie_folder = os.listdir("data_json/anime/Movie")
    ONA_folder = os.listdir("data_json/anime/ONA")
    OVA_folder = os.listdir("data_json/anime/OVA")
    Special_folder = os.listdir("data_json/anime/Special")
    TV_folder = os.listdir("data_json/anime/TV")
    TV_Special_folder = os.listdir("data_json/anime/TV Special")

    if anime_type == "all":
        anime_IDs = Movie_folder + ONA_folder + OVA_folder + Special_folder + TV_folder + TV_Special_folder
    elif anime_type == "Movie":
        anime_IDs = Movie_folder
    elif anime_type == "ONA":
        anime_IDs = ONA_folder
    elif anime_type == "OVA":
        anime_IDs = OVA_folder
    elif anime_type == "Special":
        anime_IDs = Special_folder
    elif anime_type == "TV":
        anime_IDs = TV_folder
    elif anime_type == "TV Special":
        anime_IDs = TV_Special_folder

    return anime_IDs


# getting all anime_id from tracking
# # -> data for them: data_json/season/[year]/[year]_[season].json
def get_IDs_all():
    anime_IDs = []
    with open('tracking_logging/tracking.json', encoding="utf8") as f:
        data = json.load(f)

    for anime_id in data["anime"]:
        anime_IDs.append(int(anime_id))
    return anime_IDs


# getting all anime_id for [year] from tracking
# # -> data for them: data_json/season/[year]/[year]_[season].json
def get_IDs_year(year):
    anime_IDs = []
    path = "data_json/season/" + str(year) + "/"
    for season in ["fall", "summer", "winter", "spring"]:

        with open(path + str(year) + "_" + season + '.json', encoding="utf8") as f:
            data = json.load(f)

        for entry in data["data"]:
            anime_IDs.append(entry["mal_id"])
    return anime_IDs




#   #   #   #   #   #   #
#   processing -- FROM SEASON
#   #   #   #   #   #   #
"""
Faster way to obtain data based on YEAR_SEASON.json
1. Table:
    -- head = anime_id	approved	title	anime_type	source	episodes	status	airing	start	end	duration	rating	score	scored_by	rank	popularity	on_list	favorites	synopsis	season	year	broadcast_day	broadcast_time	#studios involved	#genres	#themes
    -- anime_id is unique in row "anime_id"
2. Table:
    -- head = anime_id	studio	genre	theme
    -- anime_id can occur multiple times in row "anime_id"
    -- more row, less columns
Usage of "split_list":
    -- Since the glueing done in this function is not efficient we reduce the time by temporarily storing the df in a list.
       This could maybe improved by saving it in a file and appending the file (?)
       The split is fixed to 11 ( A range of n will be split into a list of 11 lists - some might be empty if n < 11)
"""
# todo: something is of with the table_SGT
#   -- some rows occur multiple times (not supposed to happen)
#   -- you can use .drop_duplicates() to remove duplicate rows <-- for now I do that when I use the table
# name recommendation: name = str(Years[0]) + "_" + str(Years[-1])
def get_table_season(Range , name):
    # range to list:
    Y_list = list(Range)
    Seasons = ["winter", "spring", "summer", "fall"]

    # creating list where we will collect the data frames per Years split
    main_list = []
    SGT_list = []

    problems = []
    for Years in list(split_list(Y_list,11)):
        # preparations
        #   Table_main
        # todo: approved can be removed -- always true
        columns = ["anime_id", "approved", "title", "anime_type", "source", "episodes", "status", "airing", "start", "end",
                   "duration", "rating", "score", "scored_by", "rank", "popularity", "on_list", "favorites", "synopsis",
                   "season", "year", "broadcast_day", "broadcast_time"]
        table = pd.DataFrame(columns=columns)

        #   Table_Stud_Gen_Them
        table_sgt = pd.DataFrame(columns=["anime_id", "studio", "genre", "theme"])

        #   Table_calc (combine this with Table_main
        table_calc = pd.DataFrame(columns=["#studios involved", "#genres", "#themes"])




        for Y in Years:
            print(Y, "-------------")
            for S in Seasons:
                # load data
                try:
                    data_s = open_season(Y, S)  # ad for anime data to shorten the name
                    crash_test = data_s["data"]  # check if ad is fine, else ERROR-> except
                except:
                    print("problem with", str(Y) + "_" + S)
                    problems.append(str(Y) + "_" + S)
                    continue

                for ad in data_s["data"]:
                    # open "id_full"
                    # interested in ["mal_id", "approved", "title", "anime_type", "source", "episodes", "status", "airing", "start", "end",
                    #                 "duration", "rating", "score", "scored_by", "rank", "popularity", "on_list", "favorites", "synopsis",
                    #                 "season", "year", "broadcast_day", "broadcast_time"]

                    mal_id = ad["mal_id"]
                    approved = ad["approved"]

                    try:
                        if ad["title_english"]:
                            title = ad["title_english"]
                        else:
                            title = ad["title"]
                    except:
                        title = ad["title_japanese"]

                    anime_type = ad["type"]
                    source = ad["source"]
                    episodes = ad["episodes"]
                    status = ad["status"]
                    airing = ad["airing"]

                    if ad["aired"]["from"]:
                        start = ad["aired"]["from"].split("T")[0]
                    else:
                        start = 0
                    if ad["aired"]["to"]:
                        end = ad["aired"]["to"].split("T")[0]
                    else:
                        end = 0

                    # get duration in minutes:
                    # I think ad["duration"] returns either a combination of hr and min or just sec but to be sure we catch every possible case
                    duration_str = ad["duration"]
                    hours = 0
                    minutes = 0
                    seconds = 0
                    if "min" in duration_str and "hr" in duration_str and "sec" in duration_str:
                        hours = duration_str.split(" hr ")[0]
                        minutes = duration_str.split(" hr ")[1].split(" min ")[0]
                        seconds = duration_str.split(" hr ")[1].split(" min ")[1].split(" sec")[0]
                    elif "min" in duration_str and "hr" in duration_str:
                        hours = duration_str.split(" hr ")[0]
                        minutes = duration_str.split(" hr ")[1].split(" min")[0]
                    elif "min" in duration_str and "sec" in duration_str:
                        minutes = duration_str.split(" min ")[0]
                        seconds = duration_str.split(" min ")[1].split(" sec")[0]
                    elif "hr" in duration_str and "sec" in duration_str:
                        hours = duration_str.split(" hr ")[0]
                        minutes = duration_str.split(" hr ")[1].split(" min")[0]
                    elif "min" in duration_str:
                        minutes = duration_str.split(" min")[0]
                    elif "hr" in duration_str:
                        hours = duration_str.split(" hr")[0]
                    elif "sec" in duration_str:
                        seconds = duration_str.split(" sec")[0]
                    duration = 60 * int(hours) + int(minutes) + round(int(seconds) / 60, 1)

                    rating = ad["rating"]
                    score = ad["score"]
                    scored_by = ad["scored_by"]
                    rank = ad["rank"]
                    popularity = ad["popularity"]
                    on_list = ad["members"]
                    favorites = ad["favorites"]
                    synopsis = ad["synopsis"]
                    season = S
                    year = Y
                    brod_day = ad["broadcast"]["day"]
                    broad_time = ad["broadcast"]["time"]

                    row = [mal_id, approved, title, anime_type, source, episodes, status, airing, start, end, duration,
                           rating, score, scored_by, rank, popularity, on_list, favorites, synopsis, season, year, brod_day,
                           broad_time]

                    col_s = 1
                    row_studios = []
                    for entry in ad["studios"]:
                        row_studios.append(entry["name"])
                        col_s = col_s + 1

                    col_g = 1
                    row_genres = []
                    for entry in ad["genres"]:
                        row_genres.append(entry["name"])
                        col_g = col_g + 1

                    col_t = 1
                    row_themes = []
                    for entry in ad["themes"]:
                        row_themes.append(entry["name"])
                        col_t = col_t + 1

                    # filling the tables
                    #   Table_main
                    table.loc[str(mal_id)] = row


                    #   Table_Stud_Gen_Them
                    """
                    create temp table of the form 
                        anime_id studio genre  theme
                        0     12345  Stud1  Gen1  Them1
                        1     12345  Stud2  Gen2  Them2
                        2     12345  Stud3  Gen3    NaN
                        3     12345  Stud4   NaN    NaN
                    column by column and use "pd.concat([ids, stu, gen, the], axis=1)" to combine them
                    """
                    max_len = max(col_t,col_g,col_s) -1
                    ids = pd.DataFrame({'anime_id': [mal_id] * max_len})
                    stu = pd.DataFrame({'studio': row_studios})
                    gen = pd.DataFrame({'genre': row_genres})
                    the = pd.DataFrame({'theme': row_themes})
                    table_temp = pd.concat([ids, stu, gen, the], axis=1) # combine the columns

                    # combine table_SDT with table_temp by column names (more rows)
                    table_sgt = pd.concat([table_sgt, table_temp])


                    # ["#studios involved", "#genres", "#themes"]
                    table_calc.loc[str(mal_id)] = [col_s - 1, col_g - 1, col_t - 1]

        # combining tables
        table_main = pd.concat([table, table_calc], axis=1)

        # append the lists with the created DataFrames -- hoping this save time
        main_list.append(table_main)
        SGT_list.append(table_sgt)

    table_main = pd.concat(main_list)
    table_sgt = pd.concat(SGT_list)

    # save table
    table_main.to_excel("Season_" + name + "_main" + ".xlsx",index = False)
    table_sgt.to_excel("Season_" + name + "_SGT" + ".xlsx", index = False)

    # print problems
    if problems:
        print("Problems:")
        for probs in problems:
            print(probs)


