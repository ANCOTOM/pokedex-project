#Import libraries
import pandas as pd

df = pd.read_csv('pokemon_data.csv')

#General csv info
print(df.head()) #Show the first 5 rows
print(df.info()) #Show dataframe info
print(df.isnull().sum()) #Show null values

#Show actual columns