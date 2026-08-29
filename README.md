# NBA Finals Predictor: Point Differential vs. Win Totals

Does regular-season point differential predict NBA Finals success better than win totals? 
An end-to-end data pipeline and interactive dashboard analyzing 19 NBA seasons (2006-07 to 2024-25).

🔗 **[Live App](your-streamlit-url-here)** | 📂 **[GitHub Repo](your-repo-url-here)**

![Dashboard Screenshot](path-to-screenshot.png)

## The Question

Point differential is often cited in basketball analytics as a more stable, predictive 
measure of team quality than win-loss record — since wins can be skewed by close-game luck, 
while point differential reflects sustained performance. This project tests that idea directly: 
across nearly two decades of NBA seasons, which metric better identifies the teams that go on 
to reach — and win — the Finals?

## Key Finding

Across 19 seasons, the team with the **best regular-season point differential** made the NBA 
Finals in **9/19 seasons (47%)**, compared to **8/19 (42%)** for the team with the **most wins** 
— suggesting point differential is a marginally stronger predictor of Finals contention.

However, both metrics identified the eventual **champion** at an identical rate — **7/19 seasons 
(37%)** each — suggesting neither has a clear edge once a team actually reaches the Finals.

| Metric | Made Finals | Won Finals |
|---|---|---|
| Top Point Differential | 9/19 | 7/19 |
| Top Win Total | 8/19 | 7/19 |

## Tech Stack

- **Python** — data pipeline and analysis
- **pandas** — data cleaning, joining, aggregation
- **nba_api** — pulling official NBA team statistics
- **Streamlit** — interactive dashboard/web app
- **Streamlit Community Cloud** — deployment

## How It Works

1. **Data collection** (`src/Season_Stats.py`) — pulls team-level regular season stats 
   (wins, losses, point differential) for 19 seasons via `nba_api`, cached locally to avoid 
   repeated API calls.
2. **Cleaning** (`src/clean_data.py`) — filters to relevant columns.
3. **Joining** (`src/build_dataset.py`) — merges team stats with a manually compiled Finals 
   results reference table, flagging which teams made and won the Finals each season.
4. **Analysis** (`src/analyze.py`) — for each season, identifies the top point-diff team and 
   top win-total team, and checks how often each went on to make/win the Finals.
5. **Dashboard** (`app.py`) — displays the headline comparison, a chart, and the full 
   season-by-season breakdown.

## Run It Locally

```bash
git clone your-repo-url-here
cd dashboard
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
streamlit run app.py
```

## Data Source & Caveats

Data pulled from `stats.nba.com` via the unofficial `nba_api` Python package. This is not an 
officially supported API — it's prone to rate-limiting and IP-blocking, particularly from cloud/
data-center IPs. To work around this, raw data is pulled once and cached locally as CSV rather 
than queried live on each run.

Note: a small number of franchises changed names/cities during this period (e.g. Seattle 
SuperSonics → Oklahoma City Thunder). These are treated as distinct entries in the raw data and 
were not merged into continuous franchise histories, as it didn't affect this analysis.

## What's Next

- Extend the analysis to include additional predictive stats (shooting efficiency, turnover 
  rate, strength of schedule)
- Track continuous franchise performance across relocations/rebrands
- Add a simple predictive model rather than purely descriptive comparison