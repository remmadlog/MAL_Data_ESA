import pandas as pd

import matplotlib
matplotlib.use('TkAgg',force=True)
import matplotlib.pyplot as plt



def plt_save(name):
    plt.savefig('Plots/' + name + '.png', dpi=350)
    plt.savefig('Plots/transparent_png/' + name + '.png', dpi=350, transparent=True)
    plt.savefig('Plots/SVG/' + name + '.svg', dpi=350, transparent=True)


"""
Using normalized data to get a better feel for comparison
    -- using this later
"""


# opening normalized table (years are not normalized)
table_normalized = pd.read_excel('S_1970_2024_information_by_year_normalized.xlsx')
table = pd.read_excel('S_1970_2024_information_by_year.xlsx')


# AMOUNT of TYPE & SCORE of TYPE
Amount_Score = 1
if Amount_Score:
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
    plt.figure(1)
    # plt.subplot(1, 3, 1)
    plt.plot(table["year"],table["#shows"],label="#shows")
    plt.plot(table["year"],table["#TV_Movie_OVA_Special_ONA"],label="#TV_Movie_OVA_Special_ONA")
    plt.plot(table["year"],table["#TV_OVA_ONA"],label="#TV_OVA_ONA")
    plt.plot(table["year"],table["#Movie_Special"],label="#Movie_Special")
    plt.plot(table["year"],table["#Music_CM_PV"],label="#Music_CM_PV")
    plt.plot(table["year"],table["#Rest_shows"],label="#Rest_shows")

    plt.legend(loc="upper left")

    plt.title("Amount per year (Shows - TV+ - Movie+ - Rest)")
    plt.xlabel("Years")
    plt.ylabel("Amount")
    plt.grid(linestyle = '--', linewidth = 0.5)

    plt_save('Amount per year (Shows - TV+ - Movie+ - Rest)')



    # TV_OVA_ONA, TV_shows, OVA_shows, ONA_shows
    plt.figure(figsize=(20,10))
    plt.figure(2)
    # plt.subplot(1, 3, 2)
    plt.plot(table["year"],table["#TV_OVA_ONA"],label="#TV_OVA_ONA")
    plt.plot(table["year"],table["#TV_shows"],label="#TV")
    plt.plot(table["year"],table["#OVA_shows"],label="#OVA")
    plt.plot(table["year"],table["#ONA_shows"],label="#ONA")

    plt.legend(loc="upper left")

    plt.title("Amount per year (TV - OVA - ONA)")
    plt.xlabel("Years")
    plt.ylabel("Amount")
    plt.grid(linestyle = '--', linewidth = 0.5)

    plt_save('Amount per year (TV - OVA - ONA)')


    #   # Movie_Special, #Movie_shows, #Special_shows
    plt.figure(figsize=(20,10))
    plt.figure(3)
    # plt.subplot(1, 3, 3)
    plt.plot(table["year"],table["#Movie_Special"],label="#Movie_Special")
    plt.plot(table["year"],table["#Movie_shows"],label="#Movie")
    plt.plot(table["year"],table["#Special_shows"],label="#Special")

    plt.legend(loc="upper left")

    plt.title("Amount per year (Movie - Special)")
    plt.xlabel("Years")
    plt.ylabel("Amount")
    plt.grid(linestyle = '--', linewidth = 0.5)

    plt_save('Amount per year (Movie - Special)')




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
    plt.figure(4)
    # plt.subplot(3, 1, 1)
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
    plt_save(title)


    # MIN by TYPE
    plt.figure(figsize=(20,10))
    plt.figure(5)
    # plt.subplot(3, 1, 2)
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
    plt_save(title)


    # MAX by TYPE
    plt.figure(figsize=(20,10))
    plt.figure(6)
    # plt.subplot(3, 1, 3)
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
    plt_save(title)



    # SCORES
    """Plot of Mean, Min and Max for TYPE: 1. MEAN // 2. MIN // 3. MAX"""
    #   columns:
    #       "TV_score_mean", "OVA_score_mean", "ONA_score_mean", "Movie_score_mean", "Special_score_mean",
    #       "TV_score_min", "OVA_score_min", "ONA_score_min", "Movie_score_min", "Special_score_min",
    #       "TV_score_max", "OVA_score_max", "ONA_score_max", "Movie_score_max", "Special_score_max"


    # MEAN by TYPE
    plt.figure(figsize=(20,10))
    plt.figure(7)
    # plt.subplot(3, 1, 1)
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
    plt_save(title)


    # MIN by TYPE
    plt.figure(figsize=(20,10))
    plt.figure(8)
    # plt.subplot(3, 1, 2)
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
    plt_save(title)


    # MAX by TYPE
    plt.figure(figsize=(20,10))
    plt.figure(9)
    # plt.subplot(3, 1, 3)
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
    plt_save(title)





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
    plt.figure(10)

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
    plt_save(title)


    # TV+ and Movie+
    plt.figure(figsize=(20,10))
    plt.figure(11)

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
    plt_save(title)


    # TV+
    plt.figure(figsize=(20,10))
    plt.figure(12)

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
    plt_save(title)


    # Movie+
    plt.figure(figsize=(20,10))
    plt.figure(13)

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
    plt_save(title)


    # Music+
    plt.figure(figsize=(20,10))
    plt.figure(14)

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
    plt_save(title)


    # TV
    plt.figure(figsize=(20,10))
    plt.figure(15)

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
    plt_save(title)


    # OVA
    plt.figure(figsize=(20,10))
    plt.figure(16)

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
    plt_save(title)


    # ONA
    plt.figure(figsize=(20,10))
    plt.figure(17)

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
    plt_save(title)


    # Movie
    plt.figure(figsize=(20,10))
    plt.figure(18)

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
    plt_save(title)


    # Special
    plt.figure(figsize=(20,10))
    plt.figure(19)

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
    plt_save(title)

