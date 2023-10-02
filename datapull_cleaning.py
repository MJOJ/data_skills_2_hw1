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
import zipfile #https://www.geeksforgeeks.org/read-a-zipped-file-as-a-pandas-dataframe/


BASEPATH= r'C:\Users\15083\Documents\GitHub\data_skills_2_hw1'
os.chdir(BASEPATH)

bea_df = pd.read_csv(os.path.join(BASEPATH,'data', 'Table.csv'), skiprows=3) #skip rows 1:3 as header is extranious https://www.statology.org/pandas-skip-rows/

#Note:Various geo-entitites merge/rename outside of 2005:2007 support. Additional cleaning is needed when adding years. Consult BEA header/footer.


#cleaning, droping legend/notes, recoding vars to prepare for reshape
bea_df = bea_df[bea_df['GeoName'].notna()]


bea_covars = bea_df['Description'].unique().tolist()
bea_renames = ['empxworkplace','total','manufacturing', 'military']
bea_dict = {bea_covars[covars]: bea_renames[covars] for covars in range(len(bea_renames))}
bea_df['Description'] = bea_df['Description'].replace(bea_dict) #https://sparkbyexamples.com/pandas/pandas-remap-values-in-column-with-a-dictionary-dict/

bea_df = bea_df.drop(['GeoName', 'LineCode'], axis=1)


# https://www.geeksforgeeks.org/python-pandas-melt/ 
bea_df = pd.melt(bea_df, id_vars =['GeoFips', 'Description'], var_name = 'year')
bea_df = bea_df.pivot(index=['GeoFips','year'], columns='Description', values='value')
bea_df = bea_df.drop(['empxworkplace'], axis=1)
bea_df = bea_df.reset_index()
bea_df = bea_df.rename(columns={'GeoFips': 'county'}) # https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.rename.html 
bea_df = bea_df.sort_values(['county', 'year'])



msa_df = pd.read_excel(os.path.join(BASEPATH,'data' ,'ssamatab1.xlsx'), skiprows=[0,1,3])
bea_df = bea_df.rename(columns={'GeoFips': 'county'})






