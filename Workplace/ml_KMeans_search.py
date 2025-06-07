"""
Using several different feature sets to determent which set and which amount of clusters provide an exceptable silhouette score for ``KMeans``.

Files obtained using ml_KMeans_search.py.
"""

# importing
from module_ml import *

import time


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#: for timing
start = time.time()
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
step = time.time()


#: loading files to test
#+ + + + + + + + + + + + + + + + + +
df_full = pd.read_csv('created_files/training_full_set.csv')
df_Full_ica = pd.read_csv('created_files/unsupervised_fs/df_Full_ica.csv')
df_Full_pca = pd.read_csv('created_files/unsupervised_fs/df_Full_pca.csv')
df_Full_reduced = pd.read_csv('created_files/unsupervised_fs/df_Full_reduced.csv')


df_pred_int = pd.read_csv("created_files/training_score/selection_arranged_intersection.csv")
df_pred_union = pd.read_csv("created_files/training_score/selection_arranged_union.csv")

#+ + + + + + + + + + + + + + + + + +
df_part_OnList = pd.read_csv('created_files/training_partial_set_OnList.csv')

#+ + + + + + + + + + + + + + + + + +
df_BH = pd.read_csv("created_files/unsupervised_fs/df_ByHand.csv")
df_BH_red = pd.read_csv("created_files/unsupervised_fs/df_ByHand_reduced.csv")
df_BH_enc = pd.read_csv("created_files/unsupervised_fs/df_ByHandRed_encoder.csv")
df_BH_fa = pd.read_csv("created_files/unsupervised_fs/df_ByHandRed_fa.csv")
df_BH_ica = pd.read_csv("created_files/unsupervised_fs/df_ByHandRed_ica.csv")
df_BH_pca = pd.read_csv("created_files/unsupervised_fs/df_ByHandRed_pca.csv")
df_BH_tsne = pd.read_csv("created_files/unsupervised_fs/df_ByHandRed_tsne.csv")

#+ + + + + + + + + + + + + + + + + +
df_ByHand_25_encoder = pd.read_csv("created_files/unsupervised_fs/df_ByHand_25_encoder.csv")
df_ByHand_25_fa = pd.read_csv("created_files/unsupervised_fs/df_ByHand_25_fa.csv")
df_ByHand_25_ica = pd.read_csv("created_files/unsupervised_fs/df_ByHand_25_ica.csv")
df_ByHand_25_pca = pd.read_csv("created_files/unsupervised_fs/df_ByHand_25_pca.csv")
df_ByHand_25_reduced = pd.read_csv("created_files/unsupervised_fs/df_ByHand_25_reduced.csv")
df_ByHand_25_tsne = pd.read_csv("created_files/unsupervised_fs/df_ByHand_25_tsne.csv")

#+ + + + + + + + + + + + + + + + + +
df_ByHand_10_encoder = pd.read_csv("created_files/unsupervised_fs/df_ByHand_10_encoder.csv")
df_ByHand_10_fa = pd.read_csv("created_files/unsupervised_fs/df_ByHand_10_fa.csv")
df_ByHand_10_ica = pd.read_csv("created_files/unsupervised_fs/df_ByHand_10_ica.csv")
df_ByHand_10_pca = pd.read_csv("created_files/unsupervised_fs/df_ByHand_10_pca.csv")
df_ByHand_10_reduced = pd.read_csv("created_files/unsupervised_fs/df_ByHand_10_reduced.csv")
df_ByHand_10_tsne = pd.read_csv("created_files/unsupervised_fs/df_ByHand_10_tsne.csv")


#: Transforming/preparing files
X_full = df_full.drop(['anime_id'], axis=1)
X_Full_ica = df_Full_ica.drop(['anime_id'], axis=1)
X_Full_pca = df_Full_pca.drop(['anime_id'], axis=1)
X_Full_reduced = df_Full_reduced.drop(['anime_id'], axis=1)


X_pred_int = df_pred_int.drop(['anime_id'], axis=1)
X_pred_union = df_pred_union.drop(['anime_id'], axis=1)

#+ + + + + + + + + + + + + + + + + +
X_part_OnList = df_part_OnList.drop(['anime_id'], axis=1)

#+ + + + + + + + + + + + + + + + + +
X_BH = df_BH.drop(['anime_id'], axis=1)
X_BH_red = df_BH_red.drop(['anime_id'], axis=1)
X_BH_enc = df_BH_enc.drop(['anime_id'], axis=1)
X_BH_fa = df_BH_fa.drop(['anime_id'], axis=1)
X_BH_ica = df_BH_ica.drop(['anime_id'], axis=1)
X_BH_pca = df_BH_pca.drop(['anime_id'], axis=1)
X_BH_tsne= df_BH_tsne.drop(['anime_id'], axis=1)

#+ + + + + + + + + + + + + + + + + +
X_ByHand_25_encoder = df_ByHand_25_encoder.drop(['anime_id'], axis=1)
X_ByHand_25_fa = df_ByHand_25_fa.drop(['anime_id'], axis=1)
X_ByHand_25_ica = df_ByHand_25_ica.drop(['anime_id'], axis=1)
X_ByHand_25_pca = df_ByHand_25_pca.drop(['anime_id'], axis=1)
X_ByHand_25_reduced = df_ByHand_25_reduced.drop(['anime_id'], axis=1)
X_ByHand_25_tsne = df_ByHand_25_tsne.drop(['anime_id'], axis=1)

#+ + + + + + + + + + + + + + + + + +
X_ByHand_10_encoder = df_ByHand_10_encoder.drop(['anime_id'], axis=1)
X_ByHand_10_fa = df_ByHand_10_fa.drop(['anime_id'], axis=1)
X_ByHand_10_ica = df_ByHand_10_ica.drop(['anime_id'], axis=1)
X_ByHand_10_pca = df_ByHand_10_pca.drop(['anime_id'], axis=1)
X_ByHand_10_reduced = df_ByHand_10_reduced.drop(['anime_id'], axis=1)
X_ByHand_10_tsne = df_ByHand_10_tsne.drop(['anime_id'], axis=1)

#: Lists of datasets and their names
datasets = [X_full, X_Full_ica, X_Full_pca, X_Full_reduced, X_pred_int, X_pred_union, X_part_OnList, X_BH, X_BH_red, X_BH_enc, X_BH_fa, X_BH_ica, X_BH_pca, X_BH_tsne, X_ByHand_25_encoder, X_ByHand_25_fa, X_ByHand_25_ica, X_ByHand_25_pca, X_ByHand_25_reduced, X_ByHand_25_tsne, X_ByHand_10_encoder, X_ByHand_10_fa, X_ByHand_10_ica, X_ByHand_10_pca, X_ByHand_10_reduced, X_ByHand_10_tsne]
# get variable names:
var_names = ["X_Full", "X_Full_ica", "X_Full_pca", "X_Full_reduced", "X_pred_int", "X_pred_union", "X_part_OnList", "X_BH", "X_BH_red", "X_BH_enc", "X_BH_fa", "X_BH_ica", "X_BH_pca", "X_BH_tsne", "X_ByHand_25_encoder", "X_ByHand_25_fa", "X_ByHand_25_ica", "X_ByHand_25_pca", "X_ByHand_25_reduced", "X_ByHand_25_tsne", "X_ByHand_10_encoder", "X_ByHand_10_fa", "X_ByHand_10_ica", "X_ByHand_10_pca", "X_ByHand_10_reduced", "X_ByHand_10_tsne"]


#+ + + + + + + + + + + + + + + + + +
now = time.time()
print("Execution time preparation: ",now-step)


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
col_names= ["cluster", "score"]

df_print = pd.DataFrame([], columns=col_names)

#: Iterating over datasets and names
for X, var_name in zip(datasets,var_names):
    # + + + + + + + + + + + + + + + + + + + + +
    step = time.time()

    # + + + + + + + + + + + + + + + + + + + + +
    help_y = 0
    try:
        X = X.drop(['year'], axis=1)
        help_y = 1
    except:
        pass

    # + + + + + + + + + + + + + + + + + + + + +
    if help_y==1:
        kmean_res = kmeans_search(X,range(2,11))

        data = kmean_res[1:]
        df_kmeans = pd.DataFrame(data, columns=col_names)
        df_kmeans.loc[:, 'set'] = var_name+"_NoYear"

        df_print = pd.concat([df_print,df_kmeans])

    # + + + + + + + + + + + + + + + + + + + + +
    now = time.time()
    print(var_name,"NoYear")
    print("     Execution time KMeans: ",now-step)


    # + + + + + + + + + + + + + + + + + + + + +
    step = time.time()

    # + + + + + + + + + + + + + + + + + + + + +
    kmean_res = kmeans_search(X,range(2,11))

    data = kmean_res[1:]
    df_kmeans = pd.DataFrame(data, columns=col_names)
    df_kmeans.loc[:, 'set'] = var_name

    df_print = pd.concat([df_print,df_kmeans])

    # + + + + + + + + + + + + + + + + + + + + +
    now = time.time()
    print(var_name)
    print("     Execution time KMeans: ",now-step)



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#: Saving
with open("created_files/unsupervised_fs/KMeans_Search_Output.txt", "a") as f:
    f.write(df_print.to_markdown(index=False))
    f.write("\n\n")

df_print.to_csv("created_files/unsupervised_fs/KMeans_Search_Output.csv", index=False)
