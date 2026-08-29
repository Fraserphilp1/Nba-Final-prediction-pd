import pandas as pd

df = pd.read_csv('data/team_stats_with_finals.csv')

results =[]
for season, group in df.groupby('SEASON'):
    top_pd_team = group.loc[group['PLUS_MINUS'].idxmax()]
    top_wins_team = group.loc[group['W_PCT'].idxmax()]
    results.append({
        'SEASON': season,
        'TOP_PD_TEAM': top_pd_team['TEAM_NAME'],
        'Top_pd_made_finals': top_pd_team['MADE_FINALS'],
        'Top_pd_won_finals': top_pd_team['WON_FINALS'],
        'TOP_WINS_TEAM': top_wins_team['TEAM_NAME'],
        'Top_wins_made_finals': top_wins_team['MADE_FINALS'],
        'Top_wins_won_finals': top_wins_team['WON_FINALS']
    })

summary_df = pd.DataFrame(results)
summary_df.to_csv('data/summary_stats.csv', index=False)
print("Summary statistics saved to 'data/summary_stats.csv'.")

print("Top point diff teams that made the finals:", summary_df['Top_pd_made_finals'].sum(), "/ 19 seasons")
print("Top point diff teams that won the finals:", summary_df['Top_pd_won_finals'].sum(), "/ 19 seasons")
print("Top wins made the finals:", summary_df['Top_wins_made_finals'].sum(), "/ 19 seasons")
print("Top wins won the finals:", summary_df['Top_wins_won_finals'].sum(), "/ 19 seasons")