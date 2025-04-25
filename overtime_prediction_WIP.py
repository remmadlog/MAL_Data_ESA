"""
This WAS ment to be a short using of the ARIMA algorithm in order to predict next seasons amount of TV show, average of episodes or duration, but
- my r2 values are always negative
- the prediction is off (no surprise)
- parameter search did not help

Here are some results:
- I get this in the parameter search when target it av_suration and i print the r2 values with absolute value smaller 1
- mean also not looking grate
- need more time to investigate this
- maybe ARIMA is the WRONG choose here?
    [np.float64(-0.639014194271452), np.float64(1.3955086017897294), 0, 1, 1]
    [np.float64(-0.9034109081929704), np.float64(1.3797503196041254), 0, 1, 2]
    [np.float64(-0.7818832441099284), np.float64(1.4948778295901797), 0, 3, 3]
    [np.float64(-0.7429334652980886), np.float64(1.2643335371997377), 0, 4, 4]
    [np.float64(-0.6362814142529218), np.float64(1.434242538786279), 1, 1, 0]
    [np.float64(-0.49718097001365097), np.float64(1.3251042053158277), 1, 1, 1]
    [np.float64(-0.7835297441644201), np.float64(1.4553866475978068), 1, 1, 2]
    [np.float64(-0.8702410517961163), np.float64(1.4408847060850385), 1, 1, 3]
    [np.float64(-0.6276596815913497), np.float64(1.4412997269786239), 1, 2, 1]
    [np.float64(-0.9825119450934396), np.float64(1.5835540654701967), 1, 4, 5]
    [np.float64(-0.23378922695291635), np.float64(1.2180610749234995), 1, 5, 6]
    [np.float64(-0.4887056698228286), np.float64(1.4273407306437156), 2, 1, 0]
    [np.float64(-0.7708889149586345), np.float64(1.3792918851693812), 2, 1, 1]
    [np.float64(-0.7751245000053936), np.float64(1.451573180211817), 2, 1, 2]
    [np.float64(-0.46234096876742425), np.float64(1.4139654393470404), 2, 2, 1]
"""

import numpy as np
import pandas as pd

from sklearn import preprocessing
from statsmodels.tsa.arima.model import ARIMA
from sklearn.metrics import mean_absolute_error
from sklearn.metrics import r2_score

import warnings

import matplotlib
import matplotlib.pyplot as plt
matplotlib.use('TkAgg',force=True)

warnings.filterwarnings("ignore")
print("Be aware: you are ignoring filterwarnings")





def create_dataset(table_main):

    # set help table to not change table_main
    help_table = table_main

    # to consider quarter instead of season (numeric order, easier to handle), set quarter as a feature using np.where
    help_table["quarter"] = np.where(help_table["season"]=="winter", 1,
                            np.where(help_table["season"]=="spring", 2,
                            np.where(help_table["season"]=="summer", 3,
                            np.where(help_table["season"]=="fall", 4, 0))))

    # only consider entries that have a score
    help_table = help_table[(help_table["score"] > 0) & (help_table["duration"] > 0)]


    # get a table that we use for predicting averages for next seasons
    temp_table_mean = help_table.groupby(["year","quarter"]).agg({
        "duration": "mean",
        "episodes": "mean",
        "score":"mean",
        "scored_by":"mean",
        "rank":"mean",
        "popularity":"mean",
        "on_list":"mean",
        "favorites":"mean"
    })

    # let's name the columns
    temp_table_mean.columns = ["av_duration", "av_episodes", "av_score", "av_scoredby", "av_rank", "av_popularity", "av_onlist", "av_favorites"]

    # get table with entrie amount per type
    type_list = ["Movie", "Music", "ONA", "OVA", "PV", "Special", "TV", "TV Special"]
    temp_table_size = pd.concat([
        help_table[help_table["anime_type"] == "CM"].groupby(["year","quarter"])["anime_id"].size()
    ], axis=1)
    for item in type_list:
        temp_table_size = pd.concat([
            temp_table_size,
            help_table[help_table["anime_type"] == item].groupby(["year", "quarter"])["anime_id"].size()
        ], axis=1)

    # sorting so we have 1970,1,2,3,4...
    temp_table_size = temp_table_size.sort_index()

    # let's name the columns
    temp_table_size.columns = ["total_CM", "total_Movie", "total_Music", "total_ONA", "total_OVA", "total_PV", "total_Special", "total_TV", "total_TV_Special"]

    # combining both tables
    training_table = temp_table_size = pd.concat([
    temp_table_mean,temp_table_size
    ], axis=1)

    # index is 2 level multiindex -> get the index and combine them
    temp = training_table.index.map('{0[0]}/{0[1]}'.format)
    # adding a row year/quarter
    training_table["year_quarter"] = temp

    # move column from last to first
    # get column names
    col = training_table.columns.tolist()
    # move last item to first position in list
    col = col[-1:] + col[:-1]
    # push changes onto the table
    training_table = training_table[col]

    # save table for now
    training_table.to_excel("xlsx_tables/training_yearly.xlsx")
    print("Saved dataset as: training_yearly.xlsx")


# scoring of the modle -- how good/bad is the r2 value
def interpretation(scorevalue):
    if scorevalue < 0.6:
        return("trash")
    elif scorevalue >= 0.6 and scorevalue < 0.7:
        return("worthlss")
    elif scorevalue >= 0.7 and scorevalue < 0.8:
        return("bad")
    elif scorevalue >= 0.8 and scorevalue < 0.9:
        return ("good")
    elif scorevalue >= 0.9 and scorevalue < 1:
        return("very good")
    else:
        return("perfect")

# cross validation for scoring -- how good/bad are our parameters
def corssval(dft, col, fold = 5, forcast = 4, p=0,d=0,q=0, PRINT=0):
    r2 = []
    mea = []
    train_data_count = []
    if fold * forcast > len(dft):
        print("reduce folds or forcast!")
    else:
        for f in range(fold):
            try:
                # creating folds for cross validation
                train_test_data, rest_data = np.split(dft,[len(dft)- forcast * (fold - f - 1)])
                train_data, test_data = np.split(train_test_data,[len(train_test_data)- forcast])

                # training of the ARIMA model
                # order -- are parameters, they can be changed, and they have an impact of the r2 value
                model = ARIMA(train_data[col],order=(p,d,q))
                model_fit = model.fit()

                # prediction on test_data
                # steps -- numbers of prediction steps: steps=4 -> get 4 next values
                y_pred = model_fit.get_forecast(steps=forcast)
                y_pred_series = pd.Series(y_pred.predicted_mean,index=test_data.index)

                # calculate evaluation metric
                r2.append(r2_score(test_data[col],y_pred_series))
                mea.append(mean_absolute_error(test_data[col],y_pred_series))
                train_data_count.append(len(train_data))
            except:
                # in case something went out of range
                pass

        # get an overall r2 and abs_error
        r2_exact = np.average(r2,weights= train_data_count)
        mea_exact = np.average(mea, weights=train_data_count)

        # maybe one or two digits are enough
        R2 = round(r2_exact,2)
        MAE = round(mea_exact, 1)
        if PRINT == 1:
            print("Result of cross validation:")
            print("      Arithmetic mean (weights -> average) for R2:", R2)
            print("      Arithmetic mean (weights -> average) for MAE:", MAE)
            print("      Interpretation: Regression model with", interpretation(R2), "structure.")
        return [r2_exact,mea_exact]


# parameter search fpr good choices of p, d, and q
def search_pdq(dft,col, fold=5, forcast=12):
    # range fpr pdq
    min_p = 0
    max_p = 8
    min_d = 0
    max_d = 5
    min_q = 0
    max_q = 6

    # initiate values -- estimated
    opt_p = 1
    opt_d = 2
    opt_q = 2
    opt_r2 = 0
    opt_mae = 0

    # keep track of all the parameters -> r2_mae_pdq_list = [[r2, mean_error, p,d,q]]
    r2_mae_pdq_list = []

    for i in range(min_p,max_p+1):
        for j in range(min_d, max_d+1):
            for k in range(min_q, max_q+1):
                r2_mae_list = corssval(dft,col, fold=5, forcast=4, p=i, d=j, q=k, PRINT=0)
                r2_mae_pdq_list.append(r2_mae_list + [i,j,k])
                if r2_mae_list[0] > opt_r2:
                    opt_r2 = r2_mae_list[0]
                    opt_mae = r2_mae_list[1]
                    opt_p = i
                    opt_d = j
                    opt_q = k
    # print "optimal" results
    print("Optimal results:")
    print("     R2:", opt_r2)
    print("     MAE:", opt_mae)
    print("     p:", opt_p)
    print("     d:", opt_d)
    print("     q:", opt_q)
    return r2_mae_pdq_list


# use for prediction
def pred(dft,forcast = 4, order=(0,0,0)):
    model = ARIMA(dft["PASSAGIERE"], order=order)
    model_fit = model.fit()
    y_pred = model_fit.forecast(steps=forcast)
    return y_pred



# load table
table_main = pd.read_excel('Season_1970_2024_main.xlsx')
"""
Columns of table_main:
    'anime_id', 'approved', 'title', 'anime_type', 'source', 'episodes',
    'status', 'airing', 'start', 'end', 'duration', 'rating', 'score',
    'scored_by', 'rank', 'popularity', 'on_list', 'favorites', 'synopsis',
    'season', 'year', 'broadcast_day', 'broadcast_time',
    '#studios involved', '#genres', '#themes'
"""

# create data (will be saved)   --  uncomment if you need to create
# create_dataset(table_main)




# load data that we just created
dft = pd.read_excel('training_yearly.xlsx')

# get the needed columns
alldata = dft[["year_quarter","av_duration"]]

# remove last x rows
dataset = dft[["year_quarter","av_duration"]]
dataset.drop(dataset.tail(4).index,inplace=True)

# only keep last x rows
testset = dft[["year_quarter","av_duration"]]
testset.drop(testset.head(-4).index,inplace=True)


# get good parameter (in theorie)
# r2_mae_pdq_list = search_pdq(dataset,"av_duration", fold=3, forcast=4)


# use parameters (order) to train the model
model = ARIMA(dataset["av_duration"], order=(2,2,1))
model_fit = model.fit()

# get a prediction based on the training date provided
y_pred = model_fit.forecast(steps=4)

# renaming the index of the prediction so we can plot it
# index before 1,2,3,4
# index after len(alldata)-3, len(alldata)-2, len(alldata)-1, len(alldata)
y_pred.index = testset.index

# plotting the date and put the prediction in red on top
plt.plot(alldata.index, alldata["av_duration"])
plt.plot(y_pred,"r")

# shot the plot
plt.show()


