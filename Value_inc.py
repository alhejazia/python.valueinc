# -*- coding: utf-8 -*-
"""
Created on Mon May  8 19:37:08 2023

@author: Admin
"""

import pandas as pd

data = pd.read_csv('transaction.csv')

data = pd.read_csv('transaction.csv',sep=';')

#summary of the data
data.info()

#working with calculations

#defining variables

CostPerItem = 11.73
SellingPricePerItem = 21.11
NumberofItemsPurchased = 6

#Mathematical Operations on Tableau

ProfitPerItem = 21.11-11.73
ProfitPerItem = SellingPricePerItem - CostPerItem

ProfitPerTransaction = NumberofItemsPurchased*ProfitPerItem
CostPerTransaction = NumberofItemsPurchased*CostPerItem
SellingPricePerTransaction = NumberofItemsPurchased*SellingPricePerItem

#CostPerTransaction Column Calculation

#CostPerTransaction = CostPerItem*NumberofItemsPurchased
#Variable = dataframe['column_name']

CostPerItem = data['CostPerItem']
NumberofItemsPurchased = data['NumberOfItemsPurchased']  
CostPerTransaction = CostPerItem*NumberofItemsPurchased    

#adding a new column to a dataframe

data['CostPerTransaction'] = CostPerTransaction

#Sales Per Transaction

data['SalesPerTransaction'] = data['SellingPricePerItem'] * data['NumberOfItemsPurchased']

#Profit Calculation = Sales - Cost

data['ProfitperTransaction'] = data['SalesPerTransaction'] - data['CostPerTransaction']

#MarkUp = (Sales - Cost)/Cost

data['MarkUp'] = (data['SalesPerTransaction'] - data['CostPerTransaction'])/ data['CostPerTransaction']

data['MarkUp'] = data['ProfitperTransaction'] / data['CostPerTransaction']

#Rounding Mark Up

Roundmarkup = round(data['MarkUp'],2)

data['MarkUp'] = round(data['MarkUp'],2)

#Combining data fields

my_date = 'Day'+'-'+'Month'+'-'+'Year'

#Combining data fields should be the same type

#Checking column data type

print(data['Day'].dtype)

#Changing data type

day = data['Day'].astype(str)
year= data['Year'].astype(str)
print(year.dtype)

#Combining date fields (same date type)

my_date = day+'-'+data['Month']+'-'+year

#adding to data set

data['date'] = my_date

#using iloc to view specific column/row

data.iloc[0] # views the row with the index 0
data.iloc[0:3]# first 3 rows
data.iloc[-5:]# last 5 rows

data.head(5)# views the first 5 rows
data.iloc[:,2] # brings in all rows on 2nd column

data.iloc[4,2] #brings in 4th row on 2nd column

#using split to split the client keywords field

#new_var = column.str.split('sep',expand=True)

split_col = data['ClientKeywords'].str.split(',' ,expand=True)

data['ClientAge'] = split_col[0]
data['ClientType'] = split_col[1]
data['LengthofContract'] = split_col[2]

#using the replace function
data['ClientAge'] = data['ClientAge'].str.replace('[','')
data['LengthofContract'] = data['LengthofContract'].str.replace(']','')

#using lower function to change to lowercase

data['ItemDescription'] = data['ItemDescription'].str.lower()

#how to merge files
#bringing in new data set

seasons =  pd.read_csv('value_inc_seasons.csv',sep=';')

#merging files: merge_df = pd.merge(df_old, df_new, on = 'key')

data = pd.merge(data,seasons, on ='Month')

#dropping columns

#df = df.drop('columnname' , axis = 1)

data = data.drop('ClientKeywords' , axis = 1)
data = data.drop('Day' , axis = 1)
data = data.drop(['Month','Year'] , axis = 1)

#Export into a CSV
#df.to_csv('filename.csv', index = False(No Index)/True (with Index Column))

data.to_csv('ValueInc_Cleaned.csv', index = False)




































        











