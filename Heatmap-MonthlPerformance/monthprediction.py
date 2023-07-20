import pandas as pd
import pandas_datareader as data
from datetime import date
import matplotlib.pyplot as plt
import streamlit as st




def stockPrediction(df):
    # Create lists to store the returns of each day in that month
    Jan = []
    Feb = []
    Mar = []
    Apr = []
    May = []
    June = []
    July = []
    Aug = []
    Sept = []
    Oct = []
    Nov = []
    Dec = []

    # Create a function to get returns for each month and append it to the corresponding list
    def get_returns(month, returns):
        if month == '01':
            Jan.append(float(returns))
        elif month == '02':
            Feb.append(float(returns))
        elif month == '03':
            Mar.append(float(returns))
        elif month == '04':
            Apr.append(float(returns))
        elif month == '05':
            May.append(float(returns))
        elif month == '06':
            June.append(float(returns))
        elif month == '07':
            July.append(float(returns))
        elif month == '08':
            Aug.append(float(returns))
        elif month == '09':
            Sept.append(float(returns))
        elif month == '10':
            Oct.append(float(returns))
        elif month == '11':
            Nov.append(float(returns))
        elif month == '12':
            Dec.append(float(returns))
        else:
            print('Wrong')

    # calculate and show the daily simple returns
    DSR = df['Close'].pct_change(1)
    df['DSR'] = DSR

    # Remove first row of data from dataset
    df = df[1:]

    # create a loop to gather daily simple returns of each month from the dataset and append them to list
    for i in range(0, len(df)):
        df_date = str(df.index[i])
        df_returns = df['DSR'][i]
        df_month = df_date.split('-')[1]
        # add returns to list corresponding to month
        get_returns(df_month, df_returns)

    # create a function to average the returns of each month
    def AVG(month):
        return [sum(month) / len(month)]

    # Create new dataframe
    df_AVG = pd.DataFrame()
    # Get the average returns for each month and add the values under a new column 'AVG'
    df_AVG['AVG'] = AVG(Jan) + AVG(Feb) + AVG(Mar) + AVG(Apr) + AVG(May) + AVG(June) + AVG(July) + AVG(Aug) + AVG(
        Sept) + AVG(Oct) + AVG(Nov) + AVG(Dec)
    # set index to be the corresponding integer value of month
    df_AVG = df_AVG.set_index(df_AVG.index + 1)

    # show the average monthly returns
    df_AVG = df_AVG * 100

    # Plpot the average monthly returns
    # df_AVG.plot.bar()
    st.subheader('Monthly Performance')
    st.subheader('Axes:\nX Axis: Average monthly returns(Standardize value for all stocks) Y Axis: Months')
    st.set_option('deprecation.showPyplotGlobalUse', False)
    ab = df_AVG.plot.bar()
    st.pyplot()



def mfPrediction(df):
    # Create lists to store the returns of each day in that month
    Jan = []
    Feb = []
    Mar = []
    Apr = []
    May = []
    June = []
    July = []
    Aug = []
    Sept = []
    Oct = []
    Nov = []
    Dec = []

    # Create a function to get returns for each month and append it to the corresponding list
    def get_returns(month, returns):
        if month == '01':
            Jan.append(float(returns))
        elif month == '02':
            Feb.append(float(returns))
        elif month == '03':
            Mar.append(float(returns))
        elif month == '04':
            Apr.append(float(returns))
        elif month == '05':
            May.append(float(returns))
        elif month == '06':
            June.append(float(returns))
        elif month == '07':
            July.append(float(returns))
        elif month == '08':
            Aug.append(float(returns))
        elif month == '09':
            Sept.append(float(returns))
        elif month == '10':
            Oct.append(float(returns))
        elif month == '11':
            Nov.append(float(returns))
        elif month == '12':
            Dec.append(float(returns))
        else:
            print('Wrong')

    # calculate and show the daily simple returns
    DSR = df['Close'].pct_change(1)
    df['DSR'] = DSR

    # Remove first row of data from dataset
    df = df[1:]

    # create a loop to gather daily simple returns of each month from the dataset and append them to list
    for i in range(0, len(df)):
        df_date = str(df.index[i])
        df_returns = df['DSR'][i]
        df_month = df_date.split('-')[1]
        # add returns to list corresponding to month
        get_returns(df_month, df_returns)

    # create a function to average the returns of each month
    def AVG(month):
        return [sum(month) / len(month)]

    # Create new dataframe
    df_AVG = pd.DataFrame()
    # Get the average returns for each month and add the values under a new column 'AVG'
    df_AVG['AVG'] = AVG(Jan) + AVG(Feb) + AVG(Mar) + AVG(Apr) + AVG(May) + AVG(June) + AVG(July) + AVG(Aug) + AVG(
        Sept) + AVG(Oct) + AVG(Nov) + AVG(Dec)
    # set index to be the corresponding integer value of month
    df_AVG = df_AVG.set_index(df_AVG.index + 1)

    # show the average monthly returns
    df_AVG = df_AVG * 100

    # Plpot the average monthly returns
    # df_AVG.plot.bar()
    st.subheader('Monthly performance')
    st.set_option('deprecation.showPyplotGlobalUse', False)
    ab = df_AVG.plot.bar()
    st.pyplot()





#Load stock data
st.title('Find the Best & Worst Months for investment of Stock')
user_input = st.text_input('Enter The Stock Ticker', 'TATAPOWER.NS')
start = '2010-01-02'
df = data.DataReader(user_input,'yahoo',start,date.today())
stockPrediction(df)

#Load mf data
st.title('Find the Best & Worst Months for investment of Mutual Funds')
user_input = st.text_input('Enter The Mutual Fund Ticker', 'ICICIPRULI.NS')
start = '2010-01-02'
df1 = data.DataReader(user_input,'yahoo',start,date.today())
mfPrediction(df1)





