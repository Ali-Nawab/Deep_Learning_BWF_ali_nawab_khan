import pandas as pd

df = pd.read_html('https://www.fdic.gov/resources/resolutions/bank-failures/failed-bank-list/')

print(type(df))
print(df[0].head())