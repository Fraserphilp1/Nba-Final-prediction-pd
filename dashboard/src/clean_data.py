import pandas as pd
df = pd.read_csv('data/teamseason_stats.csv')

df_clean = df[['TEAM_ID', 'TEAM_NAME', 'SEASON', 'W', 'L', 'W_PCT', 'PLUS_MINUS']]

df_clean.to_csv('data/team_results_clean.csv', index=False)
print("Cleaned data saved to 'data/team_results_clean.csv'.")
print(df_clean.shape)

