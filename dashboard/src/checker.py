import pandas as pd
df = pd.read_csv('data/team_results_clean.csv')
print(sorted(df['TEAM_NAME'].unique()))