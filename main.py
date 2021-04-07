import pandas as pd

# Flexibility of Python
# Working with Big Data

df = pd.read_csv('pokemon_data.csv')
#print(df.head())
#print(df.tail())

#df_xlsx = pd.read_excel('pokemon_data.xlsx')
#print(df_xlsx.head())

#df_txt = pd.read_csv('pokemon_data.txt', delimiter='\t')
#print(df_txt.tail())

## Read Headers
#print(df.columns)

## Read each Column
#print(df[['Name', 'Type 1', 'HP']])

## Read each Row
#print(df.iloc[0:4])

#for index, row in df.iterrows():
#    print(index, row['Name'])

## Filter the Data
#df_filted = df.loc[df['Type 1'] == "Grass"]
#print(df_filted)

## Read a specific Location
#print(df.iloc[2,1])

## Sorting/Describing Data
#print(df.sort_values(['Type 1', 'HP'], ascending=[1,0]))

## Making changes to the data
#df['Total'] = df['HP'] + df['Attack'] + df['Defense'] + df['Sp. Atk'] + df['Sp. Def'] + df['Speed']
#print(df.head(5))
#df = df.drop(columns=['Total'])

## alternativ to make a sum
#df['Total'] = df.iloc[:, 4:10].sum(axis=1)
#print(df.head())

## Change the columne position
#cols = list(df.columns.values)
#df = df[cols[0:4] + [cols[-1]] + cols[4:12]]
#print(df.head())

## Save the data
#df.to_csv('modified.csv')
#df.to_csv('modified.csv', index=False)t
#df.to_excel('modified.xlsx', index=False)
#df.to_csv('modified.txt', index=False, sep='\t')

## Filtering Data
#df_filted_2 = df.loc[(df['Type 1'] == 'Grass') & (df['Type 2'] == 'Poison') & (df['HP'] > 75)]
#df_filted_2.to_csv('Filted.csv')
#df_filted_3 = df_filted_2.reset_index()
#df_filted_3.to_csv('Filted_index.csv')

#df_name_filted = df.loc[~df['Name'].str.contains('Mega')]
#print(df_name_filted.head())

#import re
#print(df.loc[df['Type 1'].str.contains('fire|grass', flags=re.I, regex=True)])
#print(df.loc[df['Name'].str.contains('^pi[a-z]', flags=re.I, regex=True)])

## Conditional Changes
#df.loc[df['Type 1'] == 'Flamer', 'Type 1'] = 'Fire'
#df.loc[df['Type 1'] == 'Fire', 'Legendary'] = True
#print(df)

#df.loc[df['Total'] > 500, ['Generation', 'Legendary']] = 'Test Value'
#print(df)


##Aggregate Statistics (Groupby)
#print(df.groupby(['Type 1']).mean().sort_values('Attack', ascending=False))

#df['count'] = 1
#print(df.groupby(['Type 1']).count()['count'])
#print(df.groupby(['Type 1', 'Type 2']).count()['count'])


## Working with large amounts of data


#new_df = pd.DataFrame(columns=df.columns)
#for df in pd.read_csv('pokemon_data.csv', chunksize=5):
#    results = df.groupby(['Type 1']).count()
#    new_df = pd.concat([new_df, results])
