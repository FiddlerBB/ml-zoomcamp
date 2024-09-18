import pandas as pd
import seaborn


file_path = 'laptops.csv'

df = pd.read_csv(file_path)
print(f'Question 1: {df.shape[0]}')

no_brand = len(df['Brand'].unique())
print(f'Question 2: {no_brand}')

print(f'Question 3: {df.isnull().any().sum()}')

df_dell = df[df['Brand']=='Dell']
print(f"Question 4: {df_dell['Final Price'].max()}")

print(df['Screen'].median())

most_feq = df['Screen'].mode().values[0]
df['Screen'] = df['Screen'].fillna(most_feq)

print(df['Screen'].median())