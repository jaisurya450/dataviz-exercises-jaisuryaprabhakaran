#!/usr/bin/env python3
"""World Happiness Dashboard: classroom chart + GDP scatter plot."""
from pathlib import Path
import pandas as pd
import plotly.express as px
import streamlit as st

st.set_page_config(page_title="World Happiness Report", page_icon="🌐", layout="wide")
st.title("🌍 World Happiness Dashboard")
st.caption("Source: World Happiness Report 2023 | Kaggle")

# Keep the dataset beside this app so the same code works on GitHub/Streamlit Cloud.
DATA = Path(__file__).parent / "data" / "world_happiness_2023.csv"
if not DATA.exists():
    st.error("Dataset missing. Put world_happiness_2023.csv inside the data folder next to app.py.")
    st.stop()

df = pd.read_csv(DATA)
df.columns = [
    "Country", "Region", "Score", "GDP", "Social_Support",
    "Life_Expectancy", "Freedom", "Generosity", "Corruption"
]

with st.sidebar:
    st.header("Filters")
    regions = ["All Regions"] + sorted(df["Region"].dropna().unique().tolist())
    selected_region = st.selectbox("Region", regions)
    top_n = st.slider("Show top N", 5, 25, 15)

filtered = df if selected_region == "All Regions" else df[df["Region"] == selected_region]
top = filtered.nlargest(top_n, "Score").sort_values("Score")

col1, col2, col3 = st.columns(3)
col1.metric("Countries", len(filtered))
col2.metric(
    "Avg Score", f"{filtered['Score'].mean():.2f}",
    f"{filtered['Score'].mean() - df['Score'].mean():+.2f} vs global"
)
col3.metric("Happiest", filtered.nlargest(1, "Score")["Country"].iloc[0])

st.divider()
st.subheader("Chart 1 — Happiest Countries (Class Chart)")
fig = px.bar(
    top, x="Score", y="Country", orientation="h",
    labels={"Score": "Happiness Score (0–10)", "Country": ""},
    template="plotly_white",
    title=f"Happiest {top_n} Countries in 2023 - {selected_region}",
    height=600,
)
fig.update_layout(
    title_font=dict(family="Arial", size=13, color="slategrey"),
    xaxis=dict(range=[0, 8.0]),
)
st.plotly_chart(fig, use_container_width=True)

st.divider()
st.subheader("Chart 2 — GDP vs Happiness Score (My Additional Chart)")
fig2 = px.scatter(
    filtered, x="GDP", y="Score", color="Region", hover_name="Country",
    title="Is Higher GDP Associated with Higher Happiness?",
    labels={"GDP": "GDP Contribution", "Score": "Happiness Score"},
    template="plotly_white",
)
st.plotly_chart(fig2, use_container_width=True)
st.caption("Each dot represents a country. Use the region filter to explore patterns.")

st.divider()
if st.button("Send balloons!"):
    st.balloons()
st.caption("Built with Streamlit + Plotly")
