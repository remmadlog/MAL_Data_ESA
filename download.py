"""
This file is used to download all anime_id driven data using api.jikan
!!!THIS MIGHT TAKE A WHILE!!!
    -- we do about 1 request per second (slower!)
    -- for each mal_id/anime_id we do 6 requests (["full", "characters", "staff", "episodes", "forum", "statistics"])
    -- we have about 25200 ids
    -->best case: 42h
        -- this is unrealistic! we may get stuck or get a Timeout...
        -- take your time and maybe reduce the range
"""

from module_supply import *

for year in range(1970,2025):
    print("---------------------------------------------------------")
    print(str(year) + "-----------------------------------------------------")
    print("---------------------------------------------------------")
    download_anime_year(year, anime_type="all")
