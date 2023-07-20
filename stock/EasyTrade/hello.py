# import nsepy
# data_nse = nsepy.get_quote("TATAMOTORS")
# print(data_nse)
# data_nse = data_nse["data"][0]["lastPrice"]
# data_nse = data_nse.replace(",", "")
# data_nse = float(data_nse)
# print(data_nse)
from nsetools import Nse
nse = Nse()
print(nse.get_index_list())
print(nse.get_index_quote('NIFTY 50'))
