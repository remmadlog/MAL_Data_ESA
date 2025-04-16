import pandas as pd
import numpy as np

import matplotlib
matplotlib.use('TkAgg',force=True)
import matplotlib.pyplot as plt



def plt_save(name):
    plt.savefig('Plots/' + name + '.png', dpi=350)
    plt.savefig('Plots/transparent_png/' + name + '.png', dpi=350, transparent=True)
    plt.savefig('Plots/SVG/' + name + '.svg', dpi=350, transparent=True)


"""
Using normalized data to get a better feel for comparison
"""
# opening normalized table (years are not normalized)
# table_normalized = pd.read_excel('S_1970_2024_information_by_year_normalized.xlsx')
# table = pd.read_excel('S_1970_2024_information_by_year.xlsx')


table_main = pd.read_excel('Season_1970_2024_main.xlsx')


#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-
#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-
"""Source total amount 1970-2024"""
#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-
#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-
# create a table that gives the amount of each source of a shows/movie that has a score
temp_table = pd.concat([table_main[(table_main["score"] > 0)].groupby("source").size().sort_values()],axis=1)
temp_table.columns = ["amount"]

# create a bar plot
# -- temp_table.index = source names    ||  we need this since we do not save and load the table so the table head ist only "amount"
plt.figure(figsize=(20,10))
plt.barh(temp_table.index, temp_table["amount"])

name = "Amount per Source (of scored entries)"
plt.xlabel("Amount")
plt.ylabel("Source")
plt.title(name)
plt.grid(linestyle = '--', linewidth = 0.5)

plt_save(name)
plt.clf()


#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-
#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-
"""Type total amount 1970-2024"""
#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-
#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-
# create a table that gives the amount of each source of a shows/movie that has a score
temp_table = pd.concat([table_main[(table_main["score"] > 0)].groupby("anime_type").size().sort_values()],axis=1)
temp_table.columns = ["amount"]

# create a bar plot
# -- temp_table.index = source names    ||  we need this since we do not save and load the table so the table head ist only "amount"
plt.figure(figsize=(20,10))
plt.barh(temp_table.index, temp_table["amount"])

name = "Amount per Type (of scored entries)"
plt.xlabel("Amount")
plt.ylabel("Type")
plt.title(name)
plt.grid(linestyle = '--', linewidth = 0.5)

plt_save(name)
plt.clf()



#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-
#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-
"""Score average per source from year1 to year2 in TF"""
#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-
#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-
# create tables in the given timeframes that give the average score per source including the amount of the source in this timeframe
for year1,year2 in [2015,2025], [2000,2015], [1970,2000]:

    # we need the average score in the given timeframe of each source
    temp_table = pd.concat([
        table_main[(table_main["score"] > 0)
                   & (table_main["year"] >= year1)
                   & (table_main["year"] < year2)].groupby("source")["score"].mean()
    ],axis=1)
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
            source_list.append(item + " ("+ str(temp_table_2.loc[item][0]) + ")")
        except:
            source_list.append(item + str(0))


    # figure size (quite large but comfy)
    plt.figure(figsize=(20, 10))
    plt.barh(source_list, temp_table["Score average"])

    name = "Score average per Source from " + str(year1) + " to " + str(year2-1) + " (including)"
    plt.xlabel("Score average")
    plt.ylabel("Source")
    plt.title(name)
    plt.grid(linestyle = '--', linewidth = 0.5)

    # save plot
    plt_save(name)
    # clear plot    |   used if plt.show() is not used
    plt.clf()


#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-
#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-
"""Average duration per type 1970-2024"""
#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-
#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-
# create a table that gives the amount of each source of a shows/movie that has a score
temp_table = pd.concat([table_main[
                            (table_main["score"] > 0)
                            & (table_main["duration"] > 0)
                        ].groupby("anime_type")["duration"].mean()],axis=1)
temp_table.columns = ["duration"]

# create a bar plot
plt.figure(figsize=(20,10))
# -- temp_table.index = source names    ||  we need this since we do not save and load the table so the table head ist only "amount"
plt.barh(temp_table.index, temp_table["duration"])

name = "Duration per Type from " + str(1970) + " to " + str(2024) + " (of scored entries)"
plt.xlabel("Duration")
plt.ylabel("Type")
plt.title(name)
plt.grid(linestyle = '--', linewidth = 0.5)

plt_save(name)
plt.clf()


# -#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-
# -#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-
"""Collection using the TF column""" # todo: create this table in creating?
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

    plt_save(name)
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

    plt_save(name)
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

    plt_save(name)
    plt.clf()



# -#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-
# -#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-
"""Relation of Score and #Episodes in TF"""
# -#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-
# -#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-
# doing the time frame thing by hand because I did stuff without and do not want to redo everything

temp_List0 = [table_main[(table_main["score"] > 0) & (table_main["year"] <2000)
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
plt.subplot(3,1,1)
plt.barh(columns, temp_List0)

name = "Average score per number of episodes before 2000"
plt.ylabel("Number of episodes")
plt.xlim(5.5,7.5)
plt.title(name)
plt.grid(linestyle='--', linewidth=0.5)
# plt_save(name)


plt.subplot(3,1,2)
plt.barh(columns, temp_List)

name = "Average score per number of episodes between 2000 and 2015"
plt.ylabel("Number of episodes")
plt.xlim(5.5,7.5)
plt.title(name)
plt.grid(linestyle='--', linewidth=0.5)
# plt_save(name)


plt.subplot(3,1,3)
plt.barh(columns, temp_List2)

name = "Average score per number of episodes after 2015"
plt.xlabel("Average score")
plt.ylabel("Number of episodes")
plt.xlim(5.5,7.5)
plt.title("Average score per number of episodes in different years")
plt.grid(linestyle='--', linewidth=0.5)

plt_save("Average score per number of episodes in different years")
plt.clf()




# -#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-
# -#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-
"""Relation of Score and Duration in TF"""
# -#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-
# -#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-
# doing the time frame thing by hand because I did stuff without and do not want to redo everything
# create tables (LISTS cause its only ONE row) for before 2000, inbetween 2000 and 2015 and after 2015
# todo: We could use the fucking temp_table...
temp_List0 = [table_main[(table_main["score"] > 0) & (table_main["year"] <2000)
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
columns = ["10min", "19min", "26min", "50min", "90min", "130min", "more" ]


plt.figure(figsize=(20, 10))
# plt.figure(1)
plt.subplot(3,1,1)
plt.barh(columns, temp_List0)

name = "Average score per duration before 2000"
plt.ylabel("duration in min")
plt.xlim(5.25,7.75)
plt.title(name)
plt.grid(linestyle='--', linewidth=0.5)
# plt_save(name)


plt.subplot(3,1,2)
plt.barh(columns, temp_List)

name = "Average score per duration between 2000 and 2015"
# plt.xlabel("Average score")
plt.ylabel("duration in min")
plt.xlim(5.25,7.75)
plt.title(name)
plt.grid(linestyle='--', linewidth=0.5)
# plt_save(name)


plt.subplot(3,1,3)
plt.barh(columns, temp_List2)

name = "Average score per duration after 2015"
plt.xlabel("Average score")
plt.ylabel("duration in min")
plt.xlim(5.25,7.75)
plt.title(name)
plt.grid(linestyle='--', linewidth=0.5)

plt_save("Average score per duration in different years")
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
],axis=1)

temp_table.columns = ["Movieish", "TVish", "total"]

temp_table["%Movieish"] = temp_table["Movieish"]/temp_table["total"]
temp_table["%TVish"] = temp_table["TVish"]/temp_table["total"]


plt.figure(figsize=(20, 10))

plt.plot(temp_table.index, temp_table["%Movieish"], label="% of Movieish")

name = "Ratio of anime Movieish entries over years"
plt.xlabel("Year")
plt.ylabel("%")

plt.legend(loc="upper right")
plt.title("Movie=80min+ || TV=10min+ and #episodes>10")
plt.grid(linestyle='--', linewidth=0.5)
plt_save(name)
plt.clf()



