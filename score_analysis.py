"""
In this file we are going to create plots for the analysis of score
We are mainly going to create barplots and heatmaps
We also provide a few tables

Nothing major here, just the usual creating of DataFrames and plotting.


PROBLEMS/QUESTIONS:
- sns.set(font_scale=.75)
- - I thought this is ment to scale to font of labels for the heatmaps in import seaborn as sns
- - it has an impact on the looks of the barh plots
- - - WHY
- - it scales things differently
- - - somtimes the font is smaller even though the heatmap/plot was created in the same for loop
- - todo: what is happening
"""

import pandas as pd
import numpy as np
import seaborn as sns
from datetime import datetime
from sklearn import preprocessing
import matplotlib


matplotlib.use('TkAgg',force=True)
import matplotlib.pyplot as plt



def plt_save(name):
    plt.savefig('Plots/score/' + name + '.png', dpi=350)
    plt.savefig('Plots/score/transparent_png/' + name + '.png', dpi=350, transparent=True)
    plt.savefig('Plots/score/SVG/' + name + '.svg', dpi=350, transparent=True)

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
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# preparations
dfm = pd.read_excel('xlsx_tables/S_1970_2024_merged.xlsx').fillna(0)
dfmu = pd.read_excel('xlsx_tables/S_1970_2024_merged_unique.xlsx').fillna(0)

# reset file
with open("score_table_markdowns.txt", "w") as f:
    f.close()

# prepare loaded tables:
# we usually only consider entries that have scores:
dfm = dfm[dfm["score"]>0]
dfmu = dfmu[dfmu["score"]>0]

# in addition, we should only consider entries that are NOT airing currently
# # we do this episode amount and duration per episode is very unclear (sometimes just 0)
dfm = dfm[dfm["status"] == "Finished Airing"]
dfmu = dfmu[dfmu["status"] == "Finished Airing"]
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
for table in [dfm, dfmu]:
    table["TF"] = np.where(
        table["year"] < 2000, "1970-1999", np.where(
            table["year"] < 2015, "2000-2014", np.where(
                table["year"] < 2025, "2015-2024", "2025")
        )
    )
    table["DF"] = np.where(
        table["duration"] < 5, "< 005min", np.where(
            table["duration"] < 10, "< 010min", np.where(
                table["duration"] < 20, "< 020min", np.where(
                    table["duration"] < 30, "< 030min", np.where(
                        table["duration"] < 45, "< 045min", np.where(
                            table["duration"] < 60, "< 060min", np.where(
                                table["duration"] < 90, "< 090min", np.where(
                                    table["duration"] < 120, "< 120min", np.where(
                                        table["duration"] < 150, "< 150min", np.where(
                                            table["duration"] < 160, "< 160min", ">= 160min")
                                    )
                                )
                            )
                        )
                    )
                )
            )
        )
    )
    table["EF"] = np.where(
        table["episodes"] < 4, "< 004 Ep", np.where(
            table["episodes"] < 10, "< 010 Ep", np.where(
                table["episodes"] < 14, "< 014 Ep", np.where(
                    table["episodes"] < 21, "< 021 Ep", np.where(
                        table["episodes"] < 25, "< 025 Ep", np.where(
                            table["episodes"] < 60, "< 060 Ep", np.where(
                                table["episodes"] < 100, "< 100 Ep", np.where(
                                    table["episodes"] < 200, "< 200 Ep", np.where(
                                        table["episodes"] < 300, "< 300 Ep", np.where(
                                            table["episodes"] < 500, "< 500 Ep", ">= 500 Ep")
                                    )
                                )
                            )
                        )
                    )
                )
            )
        )
    )

# Add rounded times to dfm
df_temp = dfmu
times_rounded = []
for item in dfmu["broadcast_time"].fillna(0):
    if item:
        x = datetime.strptime(str(item), "%H:%M")
        hh = x.hour
        mm = round_to_nearest_quarter_hour(x.minute)
        if hh < 10:
            H = "0" + str(hh)
        else:
            H = str(hh)
        if mm == 0:
            M = "00"
        else:
            M = str(mm)
        times_rounded.append(H + ":" + M)
    else:
        times_rounded.append(np.nan)

dfmu["time_15"] = times_rounded
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
### score analysis
"""
- score and
- - on_list
- - favorites
- - duration
- - episodes
"""
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# CREATING NORMALIZED TABLE

df = dfmu[dfmu["score"]>0]
# features
features = ["on_list", "favorites", "scored_by", "duration", "episodes"]
# creating normalized table
# needed columns
df_n = df[features]
# normalize data to [0,1] -- each column
df_n = (df_n-df_n.min())/(df_n.max()-df_n.min())
# adding score back
df_n["score"] = df["score"]


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# scatter plot
for item in features:
    plt.figure(figsize=(20, 10))
    # this, I do NOT know why, results in very pretty bar plots!
    # also results in tiny font for the heatmaps so we have to account for that
    sns.set(font_scale=1)
    plt.scatter(df_n["score"], df_n[item])

    plt.title(item + " over score")
    plt.xlabel("score")
    plt.ylabel(item)

    # plt.show()
    plt_save("scatter_score_"+ item + "_normalized")
    plt.clf(), plt.close()



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# line plot (normal plot)
for item in features:
    # plot on_list mean per score
    df_n_plot = df_n.groupby("score")[item].mean().to_frame()

    plt.figure(figsize=(20, 10))
    # this, I do NOT know why, results in very pretty bar plots!
    # also results in tiny font for the heatmaps so we have to account for that
    sns.set(font_scale=1)
    plt.plot(df_n_plot.index, df_n_plot[item])

    plt.title("Mean " + item + "(normalized)" + " over score")
    plt.xlabel("score")
    plt.ylabel(item)

    # plt.show()
    plt_save("plt_score_"+ item  + "_normalized")
    plt.clf(), plt.close()


    # plot score mean per on_list
    df_n_plot = df_n.groupby(item)["score"].mean().to_frame()

    plt.figure(figsize=(20, 10))
    # this, I do NOT know why, results in very pretty bar plots!
    # also results in tiny font for the heatmaps so we have to account for that
    sns.set(font_scale=1)
    plt.plot(df_n_plot.index, df_n_plot["score"])

    plt.title("Mean score over " + item + "(normalized)")
    plt.ylabel("score")
    plt.xlabel(item)

    # plt.show()
    plt_save("plt_" + item + "_score_normalized")
    plt.clf(), plt.close()



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
"""
- score and
- - rating
- - source
- - type
- - DF
- - TF
- - broadcast_day
- - (broadcast_time) -- no real value
- - (time_15) -- no real value
"""
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# barplot todo: order of DF and EF is odd
# # tried to change this but atm I have to do this for each time frame that we consider and that would be ugly so not sorted it is
#    # if item == "DF":
#    #     df_temp = df.reindex(
#    #         index=["< 5min", "< 10min", "< 20min", "< 30min", "< 45min", "< 60min", "< 90min", "< 120min", "< 150min",
#    #                "< 160min", ">=160"])
#    # elif item == "EF":
#    #     df_temp = df.reindex(
#    #         index=["< 4 Ep", "< 10 Ep", "< 14 Ep", "< 21 Ep", "< 25 Ep", "< 60 Ep", "< 100 Ep", "< 200 Ep", "< 300 Ep",
#    #                "< 500 Ep", ">=500"])
#    # else:
#    #     df_temp = df.copy()
features = ["rating", "source", "anime_type", "DF","EF", "broadcast_day"]
for item in features:
    df_bar = df.groupby(item)["score"].mean().to_frame().reset_index()


    # if "0" is an entry in the item column, we get a problem in bar plot because it is not recognized as string but as a float
    # # This is on my, I created the table where df is based on, replaced NaN with 0 not with str(0) todo: maybe change this
    # to get around this
    name_list = list(df_bar[item])
    name_list_new = []
    for entry in name_list:
        name_list_new.append(str(entry))


    # TEST
    # # Lets see how this changed 1970-1999
    df_bar_1999 = df[(df["year"] < 2000)].groupby(item)["score"].mean().to_frame().reset_index()

    # if "0" is an entry in the item column, we get a problem in bar plot because it is not recognized as string but as a float
    # # This is on my, I created the table where df is based on, replaced NaN with 0 not with str(0) todo: maybe change this
    # to get around this
    name_list1 = list(df_bar_1999[item])
    name_list_new1 = []
    for entry in name_list1:
        name_list_new1.append(str(entry))


    # # Lets see how this changed 2000-2014
    df_bar_2000 = df[(df["year"]>1999) & (df["year"]<2015)].groupby(item)["score"].mean().to_frame().reset_index()

    # if "0" is an entry in the item column, we get a problem in bar plot because it is not recognized as string but as a float
    # # This is on my, I created the table where df is based on, replaced NaN with 0 not with str(0) todo: maybe change this
    # to get around this
    name_list2 = list(df_bar_2000[item])
    name_list_new2 = []
    for entry in name_list2:
        name_list_new2.append(str(entry))


    # # Lets see how this changed 2015-2024
    df_bar_2015 = df[df["year"] > 2014].groupby(item)["score"].mean().to_frame().reset_index()

    # if "0" is an entry in the item column, we get a problem in bar plot because it is not recognized as string but as a float
    # # This is on my, I created the table where df is based on, replaced NaN with 0 not with str(0) todo: maybe change this
    # to get around this
    name_list3 = list(df_bar_2015[item])
    name_list_new3 = []
    for entry in name_list3:
        name_list_new3.append(str(entry))



    plt.figure(figsize=(20, 10))
    # this, I do NOT know why, results in very pretty bar plots!
    # also results in tiny font for the heatmaps so we have to account for that
    sns.set(font_scale=1)
    plt.barh(name_list_new, df_bar["score"], color = "gray", label="1970-2024")
    plt.barh(name_list_new1, df_bar_1999["score"],  height = 0.5, color = "navy", label="1970-1999")
    plt.barh(name_list_new2,df_bar_2000["score"], height = 0.3, color = "darkgreen", label="2000-2014")
    plt.barh(name_list_new3,df_bar_2015["score"], height = 0.1, color = "yellowgreen", label="2015-2024")
    plt.xlim(5, 8.5)
    plt.legend(loc="upper right")
    plt.title("Average score per " + item)

    # plt.show()
    plt_save("bar_score_" + item + "_time")
    plt.clf(), plt.close()


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
"""
investigate the 100 highest scored entries
    'anime_type', 'source', 'rating','season', 'year', 'broadcast_day', 'broadcast_time'
    'episodes', 'duration', 'on_list', 'favorites'
    'theme', 'genre', 'studio'
"""
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
df_top = df.nlargest(100,"score")


features = ['anime_type', 'source', 'rating','season', 'year', 'broadcast_day', 'broadcast_time', 'DF', 'EF']

for item in features:
    df_top_bar = df_top.groupby(item)["score"].count().reset_index()
    df_top_bar.columns = [item,"Amount"]

    # if "0" is an entry in the item column, we get a problem in bar plot because it is not recognized as string but as a float
    # # This is on my, I created the table where df is based on, replaced NaN with 0 not with str(0) todo: maybe change this
    # to get around this
    name_list = list(df_top_bar[item])
    name_list_new = []
    for entry in name_list:
        name_list_new.append(str(entry))

    plt.figure(figsize=(20, 10))
    # this, I do NOT know why, results in very pretty bar plots!
    # also results in tiny font for the heatmaps so we have to account for that
    sns.set(font_scale=1)
    plt.barh(name_list_new, df_top_bar["Amount"])
    plt.title("Amount per  " + item + " in top 100")

    print("Amount per  " + item + " in top 100")
    print(df_top_bar.to_markdown(index=False))
    with open("score_table_markdowns.txt", "a") as f:
        f.write("Amount per  " + item + " in top 100\n")
        f.write(df_top_bar.to_markdown(index=False))
        f.write("\n\n")

    # plt.show()
    plt_save("bar_top100_" + item)
    plt.clf(), plt.close()


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# get the mean: 'episodes', 'duration', 'on_list', 'favorites'
value_list = []
for item in ['episodes', 'duration', 'on_list', 'favorites']:
    value_list.append(df_top[item].mean())
df_temp = pd.DataFrame(list(zip(['episodes', 'duration', 'on_list', 'favorites'],value_list)), columns = ["item", "average"])

print(df_temp.to_markdown(index=False))
with open("score_table_markdowns.txt", "a") as f:
    f.write("Average amount of  " + item + "\n")
    f.write(df_temp.to_markdown(index=False))
    f.write("\n\n")

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# Now we want to talk about genre, theme and studio
# # the problem is we are using dfmu as a base
# # we are going to merge:
# # # df_top = df.nlargest(100,"score")
# # # dfm
df_sgt = pd.merge(df_top[["anime_id", "score"]], dfm[['anime_id','theme', 'genre', 'studio']], on=["anime_id"])

features = ['theme', 'genre', 'studio']

for item in features:
    df_top_sgt_bar = df_sgt.groupby(item)["score"].count().reset_index()
    df_top_sgt_bar.columns = [item,"Amount"]

    # remove unknown entries
    df_top_sgt_bar = df_top_sgt_bar.drop([0])

    # if "0" is an entry in the item column, we get a problem in bar plot because it is not recognized as string but as a float
    # # This is on my, I created the table where df is based on, replaced NaN with 0 not with str(0) todo: maybe change this
    # to get around this
    name_list = list(df_top_sgt_bar[item])
    name_list_new = []
    for entry in name_list:
        name_list_new.append(str(entry))

    plt.figure(figsize=(20, 10))
    # this, I do NOT know why, results in very pretty bar plots!
    # also results in tiny font for the heatmaps so we have to account for that
    sns.set(font_scale=1)
    plt.barh(name_list_new, df_top_sgt_bar["Amount"])
    plt.title("Amount per  " + item + " in top 100 (unknown removed)")

    print("Amount per  " + item + " in top 100 (unknown removed)")
    print(df_top_sgt_bar.to_markdown(index=False))
    with open("score_table_markdowns.txt", "a") as f:
        f.write("Amount per  " + item + " in top 100 (unknown removed)\n")
        f.write(df_top_sgt_bar.to_markdown(index=False))
        f.write("\n\n")


    # plt.show()
    plt_save("bar_top100_" + item)
    plt.clf(), plt.close()












