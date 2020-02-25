# -*- coding: utf-8 -*-
import pandas as pd
data=pd.read_csv('Data_stock_market/SBER1D.csv',sep=';')
print(data['<OPEN>'].values[0])
print(data['<HIGH>'].values[0])
print(data['<LOW>'].values[0])
print(data['<CLOSE>'].values[0])