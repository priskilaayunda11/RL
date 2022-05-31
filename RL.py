import numpy as np
import numpy.random as nrand
import matplotlib.pyplot as plt
import math

#Define vars
S = 1000000
T = 252
mu = 1.92246
vol = .86123  #Between .76 and .86

result = []
for i in range(1000):
    daily_returns = np.random.normal(mu/T,vol/math.sqrt(T),T)+1
    
    price_list = [S]
    
    for x in daily_returns:
        price_list.append(price_list[-1]*x)
    result.append(price_list[-1]) #appending each runs end value --to calculate the mean return
        
    plt.plot(price_list)#This is key, KEEP THIS IN LOOP,votherwise it will plot one iteration/return path.
plt.title('Daily MC')