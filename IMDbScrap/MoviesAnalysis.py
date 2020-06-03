import pandas as pd
import matplotlib.pyplot as plt
import re

import numpy as np
df = pd.read_csv('C:\\Users\\Muhammad Usman\\Desktop\\Python Practice\\Assignment\\movies.csv')
df = df.dropna()


df.plot(x='Total Number of Ratings', y='Rating Score', style='o')
plt.show()


df.plot(x='Budget', y='Rating Score', style='o')
plt.show()


# first remove rows in which gross USA has None values
data = df[df['Gross USA'] != 'None']

# Remove comma sign from Gross USA
data['Gross USA'] = data['Gross USA'].str.replace(',', '')

# Remove dollar sign from Gross USA
data['Gross USA'] = data['Gross USA'].str.replace('$', '')

# Remove any kind of character
# data['Gross USA'] = re.sub('\D', data['Gross USA'])

# converting datatype of column
data['Gross USA'] = data['Gross USA'].astype('int64')

# Now apply query
result = data.groupby('Genre', as_index=False)['Gross USA'].mean()

print(result)
