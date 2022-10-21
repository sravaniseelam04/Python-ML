import pandas as pd
from matplotlib import pyplot as plt

#1
data = pd.read_csv('data.csv')
print(data.head())

#2
print(data.describe(include='all'))

#3
print("Null check: \n",data.isnull().any())
data.fillna(data.replace('',data.mean()))
data['Calories'] = data['Calories'].fillna(data['Calories'].mean())
print("Null re-check: \n",data.isnull().any())

#4
print("aggregate data \n", data.agg({'Duration':['min','max','count','mean'],'Calories':['min','max','count','mean']}), "\n")


#5
print("Calories filtering- \n",data[(data['Calories'] > 500) & (data['Calories'] < 1000)])

#6
print("Calories filtering2-\n",data[(data['Calories'] > 500) | (data['Calories'] < 100)])

#7
df_modified = data[['Duration','Pulse','Calories']]
print("data without MaxPulse column \n",df_modified)

#8
data_n = data.drop('Maxpulse', axis=1)
print(data_n)

# 9. Convert the datatype of Calories column to int datatype.
data['Calories'] = data['Calories'].astype(int)
print("datatypes ",data.dtypes, "\n")

# 10. Using pandas create a scatter plot for the two columns (Duration and Calories).
data.plot.scatter(x='Duration',y='Calories',c='DarkBlue')
plt.show()