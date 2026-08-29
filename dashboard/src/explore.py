from nba_api.stats.endpoints import leaguedashteamstats

data = leaguedashteamstats.LeagueDashTeamStats(season='2023-24')
df = data.get_data_frames()[0]
print(df.head())
print(df.columns)
df_clean = df[['TEAM_ID', 'TEAM_NAME', 'W', 'L', 'W_PCT', 'PLUS_MINUS']]
print(df_clean)
