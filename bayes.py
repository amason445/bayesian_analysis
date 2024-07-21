import pandas as pd
import numpy as np

#load data and prepare lists to be parsed
raw_df = pd.read_csv('raw_data.csv')
raw_df['User Access Group'] = raw_df['User Access Group'].apply(lambda x: x.strip('[]').replace("'", "").split(', '))

#normalize lists with Panda's dataframe explode method
normalized_df = raw_df.explode('User Access Group')
normalized_df['In Executives'] = normalized_df.groupby('Name')['User Access Group'].transform(lambda x: 'Executives' in x.values)

#create pivot table and run analysis
pivoted_df = normalized_df.pivot_table(
index= 'User Access Group',
columns = 'In Executives',
aggfunc= 'size',
fill_value=0
)

#calculate prior, posterior and input probabilities
pivoted_df.columns = ['Not in Executives Group', 'In Executives Group']
pivoted_df.loc['Total Users'] = pivoted_df.sum()
pivoted_df['Total'] = pivoted_df.sum(axis=1)

pivoted_df['Prior Probabilities'] = pivoted_df['Total'] / pivoted_df.loc['Total Users', 'Total']

pr_executives = pivoted_df.loc['Total Users', 'In Executives Group'] / pivoted_df.loc['Total Users', 'Total']
pivoted_df['Probability of Executive Membership Given Group Membership'] = pivoted_df['In Executives Group'] / pivoted_df['Total']
pivoted_df['Probability of Group Membership'] = pivoted_df['Total'] / pivoted_df.loc['Total Users', 'Total']

pivoted_df['Posterior Probabilities'] = (pivoted_df['Probability of Executive Membership Given Group Membership']  * pivoted_df['Probability of Group Membership']) / pr_executives

#drop unnecessary columns
pivoted_df = pivoted_df.drop(columns=['Probability of Executive Membership Given Group Membership', 'Probability of Group Membership'])

print(pr_executives)
print(pivoted_df)

pivoted_df.to_csv('output.csv')

