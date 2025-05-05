import os
from tqdm import tqdm
from module_supply import *

# include year_under
# exclude year_upper
def download_years(year_lower,year_upper):
    for year in tqdm(range(year_lower, year_upper)):
        print("---------------------------------------------------------")
        print(str(year) + "-----------------------------------------------------")
        print("---------------------------------------------------------")
        download_anime_year(year, anime_type="all")


# compair tracking and actually downloaded files
def check_tracking():
    missing_id = []
    missing_req = []
    missing_req_id = []
    # open tracking
    with open("tracking_logging/tracking.json", encoding="utf8") as f:
        tracking_date = json.load(f)

    # we only consider the anime part
    anime_data = tracking_date["anime"]

    """
    ANIME DATA EXAMPLE
    "52299": {
                "anime_type": "TV",
                "mal_id": 52299,
                "req_param": [
                    "full",
                    "characters",
                    "staff",
                    "episodes",
                    "forum",
                    "statistics",
                    "recommendations",
                    "relations"
                ]
            }
    """
    # Ideas:
    """
    For each entry we going to get 
    - the anime_id
    - the type
    - the req_param
    and see if a file named
    - id_req_param.json
    is in
    - "data_json/anime/" + anime_type + str(anime_id)
    
    If this is not the case we save the anime_id and req_param to see if we need to download it again
    """

    Movie_folder = os.listdir("data_json/anime/Movie")
    ONA_folder = os.listdir("data_json/anime/ONA")
    OVA_folder = os.listdir("data_json/anime/OVA")
    Special_folder = os.listdir("data_json/anime/Special")
    TV_folder = os.listdir("data_json/anime/TV")
    TV_Special_folder = os.listdir("data_json/anime/TV Special")

    # get a list with all IDs that have a folder
    all_ids = Movie_folder + ONA_folder + OVA_folder + Special_folder + TV_folder + TV_Special_folder
    for anime_id in tqdm(anime_data):
        anime_type = anime_data[anime_id]["anime_type"]

        #check if the id is fond in a folder
        if anime_id in all_ids:
            # now see if all the files are in the folder
            folder = os.listdir("data_json/anime" + "/" + anime_type + "/" + str(anime_id))
            if str(anime_id) + "_full.json" in folder:
                for param in anime_data[anime_id]["req_param"]:
                    if str(anime_id) + "_" + param + ".json" in folder:
                        # print("good--" + str(anime_id) + "_" + param + ".json")
                        pass
                    else:
                        missing_req.append([anime_id,param])
                        missing_req_id.append(anime_id)
        else:
            missing_id.append(anime_id)


    print("List of missing param and ids")
    print(missing_req)

    print("List of missing param, id ONLY")
    print(missing_req_id)

    print("List of missing ids")
    print(missing_id)



# In case of duplicates in tracking[anime][id][req_param]
# # idea: load tracking.json || get req_param as list || remove duplicates by converting to a set and back to a list || change json and save
# # # list(set([1,1,1,2,3,1,3])) = [1,2,3] -- sets are sets in mathematical sense (every element is unique
def repair_tracking():
    # load tracking
    with open('tracking_logging/tracking.json', encoding="utf8") as f:
        tracking_data = json.load(f)

    for anime_id in tracking_data["anime"]:
        # get req_param per id as list
        temp_list = tracking_data["anime"][anime_id]["req_param"]
        # make list to set -> removes duplicates || make set to list again
        temp_list = list(set(temp_list))
        # rewrite tracking
        tracking_data["anime"][anime_id]["req_param"] = temp_list

    # save rewritten tracking
    with open('tracking_logging/tracking.json',"w", encoding="utf8") as f:
        json.dump(tracking_data, f, ensure_ascii=False, indent=4)



# download only file that are not already on disk
def download_missing_only(anime_id, req_param = "all"):

    Movie_folder = os.listdir("data_json/anime/Movie")
    ONA_folder = os.listdir("data_json/anime/ONA")
    OVA_folder = os.listdir("data_json/anime/OVA")
    Special_folder = os.listdir("data_json/anime/Special")
    TV_folder = os.listdir("data_json/anime/TV")
    TV_Special_folder = os.listdir("data_json/anime/TV Special")

    all_ids = Movie_folder + ONA_folder + OVA_folder + Special_folder + TV_folder + TV_Special_folder

    if anime_id in Movie_folder:
        anime_type = "Movie"
    elif anime_id in ONA_folder:
        anime_type = "ONA"
    elif anime_id in OVA_folder:
        anime_type = "OVA"
    elif anime_id in TV_folder:
        anime_type = "TV"
    elif anime_id in TV_Special_folder:
        anime_type = "TV Special"
    else:
        anime_type = "all"
        download_full_id(anime_id)

    if anime_type != "all":
        if req_param == "all":
            request_parameter = ["full", "characters", "staff", "episodes", "forum", "statistics"]

            # getr anime_type
            # # I could save the requested data here but rn I do not care for an additional request, so I just use that to get anime_type
            data = get_data("https://api.jikan.moe/v4/anime/" + str(anime_id))[1]
            anime_type = data["data"]["type"]

            # start downloading
            for req_param in request_parameter:
                if str(anime_id) + "_" + req_param + ".json" not in os.listdir("data_json/anime" + "/" + anime_type + "/" + str(anime_id)):
                    download_by_malID(anime_id, req_param, anime_type, check_existance=0)
        else:
            if str(anime_id) + "_" + req_param + ".json" not in os.listdir("data_json/anime" + "/" + anime_type + "/" + str(anime_id)):
                download_by_malID(anime_id, req_param, anime_type, check_existance=0)

