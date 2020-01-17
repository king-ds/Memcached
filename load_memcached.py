import pandas as pd
from pymemcache.client.base import Client

t0 = time.time()

df = pd.read_csv('skunkworks.csv')

# convert csv to json
data = {}
columns = ['pickup', 'dropoff', 'distance', 'fare',
           'p_long', 'p_lat', 'd_long', 'd_lat']

client = Client(('172.31.40.140', 8000), no_delay=True)

count = 0
for index, row in df.iterrows():
    temp_value = {}
    for column in columns:
        temp_value[column] = row[column]
    client.set(str(index), temp_value)
    count += 1

print('Total count of data: %d' %count)

t1 = time.time()

total_time = t1 - t0
print(total_time)
