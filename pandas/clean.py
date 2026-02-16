import pandas as pd

df = pd.read_csv('data.csv')

# remove rows with empty values
df = df.dropna()
# remove duplicates
df = df.drop_duplicates()
# convert date column to datetime format
df['Date'] = pd.to_datetime(df['Date'])
print(df.to_string())