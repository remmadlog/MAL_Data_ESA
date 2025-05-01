"""
Here we are merging table_main and table_SGT in two ways
- similar to how SGT is build: anime_id in not unique
- - just joining with main (how = "outer" if you don't want to pay attention to the order)
- transferring table_SGT such that all studio for on anime_id are written in one cell (genre and theme respectively)
- - then joining with table_main  (we do this for each item (studio, genre, theme) separately, see below
"""
import pandas as pd
import numpy as np


table_main = pd.read_excel('xlsx_tables/Season_1970_2024_main.xlsx')
# table_main.heads()
# # anime_id	approved	title	anime_type	source	episodes	status	airing	start	end	duration	rating	score	scored_by
# # rank	popularity	on_list	favorites	synopsis	season	year	broadcast_day	broadcast_time	#studios involved	#genres	#themes

table_SGT = pd.read_excel('xlsx_tables/Season_1970_2024_SGT.xlsx')
# table_SGT.head()
# # anime_id    studio  genre   theme


"""
create two tables
- main+SGT multiple lines per id as in SGT
- main+SGT one line per id
"""
# get rid on NaN
table_sgt = table_SGT.fillna(0)
# drope duplicate rows
table_sgt = table_sgt.drop_duplicates()

# main+SGT multiple lines per id as in SGT
table_merged = pd.merge(table_sgt, table_main,on="anime_id")


# main+SGT one line per id
table_merged_unique = table_main
# # we do this for studio, theme and genre one by one
for item in ["studio", "genre", "theme"]:
    # only get id and item column
    table_temp = table_sgt[["anime_id",item]]
    # remove 0 entries in for item
    # # ! Not every anime_id has a studio entry != 0
    table_temp = table_temp[table_temp[item] != 0]
    # wirte all [item] on anime_id [id] in one cell (split the list with ",": column(item1,item2) -> [item1, item2] -> item1, item2
    table_temp = table_temp.groupby("anime_id").aggregate(lambda x: ",".join(list(x))).reset_index()
    # merge tables on anime_id
    # # OUTER join so we get all ids even if we don't have an entry for [item]
    # # # could change the order of the merge and use inner join, but I like the order (easier to keep track of what's happening while coding)
    table_merged_unique = pd.merge(table_temp, table_merged_unique,on="anime_id",  how='outer')


# saving both tables
# # using index=False so we do not save the index column
table_merged.to_excel("xlsx_tables/S_1970_2024_merged.xlsx", index=False)
table_merged_unique.to_excel("xlsx_tables/S_1970_2024_merged_unique.xlsx", index=False)

