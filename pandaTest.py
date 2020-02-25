import pandas as pd

file = 'UsMassShootings.csv'
data = pd.read_csv(file)
data.head(2)