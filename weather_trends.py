import pandas as pd
import matplotlib.pyplot as plt

years = 15
global_df = pd.read_csv('global_data.csv')
seattle_df = pd.read_csv('seattle_city_data.csv')
seattle_df.drop(columns=['city', 'country'], inplace=True)
global_df['{}yr_roll_avg'.format(years)] = global_df['avg_temp'].rolling(years).mean()
seattle_df['{}yr_roll_avg'.format(years)] = seattle_df['avg_temp'].rolling(years).mean()
plt.plot(global_df['year'], global_df['{}yr_roll_avg'.format(years)], label='Global Moving Avg')
plt.plot(seattle_df['year'], seattle_df['{}yr_roll_avg'.format(years)], label='Seattle Moving Avg')
plt.title('{}-year Moving Average'.format(years))
plt.xlabel('Year')
plt.ylabel('Degrees Celsius')
plt.legend(loc='best')
plt.savefig('{}yr_moving_avg.svg'.format(years))
