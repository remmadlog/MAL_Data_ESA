import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib
matplotlib.use('TkAgg',force=True)
import matplotlib.pyplot as plt



def plt_save(name):
    plt.savefig('Plots/' + name + '.png', dpi=350)
    # plt.savefig('Plots/transparent_png/' + name + '.png', dpi=350, transparent=True)
    # plt.savefig('Plots/SVG/' + name + '.svg', dpi=350, transparent=True)


"""
Using normalized data to get a better feel for comparison
"""
# opening normalized table (years are not normalized)
table_normalized = pd.read_excel('S_1970_2024_information_by_year_normalized.xlsx')
table = pd.read_excel('S_1970_2024_information_by_year.xlsx')

table_main = pd.read_excel('Season_1970_2024_main.xlsx')



# -#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-
# -#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-
"""Heatmap -- Rating/Anime_Type"""
# -#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-
# -#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-
#
types = ["TV", "OVA", "ONA", "TV Special", "Movie", "Special", "PV", "Music", "CM"]

temp_table = pd.concat([
    table_main[(table_main["score"] > 0)    & (table_main["duration"] > 0)
               & (table_main["anime_type"] == "TV") ].groupby("rating").size(),
    table_main[(table_main["score"] > 0) & (table_main["duration"] > 0)
               & (table_main["anime_type"] == "OVA")].groupby("rating").size(),
    table_main[(table_main["score"] > 0) & (table_main["duration"] > 0)
               & (table_main["anime_type"] == "ONA")].groupby("rating").size(),
    table_main[(table_main["score"] > 0) & (table_main["duration"] > 0)
               & (table_main["anime_type"] == "TV Special")].groupby("rating").size(),
    table_main[(table_main["score"] > 0) & (table_main["duration"] > 0)
               & (table_main["anime_type"] == "Movie")].groupby("rating").size(),
    table_main[(table_main["score"] > 0) & (table_main["duration"] > 0)
               & (table_main["anime_type"] == "Special")].groupby("rating").size(),
    table_main[(table_main["score"] > 0) & (table_main["duration"] > 0)
               & (table_main["anime_type"] == "PV")].groupby("rating").size(),
    table_main[(table_main["score"] > 0) & (table_main["duration"] > 0)
               & (table_main["anime_type"] == "Music")].groupby("rating").size(),
    table_main[(table_main["score"] > 0) & (table_main["duration"] > 0)
               & (table_main["anime_type"] == "CM")].groupby("rating").size(),
],axis=1)

temp_table.columns = ["TV", "OVA", "ONA", "TV Special", "Movie", "Special", "PV", "Music", "CM"]

# get the table but device each entry by the sum of its row:
temp_table_rating = temp_table.div(temp_table.sum(axis=1), axis=0)
temp_table_rating.index.name = None

plt.figure(figsize=(20, 10))
plt.figure(1)
sns.heatmap(temp_table_rating, linewidths=0.5, annot=True, cmap = sns.cubehelix_palette(as_cmap=True))
plt_save("Heatmap_Rating_per_Type")
plt.clf()


temp_table_type = temp_table.transpose()
temp_table_type = temp_table_type.div(temp_table_type.sum(axis=1), axis=0)
temp_table_type.index.name = None

plt.figure(figsize=(20, 10))
plt.figure(2)
hm = sns.heatmap(temp_table_type, linewidths=0.5, annot=True, cmap = sns.cubehelix_palette(as_cmap=True))
hm.set_yticklabels(hm.get_yticklabels(), rotation=0)
plt_save("Heatmap_Type_per_Rating")
plt.clf()
