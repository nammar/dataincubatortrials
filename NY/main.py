#this is a permutations question without repetition. We use multiplication rule. I have provided a script that works for #the first two examples

import pandas as pd
import numpy as np

# n=4
# k=4
# j=2

# n=4
# k=100
# j=1

# n=100
# k=100
# j=1

# n=347
# k=2281
# j=829

# n=107
# k=1012
# j=829

n=1260000
k=4170000
j=1

count=1
times=k-1
nexttolastdigit=n-1
#first and last digits are dedicated for 1 and j so no need to count them
#repetition is not allowed so deduct n each time
#if n is even we will keep alternating between 1 is allowed and not alowed so we will stay at n-1 until we reach the next to last digit then we multiply by n-2

for i in range(2,n):
    if n%2==0 and i==nexttolastdigit: 
        times=times-1
    count*=times

offset=(pow(10,10)+7)
print(offset)
print(count%offset)       
# pd.set_option("display.precision", 10)

# #CHALLENGE
# print("What is the total number of persons injured in the dataset (up to December 31, 2018?)")
# url = 'https://data.cityofnewyork.us/resource/qiz3-axqb.json?$limit=1000000&\
# $where=date%20<%20%272018-12-31T00:00:00%27'

# collisions = pd.read_json(url)
# print(collisions.count())
# print(collisions.number_of_persons_injured.sum())

# print("What proportion of all collisions in 2016 occured in Brooklyn? Only consider entries with a non-null value for BOROUGH.")
# url = 'https://data.cityofnewyork.us/resource/qiz3-axqb.json?$limit=1000000&\
# $where=date%20between%20%272016-01-01T00:00:00%27%20and%20%272016-12-31T00:00:00%27'

# collisions = pd.read_json(url)
# collisions[collisions.borough.notnull()]
# #collisions.loc[collisions['borough'].notnull()

# total=collisions.borough.count()
# print(total)

# print("collisions grouped by city")
# #collisions.city.sort_values().index
# df_by_city = collisions.iloc[collisions.borough.sort_values().index]
# collisions_by_city = df_by_city.groupby('borough').borough.count()
# print(collisions_by_city)
# brooklyn=collisions_by_city['BROOKLYN']
# #print(brooklyn)
# proportion=brooklyn/total
# print(proportion)




# import matplotlib
#import cufflinks as cf
#import plotly
#import plotly.offline as py
#import plotly.graph_objs as go
#cf.go_offline() # required to use plotly offline (no account required).
#py.init_notebook_mode() # graphs charts inline (IPython).

#assuming data set created in 04/28/2014

#print(collisions.head(10))
#print(collisions.columns)
#print(collisions.date.count())
# contributing_factors = pd.concat(
#          [collisions.contributing_factor_vehicle_1,
#           collisions.contributing_factor_vehicle_2,
#           collisions.contributing_factor_vehicle_3,
#           collisions.contributing_factor_vehicle_4,
#           collisions.contributing_factor_vehicle_5])

# number_of_injured = pd.concat(
#          [collisions.number_of_cyclist_injured,
#           collisions.number_of_motorist_injured,
#           collisions.number_of_pedestrians_injured,
#           collisions.number_of_persons_injured])

# print(contributing_factors.value_counts())
# print(number_of_injured.value_counts())

# print("collisions grouped by date")
# collisions.date = pd.to_datetime(collisions.date)
# collisions.date.sort_values().index
# df_by_date = collisions.iloc[collisions.date.sort_values().index]
# collisions_by_date = df_by_date.groupby('date').date.count()
#print(collisions_by_date)
#collisions_by_date.iplot(kind='scatter', title='Collisions Per Day')

# print("deaths by date")
# deaths_by_date = df_by_date.groupby('date')['number_of_persons_killed'].sum()
# print(deaths_by_date)



# print("injuries by date")
# injuries_by_date = df_by_date.groupby('date')['number_of_persons_injured'].sum()
# print(injuries_by_date)
#deaths_by_date.iplot(kind='bar', title='Deaths per Day')

#print(pd.__version__)
#df = pd.read_json("https://data.smcgov.org/resource/mb6a-xn89.json")
#df = pd.read_json("https://data.cityofnewyork.us/resource/qiz3-axqb.json")

#print(df.head(5))
#print(df.shape)
#print(df.dtypes)
#df.date.count()
#import requests


#api_url = 'https://www.quandl.com/api/v1/datasets/WIKI/%s.json' % stock
#session = requests.Session()
#session.mount('http://', requests.adapters.HTTPAdapter(max_retries=3))
#raw_data = session.get(api_url)
#from bokeh.plotting import figure

#plot = figure(tools=TOOLS,
#              title='Data from Quandle WIKI set',
#              x_axis_label='date',
#              x_axis_type='datetime')
#print("Hello")
