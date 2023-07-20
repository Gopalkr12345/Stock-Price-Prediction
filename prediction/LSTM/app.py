import numpy as np
import pandas as pd
import pandas_datareader as data
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler
from keras.models import load_model
plt.style.use('bmh')
import streamlit as st




st.title('STOCK PRICE PREDICTION  BASED ON MULTIPLE DATA SOURCES')
user_input = st.text_input('Enter The Stock Ticker', 'AAPL')
start = '2001-01-01'
end = '2022-10-10'
df = data.DataReader(user_input,'yahoo',start,end)
#set the date as the index
# df = df.set_index(data.DatetimeIndex(df['Date'].values))

#describing data
if st.checkbox("Show raw data", False):
    st.subheader('Raw Data From 2001-2022')
    st.write(df)
    st.subheader('Described Raw data')
    st.write(df.describe())

# df.shape


# LSTM
st.write(' ')
st.write(' ')

# VISU
st.subheader('Closing Price vs Time Chart')
fig = plt.figure(figsize=(12, 6))
plt.plot(df.Close)
plt.xlabel('Year-Month')
plt.ylabel('Close Price USD ($)')
plt.legend(['Original Close price'])
st.pyplot(fig)




#100ma vs closeprice
st.subheader('Closing Price vs Time Chart With 100MA')
ma100 = df.Close.rolling(100).mean()
fig = plt.figure(figsize=(12, 6))
plt.xlabel('Year-Month')
plt.ylabel('Close Price USD ($)')
plt.plot(df.Close)
plt.plot(ma100)
plt.legend(['Original Close Price','100Days Moving Average'])
st.pyplot(fig)




#100ma+200ma+closeprice
st.subheader('Closing Price vs Time Chart With 100MA & 200mMA')
ma100 = df.Close.rolling(100).mean()
ma200 = df.Close.rolling(200).mean()
fig = plt.figure(figsize=(12, 6))
plt.xlabel('Year-Month')
plt.ylabel('Close Price USD ($)')
plt.plot(df.Close, 'b')
plt.plot(ma100, 'r')
plt.plot(ma200, 'g')

plt.legend(['Original Close Price','100Days Moving Average','200Days Moving Average'])
st.pyplot(fig)

# spliting data into tarining and testing
data_training = pd.DataFrame(df['Close'][0:int(len(df)*0.70)])
data_testing = pd.DataFrame(df['Close'][int(len(df)*0.70): int(len(df))])

scaler = MinMaxScaler(feature_range=(0, 1))

data_training_array = scaler.fit_transform(data_training)

# spliting the data

# load my model
model = load_model('keras_model.h5')

# testing part
past_100_days = data_training.tail(100)
final_df = past_100_days.append(data_testing, ignore_index=True)
input_data = scaler.fit_transform(final_df)

x_test = []
y_test = []
for i in range(100, input_data.shape[0]):
    x_test.append(input_data[i-100:i])
    y_test.append(input_data[i, 0])
x_test, y_test = np.array(x_test), np.array(y_test)

# making prediction
y_predicted = model.predict(x_test)
scaler = scaler.scale_
scale_factor = 1/scaler[0]
y_predicted = y_predicted * scale_factor
y_test = y_test * scale_factor

# final graph
st.subheader('Prediction vs Original')
fig2 = plt.figure(figsize=(12, 6))
plt.plot(y_test, 'b', label='Original Price')
plt.plot(y_predicted, 'r', label='predicted Price')
plt.xlabel('Time')
plt.ylabel('Close Price USD ($)')
plt.legend()
st.pyplot(fig2)





