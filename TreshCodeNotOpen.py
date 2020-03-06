# -*- coding: utf-8 -*-
import pandas as pd
data=pd.read_csv('Data_stock_market/SBER1D.csv',sep=';')
#print(data['<OPEN>'].values[0])
#print(data['<HIGH>'].values[0])
#print(data['<LOW>'].values[0])
#print(data['<CLOSE>'].values[0])
def pattern1(): # Паттерны разворота бычьего тренда, 1
    sw=0
    sl=0
    for i in range(1259):
        if (data['<OPEN>'].values[i] < data['<CLOSE>'].values[i]) and (data['<OPEN>'].values[i+1] < data['<CLOSE>'].values[i+1]) and ((data['<OPEN>'].values[i+1] - data['<LOW>'].values[i+1]) < 0.005) and (data['<OPEN>'].values[i+2] > data['<CLOSE>'].values[i+2]):
            sw+=1
        elif (data['<OPEN>'].values[i] < data['<CLOSE>'].values[i]) and (data['<OPEN>'].values[i+1] < data['<CLOSE>'].values[i+1]) and ((data['<OPEN>'].values[i+1] - data['<LOW>'].values[i+1]) < 0.005) and (data['<OPEN>'].values[i+2] < data['<CLOSE>'].values[i+2]):
            sl+=1
    return [sw, sl]
        
def pattern2(): # Паттерны разворота бычьего тренда, 4
    sw=0
    sl=0
    for i in range(1259):
        if (data['<OPEN>'].values[i] < data['<CLOSE>'].values[i]) and (data['<OPEN>'].values[i+1] > data['<CLOSE>'].values[i+1]) and (data['<LOW>'].values[i] > data['<CLOSE>'].values[i+1]) and (data['<HIGH>'].values[i] < data['<OPEN>'].values[i+1]) and (data['<OPEN>'].values[i+2] < data['<CLOSE>'].values[i+2]):
            sw+=1     
        elif (data['<OPEN>'].values[i] < data['<CLOSE>'].values[i]) and (data['<OPEN>'].values[i+1] > data['<CLOSE>'].values[i+1]) and (data['<LOW>'].values[i] > data['<CLOSE>'].values[i+1]) and (data['<HIGH>'].values[i] < data['<OPEN>'].values[i+1]) and (data['<OPEN>'].values[i+2] > data['<CLOSE>'].values[i+2]):
            sl+=1
    return [sw, sl]
print(pattern2())