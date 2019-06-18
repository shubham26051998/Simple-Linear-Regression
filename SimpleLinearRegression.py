#!/usr/bin/env python
# coding: utf-8

# In[3]:


# import necessary libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import statsmodels.api as sm

# import seaborn to add more visual perfection to the graphs
import seaborn as sns
sns.set()

# load the data from csv file
data = pd.read_csv('real_estate_price_size.csv')

# declaring the variables
y= data['price']
x1= data['size']

# getting the information about whole regression
x = sm.add_constant(x1)
results = sm.OLS(y,x).fit()
results.summary()

# as it is simple linear regression we use equation:- yhat= b0 + b1*x1  where b0 is an intercept
# we get the values of b0 and b1 from the above information of the regression
plt.scatter(x1,y)
yhat = 223.1787*x1 + 1.019e+05
fig = plt.plot(x1,yhat,lw=4,c='red',label='regression line')
plt.xlabel('size',fontsize=20)
plt.ylabel('price',fontsize=20)
plt.show()

