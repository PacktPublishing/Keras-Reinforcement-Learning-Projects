import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from scipy.stats import norm

dataset = pd.read_csv('AMZN.csv',header=0, usecols=['Date', 'Close'],parse_dates=True,index_col='Date')
print(dataset.info())
print(dataset.head())
print(dataset.describe())

plt.figure(figsize=(10,5))
plt.plot(dataset)
plt.show()

DataPctChange = dataset.pct_change()

LogReturns = np.log(1 + DataPctChange) 
print(LogReturns.tail(10))

plt.figure(figsize=(10,5))
plt.plot(LogReturns)
plt.show()

MeanLogReturns = np.array(LogReturns.mean())

VarLogReturns = np.array(LogReturns.var()) 

StdevLogReturns = np.array(LogReturns.std()) 


Drift = MeanLogReturns - (0.5 * VarLogReturns)
print("Drift = ",Drift)

NumberIntervals = 4529

Iterations = 20

np.random.seed(0)
B = norm.ppf(np.random.rand(NumberIntervals, Iterations))



DailyReturns = np.exp(Drift + StdevLogReturns * B)


StockPrices0 = dataset.iloc[0]

StockPrice = np.zeros_like(DailyReturns)

StockPrice[0] = StockPrices0

for t in range(1, NumberIntervals):

    StockPrice[t] = StockPrice[t - 1] * DailyReturns[t]
    
plt.figure(figsize=(10,5))

plt.plot(StockPrice)   



df1 = np.array(dataset.iloc[:, 0:1])


plt.plot(df1,'bs')   

plt.show()
