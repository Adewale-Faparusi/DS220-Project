import pandas as pd 
data=pd.read_csv("titanic.csv")

'''access the data set
#We want to first learn about the data
Shows the first 5 values of a dataset'''
#print(data.head())


'''find the datatypes'''
# print(data.info())

'''Clean the data by dropping Cabin, Age, and Embarked because not all values are non-null'''
# data.drop(['Age','Embarked','Cabin'], axis=1, inplace=True)
# print(data.info())

'''Q1 How many people lived or died?'''
#(data['Survived'])
# print(pd.value_counts(data['Survived']))

'''Over 50% of people on the boat died so before applying any other features 
you're are more likely to die on the titanic'''

'''Q2 What is the difference of survival rate of men and women'''
print(pd.value_counts(data['Sex']))
 

 