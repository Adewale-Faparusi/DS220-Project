import pandas as pd 
data=pd.read_csv("titanic.csv")
#access the data set
#We want to first learn about the data

#print(data.head())
#shows the first 5 values of a dataset

#find the datatypes
print(data.info())

#Q1 How many people lived or died?
#(data['Survived'])
