"""
In here I want to collect the plots that are for an analysis of features over time.
I will not do that in the most effective way, mainly because I did the code of some of those already and atm do not want
to "fix" it.
    -- Some use an extra created table while other just create a table on the go (todo: do this coherently)
"""


import pandas as pd
import numpy as np

import matplotlib
matplotlib.use('TkAgg',force=True)
import matplotlib.pyplot as plt


# use for saving a plt as it is, transparent and as SVG
def plt_save(name):
    plt.savefig('Plots/' + name + '.png', dpi=350)
    plt.savefig('Plots/transparent_png/' + name + '.png', dpi=350, transparent=True)
    plt.savefig('Plots/SVG/' + name + '.svg', dpi=350, transparent=True)


# opening tables:
# "table" uses the created table
table = pd.read_excel('S_1970_2024_information_by_year.xlsx')
# "table_main" is the main table we obtained using module_creation.py
table_main = pd.read_excel('Season_1970_2024_main.xlsx')



"""
Lets us talk about nameing:
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
plt.clf()


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
plt.clf()

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
plt.clf()

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
plt.clf()


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
plt.clf()


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
plt.clf()


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
plt.clf()


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
plt.clf()


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
plt.clf()




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
plt.clf()

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
plt.clf()


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
plt.clf()


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
plt.clf()


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
plt.clf()


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
plt.clf()


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
plt.clf()


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
plt.clf()


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
plt.clf()


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
plt.clf()



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
plt.clf()


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

name = "Ratio of anime types over years"
plt.xlabel("Year")
plt.ylabel("%")
plt.legend(loc="upper right")
plt.title(name)
plt.grid(linestyle='--', linewidth=0.5)
plt_save(name)

plt_save("YEAR_Ration_Types")
plt.clf()





# -#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-
# -#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-
# -#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-
"""AD HOC plotting starts here"""
# -#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-
# -#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-
# -#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-






# -#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-
# -#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-
"""Source total amount 1970-2024"""
# -#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-
# -#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-
# create a table that gives the amount of each source of a shows/movie that has a score
temp_table = pd.concat([table_main[(table_main["score"] > 0)].groupby("source").size().sort_values()], axis=1)
temp_table.columns = ["amount"]

# create a bar plot
# -- temp_table.index = source names    ||  we need this since we do not save and load the table so the table head ist only "amount"
plt.figure(figsize=(20, 10))
plt.barh(temp_table.index, temp_table["amount"])

name = "Amount per Source (of scored entries)"
plt.xlabel("Amount")
plt.ylabel("Source")
plt.title(name)
plt.grid(linestyle='--', linewidth=0.5)

plt_save("YEAR_Amount_Source")
plt.clf()

# -#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-
# -#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-
"""Type total amount 1970-2024"""
# -#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-
# -#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-
# create a table that gives the amount of each source of a shows/movie that has a score
temp_table = pd.concat([table_main[(table_main["score"] > 0)].groupby("anime_type").size().sort_values()], axis=1)
temp_table.columns = ["amount"]

# create a bar plot
# -- temp_table.index = source names    ||  we need this since we do not save and load the table so the table head ist only "amount"
plt.figure(figsize=(20, 10))
plt.barh(temp_table.index, temp_table["amount"])

name = "Amount per Type (of scored entries)"
plt.xlabel("Amount")
plt.ylabel("Type")
plt.title(name)
plt.grid(linestyle='--', linewidth=0.5)

plt_save("YEAR_Amount_Type")
plt.clf()

# -#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-
# -#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-
"""Score average per source from year1 to year2 in TF"""
# -#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-
# -#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-
# create tables in the given timeframes that give the average score per source including the amount of the source in this timeframe
for year1, year2 in [2015, 2025], [2000, 2015], [1970, 2000]:

    # we need the average score in the given timeframe of each source
    temp_table = pd.concat([
        table_main[(table_main["score"] > 0)
                   & (table_main["year"] >= year1)
                   & (table_main["year"] < year2)].groupby("source")["score"].mean()
    ], axis=1)
    temp_table.columns = ["Score average"]

    # we want to know how often a source is used in this timeframe, there:
    temp_table_2 = pd.concat(
        [table_main[(table_main["score"] > 0)
                    & (table_main["year"] >= year1)
                    & (table_main["year"] < year2)].groupby("source").size().sort_values()], axis=1)

    # to add this to the y-axis we need to extract the precise data
    # list for name e.g. Mange ([amount used in timeframe])
    source_list = []
    # temp_table.index contains of name of sources e.g. Mange, Novel...
    for item in temp_table.index:
        # got some problems so try/except it is todo: check if this is needed and fix it
        try:
            # item = Source_Name    |   temp_table_2.loc[item][0] = Amount of Source used
            source_list.append(item + " (" + str(temp_table_2.loc[item][0]) + ")")
        except:
            source_list.append(item + str(0))

    # figure size (quite large but comfy)
    plt.figure(figsize=(20, 10))
    plt.barh(source_list, temp_table["Score average"])

    name = "Score average per Source from " + str(year1) + " to " + str(year2 - 1) + " (including)"
    plt.xlabel("Score average")
    plt.ylabel("Source")
    plt.title(name)
    plt.grid(linestyle='--', linewidth=0.5)

    # save plot
    plt_save("YEAR_SCORE_average_Source_" + str(year1) + "_" + str(year2 - 1))
    # clear plot    |   used if plt.show() is not used
    plt.clf()

# -#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-
# -#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-
"""Average duration per type 1970-2024"""
# -#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-
# -#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-
# create a table that gives the amount of each source of a shows/movie that has a score
temp_table = pd.concat([table_main[
                            (table_main["score"] > 0)
                            & (table_main["duration"] > 0)
                            ].groupby("anime_type")["duration"].mean()], axis=1)
temp_table.columns = ["duration"]

# create a bar plot
plt.figure(figsize=(20, 10))
# -- temp_table.index = source names    ||  we need this since we do not save and load the table so the table head ist only "amount"
plt.barh(temp_table.index, temp_table["duration"])

name = "Duration per Type from " + str(1970) + " to " + str(2024) + " (of scored entries)"
plt.xlabel("Duration")
plt.ylabel("Type")
plt.title(name)
plt.grid(linestyle='--', linewidth=0.5)

plt_save("YEAR_SCORE_average_Source_" + str(1970) + "_" + str(2024))
plt.clf()





# -#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-
# -#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-
# -#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-
"""Collection using the TF column"""  # todo: create this table in creating?
# -#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-
# -#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-
# -#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-
# create a table that gives the amount of each source of a shows/movie that has a score
temp_table = table_main

# create a table that is table_main with the additional column "TF", where e.g. temp_table["TF"] = "2015-2025" if temp_table["year"] is "<2025" but ">2000"
temp_table["TF"] = np.where(
    temp_table["year"] < 2000, "1970-1999", np.where(
        temp_table["year"] < 2015, "2000-2014", np.where(
            temp_table["year"] < 2025, "2015-2024", "2025")
    )
)

# -#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-
"""Average duration per given time frame for each type"""
# -#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-
# for iterating over types
types = ["TV", "OVA", "ONA", "TV Special", "Movie", "Special", "PV", "Music", "CM"]
plt.figure(figsize=(20, 10))

for item in types:
    temp_table2 = pd.concat([temp_table[
                                 (temp_table["score"] > 0)
                                 & (temp_table["duration"] > 0)
                                 & (temp_table["anime_type"] == item)
                                 ].groupby("TF")["duration"].mean()], axis=1)
    temp_table2.columns = ["duration"]

    # create a bar plot
    # -- temp_table.index = source names    ||  we need this since we do not save and load the table so the table head ist only "amount"
    plt.barh(temp_table2.index, temp_table2["duration"])

    name = "Average duration per time frame for " + item + " (of scored entries with positive duration)"
    plt.xlabel("Average Duration")
    plt.ylabel(item)
    plt.title(name)
    plt.grid(linestyle='--', linewidth=0.5)

    plt_save("YEAR_DURATION_average_TF")
    plt.clf()

# -#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-
"""Average episode amount per given time frame for each type"""
# -#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-
# for iterating over types
types = ["TV", "OVA", "ONA", "TV Special", "Movie", "Special", "PV", "Music", "CM"]
plt.figure(figsize=(20, 10))

for item in types:
    temp_table2 = pd.concat([temp_table[
                                 (temp_table["score"] > 0)
                                 & (temp_table["episodes"] > 0)
                                 & (temp_table["duration"] > 0)
                                 & (temp_table["anime_type"] == item)
                                 ].groupby("TF")["episodes"].mean()], axis=1)
    temp_table2.columns = ["Average #episodes"]

    # create a bar plot
    # -- temp_table.index = source names    ||  we need this since we do not save and load the table so the table head ist only "amount"
    plt.barh(temp_table2.index, temp_table2["Average #episodes"])

    name = "Average episode amount per time frame for " + item + " (of scored entries with positive duration)"
    plt.xlabel("Average #episodes")
    plt.ylabel(item)
    plt.title(name)
    plt.grid(linestyle='--', linewidth=0.5)

    plt_save("YEAR_EPISODE_average_TF")
    plt.clf()

# -#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-
"""Average score per given time frame for each type"""
# -#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-
# for iterating over types
types = ["TV", "OVA", "ONA", "TV Special", "Movie", "Special", "PV", "Music", "CM"]
plt.figure(figsize=(20, 10))

for item in types:
    # count +=1
    temp_table2 = pd.concat([temp_table[
                                 (temp_table["score"] > 0)
                                 & (temp_table["episodes"] > 0)
                                 & (temp_table["duration"] > 0)
                                 & (temp_table["anime_type"] == item)
                                 ].groupby("TF")["score"].mean()], axis=1)
    temp_table2.columns = ["Average score"]

    # create a bar plot
    # -- temp_table.index = source names    ||  we need this since we do not save and load the table so the table head ist only "amount"
    plt.barh(temp_table2.index, temp_table2["Average score"])

    name = "Average episode amount per time frame for " + item + " (of scored entries with positive duration)"
    plt.xlabel("Average score")
    plt.ylabel(item)
    plt.title(name)
    plt.grid(linestyle='--', linewidth=0.5)

    plt_save("YEAR_SCORE_average_TF")
    plt.clf()

# -#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-
# -#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-
"""Relation of Score and #Episodes in TF"""
# -#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-
# -#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-
# doing the time frame thing by hand because I did stuff without and do not want to redo everything

temp_List0 = [table_main[(table_main["score"] > 0) & (table_main["year"] < 2000)
                         & (table_main["episodes"] > 0)
                         & (table_main["episodes"] <= 4)
                         & (table_main["duration"] > 0)]["score"].mean(),
              table_main[(table_main["score"] > 0) & (table_main["year"] < 2000)
                         & (table_main["episodes"] > 4)
                         & (table_main["episodes"] <= 9)
                         & (table_main["duration"] > 0)]["score"].mean(),
              table_main[(table_main["score"] > 0) & (table_main["year"] < 2000)
                         & (table_main["episodes"] > 9)
                         & (table_main["episodes"] <= 13)
                         & (table_main["duration"] > 0)]["score"].mean(),
              table_main[(table_main["score"] > 0) & (table_main["year"] < 2000)
                         & (table_main["episodes"] > 13)
                         & (table_main["episodes"] <= 22)
                         & (table_main["duration"] > 0)]["score"].mean(),
              table_main[(table_main["score"] > 0) & (table_main["year"] < 2000)
                         & (table_main["episodes"] > 22)
                         & (table_main["episodes"] <= 28)
                         & (table_main["duration"] > 0)]["score"].mean(),
              table_main[(table_main["score"] > 0) & (table_main["year"] < 2000)
                         & (table_main["episodes"] > 28)
                         & (table_main["episodes"] <= 100)
                         & (table_main["duration"] > 0)]["score"].mean(),
              table_main[(table_main["score"] > 0) & (table_main["year"] < 2000)
                         & (table_main["episodes"] > 100)
                         & (table_main["duration"] > 0)]["score"].mean()
              ]
temp_List = [table_main[(table_main["score"] > 0) & (table_main["year"] >= 2000) & (table_main["year"] < 2015)
                        & (table_main["episodes"] > 0)
                        & (table_main["episodes"] <= 4)
                        & (table_main["duration"] > 0)]["score"].mean(),
             table_main[(table_main["score"] > 0) & (table_main["year"] >= 2000) & (table_main["year"] < 2015)
                        & (table_main["episodes"] > 4)
                        & (table_main["episodes"] <= 9)
                        & (table_main["duration"] > 0)]["score"].mean(),
             table_main[(table_main["score"] > 0) & (table_main["year"] >= 2000) & (table_main["year"] < 2015)
                        & (table_main["episodes"] > 9)
                        & (table_main["episodes"] <= 13)
                        & (table_main["duration"] > 0)]["score"].mean(),
             table_main[(table_main["score"] > 0) & (table_main["year"] >= 2000) & (table_main["year"] < 2015)
                        & (table_main["episodes"] > 13)
                        & (table_main["episodes"] <= 22)
                        & (table_main["duration"] > 0)]["score"].mean(),
             table_main[(table_main["score"] > 0) & (table_main["year"] >= 2000) & (table_main["year"] < 2015)
                        & (table_main["episodes"] > 22)
                        & (table_main["episodes"] <= 28)
                        & (table_main["duration"] > 0)]["score"].mean(),
             table_main[(table_main["score"] > 0) & (table_main["year"] >= 2000) & (table_main["year"] < 2015)
                        & (table_main["episodes"] > 28)
                        & (table_main["episodes"] <= 100)
                        & (table_main["duration"] > 0)]["score"].mean(),
             table_main[(table_main["score"] > 0) & (table_main["year"] >= 2000) & (table_main["year"] < 2015)
                        & (table_main["episodes"] > 100)
                        & (table_main["duration"] > 0)]["score"].mean()
             ]
temp_List2 = [table_main[(table_main["score"] > 0) & (table_main["year"] >= 2015)
                         & (table_main["episodes"] > 0)
                         & (table_main["episodes"] <= 4)
                         & (table_main["duration"] > 0)]["score"].mean(),
              table_main[(table_main["score"] > 0) & (table_main["year"] >= 2015)
                         & (table_main["episodes"] > 4)
                         & (table_main["episodes"] <= 9)
                         & (table_main["duration"] > 0)]["score"].mean(),
              table_main[(table_main["score"] > 0) & (table_main["year"] >= 2015)
                         & (table_main["episodes"] > 9)
                         & (table_main["episodes"] <= 13)
                         & (table_main["duration"] > 0)]["score"].mean(),
              table_main[(table_main["score"] > 0) & (table_main["year"] >= 2015)
                         & (table_main["episodes"] > 13)
                         & (table_main["episodes"] <= 22)
                         & (table_main["duration"] > 0)]["score"].mean(),
              table_main[(table_main["score"] > 0) & (table_main["year"] >= 2015)
                         & (table_main["episodes"] > 22)
                         & (table_main["episodes"] <= 28)
                         & (table_main["duration"] > 0)]["score"].mean(),
              table_main[(table_main["score"] > 0) & (table_main["year"] >= 2015)
                         & (table_main["episodes"] > 28)
                         & (table_main["episodes"] <= 100)
                         & (table_main["duration"] > 0)]["score"].mean(),
              table_main[(table_main["score"] > 0) & (table_main["year"] >= 2015)
                         & (table_main["episodes"] > 100)
                         & (table_main["duration"] > 0)]["score"].mean()
              ]
columns = ["0<x<=4", "4<x<=9", "9<x<=13", "13<x<=22", "22<x<=28", "28<x<=100", "100<x", ]

plt.figure(figsize=(20, 10))
plt.subplot(3, 1, 1)
plt.barh(columns, temp_List0)

name = "Average score per number of episodes before 2000"
plt.ylabel("Number of episodes")
plt.xlim(5.5, 7.5)
plt.title(name)
plt.grid(linestyle='--', linewidth=0.5)
# plt_save(name)


plt.subplot(3, 1, 2)
plt.barh(columns, temp_List)

name = "Average score per number of episodes between 2000 and 2015"
plt.ylabel("Number of episodes")
plt.xlim(5.5, 7.5)
plt.title(name)
plt.grid(linestyle='--', linewidth=0.5)
# plt_save(name)


plt.subplot(3, 1, 3)
plt.barh(columns, temp_List2)

name = "Average score per number of episodes after 2015"
plt.xlabel("Average score")
plt.ylabel("Number of episodes")
plt.xlim(5.5, 7.5)
plt.title("Average score per number of episodes in different years")
plt.grid(linestyle='--', linewidth=0.5)

plt_save("YEAR_SCORE_EPISODES_average_TF")
plt.clf()

# -#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-
# -#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-
"""Relation of Score and Duration in TF"""
# -#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-
# -#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-
# doing the time frame thing by hand because I did stuff without and do not want to redo everything
# create tables (LISTS cause its only ONE row) for before 2000, inbetween 2000 and 2015 and after 2015
# todo: We could use the fucking temp_table...
temp_List0 = [table_main[(table_main["score"] > 0) & (table_main["year"] < 2000)
                         & (table_main["duration"] > 0)
                         & (table_main["duration"] <= 10)]["score"].mean(),
              table_main[(table_main["score"] > 0) & (table_main["year"] < 2000)
                         & (table_main["duration"] > 10)
                         & (table_main["duration"] <= 19)]["score"].mean(),
              table_main[(table_main["score"] > 0) & (table_main["year"] < 2000)
                         & (table_main["duration"] > 19)
                         & (table_main["duration"] <= 26)]["score"].mean(),
              table_main[(table_main["score"] > 0) & (table_main["year"] < 2000)
                         & (table_main["duration"] > 26)
                         & (table_main["duration"] <= 50)]["score"].mean(),
              table_main[(table_main["score"] > 0) & (table_main["year"] < 2000)
                         & (table_main["duration"] > 50)
                         & (table_main["duration"] <= 90)]["score"].mean(),
              table_main[(table_main["score"] > 0) & (table_main["year"] < 2000)
                         & (table_main["duration"] > 90)
                         & (table_main["duration"] <= 130)]["score"].mean(),
              table_main[(table_main["score"] > 0) & (table_main["year"] < 2000)
                         & (table_main["duration"] > 130)]["score"].mean()
              ]
temp_List = [table_main[(table_main["score"] > 0) & (table_main["year"] >= 2000) & (table_main["year"] < 2015)
                        & (table_main["duration"] > 0)
                        & (table_main["duration"] <= 10)]["score"].mean(),
             table_main[(table_main["score"] > 0) & (table_main["year"] >= 2000) & (table_main["year"] < 2015)
                        & (table_main["duration"] > 10)
                        & (table_main["duration"] <= 19)]["score"].mean(),
             table_main[(table_main["score"] > 0) & (table_main["year"] >= 2000) & (table_main["year"] < 2015)
                        & (table_main["duration"] > 19)
                        & (table_main["duration"] <= 26)]["score"].mean(),
             table_main[(table_main["score"] > 0) & (table_main["year"] >= 2000) & (table_main["year"] < 2015)
                        & (table_main["duration"] > 26)
                        & (table_main["duration"] <= 50)]["score"].mean(),
             table_main[(table_main["score"] > 0) & (table_main["year"] >= 2000) & (table_main["year"] < 2015)
                        & (table_main["duration"] > 50)
                        & (table_main["duration"] <= 90)]["score"].mean(),
             table_main[(table_main["score"] > 0) & (table_main["year"] >= 2000) & (table_main["year"] < 2015)
                        & (table_main["duration"] > 90)
                        & (table_main["duration"] <= 130)]["score"].mean(),
             table_main[(table_main["score"] > 0) & (table_main["year"] >= 2000) & (table_main["year"] < 2015)
                        & (table_main["duration"] > 130)]["score"].mean()
             ]
temp_List2 = [table_main[(table_main["score"] > 0) & (table_main["year"] >= 2015)
                         & (table_main["duration"] > 0)
                         & (table_main["duration"] <= 10)]["score"].mean(),
              table_main[(table_main["score"] > 0) & (table_main["year"] >= 2015)
                         & (table_main["duration"] > 10)
                         & (table_main["duration"] <= 19)]["score"].mean(),
              table_main[(table_main["score"] > 0) & (table_main["year"] >= 2015)
                         & (table_main["duration"] > 19)
                         & (table_main["duration"] <= 26)]["score"].mean(),
              table_main[(table_main["score"] > 0) & (table_main["year"] >= 2015)
                         & (table_main["duration"] > 26)
                         & (table_main["duration"] <= 50)]["score"].mean(),
              table_main[(table_main["score"] > 0) & (table_main["year"] >= 2015)
                         & (table_main["duration"] > 50)
                         & (table_main["duration"] <= 90)]["score"].mean(),
              table_main[(table_main["score"] > 0) & (table_main["year"] >= 2015)
                         & (table_main["duration"] > 90)
                         & (table_main["duration"] <= 130)]["score"].mean(),
              table_main[(table_main["score"] > 0) & (table_main["year"] >= 2015)
                         & (table_main["duration"] > 130)]["score"].mean()
              ]
columns = ["10min", "19min", "26min", "50min", "90min", "130min", "more"]

plt.figure(figsize=(20, 10))
# plt.figure(1)
plt.subplot(3, 1, 1)
plt.barh(columns, temp_List0)

name = "Average score per duration before 2000"
plt.ylabel("duration in min")
plt.xlim(5.25, 7.75)
plt.title(name)
plt.grid(linestyle='--', linewidth=0.5)
# plt_save(name)


plt.subplot(3, 1, 2)
plt.barh(columns, temp_List)

name = "Average score per duration between 2000 and 2015"
# plt.xlabel("Average score")
plt.ylabel("duration in min")
plt.xlim(5.25, 7.75)
plt.title(name)
plt.grid(linestyle='--', linewidth=0.5)
# plt_save(name)


plt.subplot(3, 1, 3)
plt.barh(columns, temp_List2)

name = "Average score per duration after 2015"
plt.xlabel("Average score")
plt.ylabel("duration in min")
plt.xlim(5.25, 7.75)
plt.title(name)
plt.grid(linestyle='--', linewidth=0.5)

plt_save("YEAR_SCORE_DURATION_average_TF")
plt.clf()

# -#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-
# -#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-
"""Ratio TV/MOVIE (by #episodes and duration) over time"""
# -#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-
# -#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-
#
temp_table = pd.concat([
    table_main[
        (table_main["score"] > 0)
        & (table_main["duration"] > 80)
        ].groupby("year").size(),
    table_main[
        (table_main["score"] > 0)
        & (table_main["duration"] > 10)
        & (table_main["episodes"] > 10)
        ].groupby("year").size(),
    table_main[
        ((table_main["score"] > 0)
         & (table_main["duration"] > 80))
        | ((table_main["score"] > 0)
           & (table_main["duration"] > 10)
           & (table_main["episodes"] > 10))
        ].groupby("year").size(),
], axis=1)

temp_table.columns = ["Movieish", "TVish", "total"]

temp_table["%Movieish"] = temp_table["Movieish"] / temp_table["total"]
temp_table["%TVish"] = temp_table["TVish"] / temp_table["total"]

plt.figure(figsize=(20, 10))

plt.plot(temp_table.index, temp_table["%Movieish"], label="% of Movieish")

name = "Ratio of anime Movieish entries over years"
plt.xlabel("Year")
plt.ylabel("%")

plt.legend(loc="upper right")
plt.title("Movie=80min+ || TV=10min+ and #episodes>10")
plt.grid(linestyle='--', linewidth=0.5)
plt_save("YEAR_RATIO_TV_Movie_by_Duration_Episodes")
plt.clf()



# -#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-
# -#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-
"""Per Year plots"""
# -#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-
# -#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-

# -#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-
"""SCORE"""
# -#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-
temp_table = pd.concat([
    table_main[
        (table_main["score"] > 0)
        & (table_main["duration"] > 0) ].groupby("year")["score"].mean()
],axis=1)
temp_table.columns = ["score"]


plt.figure(figsize=(20, 10))

plt.plot(temp_table.index, temp_table["score"])

plt.xlabel("Year")
plt.ylabel("Score")
plt.title("Average score per year")
plt.grid(linestyle='--', linewidth=0.5)
plt_save("YEAR_SCORE_average")
plt.clf()


# -#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-
"""EPISODES"""
# -#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-
temp_table = pd.concat([
    table_main[
        (table_main["score"] > 0)
        & (table_main["duration"] > 0) ].groupby("year")["episodes"].mean()
],axis=1)
temp_table.columns = ["#episodes"]

plt.figure(figsize=(20, 10))

plt.plot(temp_table.index, temp_table["#episodes"])

plt.xlabel("Year")
plt.ylabel("#Episodes")
plt.title("Average #episodes per year")
plt.grid(linestyle='--', linewidth=0.5)
plt_save("YEAR_EPISODE_average")
plt.clf()



# -#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-
"""DURATION"""
# -#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-
temp_table = pd.concat([
    table_main[
        (table_main["score"] > 0)
        & (table_main["duration"] > 0) ].groupby("year")["duration"].mean()
],axis=1)
temp_table.columns = ["duration"]

plt.figure(figsize=(20, 10))

plt.plot(temp_table.index, temp_table["duration"])

plt.xlabel("Year")
plt.ylabel("Duration")
plt.title("Average duration per year")
plt.grid(linestyle='--', linewidth=0.5)
plt_save("YEAR_DURATION_average")
plt.clf()



# -#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-
"""ON_LIST"""
# -#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-
temp_table = pd.concat([
    table_main[
        (table_main["score"] > 0)
        & (table_main["duration"] > 0) ].groupby("year")["on_list"].mean()
],axis=1)
temp_table.columns = ["on_list"]

plt.figure(figsize=(20, 10))

plt.plot(temp_table.index, temp_table["on_list"])

plt.xlabel("Year")
plt.ylabel("on_list")
plt.title("Average #On_List per year")
plt.grid(linestyle='--', linewidth=0.5)
plt_save("YEAR_OnList_average")
plt.clf()



# -#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-
"""Popularity"""
# -#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-
temp_table = pd.concat([
    table_main[
        (table_main["score"] > 0)
        & (table_main["duration"] > 0) ].groupby("year")["popularity"].mean()
],axis=1)
temp_table.columns = ["popularity"]

plt.figure(figsize=(20, 10))

plt.plot(temp_table.index, temp_table["popularity"])

plt.xlabel("Year")
plt.ylabel("popularity")
plt.title("Average popularity per year")
plt.grid(linestyle='--', linewidth=0.5)
plt_save("YEAR_POPULARITY_average")
plt.clf()



# -#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-
"""scored_by"""
# -#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-
temp_table = pd.concat([
    table_main[
        (table_main["score"] > 0)
        & (table_main["duration"] > 0) ].groupby("year")["scored_by"].mean()
],axis=1)
temp_table.columns = ["scored_by"]

plt.figure(figsize=(20, 10))

plt.plot(temp_table.index, temp_table["scored_by"])

plt.xlabel("Year")
plt.ylabel("scored_by")
plt.title("Average #scored_by per year")
plt.grid(linestyle='--', linewidth=0.5)
plt_save("YEAR_ScoredBy_average")
plt.clf()



# -#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-
"""favorites"""
# -#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-
temp_table = pd.concat([
    table_main[
        (table_main["score"] > 0)
        & (table_main["duration"] > 0) ].groupby("year")["favorites"].mean()
],axis=1)
temp_table.columns = ["favorites"]

plt.figure(figsize=(20, 10))

plt.plot(temp_table.index, temp_table["favorites"])

plt.xlabel("Year")
plt.ylabel("favorites")
plt.title("Average #favorites per year")
plt.grid(linestyle='--', linewidth=0.5)
plt_save("YEAR_FAVORITES_average")
plt.clf()



# -#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-
# -#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-
"""TOTAL over time (sums)"""
# -#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-
# -#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-

# -#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-
"""EPISODES"""
# -#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-
temp_table = pd.concat([
    table_main[
        (table_main["score"] > 0)
        & (table_main["duration"] > 0) ].groupby("year")["episodes"].sum()
],axis=1)
temp_table.columns = ["#episodes"]

plt.figure(figsize=(20, 10))

plt.plot(temp_table.index, temp_table["#episodes"])

plt.xlabel("Year")
plt.ylabel("#Episodes")
plt.title("TOTAL #episodes per year")
plt.grid(linestyle='--', linewidth=0.5)
plt_save("YEAR_EPISODES_total")
plt.clf()


# -#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-
"""DURATION"""
# -#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-
temp_table = pd.concat([
    table_main[
        (table_main["score"] > 0)
        & (table_main["duration"] > 0) ].groupby("year")["duration"].sum()
],axis=1)
temp_table.columns = ["duration"]

plt.figure(figsize=(20, 10))

plt.plot(temp_table.index, temp_table["duration"])

plt.xlabel("Year")
plt.ylabel("Duration")
plt.title("TOTAL duration per year")
plt.grid(linestyle='--', linewidth=0.5)
plt_save("YEAR_DURATION_total")
plt.clf()



# -#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-
"""ON_LIST"""
# -#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-
temp_table = pd.concat([
    table_main[
        (table_main["score"] > 0)
        & (table_main["duration"] > 0) ].groupby("year")["on_list"].sum()
],axis=1)
temp_table.columns = ["on_list"]

plt.figure(figsize=(20, 10))

plt.plot(temp_table.index, temp_table["on_list"])

plt.xlabel("Year")
plt.ylabel("on_list")
plt.title("TOTAL #On_List per year")
plt.grid(linestyle='--', linewidth=0.5)
plt_save("YEAR_OnList_total")
plt.clf()



# -#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-
"""Popularity"""
# -#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-
temp_table = pd.concat([
    table_main[
        (table_main["score"] > 0)
        & (table_main["duration"] > 0) ].groupby("year")["popularity"].sum()
],axis=1)
temp_table.columns = ["popularity"]

plt.figure(figsize=(20, 10))

plt.plot(temp_table.index, temp_table["popularity"])

plt.xlabel("Year")
plt.ylabel("popularity")
plt.title("TOTAL popularity per year")
plt.grid(linestyle='--', linewidth=0.5)
plt_save("YEAR_POPULARITY_total")
plt.clf()



# -#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-
"""scored_by"""
# -#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-
temp_table = pd.concat([
    table_main[
        (table_main["score"] > 0)
        & (table_main["duration"] > 0) ].groupby("year")["scored_by"].sum()
],axis=1)
temp_table.columns = ["scored_by"]

plt.figure(figsize=(20, 10))

plt.plot(temp_table.index, temp_table["scored_by"])

plt.xlabel("Year")
plt.ylabel("scored_by")
plt.title("TOTAL #scored_by per year")
plt.grid(linestyle='--', linewidth=0.5)
plt_save("YEAR_ScoredBy_total")
plt.clf()



# -#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-
"""favorites"""
# -#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-
temp_table = pd.concat([
    table_main[
        (table_main["score"] > 0)
        & (table_main["duration"] > 0) ].groupby("year")["favorites"].sum()
],axis=1)
temp_table.columns = ["favorites"]

plt.figure(figsize=(20, 10))

plt.plot(temp_table.index, temp_table["favorites"])

plt.xlabel("Year")
plt.ylabel("favorites")
plt.title("TOTAL #favorites per year")
plt.grid(linestyle='--', linewidth=0.5)
plt_save("YEAR_FAVORITES_total")
plt.clf()




# -#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-
# -#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-
"""broadcast time and day changes per year"""
# -#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-
# -#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-


