from datetime import date, datetime
import pandas as pd
import calendar
import matplotlib.pyplot as plt
import seaborn as sns;sns.set_theme()
import jugaad_data.nse as nse
import streamlit as st


st.title('STOCK HEATMAP')
nifty = nse.index_df(symbol="NIFTY 50", from_date=date(2000,1,1), to_date=datetime.now().date())
nifty['M'] = nifty['HistoricalDate'].dt.month
nifty['Y'] = nifty['HistoricalDate'].dt.year
# print(nifty)

nifty.sort_values('HistoricalDate', inplace=True)
nifty.reset_index(drop=True, inplace=True)

nifty.set_index('HistoricalDate', inplace=True)

nifty_monthly = nifty.resample("M").last()

nifty_monthly['Returns'] = (nifty_monthly['CLOSE'] - nifty_monthly['CLOSE'].shift(1))*100/nifty_monthly['CLOSE'].shift(1)
# print(nifty_monthly)

heatmap_ret = pd.pivot_table(nifty_monthly, index='Y', columns='M', values=['Returns'])

heatmap_ret.columns = [calendar.month_name[i] for i in range(1,13) ]

ab = plt.figure(figsize=(16, 10))
ax = sns.heatmap(heatmap_ret, cmap='RdYlGn', annot=True)
ax.tick_params(top=True, labeltop=True)

st.pyplot(ab)