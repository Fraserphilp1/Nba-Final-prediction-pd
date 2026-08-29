from nba_api.stats.endpoints import leaguedashteamstats
import time
import pandas as pd
import os

All_seasons_data = []
Seasons = ['2024-25','2023-24', '2022-23', '2021-22', '2020-21', '2019-20', '2018-19', '2017-18', '2016-17', '2015-16', '2014-15', '2013-14', '2012-13', '2011-12', '2010-11', '2009-10', '2008-09', '2007-08', '2006-07']

for season in Seasons:
    print(f"Fetching data for season: {season}")
    data = leaguedashteamstats.LeagueDashTeamStats(season=season)
    df = data.get_data_frames()[0]
    df['SEASON'] = season  # Add a new column for the season
    All_seasons_data.append(df)
    time.sleep(1)  # Sleep for 1 second to avoid hitting the API rate
    print(f"Finished fetching data for season: {season}")

full_df = pd.concat(All_seasons_data, ignore_index=True)
Basedir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
full_df.to_csv(os.path.join(Basedir, 'data', 'teamseason_stats.csv'), index=False)
print("Data fetching complete. Saved to 'data/teamseason_stats.csv'.")
print(full_df.shape)