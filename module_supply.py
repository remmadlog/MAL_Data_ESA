#   #   #   #   #   #   #
#   General comments
#   #   #   #   #   #   #
"""
Some details:
    Rate limits:
        Rate Limiting by API
            Duration 	|  Requests
            Daily 	    |  Unlimited
            Per Minute 	|  60 requests
            Per Second 	|  3 requests
        Note: It's still possible to get rate limited from MyAnimeList.net instead.
            see e.g. https://myanimelist.net/forum/?topicid=2142532
                quote: "I've been doing some testing with mal-api.py API wrapper and encountered a 3-5 min cooldown (response = 504) after around 300 sequential requests, sometimes less, usually a little more."
    data = request.get(url).json()      # below assume data[...]...[...] exists (you need to check that for each case)
        in general
            data["type"] == "RateLimitException"
                -- too many api requests, wait a second or two
            data["pagination"]["has_next_page"]
                -- contains True or False
                -- there is a next page
                -- modify url by adding "?page=2" to get the next page
                -- or change X in "?page=X" suitable
            data["pagination"]["last_visible_page"]
                -- contains number of pages
        in /seasons/YEAR/SEASON
            data["data"][NUMBER]["type"]
                -- contains type (TV, Manga, Movie...)
            data["data"][NUMBER]["mal_id"]
                -- contains animme_id (MAL)
        in anime
            data["data"] == []
                -- possible if e.g. there are no recommendations for an id
                -- for large data sets one should consider checking a sample set if that's actually the case
    url information
        in general see https://docs.api.jikan.moe/#section/Information for all api information
        for our purpose below we consider as of (2025-03-28):
        short introduction:
            url_base = "https://api.jikan.moe/v4/"
            url_suffix:
                seasons/YEAR/SEASON (winter, spring, summer, fall)
                    eg: "https://api.jikan.moe/v4/seasons/2025/winter
                    -- usually has multiple pages (shows only 25 entry per page)
                anime/ANIME_ID/
                    full
                    characters
                    staff
                    episodes
                        -- can have multiple pages
                    forum
                        -- has filter options
                            filter	= "all" "episode" "other"
                    statistics
                    recommendations
                    relations

"""

#   #   #   #   #   #   #
#   ToDos
#   #   #   #   #   #   #

"""
ToDo:
    IMPORTANT
        -- extend the download of anime_types!
            -- At least this
                -- TV = TV show, BUT OVA and ONA are also shows but not broadcast to tv
            -- Maybe this too but not as important
                -- Move = Theater/TV, BUT Special is also a Movie!
    - OTHER
        -- info logging
            -- more/better logging (low priority)
        -- Main comment
            -- "forum" ONLY returns the NEWEST 15 entries (not really usable except for checking existence in order to measure engagement)
        -- better implementation
            -- additional pages
            -- update
        -- better functions
            -- download this id (basic and all)
            -- download this season
            -- download this year
            -- update options
            --
"""

#   #   #   #   #   #   #
#   Import
#   #   #   #   #   #   #
import datetime
import requests
import time
from pathlib import Path
import json
import logging


#   #   #   #   #   #   #
#   logging
#   #   #   #   #   #   #

logger = logging.getLogger("__supply__")
logging.basicConfig(filename='tracking_logging/Logging.log', encoding='utf-8', level=logging.WARNING, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s")


#   #   #   #   #   #   #
#   General Request
#   #   #   #   #   #   #

# check response code to see if the request was good
# SEE: https://docs.api.jikan.moe/#section/Information/HTTP-Responses
def check_response(response,url_ident):
    if response.status_code != 200: # in case the response is not good
        if response.status_code == 304:
            logger.warning('In check_response -- Not Modified: 304 -- ' + url_ident[2] + "/" + url_ident[1] + "/" +url_ident[0])
            return 1
        if response.status_code == 400:
            logger.error('In check_response -- Bad response: 400 - missing parameters -- ' + url_ident[2] + "/" +url_ident[1] + "/" +url_ident[0])
            tracking_error("Bad response: 400",response.url)
            # print("     Bad response: 400 -- API missing required parameters --",url_ident)
            return 0
        if response.status_code == 404:
            logger.error('In check_response -- Bad response: 404 -- ' + url_ident[2] + "/" + url_ident[1] + "/" +url_ident[0])
            tracking_error("Bad response: 404", response.url)
            # print("     Bad response: 404 --", url_ident)
            return 0
        if response.status_code == 405:
            logger.error('In check_response -- Bad response: 405 -- ' + url_ident[2] + "/" + url_ident[1] + "/" +url_ident[0])
            tracking_error("Bad response: 405", response.url)
            # print("     Bad response: 404 --", url_ident)
            return 0
        if response.status_code == 429:
            logger.error('In check_response -- Too Many Request: 429 -- ' + url_ident[2] + "/" + url_ident[1] + "/" +url_ident[0])
            print("     Too Many Request: 429 --", url_ident)
            return 3
        if response.status_code == 500:
            logger.warning('In check_response -- Internal Server Error: 504 - MAl timeout -- ' + url_ident[2] + "/" +url_ident[1] + "/" +url_ident[0]) # warning, because we catch that below
            tracking_error("Bad response: 504", response.url)
            # print("     Internal Server Error: 504 -- MAl timeout --",url_ident)
            return 0
        if response.status_code == 503:
            logger.warning('In check_response -- Service Unavailable: 504 - Sever maintenance -- ' + url_ident[2] + "/" +url_ident[1] + "/" +url_ident[0]) # warning, because we catch that below
            tracking_error("Bad response: 504", response.url)
            # print("     Service Unavailable: 504 -- Sever maintenance --",url_ident)
            return 0
        if response.status_code == 504:
            logger.warning('In check_response -- Bad response: 504 - MAl timeout -- ' + url_ident[2] + "/" +url_ident[1] + "/" +url_ident[0]) # warning, because we catch that below
            print("     Bad response: 504 -- MAl timeout --",url_ident)
            return 2
    return 1


def try_get(url):
    try:
        response = requests.get(url, timeout=10)
        return response
    except:
        print("        stuck on request, try again")
        try:
            response = requests.get(url, timeout=10)
            return response
        except:
            print("        stuck on request, skip this: return return [0,data]")
            return []


# url request as function | instead of doing it everytime by hand use this function to save space
# return is a list: control_parameter, data
# control_parameter used to deside if the request was good
def get_data(url, ignore_page_warning =0):
    # print("        Try to get", url)
    # since I get RateLimitException:
    wait = 1 #waiting time in seconds
    url_split = url.split("/")  # splitting url to obtain the api request defining information for error reporting
    url_split[-1] = url_split[-1].split("?")[0]  # in case of pathparameter e.g. ?page=2
    url_ident = [url_split[-1], url_split[-2], url_split[-3]]  # should be the last 3 entries

    response = try_get(url) # request.get(url, timeout = 10) AND try ONE more time -- return [] if timeouted twice
    if response ==[]:
        return [0,[]]

    time.sleep(wait)
    data = response.json()

    check_resp = check_response(response,url_ident)
    if check_resp == 0:
        return [0,data]
    if check_resp == 2 or check_resp == 3:
        # MAL timeout -- wait 5 minutes     || I am inpatient and need a reminder that time is indeed passing
        print("     A MAL timeout occurred -- we wait for 300 seconds.")
        time.sleep(150)
        print("     Still 150 seconds to go.")
        time.sleep(160) # 10 extra seconds to be sure
        print("     time is up, lets try one more time.")
        # Was thinking about
        # return get_data(url, ignore_page_warning)
        # but was very scared of a loop, so I went for -- loop prevention possible

        response = try_get(url)
        if response == []:
            return [0, []]

        time.sleep(wait)
        data = response.json()
        if check_response(response, url_ident) != 1:
            print("     Still problems with" + url_ident[2] +"/" + url_ident[1] + "/" +url_ident[0])
            tracking_error("Timeout", response.url)
            return [0,data]

    if "data" in data:
        if data["data"] == []:
            logger.warning('In get_data -- Bad response, data[data] == [] for -- ' + url_ident[2] +"/" + url_ident[1] + "/" +url_ident[0])
            # print("        Bad response: data is empty", url_ident)
            tracking_warning("data[data] == []",response.url)
            return [0,data]
    else:
        logger.error('In get_data -- Bad response, date notin data for -- ' + url_ident[2] + "/" + url_ident[1] + "/" + url_ident[0])
        # print("        Bad response: data notin data", url_ident)
        tracking_error("date notin data", response.url)
        return [0, data]
    if "type" in data:
        # check if we got an api timeout
        # if so, act suitable: wait a bit and try again, then check again
        # you could also wait longer between requests in general
        if data["type"] == "RateLimitException": # we send to many requests to api and have to wait a bit
            time.sleep(4)
            try:
                response = requests.get(url, timeout=10)
                print("        Got a response")
            except:
                print("        stuck on request, try again")
                try:
                    response = requests.get(url, timeout=10)
                    print("        Got a response")
                except:
                    print("        stuck on request, skip this: return return [0,data]")
                    return [0, []]
            time.sleep(wait)
            data = response.json()
            if "type" in data: # let's see if t works again
                if data["type"] == "RateLimitException":
                    # second timeout in a row -> print a note and check it by hand or try again later
                    # we return the "To many requests" data
                    # print("     please check", url_ident)
                    tracking_warning("Second RateLimitException", response.url)
                    logger.error('In get_data -- second time: RateLimitException -- ' + url_ident[2] +"/" + url_ident[1] + "/" +url_ident[0])
                    return [0, data]

    if "pagination" in data:
        if data["pagination"]["has_next_page"]:
            # check if there might be a next_page
            # ignore this output if you are aware of additional pages and know (or think you know) what you are doing | e.g. seasons, reviews
            if ignore_page_warning == 0:
                # if there is a next_page go and check by hand
                logger.warning('In get_data -- there might be additional pages -- ' + url_ident[2] + "/" +url_ident[1] + "/" +url_ident[0])
                # print("     please check",url_ident, "for additional pages")
                tracking_warning("Additional Pages", response.url)
            return [2, data]
    return [1,data]


#   #   #   #   #   #   #
#   Specific Request or Exception
#   #   #   #   #   #   #

# get all data from season page -- depending on year and season
#   here because we have to consider multiple pages
#   possible generalization using (url_suffix) instead of (year,season) as input
#       url_suffix = str(YEAR) + "/" + SEASON
def get_data_season(year,season):
    url = "https://api.jikan.moe/v4/seasons/" + str(year) + "/" + season
    [control_param,data] = get_data(url, ignore_page_warning=1)
    if control_param != 0:
        if data["pagination"]["has_next_page"]:
            number_pages = data["pagination"]["last_visible_page"]
            for i in range(2,number_pages+1):
                url_next_page = "https://api.jikan.moe/v4/seasons/" + str(year) + "/" + season + "?page=" +str(i)
                [control_param,data_next_page] = get_data(url_next_page, ignore_page_warning=1)
                if control_param != 0:
                    for entry in data_next_page["data"]:
                        data["data"].append(entry) # appending crucial information about releases
                        # data content on first level ["pagination"] || ["data"]
                        # ["pagination"]    --  information about additional pages
                        # ["data"]          --  data["data"][NUMBER] contains entry of one release ("tv" "movie" "ova" "special" "ona" "music")
    return [control_param, data]


# for manually collection data if data["pagination"]["has_next_page"]==True
def get_pages(anime_id,req_param):
    url = "https://api.jikan.moe/v4/anime/" + str(anime_id) + "/" + req_param
    [control_param, data] = get_data(url, ignore_page_warning=1)
    if control_param != 0:
        if data["pagination"]["has_next_page"]:
            number_pages = data["pagination"]["last_visible_page"]
            for i in range(2, number_pages + 1):
                url_next_page = "https://api.jikan.moe/v4/anime/" + str(anime_id) + "/" + req_param + "?page=" + str(i)
                [control_param, data_next_page] = get_data(url_next_page, ignore_page_warning=1)
                if control_param != 0:
                    for entry in data_next_page["data"]:
                        data["data"].append(entry)  # appending crucial information about releases
    return [control_param, data]


#   #   #   #   #   #   #
#   File Saving
#   #   #   #   #   #   #

# simple saving function to "save" space
def save_json(data_json,path,name):
    Path(path).mkdir(parents=True, exist_ok=True)
    with open(path + "/" + name, 'w', encoding='utf-8') as f:
        json.dump(data_json, f, ensure_ascii=False, indent=4)


# tracking
# tracking_dic = \
# {
#     "season": {
#         "2024": {
#             "year": 2024,
#             "season": [
#                 "winter"
#             ]
#         },
#         "2025": {
#             "year": 2025,
#             "season": [
#                 "summer"
#             ]
#         }
#     },
#     "anime": {
#         "55791": {
#             "anime_type": "tv",
#             "mal_id": 55791,
#             "req_param": [
#                 "full",
#                 "characters",
#                 "staff",
#                 "episodes",
#                 "forum"
#             ]
#         }
#     }
# }
def save_tracking(Type,year_id,season_reqparam, anime_type = "unknown"):
    with open('tracking_logging/tracking.json', encoding="utf8") as f:
        data = json.load(f)
    if Type == "season":
        with open("tracking_logging/tracking.json", "w", encoding="utf8") as f:
            try:
                data["season"][str(year_id)]["season"].append(season_reqparam)
            except:
                data["season"][str(year_id)] = {"year": year_id,
                                               "season": [season_reqparam
                                                             ]}
            json.dump(data, f, ensure_ascii=False, indent=4)
    elif Type == "anime":
        with open("tracking_logging/tracking.json", "w", encoding="utf8") as f:
            try:
                data["anime"][str(year_id)]["req_param"].append(season_reqparam)
            except:
                data["anime"][str(year_id)] = {"anime_type": anime_type,
                                               "mal_id": year_id,
                                               "req_param": [season_reqparam
                                               ]}
            json.dump(data, f, ensure_ascii=False, indent=4)
    else:
        print("     Error: incorrect Type. Type = season or Type = anime")


# check if a requested data was saved before
# returns: 1 = file was saved before // 0 = file is not saved on disk
def check_exist(Type, year_id, season_reqparam):
    with open('tracking_logging/tracking.json', encoding="utf8") as f:
        data = json.load(f)
        if Type == "season":
            try:
                if season_reqparam in data[Type][str(year_id)]["season"]:
                    return 1
                else:
                    return 0
            except:
                return 0
        elif Type == "anime":
            try:
                if season_reqparam in data[Type][str(year_id)]["req_param"]:
                    return 1
                else:
                    return 0
            except:
                return 0


# get a list of all id/req_param so we can check the list and not always open tracking for each id/req_param -- think that might be better
# use this if you want to download a lot of ids in one go e.g. download_json_all_param
def get_existing_ids():
    with open('tracking_logging/tracking.json', encoding="utf8") as f:
        data = json.load(f)
    id_list = []
    for item in data["anime"]:
        # item = mal_id
        for rep in data["anime"][str(item)]["req_param"]:
            # data["anime"][str(item)]["req_param"] is a lit of the req_param
            id_list.append(str(item) + "/" + rep)
    return id_list



#   #   #   #   #   #   #
#   Download
#   #   #   #   #   #   #

# download one file depending on anime_id and path Parameter
# do not use this to get season information
# check_existance != 1 used if you want to download a lot of ids and check existing ids using get_existing_ids()
def download_by_malID(anime_id, req_param, anime_type, check_existance = 1):
    if check_existance == 1:
        if check_exist("anime", anime_id, req_param) == 0:
            # print("    Request:",req_param, "for", anime_id)

            url = "https://api.jikan.moe/v4/anime/" + str(anime_id)  + "/" + req_param
            path = "data_json/anime/" + anime_type + "/" + str(anime_id)
            name = str(anime_id) + "_" + req_param  + ".json"

            [control_param,data] = get_data(url)
            # print("        " + str(anime_id) + "/" + req_param + " --- " + anime_type)
            if control_param != 0:
                if control_param ==2:
                    # print("     The requested data:",anime_id, req_param, "has multiple pages")
                    [control_param,data] = get_pages(anime_id, req_param)
                save_json(data,path,name)
                save_tracking("anime",anime_id,req_param, anime_type = anime_type)
    else:
        # print("    Request:", req_param, "for", anime_id)

        url = "https://api.jikan.moe/v4/anime/" + str(anime_id) + "/" + req_param
        path = "data_json/anime/" + anime_type + "/" + str(anime_id)
        name = str(anime_id) + "_" + req_param + ".json"

        [control_param, data] = get_data(url)
        # print("        " + str(anime_id) + "/" + req_param + " --- " + anime_type)
        if control_param != 0:
            if control_param == 2:
                # print("     The requested data:",anime_id, req_param, "has multiple pages")
                [control_param, data] = get_pages(anime_id, req_param)
            save_json(data, path, name)
            save_tracking("anime", anime_id, req_param, anime_type=anime_type)




# download for all anime_type ["full", "characters", "staff", "episodes", "forum", "statistics", "recommendations", "relations"]
def download_json_all_param(anime_id, anime_type):
    # path Parameters =
    # request_parameter = ["full", "characters", "staff", "episodes", "forum", "statistics", "recommendations",  "userupdates", "reviews", "relations"]
    # skip userupdates and reviews -- to many data AND no idea how to use it
    request_parameter = ["full", "characters", "staff", "episodes", "forum", "statistics"] # deleted recommendations and relations due to usage

    # no need to try to get "https://api.jikan.moe/v4/anime/4907/episodes" again if "4907" has no "episodes" side
    exception_list = get_empty_suffix_list()
    exists_list = get_existing_ids()
    for req_param in request_parameter:
        if str(anime_id)+"/"+req_param not in exception_list:
            if str(anime_id) + "/" + req_param not in exists_list:
                # print("----", anime_id)  # just to check that nothing is stuck
                download_by_malID(anime_id, req_param,anime_type, check_existance=0)


# download season for season, year
# e.g. all season from 2010 to 2024
# for year in range(2010,2025):
#     for season in ["winter", "spring", "summer", "fall"]:
#         download_season(year, season)
def download_season(year, season):
    #print("Request season:", season, "for", year)
    if check_exist("season", year, season) == 0:
        [control_param, data] = get_data_season(year, season)


        path = "data_json/season/" + str(year)
        name = str(year) + "_" + season  + ".json"


        if control_param != 0:
            save_json(data,path,name)
            save_tracking("season",year, season)
    else:
        print("     ",season, year, "exists on disk.")


#   #   #   #   #   #   #
#   Appendix
#   #   #   #   #   #   #

# returns a list of all anime_type (e.g. "TV") in a season
# ONLY if "Finished Airing" and has score
def get_ids_in_season(year,season = "all",anime_type = "TV"):
    anime_IDs = []
    if season == "all":
        for season in ["winter", "spring", "summer", "fall"]:
            if check_exist("season", year, season) == 1:
                with open("data_json/season/" + str(year) + "/" + str(year) + "_" + season + ".json", encoding="utf8") as f:
                    data = json.load(f)
                for entry in data["data"]:
                    if entry["type"] == anime_type and entry["status"] == "Finished Airing" and entry["score"]:
                        anime_IDs.append(entry["mal_id"])
    else:
        if check_exist("season", year, season) == 1:
            with open("data_json/season/" + str(year) + "/" + str(year) + "_" + season + ".json", encoding="utf8") as f:
                data = json.load(f)
            for entry in data["data"]:
                if entry["type"] == anime_type and entry["status"] == "Finished Airing" and entry["score"]:
                    anime_IDs.append(entry["mal_id"])
    return anime_IDs


# function to easily download all anime that are _done airing_ and _have score_
# nothing to see here, one could wirte that on the flow, needed it for testing, kept it.
# TV, ONA, OVA are shows
# Movie, Special are Movie types
# all = shows + Movie types -- No music types
def download_anime_year(year, anime_type = "all"):
    if anime_type == "all":
        for a_type in ['TV', 'Movie', 'Special', 'TV Special', 'OVA', 'ONA']:
            IDs = get_ids_in_season(year,anime_type=a_type)
            for anime_id in IDs:
                # print(year, "----", anime_id)  # just to check that nothing is stuck
                download_json_all_param(anime_id, a_type)
    else:
        IDs = get_ids_in_season(year,anime_type=anime_type)
        for anime_id in IDs:
            print(year,"----",anime_id)  # just to check that nothing is stuck
            download_json_all_param(anime_id, anime_type)


def download_anime_season(year, season, anime_type = "all"):
    if anime_type == "all":
        for a_type in ['TV', 'Movie', 'Special', 'TV Special', 'OVA', 'ONA']:
            IDs = get_ids_in_season(year, season,anime_type=a_type)
            for anime_id in IDs:
                # print(anime_id)  # just to check that nothing is stuck
                download_json_all_param(anime_id, anime_type)
    else:
        IDs = get_ids_in_season(year, season,anime_type=anime_type)
        for anime_id in IDs:
            # print(anime_id)  # just to check that nothing is stuck
            download_json_all_param(anime_id, anime_type)


# a more direct list of errors compared to logging todo: make logging better if you need this!
def tracking_error(error_text,url):
    with open("tracking_logging/tracking_errors.txt", 'a', encoding='utf-8') as f:
        f.write(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S') + "---" + error_text + "---" + url + "\n")

# if
# "data" is not in data it is usually the case, that the "id" has no information under "episodes" or "characters"
# get a list of this so we can check a sample if that is the case
def tracking_warning(error_text,url):
    with open("tracking_logging/tracking_possible_problems.txt", 'a', encoding='utf-8') as f:
        f.write(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S') + "---" + error_text + "---" + url + "\n")
    with open("tracking_logging/tracking_data=[].txt", 'a', encoding='utf-8') as g:
        if error_text == "data[data] == []":
            spl = url.split("/")
            g.write(spl[-2]+"/"+spl[-1] + "\n")


# to keep a better overview it helps to be able to reset the warning and error tracking txt files
def reset_error_warning_tracking():
    with open("tracking_logging/tracking_errors.txt", 'w', encoding='utf-8') as f:
        f.close()
    with open("tracking_logging/tracking_possible_problems.txt", 'w', encoding='utf-8') as f:
        f.close()


# we keep track of IDs that result in a waring with "data[data] == []". In that case the url probably does not have an e.g "episode" so why try again
# Usage: obtain a list of IDs that probably don't need further download attempts
# makes sense if you not try to get this specific id but all ids
def get_empty_suffix_list():
    id_list = []
    with open("tracking_logging/tracking_data=[].txt", 'r', encoding='utf-8') as f:
        for line in f:
            id_list.append(line.split("\n")[0])
    return id_list

