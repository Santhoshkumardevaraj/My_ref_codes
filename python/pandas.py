# -*- coding: utf-8 -*-

import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error
from sklearn.preprocessing import LabelEncoder

df_archive=pd.read_csv('Resources/InputFiles/Archive4_IPL_Ball_by_Ball_2022.csv')

df_archive.columns
df_archive.describe()
df_archive.head
df_archive.tail
df_archive.to_numpy()
#dataframe sorting
df_archive.sort_index(axis=1,ascending=False)
df_archive.sort_values(by='batter')
#data selction
df_archive['batter']
df_archive[0:3]
#3get rows by location
df_archive.loc[19]
df_archive.iloc[3:5,0:2]
#copy dataframe to new
copy_of_df_archive=df_archive.copy
copy_of_df_archive
#filtering
df_archive[df_archive.isin(['Buttler','Ashwin'])]
#drop rows with issing data
df_archive.dropna(how='any')
#fill missing values
df_archive_result=df_archive.fillna(value=0)
#boolean mask where nan
df_archive_result=pd.isna(df_archive)
#value_counts
df_archive['batter'].value_counts()
#string functions
df_archive['batter'].str.lower()
#concatenate parts of Dataframe
parts=[df_archive[:5],df_archive[1:10]]
df_archive_result=pd.concat(parts)
#Dataframe merge
dfleft=pd.DataFrame({"Key":['test1','test2'],"lval":['1','2']})
dfright=pd.DataFrame({"Key":['test1','test2'],"rval":['3','4']})
pd.merge(dfleft,dfright,on="Key")
