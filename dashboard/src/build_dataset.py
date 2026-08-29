import pandas as pd

# Load both datasets
stats = pd.read_csv('data/team_results_clean.csv')
finals = pd.read_csv('data/finals_results.csv')

# Defensive whitespace strip
finals.columns = finals.columns.str.strip()
finals['CHAMPION'] = finals['CHAMPION'].str.strip()
finals['RUNNER_UP'] = finals['RUNNER_UP'].str.strip()

def made_finals(row):
    season_finals = finals[finals['SEASON'] == row['SEASON']]
    if season_finals.empty:
        return 0
    return int(row['TEAM_NAME'] in [season_finals.iloc[0]['CHAMPION'], season_finals.iloc[0]['RUNNER_UP']])

def won_finals(row):
    season_finals = finals[finals['SEASON'] == row['SEASON']]
    if season_finals.empty:
        return 0
    return int(row['TEAM_NAME'] == season_finals.iloc[0]['CHAMPION'])

stats['MADE_FINALS'] = stats.apply(made_finals, axis=1)
stats['WON_FINALS'] = stats.apply(won_finals, axis=1)

stats.to_csv('data/team_stats_with_finals.csv', index=False)
print(stats[['MADE_FINALS', 'WON_FINALS']].sum())
print(stats.shape)