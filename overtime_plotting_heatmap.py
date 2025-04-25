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
# "table_main" is the main table we obtained using module_creation.py
table_main = pd.read_excel('Season_1970_2024_main.xlsx')



"""
For more comments consider plotting_yearly_analysis_ByTable 
    (This was supposed to be the main file. It was changed to get a better overview)

table_main.heads()
anime_id	approved	title	anime_type	source	episodes	status	airing	start	end	duration	rating	score	scored_by	rank	popularity	on_list	favorites	synopsis	season	year	broadcast_day	broadcast_time	#studios involved	#genres	#themes

"""
# -#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-
# -#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-
help_table = table_main
# create a table that is table_main with the additional column "TF", where e.g. temp_table["TF"] = "2015-2025" if temp_table["year"] is "<2025" but ">2000"
# todo: it would be smarter to create this once, save it, and load it
help_table["TF"] = np.where(
    help_table["year"] < 2000, "1970-1999", np.where(
        help_table["year"] < 2015, "2000-2014", np.where(
            help_table["year"] < 2025, "2015-2024", "2025")
    )
)

# -#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-
help_table["DF"] = np.where(
    help_table["duration"] < 5, "< 5min", np.where(
        help_table["duration"] < 10, "< 10min", np.where(
            help_table["duration"] < 20, "< 20min", np.where(
                help_table["duration"] < 30, "< 30min", np.where(
                    help_table["duration"] < 45, "< 45min", np.where(
                        help_table["duration"] < 60, "< 60min", np.where(
                            help_table["duration"] < 90, "< 90min", np.where(
                                help_table["duration"] < 120, "< 120min", np.where(
                                    help_table["duration"] < 150, "< 150min", np.where(
                                        help_table["duration"] < 160, "< 160min", ">=160")
                                )
                            )
                        )
                    )
                )
            )
        )
    )
)

# -#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-
help_table["EF"] = np.where(
    help_table["episodes"] < 4, "< 4 Ep", np.where(
        help_table["episodes"] < 10, "< 10 Ep", np.where(
            help_table["episodes"] < 14, "< 14 Ep", np.where(
                help_table["episodes"] < 21, "< 21 Ep", np.where(
                    help_table["episodes"] < 25, "< 25 Ep", np.where(
                        help_table["episodes"] < 60, "< 60 Ep", np.where(
                            help_table["episodes"] < 100, "< 100 Ep", np.where(
                                help_table["episodes"] < 200, "< 200 Ep", np.where(
                                    help_table["episodes"] < 300, "< 300 Ep", np.where(
                                        help_table["episodes"] < 500, "< 500 Ep", ">=500")
                                )
                            )
                        )
                    )
                )
            )
        )
    )
)
# -#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-
# -#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-
"""HeatMap_Rating_TF"""
# -#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-
# -#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-
temp_table = pd.concat([
    table_main[(table_main["score"] > 0)
               & (table_main["duration"] > 0)
               & (table_main["year"] < 2000) ].groupby("rating").size(),
    table_main[(table_main["score"] > 0)
               & (table_main["duration"] > 0)
               & (table_main["year"] < 2015)
               & (table_main["year"] >= 2000)].groupby("rating").size(),
    table_main[(table_main["score"] > 0)
               & (table_main["duration"] > 0)
               & (table_main["year"] >=2015)].groupby("rating").size()
],axis=1)

temp_table.columns = ["1970-1999","2000-2014","2015-2024"]

# get the table but device each entry by the sum of its row:
temp_table_rating = temp_table.div(temp_table.sum(axis=1), axis=0)
temp_table_rating.index.name = None

plt.figure(figsize=(20, 10))
sns.heatmap(temp_table_rating, linewidths=0.5, annot=True, cmap = sns.cubehelix_palette(as_cmap=True))

plt.title("Rating share per TF")
plt_save("Heatmap_TF_Rating")
plt.clf()


# -#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-
temp_table_y = temp_table.transpose()
temp_table_y = temp_table_y.div(temp_table_y.sum(axis=1), axis=0)
temp_table_y.index.name = None

plt.figure(figsize=(20, 10))
hm = sns.heatmap(temp_table_y, linewidths=0.5, annot=True, cmap = sns.cubehelix_palette(as_cmap=True))
hm.set_yticklabels(hm.get_yticklabels(), rotation=0)

plt.title("TF share per rating")
plt_save("Heatmap_TF_Rating_T")
plt.clf()



# -#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-
# -#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-
"""HeatMap_type_TF"""
# -#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-
# -#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-
temp_table = pd.concat([
    table_main[(table_main["score"] > 0)
               & (table_main["duration"] > 0)
               & (table_main["year"] < 2000) ].groupby("anime_type").size(),
    table_main[(table_main["score"] > 0)
               & (table_main["duration"] > 0)
               & (table_main["year"] < 2015)
               & (table_main["year"] >= 2000)].groupby("anime_type").size(),
    table_main[(table_main["score"] > 0)
               & (table_main["duration"] > 0)
               & (table_main["year"] >=2015)].groupby("anime_type").size()
],axis=1)

temp_table.columns = ["1970-1999","2000-2014","2015-2024"]

# get the table but device each entry by the sum of its row:
temp_table_type = temp_table.div(temp_table.sum(axis=1), axis=0)
temp_table_type.index.name = None

plt.figure(figsize=(20, 10))
temp = sns.heatmap(temp_table_type, linewidths=0.5, annot=True, cmap = sns.cubehelix_palette(as_cmap=True))
temp.set_yticklabels(temp.get_yticklabels(), rotation=0)

plt.title("Type share per TF")
plt_save("Heatmap_TF_Type")
plt.clf()


# -#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-
temp_table_y = temp_table.transpose()
temp_table_y = temp_table_y.div(temp_table_y.sum(axis=1), axis=0)
temp_table_y.index.name = None

plt.figure(figsize=(20, 10))
hm = sns.heatmap(temp_table_y, linewidths=0.5, annot=True, cmap = sns.cubehelix_palette(as_cmap=True))
hm.set_yticklabels(hm.get_yticklabels(), rotation=0)

plt.title("TF share per Type")
plt_save("Heatmap_TF_Type_T")
plt.clf()




# -#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-
# -#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-
"""HeatMap_source_TF"""
# -#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-
# -#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-
temp_table = pd.concat([
    table_main[(table_main["score"] > 0)
               & (table_main["duration"] > 0)
               & (table_main["year"] < 2000) ].groupby("source").size(),
    table_main[(table_main["score"] > 0)
               & (table_main["duration"] > 0)
               & (table_main["year"] < 2015)
               & (table_main["year"] >= 2000)].groupby("source").size(),
    table_main[(table_main["score"] > 0)
               & (table_main["duration"] > 0)
               & (table_main["year"] >=2015)].groupby("source").size()
],axis=1)

temp_table.columns = ["1970-1999","2000-2014","2015-2024"]

# get the table but device each entry by the sum of its row:
temp_table_type = temp_table.div(temp_table.sum(axis=1), axis=0)
temp_table_type.index.name = None

plt.figure(figsize=(20, 10))
temp = sns.heatmap(temp_table_type, linewidths=0.5, annot=True, cmap = sns.cubehelix_palette(as_cmap=True))
temp.set_yticklabels(temp.get_yticklabels(), rotation=0)

plt.title("Source share per TF")
plt_save("Heatmap_TF_Source")
plt.clf()


# -#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-
temp_table_y = temp_table.transpose()
temp_table_y = temp_table_y.div(temp_table_y.sum(axis=1), axis=0)
temp_table_y.index.name = None

plt.figure(figsize=(20, 10))
hm = sns.heatmap(temp_table_y, linewidths=0.5, annot=True, cmap = sns.cubehelix_palette(as_cmap=True))
# hm.set_xticklabels(hm.get_xticklabels(), rotation=0)
hm.set_yticklabels(hm.get_yticklabels(), rotation=0)

plt.title("TF share per Source")
plt_save("Heatmap_TF_Source_T")
plt.clf()


# -#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-
# -#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-
"""HeatMap_broadcast_day_TF"""
# -#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-
# -#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-
temp_table = pd.concat([
    table_main[(table_main["score"] > 0)
               & (table_main["duration"] > 0)
               & (table_main["year"] < 2000) ].groupby("broadcast_day").size(),
    table_main[(table_main["score"] > 0)
               & (table_main["duration"] > 0)
               & (table_main["year"] < 2015)
               & (table_main["year"] >= 2000)].groupby("broadcast_day").size(),
    table_main[(table_main["score"] > 0)
               & (table_main["duration"] > 0)
               & (table_main["year"] >=2015)].groupby("broadcast_day").size()
],axis=1)

temp_table.columns = ["1970-1999","2000-2014","2015-2024"]
temp_table = temp_table.reindex(index=['Mondays', 'Tuesdays', 'Wednesdays', 'Thursdays', 'Fridays', 'Saturdays', 'Sundays'])

# get the table but device each entry by the sum of its row:
temp_table_type = temp_table.div(temp_table.sum(axis=1), axis=0)
temp_table_type.index.name = None

plt.figure(figsize=(20, 10))
temp = sns.heatmap(temp_table_type, linewidths=0.5, annot=True, cmap = sns.cubehelix_palette(as_cmap=True))
temp.set_yticklabels(temp.get_yticklabels(), rotation=0)

plt.title("Day share per TF")
plt_save("Heatmap_TF_Day")
plt.clf()


# -#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-
temp_table_y = temp_table.transpose()
temp_table_y = temp_table_y.div(temp_table_y.sum(axis=1), axis=0)
temp_table_y.index.name = None

plt.figure(figsize=(20, 10))
hm = sns.heatmap(temp_table_y, linewidths=0.5, annot=True, cmap = sns.cubehelix_palette(as_cmap=True))
# hm.set_xticklabels(hm.get_xticklabels(), rotation=0)
hm.set_yticklabels(hm.get_yticklabels(), rotation=0)

plt.title("TF share per Day")
plt_save("Heatmap_TF_Day_T")
plt.clf()




# -#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-
# -#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-
"""HeatMap_broadcast_time_TF"""
# -#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-
# -#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-
temp_table1 = table_main
times_rounded = []
for item in table_main["broadcast_time"].fillna(0):
    if item:
        x = datetime.strptime(str(item),"%H:%M")
        hh = x.hour
        mm = round_to_nearest_quarter_hour(x.minute)
        if hh<10:
            H = "0"+str(hh)
        else:
            H = str(hh)
        if mm ==0:
            M = "00"
        else:
            M = str(mm)
        times_rounded.append(H + ":" + M)
    else:
        times_rounded.append(np.nan)


temp_table1["time_15"] = times_rounded

temp_table = pd.concat([
    temp_table1[(temp_table1["score"] > 0)
               & (temp_table1["duration"] > 0)
               & (temp_table1["year"] < 2000) ].groupby("time_15").size(),
    temp_table1[(temp_table1["score"] > 0)
               & (temp_table1["duration"] > 0)
               & (temp_table1["year"] < 2015)
               & (temp_table1["year"] >= 2000)].groupby("time_15").size(),
    temp_table1[(temp_table1["score"] > 0)
               & (temp_table1["duration"] > 0)
               & (temp_table1["year"] >=2015)].groupby("time_15").size()
],axis=1)

temp_table.columns = ["1970-1999","2000-2014","2015-2024"]
temp_table = temp_table.reindex(index=['00:00', '00:15', '00:30', '00:45', '01:00', '01:15', '01:30', '01:45', '02:00', '02:15', '02:30', '02:45', '03:00', '03:15', '03:30', '03:45', '04:00', '04:15', '04:45', '05:00', '05:30', '05:45', '06:00', '06:15', '06:30', '06:45', '07:00', '07:15', '07:30', '07:45', '08:00', '08:15', '08:30', '08:45', '09:00', '09:15', '09:30', '09:45', '10:00', '10:15', '10:30', '11:00', '11:15', '11:30', '11:45', '12:00', '12:30', '13:00', '13:30', '13:45', '14:00', '14:30', '14:45', '15:15', '15:30', '15:45', '16:00', '16:15', '16:30', '16:45', '17:00', '17:15', '17:30', '17:45', '18:00', '18:15', '18:30', '18:45', '19:00', '19:15', '19:30', '19:45', '20:00', '20:15', '20:30', '20:45', '21:00', '21:15', '21:30', '21:45', '22:00', '22:15', '22:30', '22:45', '23:00', '23:15', '23:30', '23:45'])

# get the table but device each entry by the sum of its row:
temp_table_type = temp_table.div(temp_table.sum(axis=1), axis=0)
temp_table_type.index.name = None

plt.figure(figsize=(20, 10))
temp = sns.heatmap(temp_table_type, linewidths=0.5, cmap = sns.cubehelix_palette(as_cmap=True))
temp.set_yticklabels(temp.get_yticklabels(), rotation=0)

plt.title("Time share per TF")
plt_save("Heatmap_TF_Time")
plt.clf()

# -#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-
temp_table_y = temp_table.transpose()
temp_table_y = temp_table_y.div(temp_table_y.sum(axis=1), axis=0)
temp_table_y.index.name = None

plt.figure(figsize=(20, 10))
hm = sns.heatmap(temp_table_y, linewidths=0.5, cmap = sns.cubehelix_palette(as_cmap=True))
# hm.set_xticklabels(hm.get_xticklabels(), rotation=0)
hm.set_yticklabels(hm.get_yticklabels(), rotation=0)

plt.title("TF share per Time")
plt_save("Heatmap_TF_Time_T")
plt.clf()



# -#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-
# -#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-
"""HeatMap_EpisodeFrame_TimeFrame"""
# -#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-
# -#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-
temp_table = pd.concat([
    help_table[(help_table["score"] > 0)
               & (help_table["duration"] > 0)
               & (help_table["episodes"] > 0)
               & (help_table["TF"] == "1970-1999")].groupby("EF").size(),
    help_table[(table_main["score"] > 0)
               & (help_table["duration"] > 0)
               & (help_table["episodes"] > 0)
               & (help_table["TF"] == "2000-2014")].groupby("EF").size(),
    help_table[(help_table["score"] > 0)
               & (help_table["duration"] > 0)
               & (help_table["episodes"] > 0)
               & (help_table["TF"] == "2015-2024")].groupby("EF").size()
],axis=1)

temp_table.columns = ["1970-1999","2000-2014","2015-2024"]
temp_table = temp_table.reindex(index=["< 4 Ep","< 10 Ep","< 14 Ep", "< 21 Ep",  "< 25 Ep",  "< 60 Ep", "< 100 Ep","< 200 Ep","< 300 Ep","< 500 Ep", ">=500"])

# get the table but device each entry by the sum of its row:
temp_table_type = temp_table.div(temp_table.sum(axis=1), axis=0)
temp_table_type.index.name = None

plt.figure(figsize=(20, 10))
temp = sns.heatmap(temp_table_type, linewidths=0.5, annot=True, cmap = sns.cubehelix_palette(as_cmap=True))
temp.set_yticklabels(temp.get_yticklabels(), rotation=0)

plt.title("EF share per TF")
plt_save("Heatmap_EF_TF")
plt.clf()

# -#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-
temp_table_y = temp_table.transpose()
temp_table_y = temp_table_y.div(temp_table_y.sum(axis=1), axis=0)
temp_table_y.index.name = None

plt.figure(figsize=(20, 10))
hm = sns.heatmap(temp_table_y, linewidths=0.5, annot=True, cmap = sns.cubehelix_palette(as_cmap=True))
hm.set_yticklabels(hm.get_yticklabels(), rotation=0)

plt.title("TF share per EF")
plt_save("Heatmap_EF_TF_T")
plt.clf()


# -#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-
# -#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-
"""HeatMap_DurationFrame_TimeFrame"""
# -#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-
# -#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-
temp_table = pd.concat([
    help_table[(help_table["score"] > 0)
               & (help_table["duration"] > 0)
               & (help_table["episodes"] > 0)
               & (help_table["TF"] == "1970-1999")].groupby("DF").size(),
    help_table[(help_table["score"] > 0)
               & (help_table["duration"] > 0)
               & (help_table["episodes"] > 0)
               & (help_table["TF"] == "2000-2014")].groupby("DF").size(),
    help_table[(help_table["score"] > 0)
               & (help_table["duration"] > 0)
               & (help_table["episodes"] > 0)
               & (help_table["TF"] == "2015-2024")].groupby("DF").size()
],axis=1)

temp_table.columns = ["1970-1999","2000-2014","2015-2024"]
temp_table = temp_table.reindex(index=["< 5min",  "< 10min","< 20min", "< 30min", "< 45min", "< 60min", "< 90min","< 120min", "< 150min","< 160min", ">=160"])

# get the table but device each entry by the sum of its row:
temp_table_type = temp_table.div(temp_table.sum(axis=1), axis=0)
temp_table_type.index.name = None

plt.figure(figsize=(20, 10))
temp = sns.heatmap(temp_table_type, linewidths=0.5, annot=True, cmap = sns.cubehelix_palette(as_cmap=True))
temp.set_yticklabels(temp.get_yticklabels(), rotation=0)

plt.title("DF share per TF")
plt_save("Heatmap_DF_TF")
plt.clf()

# -#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-
temp_table_y = temp_table.transpose()
temp_table_y = temp_table_y.div(temp_table_y.sum(axis=1), axis=0)
temp_table_y.index.name = None

plt.figure(figsize=(20, 10))
hm = sns.heatmap(temp_table_y, linewidths=0.5, annot=True, cmap = sns.cubehelix_palette(as_cmap=True))
hm.set_yticklabels(hm.get_yticklabels(), rotation=0)

plt.title("TF share per DF")
plt_save("Heatmap_DF_TF_T")
plt.clf()



# -#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-
# -#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-
"""Average DURATION for each ANIME_TYPE in different TIMEFRAMES"""
# -#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-
# -#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-
temp_table = pd.concat([help_table[
                            (help_table["score"] > 0)
                            & (help_table["duration"] > 0)
                            ].groupby(["anime_type","TF"])["duration"].mean()], axis=1)
# .unstack() -> reduce index level from +1 to 1
temp_table = temp_table.unstack()

plt.figure(figsize=(20, 10))
# heat plot (not %)
hm = sns.heatmap(temp_table, linewidths=0.5, annot=True, cmap = sns.cubehelix_palette(as_cmap=True))
hm.set_yticklabels(hm.get_yticklabels(), rotation=0)

name = "Average duration per type per time frame (of scored entries with positive duration)"
plt.title(name)
plt_save("Heatmap_average_Duration_Type_TF")
plt.clf()

# -#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-
# -#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-
"""Average EPISODES for each ANIME_TYPE in different TIMEFRAMES"""
# -#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-
# -#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-
temp_table = pd.concat([help_table[
                            (help_table["score"] > 0)
                            & (help_table["duration"] > 0)
                            ].groupby(["anime_type","TF"])["episodes"].mean()], axis=1)
# .unstack() -> reduce index level from +1 to 1
temp_table = temp_table.unstack()

plt.figure(figsize=(20, 10))
# heat plot (not %)
hm = sns.heatmap(temp_table, linewidths=0.5, annot=True, cmap = sns.cubehelix_palette(as_cmap=True))
hm.set_yticklabels(hm.get_yticklabels(), rotation=0)

name = "Average episodes per type per time frame (of scored entries with positive duration)"
plt.title(name)
plt_save("Heatmap_average_Episodes_Type_TF")
plt.clf()


# -#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-
# -#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-
"""Average SCORE for each ANIME_TYPE in different TIMEFRAMES"""
# -#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-
# -#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-
temp_table = pd.concat([help_table[
                            (help_table["score"] > 0)
                            & (help_table["duration"] > 0)
                            ].groupby(["anime_type","TF"])["score"].mean()], axis=1)
# .unstack() -> reduce index level from +1 to 1
temp_table = temp_table.unstack()

plt.figure(figsize=(20, 10))
# heat plot (not %)
hm = sns.heatmap(temp_table, linewidths=0.5, annot=True, cmap = sns.cubehelix_palette(as_cmap=True))
hm.set_yticklabels(hm.get_yticklabels(), rotation=0)

name = "Average score per type per time frame (of scored entries with positive duration)"
plt.title(name)
plt_save("Heatmap_average_Score_Type_TF")
plt.clf()