# -*- coding: utf-8 -*-
"""
Created on Sun Oct  1 13:39:55 2023

@author: Michael O'Neil
"""

#preamble
import pandas as pd
from pandas_datareader import wb
import pandas_datareader.data as web
import datetime
import os

BASEPATH= r'C:\Users\15083\Documents\GitHub\data_skills_2_hw1'
os.chdir(BASEPATH)
YEARS = list(range(2005, 2008, 1)) #https://stackoverflow.com/questions/18265935/how-do-i-create-a-list-with-numbers-between-two-values

df = pd.read_csv(os.path.join(BASEPATH,'data' , 'Table.csv'), skiprows=3) #skip rows 1:3 as header is extranious https://www.statology.org/pandas-skip-rows/

#Note:Various geo-entitites merge/rename outside of 2005:2007 support. Additional cleaning is needed when adding years. Consult BEA header/footer.


#cleaning, droping legend/notes, recoding vars to prepare for reshape
df = df[df['GeoName'].notna()]


bea_covars = df['Description'].unique().tolist()
bea_renames = ['empxworkplace','total','manufacturing', 'military']
bea_dict = {bea_covars[covars]: bea_renames[covars] for covars in range(len(bea_renames))}
df['Description'] = df['Description'].replace(bea_dict) #https://sparkbyexamples.com/pandas/pandas-remap-values-in-column-with-a-dictionary-dict/

df = df.drop(['GeoName', 'LineCode'], axis=1)


# https://www.geeksforgeeks.org/python-pandas-melt/ 
df = pd.melt(df, id_vars =['GeoFips', 'Description'], var_name = 'year')
df = df.pivot(index=['GeoFips','year'], columns='Description', values='value')
df = df.drop(['empxworkplace'], axis=1)
df = df.reset_index()
df = df.rename(columns={'GeoFips': 'county'}) # https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.rename.html 






