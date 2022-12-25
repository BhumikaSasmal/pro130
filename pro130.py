import pandas as pd
import csv

df = pd.read_csv('total_stars.csv')
print(df.columns)
del df["Luminosity"]
del df['Unnamed: 6']
del df['id.1']
del df["Star_name.1"]
del df['Distance.1']
del df['Mass.1']
del df['Radius.1']
final_data = df.dropna()
final_data.to_csv('final_data.csv')