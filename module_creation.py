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
    -- Information of anime (line-brakes just for readebility)
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

# function for returning "ALL" ids of anime shows (anime_type = TV)
# added the option to get more specific ids
# We usually don't want tio use this if we want to access the related files
# it is likely they don't exist -- e.g. entry["status"] != "Finished Airing"
def get_IDs_do_not_use(anime_type = "TV", season = "all", year = 0):
    with open("tracking_logging/tracking.json", encoding="utf8") as f:
        tracking = json.load(f)
    anime_IDs = []
    if season =="all" and year == 0:
        for entry in tracking["anime"]:
            if entry["mal_id"] == anime_type:
                anime_IDs.append(entry["mal_id"])
    elif season == "all":
        for seas in ["winter", "spring", "summer", "fall"]:
            try:
                data = open_data("season", year, seas, anime_type)
                for entry in data["data"]:
                    if  entry["type"] == anime_type:
                        anime_IDs.append(entry["mal_id"])
            except:
                logger.warning("In get_IDs -- " + 'Problems with: -- ' + str(year) + "_" + seas)
                print("IDs for the season", year, seas, anime_type, "is not on disk")
    elif year == 0:
        print("Please set season to __all__ if you use __year=0__")
    else:
        try:
            data = open_data("season", year, season, anime_type)
            for entry in data["data"]:
                if entry["type"] == anime_type:
                    anime_IDs.append(entry["mal_id"])
        except:
            logger.warning("In get_IDs -- " + 'Problems with: -- ' + str(year) + "_" + season)
            print("IDs for the season", year, season, anime_type, "is not on disk")
    return anime_IDs



#   #   #   #   #   #   #
#   processing (first try)
#   #   #   #   #   #   #
# secion comment:
"""
The main problem with the following functions is that are probably inefficient created and that their content might
be overwhelming -- a LOT of columns. To reduce that we will change the output from one table to more than one.
For this see processing (second try)
"""

# proof of concept -- do not use
# Firs version, columns are often categories. This was used as a proof of concept and to get used to working with dataframes
def get_table_id_do_not_use(anime_IDs):
    # preparations
    #   TABLE1: "full"
    columns_full = ["anime_id", "title", "source", "# episodes", "duration in min", "rating", "score (1-10)",
                    "#scored_by", "rank", "popularity", "#on list",
                    "#favorites", "season", "year", "has_prequel"]
    table_full = pd.DataFrame(columns=columns_full)

    #   studios_name_, genres_, themes_name_ || rest of full
    #   Table1_studios
    table_full_studios = pd.DataFrame(columns=["studio_1"])

    #   Table1_genres
    table_full_genre = pd.DataFrame(columns=["genre_1"])

    #   Table1_themes
    table_full_themes = pd.DataFrame(columns=["themes_1"])

    #   Table1_cals
    table_full_calc = pd.DataFrame(columns=["#studios involved", "#genres", "#themes"])

    # Tabel2: "characters"
    table_char_calc = pd.DataFrame(
        columns=["#characters", "#characters with votes", "#all votes for characters", "character vote average",
                 "highest vote", " highest vote in ratio"])

    # Table3: "staff"
    table_staff_calc = pd.DataFrame(columns=["#staff"])

    # Tabel4: "episodes"
    table_episodes = pd.DataFrame(columns=["average episode score", "first episode score", "last episode score"])

    # Table5: "forum"
    table_forum = pd.DataFrame(columns=["Forum used"])

    # Table5: "statistics"
    table_stats = pd.DataFrame(columns=["watching", "completed", "on_hold", "dropped", "plan_to_watch",
                                        "point1", "point2", "point3", "point4", "point5", "point6", "point7", "point8",
                                        "point9", "point10",
                                        "%lower_score", "score_mod (ignore 1*)", "score_mod2 (ignore 1* & 10*)"])


    for id in anime_IDs:
        print(id)
        # open "id_full"
        # interested in ["anime_id", "title", "source", "# episodes", "duration in min", "rating", "score (1-10)",
        #               "#scored_by", "rank", "popularity", "#on list", "#favorites", "season", "year"]
        try:
            ad = open_id(id, req_param="full")  # ad for anime data to shorten the name
            crash_test = ad["data"] # check if ad is fine, else ERROR-> except
        except:
            print("problem with", str(id) + "_full")
            continue

        anime_id = id
        try:
            title = ad["data"]["title_english"]
        except:
            title = ad["data"]["title"]
        source = ad["data"]["source"]
        episodes = ad["data"]["episodes"]
        duration = ad["data"]["duration"]
        rating = ad["data"]["rating"]
        score = ad["data"]["score"]
        scored_by = ad["data"]["scored_by"]
        rank = ad["data"]["rank"]
        popularity = ad["data"]["popularity"]
        on_list = ad["data"]["members"]
        favorites = ad["data"]["favorites"]
        season = ad["data"]["season"]
        year = ad["data"]["year"]

        try:
            has_prequel = 0
            for entry in ad["data"]["relations"]:
                if entry["relation"] == "Prequel":
                    has_prequel = 1
        except:
            has_prequel = 0

        row_full = [
            anime_id, title, source, episodes, duration, rating, score, scored_by, rank, popularity, on_list, favorites,
            season,
            year, has_prequel
        ]

        row_full_studios = []
        for entry in ad["data"]["studios"]:
            row_full_studios.append(entry["name"])

        row_full_genres = []
        for entry in ad["data"]["genres"]:
            row_full_genres.append(entry["name"])

        row_full_themes = []
        for entry in ad["data"]["themes"]:
            row_full_themes.append(entry["name"])

        table_full.loc[str(id)] = row_full

        col_s = 1
        for item in row_full_studios:
            table_full_studios.loc[str(id), "studio" + "_" + str(col_s)] = item
            col_s = col_s + 1

        col_g = 1
        for item in row_full_genres:
            table_full_genre.loc[str(id), "genre" + "_" + str(col_g)] = item
            col_g = col_g + 1

        col_t = 1
        for item in row_full_themes:
            table_full_themes.loc[str(id), "themes" + "_" + str(col_t)] = item
            col_t = col_t + 1

        # ["#studios involved", "#genres", "#themes"]
        table_full_calc.loc[str(id)] = [col_s - 1, col_g - 1, col_t - 1]

        # open "id_characters"
        # interested in ["#characters", "#characters with votes", "#all votes for characters", "character vote average""highest vote"," highest vote in ratio"]
        check = 1
        try:
            ad = open_id(id, req_param="characters")  # ad for anime data to shorten the name
            crash_test = ad["data"] # check if ad is fine, else ERROR-> except
        except:
            print("empty", str(id) + "_characters")
            table_char_calc.loc[str(id)] = [np.nan, np.nan, np.nan, np.nan, np.nan, np.nan]
            check = 0

        if check:
            char_amount = len(ad["data"])
            char_w_vote = 0
            vote_amount = 0
            high_vote = 0
            for entry in ad["data"]:
                votes = entry["favorites"]
                if votes != 0:
                    char_w_vote += 1
                    vote_amount += votes
                if votes > high_vote:
                    high_vote = votes

            if vote_amount != 0:
                row_char = [char_amount, char_w_vote, vote_amount, round(vote_amount / char_amount, 2), high_vote,
                            round(high_vote / vote_amount, 2)]
            else:
                row_char = [char_amount, char_w_vote, vote_amount, round(vote_amount / char_amount, 2), high_vote,
                            0]

            table_char_calc.loc[str(id)] = row_char

        # open "id_staff"
        # interested in ["#staff"]
        check = 1
        try:
            ad = open_id(id, req_param="staff")  # ad for anime data to shorten the name
            crash_test = ad["data"] # check if ad is fine, else ERROR-> except
        except:
            print("empty", str(id) + "_staff")
            table_char_calc.loc[str(id)] = [np.nan]
            check = 0

        if check:
            staff_amount = len(ad["data"])
            row_staff = [staff_amount]

            table_staff_calc.loc[str(id)] = row_staff

        # open "id_episodes"
        # interested in ["average episode score", "first episode score", "last episode score"]
        check = 1
        try:
            ad = open_id(id, req_param="episodes")  # ad for anime data to shorten the name
            crash_test = ad["data"] # check if ad is fine, else ERROR-> except
        except:
            print("empty", str(id) + "_episodes")
            table_char_calc.loc[str(id)] = [np.nan, np.nan, np.nan]
            check = 0

        if check:
            # episode score can be "null"
            ep_frist_score = 0
            ep_last_score = 0

            for entry in ad["data"]:
                if entry["score"]:
                    ep_frist_score = entry["score"]
                    break

            for i in range(1, len(ad["data"])):
                if ad["data"][-i]["score"]:
                    ep_last_score = ad["data"][-i]["score"]
                    break

            ep_score_sum = 0
            count = 0
            for entry in ad["data"]:
                if entry["score"]:
                    count += 1
                    ep_score_sum += entry["score"]

            # score can be "null" - if there is a lot of "null" we don't consider this valuable data
            # -- in theory it could be that case that there are just a lot of canceled or wrongly added episodes, therefore we compare with #episodes given in id_full
            if count == 0 or count <= episodes / 2:
                table_episodes.loc[str(id)] = [np.nan, np.nan, np.nan]
            else:
                ep_score_average = round(ep_score_sum / count, 2)
                table_episodes.loc[str(id)] = [ep_score_average, ep_frist_score, ep_last_score]

        # open "id_forum"
        # interested in ["#of comments", "#of threats", "threat_amout - episodes"]
        check = 1
        try:
            ad = open_id(id, req_param="forum")  # ad for anime data to shorten the name
            crash_test = ad["data"] # check if ad is fine, else ERROR-> except
        except:
            print("empty", str(id) + "_forum")
            check = 0

        if check:
            table_forum.loc[str(id)] = [1]

        # open "statistics"
        # interested in ["watching", "completed", "on_hold", "dropped", "plan_to_watch",
        #                "point1", "point2", "point3", "point4", "point5", "point6", "point7", "point8", "point9", "point10",
        #                "%lower_score", "score_mod (ignore 1*)", "score_mod2 (ignore 1* & 10*)" ]
        check = 1
        try:
            ad = open_id(id, req_param="statistics")  # ad for anime data to shorten the name
            crash_test = ad["data"] # check if ad is fine, else ERROR-> except
        except:
            print("empty", str(id) + "_statistics")
            table_stats.loc[str(id)] = [np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan,
                                        np.nan, np.nan, np.nan, np.nan, np.nan]
            check = 0

        if check:
            watching = ad["data"]["watching"]
            completed = ad["data"]["completed"]
            on_hold = ad["data"]["on_hold"]
            dropped = ad["data"]["dropped"]
            plan_to_watch = ad["data"]["plan_to_watch"]
            point1 = ad["data"]["scores"][0]["votes"]
            point2 = ad["data"]["scores"][1]["votes"]
            point3 = ad["data"]["scores"][2]["votes"]
            point4 = ad["data"]["scores"][3]["votes"]
            point5 = ad["data"]["scores"][4]["votes"]
            point6 = ad["data"]["scores"][5]["votes"]
            point7 = ad["data"]["scores"][6]["votes"]
            point8 = ad["data"]["scores"][7]["votes"]
            point9 = ad["data"]["scores"][8]["votes"]
            point10 = ad["data"]["scores"][9]["votes"]

            help_votes_total = 0
            help_low_votes = 0
            help_mod1 = 0
            help_mod2 = 0
            for i in range(0, 10):
                help_votes = ad["data"]["scores"][i]["votes"]
                help_votes_total += help_votes
                if i < 5:
                    help_low_votes += help_votes
                if i != 0:
                    help_mod1 += (i + 1) * help_votes
                    if i != 9:
                        help_mod2 += (i + 1) * help_votes

            lower_score_perc = round(help_low_votes / help_votes_total, 2)
            score_mod = round(help_mod1 / (help_votes_total - point1), 2)
            score_mod2 = round(help_mod2 / (help_votes_total - point1 - point10), 2)

            row_stats = [watching, completed, on_hold, dropped, plan_to_watch, point1, point2, point3, point4, point5,
                         point6, point7, point8, point9, point10, lower_score_perc, score_mod, score_mod2]
            table_stats.loc[str(id)] = row_stats

    result = pd.concat(
        [table_full, table_full_studios, table_full_themes, table_full_genre, table_full_calc, table_char_calc,
         table_staff_calc, table_episodes, table_forum, table_stats], axis=1)
    return result


# Comment on get_table_id
"""
For obtaining a largish table with
    meta: anime_id
    features: [a lot]^*
^*:
    I tried to add most of the common features I'm going to use, that relies on anime_id as the identifier.
    instead of one feature with different entries I went to 0/1 those (there is probably a better was to say that)
    e.g. 
        instead of [1 column ]:
            genres: Action, Fantasy, Romance,... 
        I did [#genres columns]: 
            Action: 1
            Fantasy: 1
            Comedy: 0

Information we have, and where to find:
    TABLE1: "full":
        anime_id, title, source, #episodes, duration in min, rating(?), score (1-10), #scored_by, rank, popularity, 
        #on list, #favorites, season, year
    Table1_studios:
        studios_name_1,studios_name_2,studios_name_3
    Table1_genres:
        genres_1, genres_2, genres_3
    Table1_themes:
        themes_name_1, themes_name_2, themes_name_3,
    Tabel1_calc
        #studios involved, #genres, #themes
    Tabel2: "characters":
        #characters, #characters with votes, #all votes for characters, character vote average, 
        highest vote, highest vote in ratio
    Tabel3: "staff":
        #staff
    Table4: "episodes":
        average episode score, first episode score, last episode score
    Table5: "statistics":
        #watching, #completed, #on_hold, #dropped, #plan_to_watch, #1point,...,#10point, %of <=5*
            score_mod (ignore 1*), score_mod2 (ignore 1* & 10*)
    Table6: "forum" + engagement
        "Character used", "Statistics used", "Episodes used","Forum used", "Staff used"
    
EXAMPLE (shortened):
    anime_id	title	    #episodes	duration in min	    rating	                        score (1-10)	#scored_by	rank	popularity	#on list	#favorites	season	year	has_prequel	    Source: Manga	Source: Original	Source: Light novel
    57334	    Dan Da Dan	12	        23	                R - 17+ (violence & profanity)	8,54	        382414	    126 	324	        682820	    10694	    fall	2024	0	            1	            0	                0
"""
# USAGE:
"""
    To create a detailed table of all anime that aired and have a score
    for example use
        Years = range(2020,2025)
    to get all downloaded ids that aired and have a score and then use
        get_table_id(Years, name="Table_IDs")
    to create and save a table containing all the downloaded data, that i thought could be of interest
"""
# Deeper look into id_full.json (the othere .json work similar)
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
def get_table_id_old(Years, name="Table_IDs"):
    anime_IDs = []
    for Y in Years:
        anime_IDs += get_ids_in_season(Y, season="all", anime_type="TV")

    # preparations
    # TABLE1: "full"
    columns_full = ["anime_id", "title", "#episodes", "duration_in_min", "rating", "score",
               "scored_by", "rank", "popularity", "#on_list",
               "#favorites", "season", "year","has_prequel"]

    table_full = pd.DataFrame(columns=columns_full)

    # studios_name_, genres_, themes_name_ || rest of full
    # Table1_studios
    table_full_studios = pd.DataFrame(columns=[])

    # Table1_genres
    table_full_genre = pd.DataFrame(columns=[])

    # Table1_themes
    table_full_themes = pd.DataFrame(columns=[])

    # Table1_source
    table_full_source = pd.DataFrame(columns=[])

    # Table1_times
    table_full_times = pd.DataFrame(columns=["start", "end", "broadcast_day", "broadcast_time"])

    # Table1_calc
    table_full_calc = pd.DataFrame(columns=["#studios_involved", "#genres", "#themes"])

    # Table1_synopsis
    table_synopsis = pd.DataFrame(columns=["synopsis"])

    # Tabel2: "characters"
    table_char_calc = pd.DataFrame(columns=["#characters", "#characters_with_votes", "total_character_votes", "character_vote_average", "highest_vote"," highest_vote_ratio"])

    # Table3: "staff"
    table_staff_calc = pd.DataFrame(columns=["#staff"])


    # Tabel4: "episodes"
    table_episodes = pd.DataFrame(columns=["average_episode_score", "first_episode_score", "last_episode_score"])


    # Table5: "statistics"
    table_stats = pd.DataFrame(columns=["watching", "completed", "on_hold", "dropped", "plan_to_watch",
                                        "votes_1", "votes_2", "votes_3", "votes_4", "votes_5", "votes_6", "votes_7", "votes_8", "votes_9", "votes_10",
                                        "%lower_score", "score_mod (ignore 1*)", "score_mod2 (ignore 1* & 10*)" ])

    # Table6: "forum" and engagement
    table_forum = pd.DataFrame(columns=["id_characters_is_used", "id_statistics_is_used", "id_episodes_is_used","id_forum_is_used", "id_staff_is_used"])


    # save ids that do not load the basic file: id_full
    prob_with_full =[]

    for id in anime_IDs:
        # open "id_full"
        # interested in ["anime_id", "title", "source", "# episodes", "duration in min", "rating", "score (1-10)",
        #               "#scored_by", "rank", "popularity", "#on list", "#favorites", "season", "year"]
        try:
            ad = open_id(id, req_param="full") # ad for anime data to shorten the name
            crash_test = ad["data"] # check if ad is fine, else ERROR-> except
        except:
            print("problem with", str(id) + "_full")
            prob_with_full.append(id)
            continue
        anime_id = id
        try:
            if ad["data"]["title_english"]:
                title = ad["data"]["title_english"]
            else:
                title = ad["data"]["title"]
        except:
            title = ad["data"]["title"]
        score = ad["data"]["score"]
        episodes = ad["data"]["episodes"]

        # get duration in minutes:
        # I think ad["data"]["duration"] returns either a combination of hr and min or just sec but to be sure we catch every possible case
        duration_str = ad["data"]["duration"]
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

        rating = ad["data"]["rating"]
        scored_by = ad["data"]["scored_by"]
        rank = ad["data"]["rank"]
        popularity = ad["data"]["popularity"]
        on_list = ad["data"]["members"]
        favorites = ad["data"]["favorites"]
        season = ad["data"]["season"]
        year = ad["data"]["year"]

        # for checking if ths id is a continuation
        try:
            has_prequel = 0
            for entry in ad["data"]["relations"]:
                if entry["relation"] == "Prequel":
                    has_prequel = 1
        except:
            has_prequel = 0

        row_full = [
            anime_id,title, episodes, duration, rating,score, scored_by, rank, popularity, on_list, favorites, season,
            year,has_prequel
        ]

        # getting rows of all studios, genres and themes for the id
        row_full_studios = []
        for entry in ad["data"]["studios"]:
            row_full_studios.append(entry["name"])

        row_full_genres = []
        for entry in ad["data"]["genres"]:
            row_full_genres.append(entry["name"])

        row_full_themes = []
        for entry in ad["data"]["themes"]:
            row_full_themes.append(entry["name"])


        # now we have all the rows, we are going to fill the DataFrame
        table_full.loc[str(id)] = row_full

        # ad source
        table_full_source.loc[str(id), "Source: " + ad["data"]["source"]] = 1

        # ad times ["Starts", "Ends", "Broadcast_day", "Broadcast_time"]
        try:
            From = ad["data"]["aired"]["from"].split("T")[0]
        except:
            From = 0
        try:
            To = ad["data"]["aired"]["to"].split("T")[0]
        except:
            To = 0
        try:
            Day = ad["data"]["broadcast"]["day"]
        except:
            Day = 0
        try:
            Time =  ad["data"]["broadcast"]["time"]
        except:
            Time = 0


        table_full_times.loc[str(id)] = [From, To, Day, Time]

        # ad synopsis
        table_synopsis.loc[str(id)] = [ad["data"]["synopsis"]]

        # Since we do not know how many studios/themes/genres are involved we expand the table head if needed
        col_s = 1
        for item in row_full_studios:
            table_full_studios.loc[str(id),"studio_" + item] = 1
            col_s = col_s + 1

        col_g = 1
        for item in row_full_genres:
            table_full_genre.loc[str(id),"genre_" + item] = 1
            col_g = col_g + 1

        col_t = 1
        for item in row_full_themes:
            table_full_themes.loc[str(id),"theme_" + item] = 1
            col_t = col_t + 1

        # ["#studios involved", "#genres", "#themes"]
        table_full_calc.loc[str(id)] = [col_s-1,col_g-1,col_t-1]


        # open "id_characters"
        # interested in ["#characters", "#characters with votes", "#all votes for characters", "character vote average""highest vote"," highest vote in ratio"]
        char_check = 1
        try:
            ad = open_id(id, req_param="characters") # ad for anime data to shorten the name
            crash_test = ad["data"] # check if ad is fine, else ERROR-> except
        except:
            # print("empty", str(id) + "_characters")
            table_char_calc.loc[str(id)] = [np.nan, np.nan, np.nan, np.nan, np.nan, np.nan]
            char_check = 0

        if char_check:
            char_amount = len(ad["data"])
            char_w_vote = 0
            vote_amount = 0
            high_vote = 0
            for entry in ad["data"]:
                votes = entry["favorites"]
                if votes != 0:
                    char_w_vote +=1
                    vote_amount += votes
                if votes > high_vote:
                    high_vote = votes

            # prevent division by zero
            if vote_amount != 0:
                row_char = [char_amount, char_w_vote, vote_amount, round(vote_amount/char_amount,2), high_vote, round(high_vote/vote_amount,2)]
            else:
                row_char = [char_amount, char_w_vote, vote_amount, round(vote_amount / char_amount, 2), high_vote,
                            0]

            table_char_calc.loc[str(id)] = row_char


        # open "id_staff"
        # interested in ["#staff"]
        staff_check = 1
        try:
            ad = open_id(id, req_param="staff")  # ad for anime data to shorten the name
            crash_test = ad["data"] # check if ad is fine, else ERROR-> except
        except:
            # print("empty", str(id) + "_staff")
            table_char_calc.loc[str(id)] = [np.nan]
            staff_check = 0

        if staff_check:
            staff_amount = len(ad["data"])
            row_staff = [staff_amount]

            table_staff_calc.loc[str(id)] = row_staff


        # open "id_episodes"
        # interested in ["average episode score", "first episode score", "last episode score"]
        epi_check = 1
        try:
            ad = open_id(id, req_param="episodes")  # ad for anime data to shorten the name
            crash_test = ad["data"] # check if ad is fine, else ERROR-> except
        except:
            # print("empty", str(id) + "_episodes")
            table_episodes.loc[str(id)] = [np.nan,np.nan,np.nan]
            epi_check = 0

        if epi_check:
            # episode score can be "null"
            ep_frist_score = 0
            ep_last_score = 0

            for entry in ad["data"]:
                if entry["score"]:
                    ep_frist_score = entry["score"]
                    break

            for i in range(1,len(ad["data"])):
                if ad["data"][-i]["score"]:
                    ep_last_score = ad["data"][-i]["score"]
                    break

            ep_score_sum = 0
            count = 0
            for entry in ad["data"]:
                if entry["score"]:
                    count +=1
                    ep_score_sum += entry["score"]

            # score can be "null" - if there is a lot of "null" we don't consider this valuable data
            # -- in theory it could be that case that there are just a lot of canceled or wrongly added episodes, therefore we compare with #episodes given in id_full
            if count == 0 or count <=episodes/2:
                table_episodes.loc[str(id)] = [np.nan, np.nan, np.nan]
            else:
                ep_score_average = round(ep_score_sum/count,2)
                table_episodes.loc[str(id)] = [ep_score_average,ep_frist_score,ep_last_score]


        # open "statistics"
        # interested in ["watching", "completed", "on_hold", "dropped", "plan_to_watch",
        #                "point1", "point2", "point3", "point4", "point5", "point6", "point7", "point8", "point9", "point10",
        #                "%lower_score", "score_mod (ignore 1*)", "score_mod2 (ignore 1* & 10*)" ]
        stat_check = 1
        try:
            ad = open_id(id, req_param="statistics")  # ad for anime data to shorten the name
            crash_test = ad["data"] # check if ad is fine, else ERROR-> except
        except:
            # print("empty", str(id) + "_statistics")
            table_stats.loc[str(id)] = [np.nan, np.nan, np.nan, np.nan, np.nan, np.nan,
                                        np.nan, np.nan, np.nan, np.nan, np.nan, np.nan,
                                        np.nan, np.nan, np.nan, np.nan, np.nan, np.nan]
            stat_check = 0

        if stat_check:
            watching = ad["data"]["watching"]
            completed = ad["data"]["completed"]
            on_hold = ad["data"]["on_hold"]
            dropped = ad["data"]["dropped"]
            plan_to_watch = ad["data"]["plan_to_watch"]
            point1 = ad["data"]["scores"][0]["votes"]
            point2 = ad["data"]["scores"][1]["votes"]
            point3 = ad["data"]["scores"][2]["votes"]
            point4 = ad["data"]["scores"][3]["votes"]
            point5 = ad["data"]["scores"][4]["votes"]
            point6 = ad["data"]["scores"][5]["votes"]
            point7 = ad["data"]["scores"][6]["votes"]
            point8 = ad["data"]["scores"][7]["votes"]
            point9 = ad["data"]["scores"][8]["votes"]
            point10 = ad["data"]["scores"][9]["votes"]

            help_votes_total = 0
            help_low_votes = 0
            help_mod1 = 0
            help_mod2 = 0
            for i in range(0,10):
                help_votes =  ad["data"]["scores"][i]["votes"]
                help_votes_total += help_votes
                if i <5:
                    help_low_votes += help_votes
                if i != 0:
                    help_mod1 += (i+1)*help_votes
                    if i != 9:
                        help_mod2 += (i + 1) * help_votes

            if help_votes_total != 0:
                lower_score_perc = round(help_low_votes/help_votes_total,2)
            else:
                lower_score_perc = np.nan

            if (help_votes_total - point1) != 0:
                score_mod = round(help_mod1/(help_votes_total - point1),2)
            else:
                score_mod = np.nan

            if (help_votes_total - point1 - point10) != 0:
                score_mod2 = round(help_mod2/(help_votes_total - point1 - point10),2)
            else:
                score_mod2 = np.nan
            row_stats = [watching, completed, on_hold, dropped, plan_to_watch, point1, point2, point3, point4, point5, point6, point7, point8, point9, point10, lower_score_perc, score_mod, score_mod2]
            table_stats.loc[str(id)] = row_stats


            # open "id_forum" + mark occurring files
            # interested in [char_check,stat_check,epi_check,forum_check,staff_check]
            forum_check = 1
            try:
                ad = open_id(id, req_param="forum")  # ad for anime data to shorten the name
                crash_test = ad["data"]  # check if ad is fine, else ERROR-> except
            except:
                # print("empty", str(id) + "_forum")
                forum_check = 0

            table_forum.loc[str(id)] = [char_check,stat_check,epi_check,forum_check,staff_check]

    result = pd.concat([table_full, table_full_source, table_synopsis, table_full_studios, table_full_themes, table_full_genre,table_full_calc,table_char_calc,table_staff_calc,table_episodes,table_stats,table_forum], axis=1)
    result_0 = result.fillna(0)
    # print(result_0)
    result_0.to_excel(name + ".xlsx")
    print("IDs with _full problems:")
    print(prob_with_full)
    # return result_0       # remove comment if you want to get the table as a return


"""
For obtaining a table based on season data:
    -- using data obtained by https://api.jikan.moe/v4/seasons/[YEAR]/[SEASON]
    -- saved in: data_json/season/[YEAR]/[YEAR]_[SEASON].json
    -- using get_table_id() as a foundation
"""
# Usage:
"""
e.g.
    Seasons = ["winter", "spring", "summer", "fall"]
    name = "1970_2024_table_season"
    Years = range(1970,2025)
        # This gets VERY VERY slow starting around 2000
        # Better range(1970,2000) + range(2000,2025) and combine them afterward
    get_table_season(Years, Seasons, name)
        -> obtain a saved file named "1970_2024_table_season.xlsx"
    If you want to use the output immediately, remove the comment at the end so you return the dataframe
"""
# for more comments and explanation see get_table_id
def get_table_season_old(Years, Seasons, name):

    # preparations
    columns = ["anime_id", "approved", "title", "anime_type", "source", "episodes", "status", "airing", "start", "end",
                    "duration", "rating", "score", "scored_by", "rank", "popularity", "on_list", "favorites", "synopsis",
                    "season", "year", "broadcast_day", "broadcast_time"]
    table = pd.DataFrame(columns=columns)

    #   studios_name_, genres_, themes_name_ || rest of full
    #   Table_studios
    table_studios = pd.DataFrame(columns=[])

    #   Table_genres
    table_genre = pd.DataFrame(columns=[])

    #   Table_themes
    table_themes = pd.DataFrame(columns=[])

    #   Table_calc
    table_calc = pd.DataFrame(columns=["#studios involved", "#genres", "#themes"])
    problems = []
    for Y in Years:
        print(Y,"-------------")
        for S in Seasons:
            # load data
            try:
                data_s = open_season(Y,S)  # ad for anime data to shorten the name
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

                row = [mal_id, approved, title, anime_type, source, episodes, status, airing, start, end, duration, rating, score, scored_by, rank, popularity, on_list, favorites, synopsis, season, year, brod_day, broad_time]

                row_full_studios = []
                for entry in ad["studios"]:
                    row_full_studios.append(entry["name"])

                row_full_genres = []
                for entry in ad["genres"]:
                    row_full_genres.append(entry["name"])

                row_full_themes = []
                for entry in ad["themes"]:
                    row_full_themes.append(entry["name"])



                col_s = 1
                for item in row_full_studios:
                    table_studios.loc[str(mal_id),"Studio: " + item] = 1
                    col_s = col_s + 1

                col_g = 1
                for item in row_full_genres:
                    table_genre.loc[str(mal_id),"Genre: " + item] = 1
                    col_g = col_g + 1

                col_t = 1
                for item in row_full_themes:
                    table_themes.loc[str(mal_id),"Theme: " + item] = 1
                    col_t = col_t + 1


                # filling the table
                table.loc[str(mal_id)] = row

                # ["#studios involved", "#genres", "#themes"]
                table_calc.loc[str(mal_id)] = [col_s-1,col_g-1,col_t-1]

    # combining tables
    result = pd.concat([table, table_studios, table_themes, table_genre,table_calc], axis=1)

    # nan or empty to 0
    result_0 = result.fillna(0)
    print(result_0)

    # save table
    result_0.to_excel(name + ".xlsx")

    # print problems
    print("Problems:")
    for probs in problems:
        print(probs)
    # return result_0   #return the DataFrame



#   #   #   #   #   #   #
#   processing (second try)
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
