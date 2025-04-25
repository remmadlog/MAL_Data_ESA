"""
Here we create plots for the analysis over time
Since the overview is better if we be a bit less general this is only one file af at least 3
Here we have the plots that are based on a table that was created for that purpose
    -> plots that are based of table = pd.read_excel('S_1970_2024_information_by_year.xlsx')
"""


import pandas as pd
import numpy as np
from sklearn import preprocessing
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
# "table_main" is the main table we obtained using module_creation.py
table_main = pd.read_excel('Season_1970_2024_main.xlsx')



"""
For more comments consider plotting_yearly_analysis_ByTable 
    (This was supposed to be the main file. It was changed to get a better overview)

table_main.heads()
anime_id	approved	title	anime_type	source	episodes	status	airing	start	end	duration	rating	score	scored_by	rank	popularity	on_list	favorites	synopsis	season	year	broadcast_day	broadcast_time	#studios involved	#genres	#themes

"""


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
    source_list.sort()
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
    plt.clf(), plt.close()

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

plt_save("YEAR_DURATION_average_Source_" + str(1970) + "_" + str(2024))
plt.clf(), plt.close()





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
#
# # -#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-
# """Average duration per given time frame for each type"""
# # -#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-
# # for iterating over types
# types = ["TV", "OVA", "ONA", "TV Special", "Movie", "Special", "PV", "Music", "CM"]
# plt.figure(figsize=(20, 10))
#
# for item in types:
#     temp_table2 = pd.concat([temp_table[
#                                  (temp_table["score"] > 0)
#                                  & (temp_table["duration"] > 0)
#                                  & (temp_table["anime_type"] == item)
#                                  ].groupby("TF")["duration"].mean()], axis=1)
#     temp_table2.columns = ["duration"]
#
#     # create a bar plot
#     # -- temp_table.index = source names    ||  we need this since we do not save and load the table so the table head ist only "amount"
#     plt.barh(temp_table2.index, temp_table2["duration"])
#
#     name = "Average duration per time frame for " + item + " (of scored entries with positive duration)"
#     plt.xlabel("Average Duration")
#     plt.ylabel(item)
#     plt.title(name)
#     plt.grid(linestyle='--', linewidth=0.5)
#
#     plt_save("YEAR_DURATION_" + item + "_average_TF")
#     plt.clf(), plt.close()
#
# # -#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-
# """Average episode amount per given time frame for each type"""
# # -#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-
# # for iterating over types
# types = ["TV", "OVA", "ONA", "TV Special", "Movie", "Special", "PV", "Music", "CM"]
# plt.figure(figsize=(20, 10))
#
# for item in types:
#     temp_table2 = pd.concat([temp_table[
#                                  (temp_table["score"] > 0)
#                                  & (temp_table["episodes"] > 0)
#                                  & (temp_table["duration"] > 0)
#                                  & (temp_table["anime_type"] == item)
#                                  ].groupby("TF")["episodes"].mean()], axis=1)
#     temp_table2.columns = ["Average #episodes"]
#
#     # create a bar plot
#     # -- temp_table.index = source names    ||  we need this since we do not save and load the table so the table head ist only "amount"
#     plt.barh(temp_table2.index, temp_table2["Average #episodes"])
#
#     name = "Average episode amount per time frame for " + item + " (of scored entries with positive duration)"
#     plt.xlabel("Average #episodes")
#     plt.ylabel(item)
#     plt.title(name)
#     plt.grid(linestyle='--', linewidth=0.5)
#
#     plt_save("YEAR_EPISODE_ + item + "_average_TF")
#     plt.clf(), plt.close()
#
# # -#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-
# """Average score per given time frame for each type"""
# # -#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-
# # for iterating over types
# types = ["TV", "OVA", "ONA", "TV Special", "Movie", "Special", "PV", "Music", "CM"]
# plt.figure(figsize=(20, 10))
#
# for item in types:
#     # count +=1
#     temp_table2 = pd.concat([temp_table[
#                                  (temp_table["score"] > 0)
#                                  & (temp_table["episodes"] > 0)
#                                  & (temp_table["duration"] > 0)
#                                  & (temp_table["anime_type"] == item)
#                                  ].groupby("TF")["score"].mean()], axis=1)
#     temp_table2.columns = ["Average score"]
#
#     # create a bar plot
#     # -- temp_table.index = source names    ||  we need this since we do not save and load the table so the table head ist only "amount"
#     plt.barh(temp_table2.index, temp_table2["Average score"])
#
#     name = "Average episode amount per time frame for " + item + " (of scored entries with positive duration)"
#     plt.xlabel("Average score")
#     plt.ylabel(item)
#     plt.title(name)
#     plt.grid(linestyle='--', linewidth=0.5)
#
#     plt_save("YEAR_SCORE_ + item + "_average_TF")
#     plt.clf(), plt.close()

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
plt.title(name)
plt.grid(linestyle='--', linewidth=0.5)

plt_save("YEAR_SCORE_EPISODES_average_TF")
plt.clf(), plt.close()

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
plt.clf(), plt.close()

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
plt.clf(), plt.close()




# -#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-
# -#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-
"""SCORE TV/MOVIE (by #episodes and duration) over time"""
# -#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-
# -#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-
#
temp_table = pd.concat([
    table_main[
        (table_main["score"] > 0)
        & (table_main["duration"] > 80)
        ].groupby("year")["score"].mean(),
    table_main[
        (table_main["score"] > 0)
        & (table_main["duration"] > 10)
        & (table_main["episodes"] > 10)
        ].groupby("year")["score"].mean(),
    table_main[
        ((table_main["score"] > 0)
         & (table_main["duration"] > 80))
        | ((table_main["score"] > 0)
           & (table_main["duration"] > 10)
           & (table_main["episodes"] > 10))
        ].groupby("year")["score"].mean(),
    table_main[
        (table_main["score"] > 0)
        & (table_main["duration"] > 80)
        ].groupby("year")["score"].median(),
    table_main[
        (table_main["score"] > 0)
        & (table_main["duration"] > 10)
        & (table_main["episodes"] > 10)
        ].groupby("year")["score"].median()
], axis=1)

temp_table.columns = ["Movieish", "TVish", "total", "median_TV", "median_Movie"]
temp_table = temp_table.sort_values(by=['year'])

# temp_table["%Movieish"] = temp_table["Movieish"] / temp_table["total"]
# temp_table["%TVish"] = temp_table["TVish"] / temp_table["total"]

plt.figure(figsize=(20, 10))

plt.plot(temp_table.index, temp_table["Movieish"], label="Average Movieish")
plt.plot(temp_table.index, temp_table["TVish"], label="Average TVish")
plt.plot(temp_table.index, temp_table["total"], label="Average total")

# plt.plot(temp_table.index, temp_table["median_TV"], "r--", label = "median TVish")
# plt.plot(temp_table.index, temp_table["median_Movie"], "b--", label = "median Movieish")

name = "Average Score of anime TVish and Movieish entries over years"
plt.xlabel("Year")
plt.ylabel("%")

plt.legend(loc="upper right")
plt.title("Movie=80min+ || TV=10min+ and #episodes>10")
plt.grid(linestyle='--', linewidth=0.5)
plt_save("YEAR_average_SCORE_TV_Movie_by_Duration_Episodes")
plt.clf(), plt.close()



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
        & (table_main["duration"] > 0) ].groupby("year")["score"].mean(),
    table_main[
        (table_main["score"] > 0)
        & (table_main["duration"] > 0)].groupby("year")["score"].median()
],axis=1)
temp_table.columns = ["score", "median"]


plt.figure(figsize=(20, 10))

plt.plot(temp_table.index, temp_table["score"], label = "average")
plt.plot(temp_table.index, temp_table["median"], "r--", label = "median")
plt.legend(loc="upper left")


plt.xlabel("Year")
plt.ylabel("Score")
plt.title("Average score per year")
plt.grid(linestyle='--', linewidth=0.5)
plt_save("YEAR_SCORE_average")
plt.clf(), plt.close()


# -#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-
"""EPISODES"""
# -#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-
temp_table = pd.concat([
    table_main[
        (table_main["score"] > 0)
        & (table_main["duration"] > 0) ].groupby("year")["episodes"].mean(),
    table_main[
        (table_main["score"] > 0)
        & (table_main["duration"] > 0)].groupby("year")["episodes"].median()
],axis=1)
temp_table.columns = ["#episodes", "median"]

plt.figure(figsize=(20, 10))

plt.plot(temp_table.index, temp_table["#episodes"], label = "average")
plt.plot(temp_table.index, temp_table["median"], "r--", label = "median")
plt.legend(loc="upper left")

plt.xlabel("Year")
plt.ylabel("#Episodes")
plt.title("Average #episodes per year")
plt.grid(linestyle='--', linewidth=0.5)
plt_save("YEAR_EPISODE_average")
plt.clf(), plt.close()



# -#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-
"""DURATION"""
# -#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-
temp_table = pd.concat([
    table_main[
        (table_main["score"] > 0)
        & (table_main["duration"] > 0) ].groupby("year")["duration"].mean(),
    table_main[
        (table_main["score"] > 0)
        & (table_main["duration"] > 0)].groupby("year")["duration"].median()
],axis=1)
temp_table.columns = ["duration","median"]

plt.figure(figsize=(20, 10))

plt.plot(temp_table.index, temp_table["duration"], label  ="average")
plt.plot(temp_table.index, temp_table["median"], "r--", label = "median")
plt.legend(loc="upper left")

plt.xlabel("Year")
plt.ylabel("Duration")
plt.title("Average duration per year")
plt.grid(linestyle='--', linewidth=0.5)
plt_save("YEAR_DURATION_average")
plt.clf(), plt.close()



# -#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-
"""ON_LIST"""
# -#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-
temp_table = pd.concat([
    table_main[
        (table_main["score"] > 0)
        & (table_main["duration"] > 0) ].groupby("year")["on_list"].mean(),
    table_main[
        (table_main["score"] > 0)
        & (table_main["duration"] > 0)].groupby("year")["on_list"].median()
],axis=1)
temp_table.columns = ["on_list", "median"]

plt.figure(figsize=(20, 10))

plt.plot(temp_table.index, temp_table["on_list"], label  ="average")
plt.plot(temp_table.index, temp_table["median"], "r--", label = "median")
plt.legend(loc="upper left")

plt.xlabel("Year")
plt.ylabel("on_list")
plt.title("Average #On_List per year")
plt.grid(linestyle='--', linewidth=0.5)
plt_save("YEAR_OnList_average")
plt.clf(), plt.close()



# -#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-
"""Popularity"""
# -#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-
temp_table = pd.concat([
    table_main[
        (table_main["score"] > 0)
        & (table_main["duration"] > 0) ].groupby("year")["popularity"].mean(),
    table_main[
        (table_main["score"] > 0)
        & (table_main["duration"] > 0)].groupby("year")["popularity"].median()
],axis=1)
temp_table.columns = ["popularity", "median"]

plt.figure(figsize=(20, 10))

plt.plot(temp_table.index, temp_table["popularity"], label  ="average")
plt.plot(temp_table.index, temp_table["median"], "r--", label = "median")
plt.legend(loc="upper left")

plt.xlabel("Year")
plt.ylabel("popularity")
plt.title("Average popularity per year")
plt.grid(linestyle='--', linewidth=0.5)
plt_save("YEAR_POPULARITY_average")
plt.clf(), plt.close()



# -#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-
"""scored_by"""
# -#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-
temp_table = pd.concat([
    table_main[
        (table_main["score"] > 0)
        & (table_main["duration"] > 0) ].groupby("year")["scored_by"].mean(),
    table_main[
        (table_main["score"] > 0)
        & (table_main["duration"] > 0)].groupby("year")["scored_by"].median()
],axis=1)
temp_table.columns = ["scored_by", "median"]

plt.figure(figsize=(20, 10))

plt.plot(temp_table.index, temp_table["scored_by"], label  ="average")
plt.plot(temp_table.index, temp_table["median"], "r--", label = "median")
plt.legend(loc="upper left")


plt.xlabel("Year")
plt.ylabel("scored_by")
plt.title("Average #scored_by per year")
plt.grid(linestyle='--', linewidth=0.5)
plt_save("YEAR_ScoredBy_average")
plt.clf(), plt.close()



# -#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-
"""favorites"""
# -#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-
temp_table = pd.concat([
    table_main[
        (table_main["score"] > 0)
        & (table_main["duration"] > 0)
        & (table_main["favorites"] > 10)].groupby("year")["favorites"].mean(),
    table_main[
        (table_main["score"] > 0)
        & (table_main["duration"] > 0)
        & (table_main["favorites"] > 10)].groupby("year")["favorites"].median()
],axis=1)
temp_table.columns = ["favorites", "median"]

plt.figure(figsize=(20, 10))

plt.plot(temp_table.index, temp_table["favorites"], label  ="average")
plt.plot(temp_table.index, temp_table["median"], "r--", label = "median")
plt.legend(loc="upper left")

plt.xlabel("Year")
plt.ylabel("favorites")
plt.title("Average #favorites per year (#fav > 10)")
plt.grid(linestyle='--', linewidth=0.5)
plt_save("YEAR_FAVORITES_average")
plt.clf(), plt.close()



# -#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-
"""ranke"""
# -#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-
temp_table = pd.concat([
    table_main[
        (table_main["score"] > 0)
        & (table_main["duration"] > 0) ].groupby("year")["rank"].mean(),
    table_main[
        (table_main["score"] > 0)
        & (table_main["duration"] > 0)].groupby("year")["rank"].median()
],axis=1)
temp_table.columns = ["rank","median"]

plt.figure(figsize=(20, 10))

plt.plot(temp_table.index, temp_table["rank"], label  ="average")
plt.plot(temp_table.index, temp_table["median"], "r--", label = "median")
plt.legend(loc="upper left")

plt.xlabel("Year")
plt.ylabel("rank")
plt.title("Average rank per year")
plt.grid(linestyle='--', linewidth=0.5)
plt_save("YEAR_RANK_average")
plt.clf(), plt.close()



# -#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-
# -#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-
"""TOTAL over time (sums)"""
# -#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-
# -#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-

# -#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-
"""EPISODES|DURATION"""
# -#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-
temp_table = pd.concat([
    table_main[
        (table_main["score"] > 0)
        & (table_main["duration"] > 0) ].groupby("year")["episodes"].sum(),
    table_main[
        (table_main["score"] > 0)
        & (table_main["duration"] > 0)].groupby("year")["duration"].sum()
],axis=1)

x = temp_table.values #returns a numpy array
min_max_scaler = preprocessing.MinMaxScaler()
x_scaled = min_max_scaler.fit_transform(x)
temp_table = pd.DataFrame(x_scaled)

temp_table.columns = ["duration","#episodes"]

plt.figure(figsize=(20, 10))
plt.plot(temp_table.index, temp_table["#episodes"],label="episodes")
plt.plot(temp_table.index, temp_table["duration"],label="duration")

plt.xlabel("Year")
plt.title("Normalized amount|duration")
plt.legend(loc="upper left")
plt.grid(linestyle='--', linewidth=0.5)
plt.title("Normalized comparison episode amount and duration")
plt_save("YEAR_normalized_episodes_duration")
plt.clf(), plt.close()


# -#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-
"""OnList|ScoredBy|Favorites"""
# -#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-
temp_table = pd.concat([
    table_main[
        (table_main["score"] > 0)
        & (table_main["duration"] > 0)].groupby("year")["on_list"].sum(),
    table_main[
        (table_main["score"] > 0)
        & (table_main["duration"] > 0)].groupby("year")["scored_by"].sum(),
    table_main[
        (table_main["score"] > 0)
        & (table_main["duration"] > 0) ].groupby("year")["favorites"].sum()
],axis=1)

x = temp_table.values #returns a numpy array
min_max_scaler = preprocessing.MinMaxScaler()
x_scaled = min_max_scaler.fit_transform(x)
temp_table = pd.DataFrame(x_scaled)

temp_table.columns = ["on_list","scored_by","favorites"]

plt.figure(figsize=(20, 10))
plt.plot(temp_table.index, temp_table["on_list"],label="on_list")
plt.plot(temp_table.index, temp_table["scored_by"],label="scored_by")
plt.plot(temp_table.index, temp_table["favorites"],label="favorites")

plt.xlabel("Year")
plt.ylabel("Normalized amount")
plt.legend(loc="upper left")
plt.title("Normalized comparison of engagement")
plt.grid(linestyle='--', linewidth=0.5)

plt_save("YEAR_normalized_engagement")
plt.clf(), plt.close()




# -#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-
# -#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-
"""Amount of Genre/Studios/Themes"""
# -#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-
# -#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-
# temp_table = pd.concat([
#     table_main[
#         (table_main["score"] > 0)
#         & (table_main["duration"] > 0)].groupby("year")["on_list"].sum(),
#     table_main[
#         (table_main["score"] > 0)
#         & (table_main["duration"] > 0)].groupby("year")["scored_by"].sum(),
#     table_main[
#         (table_main["score"] > 0)
#         & (table_main["duration"] > 0) ].groupby("year")["favorites"].sum()
# ],axis=1)

temp_table_mean = table_main[
    (table_main["score"]>0) & (table_main["duration"]>0) & (table_main["episodes"]>0)
    &(table_main["#studios involved"]>0) & (table_main["#genres"]>0) & (table_main["#themes"]>0)
].groupby("year").agg({"#studios involved":"mean","#genres":"mean","#themes":"mean"})

temp_table_median = table_main[
    (table_main["score"]>0) & (table_main["duration"]>0) & (table_main["episodes"]>0)
    &(table_main["#studios involved"]>0) & (table_main["#genres"]>0) & (table_main["#themes"]>0)
].groupby("year").agg({"#studios involved":"median","#genres":"median","#themes":"median"})


plt.figure(figsize=(20, 10))
plt.plot(temp_table_mean.index, temp_table_mean["#studios involved"],"r",label="average #studios")
plt.plot(temp_table_mean.index, temp_table_mean["#genres"],"b",label="average #genres")
plt.plot(temp_table_mean.index, temp_table_mean["#themes"],"m",label="average #themes")
plt.plot(temp_table_median.index, temp_table_median["#studios involved"],"r+",label="median #studios")
plt.plot(temp_table_median.index, temp_table_median["#genres"],"b.",label="median #genres")
plt.plot(temp_table_median.index, temp_table_median["#themes"],"m*",label="median #themes")

plt.xlabel("Year")
plt.ylabel("Amount")
plt.legend(loc="upper left")
plt.title("Average/Mean of number of Studios|Genres|Themes")
plt.grid(linestyle='--', linewidth=0.5)

plt_save("YEAR_average_median_SGT")
plt.clf(), plt.close()




