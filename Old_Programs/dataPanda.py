import pandas as pd

csvFile = 'file1.csv'
#creating a dataframe by reading the csv file, read_csv() function
#also read_excel function
df = pd.read_csv(csvFile)
print(df.head())

dict1 = {'num': [1, 2, 3, 4, 5], 'square' : [1, 4, 9, 16, 25], 'cube' : [1, 8, 27, 64, 125]}
df2 = pd.DataFrame(dict1)
print(df2)

#slicing the dataframe
print(df2[['num', 'cube']])

import numpy as np
x = np.linspace(0, 2*np.pi, 100)
y = np.sin(x)

import matplotlib.pyplot as plt
plt.plot(x, y)