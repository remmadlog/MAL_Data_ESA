"""
Here we create plots for the analysis over time
Since the overview is better if we be a bit less general this is only one file af at least 3
Here we have the plots that are based on a table that was created for that purpose
    -> plots that are based of table = pd.read_excel('S_1970_2024_information_by_year.xlsx')
"""


import pandas as pd
import numpy as np
import seaborn as sns
from datetime import datetime

import matplotlib
matplotlib.use('TkAgg',force=True)
import matplotlib.pyplot as plt


# use for saving a plt as it is, transparent and as SVG
def plt_save(name):
    plt.savefig('Plots/' + name + '.png', dpi=350)
    plt.savefig('Plots/transparent_png/' + name + '.png', dpi=350, transparent=True)
    plt.savefig('Plots/SVG/' + name + '.svg', dpi=350, transparent=True)


# found this here: https://gist.github.com/mdiener21/b4924815497a61954a68cfe3c942360f
def round_to_nearest_quarter_hour(minutes, base=15):
    """
    Input: A value in minutes.
    Return: An integer rounded to the nearest quarter-hour (0, 15, 30, 45) based on the base interval,
    with special handling to ensure rounding from 0 up to 7 goes to 0 and 8 to 15 round to 15

    Example  round_to_nearest_quarter_hour(0) rounds to 0
             round_to_nearest_quarter_hour(7) rounds to 0
             round_to_nearest_quarter_hour(8) rounds to 15
             round_to_nearest_quarter_hour(22) rounds to 15
             round_to_nearest_quarter_hour(23) rounds to 30
    """
    # Calculate how far into the current quarter we are
    fraction = minutes % base
    if fraction == 0:
        return minutes  # Exactly on a quarter hour
    elif fraction < (base / 2):
        # If before the halfway point, round down
        rounded = minutes - fraction
    else:
        # If at or past the halfway point, round up
        rounded = minutes + (base - fraction)

    # Ensure the result is always within the hour range
    return int(rounded) % 60


# opening tables:
# "table" uses the created table
table = pd.read_excel('S_1970_2024_information_by_year.xlsx')



"""
Lets us talk about naming:
    -- I have no idea how I should do that
    -- I will go for smth like YEAR_feature1_feature2_...

"""

#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-
#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-
"""Amount of TYPES and TYPE_COMBINATIONS"""
#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-
#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-

# ANIME_TYPE
""" Plot of AMOUNT of TYPE and TYP_COMBINATIONS."""
#   columns:
#      "#shows", "#TV_Movie_OVA_Special_ONA", "#TV_OVA_ONA", "#Movie_Special", "#Music_CM_PV",
#      "#TV_shows", "#OVA_shows", "#ONA_shows", "#Movie_shows", "#Special_shows",
#      "#Music_shows", "#CM_shows", "PV_shows", "#Rest_shows"



# total amount and combinations
plt.figure(figsize=(20,10))
plt.plot(table["year"],table["#shows"],label="#shows")
plt.plot(table["year"],table["#TV_Movie_OVA_Special_ONA"],label="#TV_Movie_OVA_Special_ONA")
plt.plot(table["year"],table["#TV_OVA_ONA"],label="#TV_OVA_ONA")
plt.plot(table["year"],table["#Movie_Special"],label="#Movie_Special")
plt.plot(table["year"],table["#Music_CM_PV"],label="#Music_CM_PV")
# plt.plot(table["year"],table["#Rest_shows"],label="#Other_shows")     # all but one is NaN

plt.legend(loc="upper left")
plt.title("Amount per year (Shows - TV+ - Movie+ - Other)")
plt.xlabel("Years")
plt.ylabel("Amount")
plt.grid(linestyle = '--', linewidth = 0.5)

plt_save('YEAR_Amount_(Shows_TV+_Movie+_Other)')
plt.clf(), plt.close()


# TV_OVA_ONA, TV_shows, OVA_shows, ONA_shows
plt.figure(figsize=(20,10))
plt.plot(table["year"],table["#TV_OVA_ONA"],label="#TV_OVA_ONA")
plt.plot(table["year"],table["#TV_shows"],label="#TV")
plt.plot(table["year"],table["#OVA_shows"],label="#OVA")
plt.plot(table["year"],table["#ONA_shows"],label="#ONA")

plt.legend(loc="upper left")
plt.title("Amount per year (TV - OVA - ONA)")
plt.xlabel("Years")
plt.ylabel("Amount")
plt.grid(linestyle = '--', linewidth = 0.5)

plt_save('YEAR_Amount_(TV_OVA_ONA)')
plt.clf(), plt.close()

#   # Movie_Special, #Movie_shows, #Special_shows
plt.figure(figsize=(20, 10))
plt.plot(table["year"], table["#Movie_Special"], label="#Movie_Special")
plt.plot(table["year"], table["#Movie_shows"], label="#Movie")
plt.plot(table["year"], table["#Special_shows"], label="#Special")

plt.legend(loc="upper left")
plt.title("Amount per year (Movie - Special)")
plt.xlabel("Years")
plt.ylabel("Amount")
plt.grid(linestyle='--', linewidth=0.5)

plt_save('YEAR_Amount_(Movie_Special)')
plt.clf(), plt.close()

#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-
#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-
"""SCORES -- Here sorted by MEAN, MIN, MAX"""
#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-
#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-


# SCORES
"""Plot of Mean, Min and Max for TYP_COMBINATIONS: 1. MEAN // 2. MIN // 3. MAX"""
#   columns:
#       "score_mean","score_min", "score_max",
#       "TV_Movie_OVA_Special_ONA_score_mean","TV_OVA_ONA_score_mean", "Movie_Special_score_mean", "Music_CM_PV_score_mean",
#       "TV_Movie_OVA_Special_ONA_score_min","TV_OVA_ONA_score_min", "Movie_Special_score_min", "Music_CM_PV_score_min",
#       "TV_Movie_OVA_Special_ONA_score_max","TV_OVA_ONA_score_max", "Movie_Special_score_max", "Music_CM_PV_score_max",


# MEAN by TYPE
plt.figure(figsize=(20,10))
plt.plot(table["year"],table["score_mean"],label="score_mean")
plt.plot(table["year"],table["TV_Movie_OVA_Special_ONA_score_mean"],label="TV+ and Movie+")
plt.plot(table["year"],table["TV_OVA_ONA_score_mean"],label="TV+")
plt.plot(table["year"],table["Movie_Special_score_mean"],label="Movie+")
plt.plot(table["year"],table["Music_CM_PV_score_mean"],label="Music+")

plt.legend(loc="upper left")
title = "Score average -- Overview"
plt.title(title)
plt.xlabel("Years")
plt.ylabel("average score")
plt.grid(linestyle = '--', linewidth = 0.5)
plt.ylim(0,10)
plt_save("YEAR_SCORE_average")
plt.clf(), plt.close()


# MIN by TYPE
plt.figure(figsize=(20,10))
plt.plot(table["year"],table["score_min"],label="score_min")
plt.plot(table["year"],table["TV_Movie_OVA_Special_ONA_score_min"],label="TV+ and Movie+")
plt.plot(table["year"],table["TV_OVA_ONA_score_min"],label="TV+")
plt.plot(table["year"],table["Movie_Special_score_min"],label="Movie+")
plt.plot(table["year"],table["Music_CM_PV_score_min"],label="Music+")

plt.legend(loc="upper left")
title = "Score MIN -- Overview"
plt.title(title)
plt.xlabel("Years")
plt.ylabel("average score")
plt.grid(linestyle = '--', linewidth = 0.5)
plt.ylim(0,10)
plt_save("YEAR_SCORE_min")
plt.clf(), plt.close()


# MAX by TYPE
plt.figure(figsize=(20,10))
plt.plot(table["year"],table["score_max"],label="score_max")
plt.plot(table["year"],table["TV_Movie_OVA_Special_ONA_score_max"],label="TV+ and Movie+")
plt.plot(table["year"],table["TV_OVA_ONA_score_max"],label="TV+")
plt.plot(table["year"],table["Movie_Special_score_max"],label="Movie+")
plt.plot(table["year"],table["Music_CM_PV_score_max"],label="Music+")

plt.legend(loc="upper left")
title = "Score MAX -- Overview"
plt.title(title)
plt.xlabel("Years")
plt.ylabel("average score")
plt.grid(linestyle = '--', linewidth = 0.5)
plt.ylim(0,10)
plt_save("YEAR_SCORE_max")
plt.clf(), plt.close()


# SCORES
"""Plot of Mean, Min and Max for TYPE: 1. MEAN // 2. MIN // 3. MAX"""
#   columns:
#       "TV_score_mean", "OVA_score_mean", "ONA_score_mean", "Movie_score_mean", "Special_score_mean",
#       "TV_score_min", "OVA_score_min", "ONA_score_min", "Movie_score_min", "Special_score_min",
#       "TV_score_max", "OVA_score_max", "ONA_score_max", "Movie_score_max", "Special_score_max"


# MEAN by TYPE
plt.figure(figsize=(20,10))
plt.plot(table["year"],table["TV_score_mean"],label="TV_score_mean")
plt.plot(table["year"],table["OVA_score_mean"],label="OVA_score_mean")
plt.plot(table["year"],table["ONA_score_mean"],label="ONA_score_mean")
plt.plot(table["year"],table["Movie_score_mean"],label="Movie_score_mean")
plt.plot(table["year"],table["Special_score_mean"],label="Special_score_mean")

plt.legend(loc="upper left")
tilte = "Score average -- Type"
plt.title(tilte)
plt.xlabel("Years")
plt.ylabel("average score")
plt.grid(linestyle = '--', linewidth = 0.5)
plt.ylim(0,10)
plt_save("YEAR_SCORE_average_TYPE")
plt.clf(), plt.close()


# MIN by TYPE
plt.figure(figsize=(20,10))
plt.plot(table["year"],table["TV_score_min"],label="TV_score_min")
plt.plot(table["year"],table["OVA_score_min"],label="OVA_score_min")
plt.plot(table["year"],table["ONA_score_min"],label="ONA_score_min")
plt.plot(table["year"],table["Movie_score_min"],label="Movie_score_min")
plt.plot(table["year"],table["Special_score_min"],label="Special_score_min")

plt.legend(loc="upper left")
title = "Score MIN -- Type"
plt.title(title)
plt.xlabel("Years")
plt.ylabel("average score")
plt.grid(linestyle = '--', linewidth = 0.5)
plt.ylim(0,10)
plt_save("YEAR_SCORE_min_TYPE")
plt.clf(), plt.close()


# MAX by TYPE
plt.figure(figsize=(20,10))
plt.plot(table["year"],table["TV_score_max"],label="TV_score_max")
plt.plot(table["year"],table["OVA_score_max"],label="OVA_score_max")
plt.plot(table["year"],table["ONA_score_max"],label="ONA_score_max")
plt.plot(table["year"],table["Movie_score_max"],label="Movie_score_max")
plt.plot(table["year"],table["Special_score_max"],label="Special_score_max")

plt.legend(loc="upper left")
title = "Score MAX -- Type"
plt.title(title)
plt.xlabel("Years")
plt.ylabel("average score")
plt.grid(linestyle = '--', linewidth = 0.5)
plt.ylim(0,10)
plt_save("YEAR_SCORE_max_TYPE")
plt.clf(), plt.close()




#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-
#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-
"""SCORES -- Here sorted by TYPE and TYPE_COMBINATION"""
#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-
#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-

# SCORES
"""Plot of Mean, Min and Max for TYP_COMBINATIONS: 1. MEAN // 2. MIN // 3. MAX"""
#   columns:
#       "score_mean","score_min", "score_max",
#       "TV_Movie_OVA_Special_ONA_score_mean","TV_OVA_ONA_score_mean", "Movie_Special_score_mean", "Music_CM_PV_score_mean",
#       "TV_Movie_OVA_Special_ONA_score_min","TV_OVA_ONA_score_min", "Movie_Special_score_min", "Music_CM_PV_score_min",
#       "TV_Movie_OVA_Special_ONA_score_max","TV_OVA_ONA_score_max", "Movie_Special_score_max", "Music_CM_PV_score_max",

# Total
plt.figure(figsize=(20,10))
plt.plot(table["year"],table["score_mean"],label="score_mean")
plt.plot(table["year"],table["score_min"],label="score_min")
plt.plot(table["year"],table["score_max"],label="score_max")

plt.legend(loc="upper left")
title = "Score overview -- Total"
plt.title(title)
plt.xlabel("Years")
plt.ylabel("Score")
plt.grid(linestyle = '--', linewidth = 0.5)
plt.ylim(0,10)
plt_save("YEAR_SCORE_overview_total")
plt.clf(), plt.close()

# TV+ and Movie+
plt.figure(figsize=(20,10))
plt.plot(table["year"],table["TV_Movie_OVA_Special_ONA_score_mean"],label="TV+ and Movie+_score_mean")
plt.plot(table["year"],table["TV_Movie_OVA_Special_ONA_score_min"],label="TV+ and Movie+_score_min")
plt.plot(table["year"],table["TV_Movie_OVA_Special_ONA_score_max"],label="TV+ and Movie+_score_max")

plt.legend(loc="upper left")
title = "Score overview -- TV+ and Movie+"
plt.title(title)
plt.xlabel("Years")
plt.ylabel("Score")
plt.grid(linestyle = '--', linewidth = 0.5)
plt.ylim(0,10)
plt_save("YEAR_SCORE_overview_TV+_Movie+")
plt.clf(), plt.close()


# TV+
plt.figure(figsize=(20,10))
plt.plot(table["year"],table["TV_OVA_ONA_score_mean"],label="TV+_score_mean")
plt.plot(table["year"],table["TV_OVA_ONA_score_min"],label="TV+_score_min")
plt.plot(table["year"],table["TV_OVA_ONA_score_max"],label="TV+_score_max")

plt.legend(loc="upper left")
title = "Score overview -- TV+"
plt.title(title)
plt.xlabel("Years")
plt.ylabel("Score")
plt.grid(linestyle = '--', linewidth = 0.5)
plt.ylim(0,10)
plt_save("YEAR_SCORE_overview_TV+")
plt.clf(), plt.close()


# Movie+
plt.figure(figsize=(20,10))
plt.plot(table["year"],table["Movie_Special_score_mean"],label="Movie+_score_mean")
plt.plot(table["year"],table["Movie_Special_score_min"],label="Movie+_score_min")
plt.plot(table["year"],table["Movie_Special_score_max"],label="Movie+_score_max")

plt.legend(loc="upper left")
title = "Score overview -- Movie+"
plt.title(title)
plt.xlabel("Years")
plt.ylabel("Score")
plt.grid(linestyle = '--', linewidth = 0.5)
plt.ylim(0,10)
plt_save("YEAR_SCORE_overview_Movie+")
plt.clf(), plt.close()


# Music+
plt.figure(figsize=(20,10))
plt.plot(table["year"],table["Music_CM_PV_score_mean"],label="Music+_score_mean")
plt.plot(table["year"],table["Music_CM_PV_score_min"],label="Music+_score_min")
plt.plot(table["year"],table["Music_CM_PV_score_max"],label="Music+_score_max")

plt.legend(loc="upper left")
title = "Score overview -- Music+"
plt.title(title)
plt.xlabel("Years")
plt.ylabel("Score")
plt.grid(linestyle = '--', linewidth = 0.5)
plt.ylim(0,10)
plt_save("YEAR_SCORE_overview_Music+")
plt.clf(), plt.close()


# TV
plt.figure(figsize=(20,10))
plt.plot(table["year"],table["TV_score_mean"],label="TV_score_mean")
plt.plot(table["year"],table["TV_score_min"],label="TV_score_min")
plt.plot(table["year"],table["TV_score_max"],label="TV_score_max")

plt.legend(loc="upper left")
title = "Score overview -- TV"
plt.title(title)
plt.xlabel("Years")
plt.ylabel("Score")
plt.grid(linestyle = '--', linewidth = 0.5)
plt.ylim(0,10)
plt_save("YEAR_SCORE_overview_TV")
plt.clf(), plt.close()


# OVA
plt.figure(figsize=(20,10))
plt.plot(table["year"],table["OVA_score_mean"],label="OVA_score_mean")
plt.plot(table["year"],table["OVA_score_min"],label="OVA_score_min")
plt.plot(table["year"],table["OVA_score_max"],label="OVA_score_max")

plt.legend(loc="upper left")
title = "Score overview -- OVA"
plt.title(title)
plt.xlabel("Years")
plt.ylabel("Score")
plt.grid(linestyle = '--', linewidth = 0.5)
plt.ylim(0,10)
plt_save("YEAR_SCORE_overview_OVA")
plt.clf(), plt.close()


# ONA
plt.figure(figsize=(20,10))
plt.plot(table["year"],table["ONA_score_mean"],label="ONA_score_mean")
plt.plot(table["year"],table["ONA_score_min"],label="ONA_score_min")
plt.plot(table["year"],table["ONA_score_max"],label="ONA_score_max")

plt.legend(loc="upper left")
title = "Score overview -- ONA"
plt.title(title)
plt.xlabel("Years")
plt.ylabel("Score")
plt.grid(linestyle = '--', linewidth = 0.5)
plt.ylim(0,10)
plt_save("YEAR_SCORE_overview_ONA")
plt.clf(), plt.close()


# Movie
plt.figure(figsize=(20,10))
plt.plot(table["year"],table["Movie_score_mean"],label="Movie_score_mean")
plt.plot(table["year"],table["Movie_score_min"],label="Movie_score_min")
plt.plot(table["year"],table["Movie_score_max"],label="Movie_score_max")

plt.legend(loc="upper left")
title = "Score overview -- Movie"
plt.title(title)
plt.xlabel("Years")
plt.ylabel("Score")
plt.grid(linestyle = '--', linewidth = 0.5)
plt.ylim(0,10)
plt_save("YEAR_SCORE_overview_Movie")
plt.clf(), plt.close()


# Special
plt.figure(figsize=(20,10))
plt.plot(table["year"],table["Special_score_mean"],label="Special_score_mean")
plt.plot(table["year"],table["Special_score_min"],label="Special_score_min")
plt.plot(table["year"],table["Special_score_max"],label="Special_score_max")

plt.legend(loc="upper left")
title = "Score overview -- Special"
plt.title(title)
plt.xlabel("Years")
plt.ylabel("Score")
plt.grid(linestyle = '--', linewidth = 0.5)
plt.ylim(0,10)
plt_save("YEAR_SCORE_overview_Special")
plt.clf(), plt.close()



#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-
#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-
"""Source per Year"""
#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-
#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-
# Source per year
plt.figure(figsize=(20,10))

for item in ['Manga', 'Original', 'Game', 'Visual novel', 'Web manga', 'Light novel', 'Novel', 'Unknown', 'Other']:
    plt.plot(table["year"], table["#" + item], label=item)

name = "Amount of Source per year (of scored entries)"
plt.xlabel("Year")
plt.ylabel("Amount")
plt.legend(loc="upper left")
plt.title(name)
plt.grid(linestyle = '--', linewidth = 0.5)

plt_save("YEAR_Amount_SOURCE")
plt.clf(), plt.close()


# -#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-
# -#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-
"""Ratio TV/MOVIE over time"""
# -#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-
# -#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-
# get ratios (%)
temp_table = table
temp_table["%TV_shows"] = temp_table["#TV_shows"]/temp_table["#TV_Movie_OVA_Special_ONA"]
temp_table["%OVA_shows"] = temp_table["#OVA_shows"]/temp_table["#TV_Movie_OVA_Special_ONA"]
temp_table["%ONA_shows"] = temp_table["#ONA_shows"]/temp_table["#TV_Movie_OVA_Special_ONA"]
temp_table["%Movie_shows"] = temp_table["#Movie_shows"]/temp_table["#TV_Movie_OVA_Special_ONA"]
temp_table["%Special_shows"] = temp_table["#Special_shows"]/temp_table["#TV_Movie_OVA_Special_ONA"]

plt.figure(figsize=(20, 10))

plt.plot(temp_table["year"], temp_table["%TV_shows"], label="% of TV")
plt.plot(temp_table["year"], temp_table["%OVA_shows"], label="% of ONA")
plt.plot(temp_table["year"], temp_table["%ONA_shows"], label="% of OVA")
plt.plot(temp_table["year"], temp_table["%Movie_shows"], label="% of Movie")
plt.plot(temp_table["year"], temp_table["%Special_shows"], label="% of Special")

name = "YEAR_Ration_TYPE"
plt.xlabel("Year")
plt.ylabel("%")
plt.legend(loc="upper right")
plt.title(name)
plt.grid(linestyle='--', linewidth=0.5)
plt_save(name)

plt_save("YEAR_Ration_Types")
plt.clf(), plt.close()

