#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np # library to handle data in a vectorized manner

import pandas as pd # library for data analsysis
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)

import json # library to handle JSON files

#!conda install -c conda-forge geopy --yes # uncomment this line if you haven't completed the Foursquare API lab
#from geopy.geocoders import Nominatim # convert an address into latitude and longitude values

import requests # library to handle requests
from pandas.io.json import json_normalize # tranform JSON file into a pandas dataframe

# Matplotlib and associated plotting modules
import matplotlib.cm as cm
import matplotlib.colors as colors

# import k-means from clustering stage
from sklearn.cluster import KMeans

#!conda install -c conda-forge folium=0.5.0 --yes # uncomment this line if you haven't completed the Foursquare API lab
import folium # map rendering library

print('Libraries imported.')


# In[13]:


pip install lxml # install lxml


# In[2]:


import lxml # import lxml


# ## Scrapping Toronto Neighborhood Data from weekipedia

# In[12]:


url= "https://en.wikipedia.org/wiki/List_of_postal_codes_of_Canada:_M"

r = requests.get(url)
df_list = pd.read_html(r.text) # this parses all the tables in webpages to a list
df = df_list[0]


# ### dropping Not assigned rows and renaming postal code to PostalCode

# In[17]:


df. drop(df[df['Borough']=="Not assigned"]. index, axis=0, inplace=True)
df.rename( columns={'Postal Code': 'PostalCode'}, inplace=True)
df.head(12)


# In[16]:


df.shape

