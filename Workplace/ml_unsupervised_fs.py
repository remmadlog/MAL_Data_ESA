"""
Main Idea

- Use different starting points to apply feature selection.
    - Full set with all the features.
    - Reduced set used for score prediction.
    - Selected set, where features were removed by hand.
- Use quick and easy methods for a fast iterative reduction.
    - Variance Selector
    - Correlation Selector
    - Entropy Selector
- Save the outcome as our first reduction file.
- Use this outcome for more time-consuming and complex feature selection methods.
    - Factor Analysis
    - Auto Encoder
    - TSNE Selector
    - PCA Selector
    - ICA Selector
- Save each outcome separately.
- Thus creating several feature sets.

Those can be than tested to see wich set fits best.
This was done in [ml_KMeans_search.py](../Workplace/ml_KMeans_search.py) to obtain a good feature set for clustering.

For more information on this see [notes_ml_clustering.md](notes_ml_clustering.md).

A brief overview of all the feature selection is given in [notes_ml_feature_selection.md](notes_ml_feature_selection.md).

For the documentation see [Documentation_module_ml.md](Documentation_module_ml.md).
"""
from module_ml import *
import time

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#: for timing
start = time.time()
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#: Main preparations: Loading, selecting, defining
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
step = time.time()

#+ + + + + + + + + + + + +
# loading file
df = pd.read_csv('created_files/training_full_set.csv').fillna(0)

#+ + + + + + + + + + + + +
#, Choose feature set _ByHand_
# selecting features by hand
#. Only consider features with more than 150 entries
# features_hand = ['anime_id', 'theme_Adult Cast', 'theme_Anthropomorphic', 'theme_CGDCT', 'theme_Detective', 'theme_Gag Humor', 'theme_Gore', 'theme_Harem', 'theme_Historical', 'theme_Idols (Female)', 'theme_Idols (Male)', 'theme_Isekai', 'theme_Iyashikei', 'theme_Mahou Shoujo', 'theme_Martial Arts', 'theme_Mecha', 'theme_Military', 'theme_Music', 'theme_Mythology', 'theme_Parody', 'theme_Psychological', 'theme_Racing', 'theme_Samurai', 'theme_School', 'theme_Space', 'theme_Strategy Game', 'theme_Super Power', 'theme_Team Sports', 'theme_Urban Fantasy', 'theme_Vampire', 'theme_Workplace', 'genre_Action', 'genre_Adventure', 'genre_Avant Garde', 'genre_Award Winning', 'genre_Boys Love', 'genre_Comedy', 'genre_Drama', 'genre_Ecchi', 'genre_Fantasy', 'genre_Hentai', 'genre_Horror', 'genre_Mystery', 'genre_Romance', 'genre_Sci-Fi', 'genre_Slice of Life', 'genre_Sports', 'genre_Supernatural', 'genre_Suspense', 'studio_A-1 Pictures', 'studio_AIC', 'studio_Bones', 'studio_J.C.Staff', 'studio_Madhouse', 'studio_Nippon Animation', 'studio_OLM', 'studio_Pierrot', 'studio_Production I.G', 'studio_Shin-Ei Animation', 'studio_Studio Deen', 'studio_Sunrise', 'studio_TMS Entertainment', 'studio_Tatsunoko Production', 'studio_Toei Animation', 'studio_Xebec', 'anime_type_CM', 'anime_type_Movie', 'anime_type_Music', 'anime_type_ONA', 'anime_type_OVA', 'anime_type_PV', 'anime_type_Special', 'anime_type_TV', 'anime_type_TV Special', 'source_4-koma manga', 'source_Game', 'source_Light novel', 'source_Manga', 'source_Mixed media', 'source_Music', 'source_Novel', 'source_Original', 'source_Other', 'source_Unknown', 'source_Visual novel', 'source_Web manga', 'rating_G - All Ages', 'rating_PG - Children', 'rating_PG-13 - Teens 13 or older', 'rating_R - 17+ (violence & profanity)', 'rating_R+ - Mild Nudity', 'rating_Rx - Hentai', 'season_fall', 'season_spring', 'season_summer', 'season_winter', 'year', 'score', 'rank', 'episodes', 'duration', 'scored_by', 'on_list', 'favorites']
#. Only consider features with more than 25 entries
# features_hand = ['anime_id', 'theme_Adult Cast', 'theme_Anthropomorphic', 'theme_CGDCT', 'theme_Childcare', 'theme_Combat Sports', 'theme_Crossdressing', 'theme_Delinquents', 'theme_Detective', 'theme_Educational', 'theme_Gag Humor', 'theme_Gore', 'theme_Harem', 'theme_High Stakes Game', 'theme_Historical', 'theme_Idols (Female)', 'theme_Idols (Male)', 'theme_Isekai', 'theme_Iyashikei', 'theme_Love Polygon', 'theme_Love Status Quo', 'theme_Magical Sex Shift', 'theme_Mahou Shoujo', 'theme_Martial Arts', 'theme_Mecha', 'theme_Medical', 'theme_Military', 'theme_Music', 'theme_Mythology', 'theme_Organized Crime', 'theme_Otaku Culture', 'theme_Parody', 'theme_Performing Arts', 'theme_Pets', 'theme_Psychological', 'theme_Racing', 'theme_Reincarnation', 'theme_Reverse Harem', 'theme_Samurai', 'theme_School', 'theme_Showbiz', 'theme_Space', 'theme_Strategy Game', 'theme_Super Power', 'theme_Survival', 'theme_Team Sports', 'theme_Time Travel', 'theme_Urban Fantasy', 'theme_Vampire', 'theme_Video Game', 'theme_Visual Arts', 'theme_Workplace', 'genre_Action', 'genre_Adventure', 'genre_Avant Garde', 'genre_Award Winning', 'genre_Boys Love', 'genre_Comedy', 'genre_Drama', 'genre_Ecchi', 'genre_Erotica', 'genre_Fantasy', 'genre_Girls Love', 'genre_Gourmet', 'genre_Hentai', 'genre_Horror', 'genre_Mystery', 'genre_Romance', 'genre_Sci-Fi', 'genre_Slice of Life', 'genre_Sports', 'genre_Supernatural', 'genre_Suspense', 'studio_8bit', 'studio_A-1 Pictures', 'studio_A.C.G.T.', 'studio_AIC', 'studio_AIC ASTA', 'studio_APPP', 'studio_AQUA ARIS', 'studio_Actas', 'studio_Ajia-do', 'studio_Anime Antenna Iinkai', 'studio_Arms', 'studio_Artland', 'studio_Asahi Production', 'studio_Ashi Productions', 'studio_Bandai Namco Pictures', 'studio_Bee Train', 'studio_Blue bread', 'studio_Bones', "studio_Brain's Base", 'studio_Bridge', 'studio_C2C', 'studio_CloverWorks', 'studio_CoMix Wave Films', 'studio_Connect', 'studio_Creators in Pack', 'studio_DLE', 'studio_Daume', 'studio_David Production', 'studio_Diomedéa', 'studio_Doga Kobo', 'studio_EMT Squared', 'studio_Fanworks', 'studio_Foch Film', 'studio_Gainax', 'studio_Gallop', 'studio_Gathering', 'studio_GoHands', 'studio_Gonzo', 'studio_Group TAC', 'studio_HAL Film Maker', 'studio_Haoliners Animation League', 'studio_Hoods Entertainment', 'studio_ILCA', 'studio_J.C.Staff', 'studio_Kamikaze Douga', 'studio_Kinema Citrus', 'studio_Knack Productions', 'studio_Kyoto Animation', 'studio_LIDENFILMS', 'studio_Lerche', 'studio_MAPPA', 'studio_Madhouse', 'studio_Magic Bus', 'studio_Manglobe', 'studio_Millepensee', 'studio_Nippon Animation', 'studio_Nomad', 'studio_OLM', 'studio_Office TakeOut', 'studio_Orange', 'studio_P.A. Works', 'studio_Passione', 'studio_Pierrot', 'studio_PoRO', 'studio_Polygon Pictures', 'studio_Production I.G', 'studio_Production IMS', 'studio_Project No.9', 'studio_Radix', 'studio_Ruo Hong Culture', 'studio_SANZIGEN', 'studio_SILVER LINK.', 'studio_Satelight', 'studio_Seven', 'studio_Seven Arcs', 'studio_Shaft', 'studio_Shin-Ei Animation', 'studio_Shirogumi', 'studio_Signal.MD', 'studio_Sparkly Key Animation Studio', 'studio_Studio 1st', 'studio_Studio 4°C', 'studio_Studio 9 Maiami', 'studio_Studio Colorido', 'studio_Studio Comet', 'studio_Studio Deen', 'studio_Studio Eromatick', 'studio_Studio Fantasia', 'studio_Studio Ghibli', 'studio_Studio Gokumi', 'studio_Studio Hibari', 'studio_Studio Jam', 'studio_Studio Kai', 'studio_Studio PuYUKAI', 'studio_Sunrise', 'studio_Suoyi Technology', 'studio_Suzuki Mirano', 'studio_SynergySP', 'studio_T-Rex', 'studio_TMS Entertainment', 'studio_TNK', 'studio_TYO Animations', 'studio_Takun Manga Box', 'studio_Tatsunoko Production', 'studio_Telecom Animation Film', 'studio_Tezuka Productions', 'studio_Toei Animation', 'studio_Tokyo Kids', 'studio_Tokyo Movie Shinsha', 'studio_Triangle Staff', 'studio_Trigger', 'studio_Triple X', 'studio_White Fox', 'studio_Wit Studio', 'studio_Xebec', 'studio_Y.O.U.C', 'studio_Yamamura Animation, Inc.', 'studio_Yumeta Company', 'studio_Zero-G', 'studio_Zexcs', 'studio_animate Film', 'studio_asread.', 'studio_feel.', 'studio_ufotable', 'anime_type_CM', 'anime_type_Movie', 'anime_type_Music', 'anime_type_ONA', 'anime_type_OVA', 'anime_type_PV', 'anime_type_Special', 'anime_type_TV', 'anime_type_TV Special', 'source_4-koma manga', 'source_Book', 'source_Card game', 'source_Game', 'source_Light novel', 'source_Manga', 'source_Mixed media', 'source_Music', 'source_Novel', 'source_Original', 'source_Other', 'source_Picture book', 'source_Unknown', 'source_Visual novel', 'source_Web manga', 'source_Web novel', 'rating_G - All Ages', 'rating_PG - Children', 'rating_PG-13 - Teens 13 or older', 'rating_R - 17+ (violence & profanity)', 'rating_R+ - Mild Nudity', 'rating_Rx - Hentai', 'season_fall', 'season_spring', 'season_summer', 'season_winter', 'year', 'score', 'rank', 'episodes', 'duration', 'scored_by', 'on_list', 'favorites']
#. Only consider features with more than 10 entries
features_hand = ['anime_id', 'theme_Adult Cast', 'theme_Anthropomorphic', 'theme_CGDCT', 'theme_Childcare', 'theme_Combat Sports', 'theme_Crossdressing', 'theme_Delinquents', 'theme_Detective', 'theme_Educational', 'theme_Gag Humor', 'theme_Gore', 'theme_Harem', 'theme_High Stakes Game', 'theme_Historical', 'theme_Idols (Female)', 'theme_Idols (Male)', 'theme_Isekai', 'theme_Iyashikei', 'theme_Love Polygon', 'theme_Love Status Quo', 'theme_Magical Sex Shift', 'theme_Mahou Shoujo', 'theme_Martial Arts', 'theme_Mecha', 'theme_Medical', 'theme_Military', 'theme_Music', 'theme_Mythology', 'theme_Organized Crime', 'theme_Otaku Culture', 'theme_Parody', 'theme_Performing Arts', 'theme_Pets', 'theme_Psychological', 'theme_Racing', 'theme_Reincarnation', 'theme_Reverse Harem', 'theme_Samurai', 'theme_School', 'theme_Showbiz', 'theme_Space', 'theme_Strategy Game', 'theme_Super Power', 'theme_Survival', 'theme_Team Sports', 'theme_Time Travel', 'theme_Urban Fantasy', 'theme_Vampire', 'theme_Video Game', 'theme_Villainess', 'theme_Visual Arts', 'theme_Workplace', 'genre_Action', 'genre_Adventure', 'genre_Avant Garde', 'genre_Award Winning', 'genre_Boys Love', 'genre_Comedy', 'genre_Drama', 'genre_Ecchi', 'genre_Erotica', 'genre_Fantasy', 'genre_Girls Love', 'genre_Gourmet', 'genre_Hentai', 'genre_Horror', 'genre_Mystery', 'genre_Romance', 'genre_Sci-Fi', 'genre_Slice of Life', 'genre_Sports', 'genre_Supernatural', 'genre_Suspense', 'studio_8bit', 'studio_A-1 Pictures', 'studio_A.C.G.T.', 'studio_AIC', 'studio_AIC ASTA', 'studio_AIC PLUS+', 'studio_AIC Spirits', 'studio_APPP', 'studio_AQUA ARIS', 'studio_AT-2', 'studio_AXsiZ', 'studio_Actas', 'studio_Ajia-do', 'studio_Anima', 'studio_Anime Antenna Iinkai', 'studio_Arms', 'studio_Artland', 'studio_Artmic', 'studio_Asahi Production', 'studio_Ascension', 'studio_Ashi Productions', 'studio_Aubec', 'studio_B.CMAY PICTURES', 'studio_Bandai Namco Pictures', 'studio_Bee Train', 'studio_Bibury Animation Studios', 'studio_Big Firebird Culture', 'studio_Blade', 'studio_Blue bread', 'studio_Bones', "studio_Brain's Base", 'studio_BreakBottle', 'studio_Bridge', 'studio_C-Station', 'studio_C2C', 'studio_CG Year', 'studio_Chaos Project', 'studio_CloverWorks', 'studio_CoMix Wave Films', 'studio_Collaboration Works', 'studio_Colored Pencil Animation', 'studio_Connect', 'studio_Creators in Pack', 'studio_CygamesPictures', 'studio_DLE', 'studio_DMM.futureworks', 'studio_DandeLion Animation Studio', 'studio_Daume', 'studio_David Production', 'studio_Diomedéa', 'studio_Doga Kobo', 'studio_Dongwoo A&E', 'studio_Dream Entertainment', 'studio_E&G Films', 'studio_EMT Squared', 'studio_ENGI', 'studio_Echoes', 'studio_Eiken', 'studio_Encourage Films', 'studio_Fanworks', 'studio_Felix Film', 'studio_Flat Studio', 'studio_Flavors Soft', 'studio_Foch Film', 'studio_Gaina', 'studio_Gainax', 'studio_Gallop', 'studio_Gathering', 'studio_Geek Toys', 'studio_GoHands', 'studio_Gonzo', 'studio_Graphinica', 'studio_Group TAC', 'studio_HAL Film Maker', 'studio_HMCH', 'studio_HOTZIPANG', 'studio_Haoliners Animation League', 'studio_Happy Elements', 'studio_Himajin Planning', 'studio_Hoods Entertainment', 'studio_ILCA', 'studio_Ijigen Tokyo', 'studio_J.C.Staff', 'studio_Kachidoki Studio', 'studio_Kamikaze Douga', 'studio_Kanaban Graphics', 'studio_Khara', 'studio_Kinema Citrus', 'studio_Kitty Film Mitaka Studio', 'studio_Knack Productions', 'studio_Kyoto Animation', 'studio_LAN Studio', 'studio_LIDENFILMS', 'studio_Lay-duce', 'studio_Lerche', 'studio_Lesprit', 'studio_L²Studio', 'studio_M.S.C', 'studio_MAPPA', 'studio_Madhouse', 'studio_Magic Bus', 'studio_Maho Film', 'studio_Majin', 'studio_Manglobe', 'studio_Marza Animation Planet', 'studio_Millepensee', 'studio_Mirai Film', 'studio_Motion Magic', 'studio_Mushi Production', 'studio_NAZ', 'studio_New Generation', 'studio_Nippon Animation', 'studio_Nomad', 'studio_Nur', 'studio_Nut', 'studio_OLM', 'studio_OLM Digital', 'studio_OTOIRO', 'studio_Office No. 8', 'studio_Office TakeOut', 'studio_Onionskin', 'studio_Orange', 'studio_Ordet', 'studio_P.A. Works', 'studio_PINE JAM', 'studio_PP Project', 'studio_Passione', 'studio_Pastel', 'studio_Peak Hunt', 'studio_Phoenix Entertainment', 'studio_Picture Magic', 'studio_Pie in the sky', 'studio_Pierrot', 'studio_Pierrot Plus', 'studio_Platinum Vision', 'studio_PoRO', 'studio_Polygon Pictures', 'studio_Production I.G', 'studio_Production IMS', 'studio_Production Reed', 'studio_Project No.9', 'studio_RG Animation Studios', 'studio_Rabbit Gate', 'studio_Radix', 'studio_Robot Communications', 'studio_Rocen', 'studio_Ruo Hong Culture', 'studio_SANZIGEN', 'studio_SILVER LINK.', 'studio_Saigo no Shudan', 'studio_Satelight', 'studio_Schoolzone', 'studio_Science SARU', 'studio_Seven', 'studio_Seven Arcs', 'studio_Seven Arcs Pictures', 'studio_Shaft', 'studio_Shin-Ei Animation', 'studio_Shinkuukan', 'studio_Shirogumi', 'studio_Shogakukan Music & Digital Entertainment', 'studio_Shuka', 'studio_Signal.MD', 'studio_Sola Digital Arts', 'studio_Sparkly Key Animation Studio', 'studio_Studio 1st', 'studio_Studio 3Hz', 'studio_Studio 4°C', 'studio_Studio 9 Maiami', 'studio_Studio A-CAT', 'studio_Studio Colorido', 'studio_Studio Comet', 'studio_Studio Deen', 'studio_Studio Eromatick', 'studio_Studio Fantasia', 'studio_Studio Ghibli', 'studio_Studio Gohan', 'studio_Studio Gokumi', 'studio_Studio Hibari', 'studio_Studio Hokiboshi', 'studio_Studio Jam', 'studio_Studio Junio', 'studio_Studio Kai', 'studio_Studio Kyuuma', 'studio_Studio Live', 'studio_Studio PuYUKAI', 'studio_Sunrise', 'studio_Suoyi Technology', 'studio_Suzuki Mirano', 'studio_SynergySP', 'studio_T-Rex', 'studio_TMS Entertainment', 'studio_TNK', 'studio_TROYCA', 'studio_TYO Animations', 'studio_Takun Manga Box', 'studio_Tatsunoko Production', 'studio_Telecom Animation Film', 'studio_Tezuka Productions', 'studio_The Answer Studio', 'studio_Toei Animation', 'studio_Tokyo Kids', 'studio_Tokyo Movie Shinsha', 'studio_Trans Arts', 'studio_Triangle Staff', 'studio_Trigger', 'studio_Trinet Entertainment', 'studio_Triple X', 'studio_Typhoon Graphics', 'studio_Vega Entertainment', 'studio_Visual 80', 'studio_W-Toon Studio', 'studio_WAO World', 'studio_Wawayu Animation', 'studio_White Fox', 'studio_Wit Studio', 'studio_Wonder Cat Animation', 'studio_Xebec', 'studio_Y.O.U.C', 'studio_Yamamura Animation, Inc.', 'studio_Yaoyorozu', 'studio_Yokohama Animation Laboratory', 'studio_Yostar Pictures', 'studio_Yumeta Company', 'studio_Zero-G', 'studio_Zexcs', 'studio_animate Film', 'studio_asread.', 'studio_dwarf', 'studio_feel.', 'studio_ufotable', 'anime_type_CM', 'anime_type_Movie', 'anime_type_Music', 'anime_type_ONA', 'anime_type_OVA', 'anime_type_PV', 'anime_type_Special', 'anime_type_TV', 'anime_type_TV Special', 'source_4-koma manga', 'source_Book', 'source_Card game', 'source_Game', 'source_Light novel', 'source_Manga', 'source_Mixed media', 'source_Music', 'source_Novel', 'source_Original', 'source_Other', 'source_Picture book', 'source_Unknown', 'source_Visual novel', 'source_Web manga', 'source_Web novel', 'rating_G - All Ages', 'rating_PG - Children', 'rating_PG-13 - Teens 13 or older', 'rating_R - 17+ (violence & profanity)', 'rating_R+ - Mild Nudity', 'rating_Rx - Hentai', 'season_fall', 'season_spring', 'season_summer', 'season_winter', 'year', 'score', 'rank', 'episodes', 'duration', 'scored_by', 'on_list', 'favorites']


#+ + + + + + + + + + + + +
X_full = df.drop(['anime_id'], axis=1)
features = X_full.columns

X_reduced = df[features_hand]
X_reduced = X_reduced.drop(['anime_id'], axis=1)

#+ + + + + + + + + + + + +
#, choose data to start with
X = X_reduced
name_param = "ByHand_10"

# X = X_full
# name_param = "Full"

X_reduced.set_index(df["anime_id"]).to_csv("created_files/unsupervised_fs/df_" + name_param + ".csv")


#+ + + + + + + + + + + + +
now = time.time()
print("Execution time preparation: ",now-step)
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#: Forward feature selection
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#:      Fastish selection methods
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#+ + + + + + + + + + + + +
step = time.time()
print("Executing correlation_selector")
features_cor = correlation_selector(X, threshold=0.9)
now = time.time()
print("     Execution time correlation_selector: ",now-step)
print("         Resulting in: " + str(len(features_cor)) + " feature.")

# Make Dataframe
df_cor = df[features_cor]


#+ + + + + + + + + + + + +
step = time.time()
print("Executing variance_threshold_selector")
features_var = variance_threshold_selector(df_cor, threshold=0.1)
now = time.time()
print("     Execution time variance_threshold_selector: ",now-step)
print("         Resulting in: " + str(len(features_var)) + " feature.")

# Make Dataframe
df_var = df[features_var]


#! Insert Laplace Score if corrected


#+ + + + + + + + + + + + +
step = time.time()
print("Executing entropy_feature_selector")
features_entropy = entropy_feature_selector(df_var, n_features=int(len(features_var) * 0.8), bins=20)
now = time.time()
print("     Execution time entropy_feature_selector: ",now-step)
print("         Resulting in: " + str(len(features_entropy)) + " feature.")

# Make Dataframe
df_entropy = df[features_entropy].set_index(df["anime_id"])


# Remember the result of the first reduction round
df_entropy.to_csv("created_files/unsupervised_fs/df_" + name_param + "_reduced.csv")

feature_1round = features_entropy
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#:      Slower selection methods -- (Reason for first feature reduction)
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#:          No clustering
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#, using the reduced df_entropy for all || one could reduce even further but ending up with around 60ish features is okay

#! 6s/it // 50s/it for larger sets (1k)
#+ + + + + + + + + + + + +
step = time.time()
print("Executing fa_selector")
features_fa = fa_selector(df_entropy, n_features=int(len(features_entropy) * 0.75), show_plot=True, n_selected_factors=0)
now = time.time()
print("Execution time fa_selector: ",now-step)
print("         Resulting in: " + str(len(features_fa)) + " feature.")

# Make Dataframe
df_fa = df[features_fa].set_index(df["anime_id"])
df_fa.to_csv("created_files/unsupervised_fs/df_" + name_param + "_fa.csv")


#! ca. 6s/it for small sets (100)
#+ + + + + + + + + + + + +
step = time.time()
print("Executing autoencoder_feature_selector")
features_encoder = autoencoder_feature_selector(df_entropy, n_features=int(len(features_entropy) * 0.75), hidden_layer_size=int(len(features_var) * 0.75))
now = time.time()
print("Execution time autoencoder_feature_selector: ",now-step)
print("         Resulting in: " + str(len(features_encoder)) + " feature.")

# Make Dataframe
df_encoder = df[features_encoder].set_index(df["anime_id"])
df_encoder.to_csv("created_files/unsupervised_fs/df_" + name_param + "_encoder.csv")


#! 50s/it
#+ + + + + + + + + + + + +
step = time.time()
print("Executing tsne_sensitivity_selector")
features_tsne = tsne_sensitivity_selector(df_entropy, n_features=int(len(features_entropy) * 0.75), perplexity=50, tsne_components=2)
now = time.time()
print("Execution time tsne_sensitivity_selector: ",now-step)
print("         Resulting in: " + str(len(features_tsne)) + " feature.")

# Make Dataframe
df_tsne = df[features_tsne].set_index(df["anime_id"])
df_tsne.to_csv("created_files/unsupervised_fs/df_" + name_param + "_tsne.csv")


#, getting dataframe as return (features are combinations here) - - - - - - - - - - - - - - - - - - - - - - - - - - - -
#! 1s
#+ + + + + + + + + + + + +
step = time.time()
print("Executing pca_selector")
df_pca = pca_selector(df_entropy, n_features=int(len(features_entropy) * 0.5)).set_index(df["anime_id"])
now = time.time()
print("Execution time pca_selector: ",now-step)
df_pca.to_csv("created_files/unsupervised_fs/df_" + name_param + "_pca.csv")


#! 10s
#+ + + + + + + + + + + + +
step = time.time()
print("Executing ica_selector")
df_ica = ica_selector(df_entropy, n_features=int(len(features_entropy) * 0.5)).set_index(df["anime_id"])
now = time.time()
print("Execution time ica_selector: ",now-step)
df_ica.to_csv("created_files/unsupervised_fs/df_" + name_param + "_ica.csv")



































