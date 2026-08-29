import streamlit as st
import pandas as pd

st.set_page_config(page_title="NBA: Point Differential Analysis", layout="centered")
df = pd.read_csv("data/team_stats_with_finals.csv")
summary_df = pd.read_csv("data/summary_stats.csv")

st.title("Does Point Differential Predict NBA Finals Success better than Win Percentage?")
st.markdown("Analyzing 19 seasons of NBA data, we compare the top teams by point differential and win percentage to see which metric better predicts success in the NBA Finals.")

col1, col2 = st.columns(2)
with col1:
    st.subheader("Top Point Differential Teams")
    st.write(summary_df[['SEASON', 'TOP_PD_TEAM', 'TOP_PD_MADE_FINALS', 'TOP_PD_WON_FINALS']])
    st.metric("Made Finals", f"{summary_df['TOP_PD_MADE_FINALS'].sum()}", delta=None)
    st.metric("Won Finals", f"{summary_df['TOP_PD_WON_FINALS'].sum()}", delta=None)

with col2:
    st.subheader("Top Win totals Team")
    st.metric("Made Finals", f"{summary_df['TOP_WINS_MADE_FINALS'].sum()}", delta=None)
    st.metric("Won Finals", f"{summary_df['TOP_WINS_WON_FINALS'].sum()}", delta=None)

st.markdown("---")

chart_data = pd.DataFrame({
    'Metric': ['Made Finals', 'Made Finals', 'Won Finals', 'Won Finals'],
    'Predictor': ['Point Differential', 'Win Total', 'Point Differential', 'Win Total'],
    'Seasons': [
        summary_df['TOP_PD_MADE_FINALS'].sum(),
        summary_df['TOP_WINS_MADE_FINALS'].sum(),
        summary_df['TOP_PD_WON_FINALS'].sum(),
        summary_df['TOP_WINS_WON_FINALS'].sum(),
    ]
})

st.subheader("Comparison")
st.bar_chart(chart_data.pivot(index='Metric', columns='Predictor', values='Seasons'))

st.markdown("---")
st.subheader("Season-by-Season Breakdown")
st.dataframe(summary_df)