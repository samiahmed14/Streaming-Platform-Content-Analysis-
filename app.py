
import streamlit as st
import pandas as pd
import plotly.express as px


us_df = pd.read_csv("streaming_us_cleaned.csv")  
us_df = us_df.dropna(subset=["platform", "main_genre", "release_year"])


platform_colors = {
    "Netflix": "#E50914",      
    "Disney+": "#113CCF",     
    "Hulu": "#1CE783",         
    "Amazon Prime": "#00A8E1"  
}


st.set_page_config(page_title="Streaming Analytics Dashboard", layout="wide")

st.title(" Streaming Platform Insights Dashboard (US Market)")
st.write("Interactive analysis of content libraries across Netflix, Hulu, Disney+, and Amazon Prime.")

st.sidebar.header("Filters")
platforms_selected = st.sidebar.multiselect(
    "Select Platforms",
    options=us_df["platform"].unique(),
    default=us_df["platform"].unique()
)

years_selected = st.sidebar.slider(
    "Select Release Year Range",
    int(us_df["release_year"].min()),
    int(us_df["release_year"].max()),
    (2010, 2024)
)

filtered_df = us_df[
    (us_df["platform"].isin(platforms_selected)) &
    (us_df["release_year"].between(years_selected[0], years_selected[1]))
]


st.subheader(" Platform Distribution")
col1, col2 = st.columns(2)

with col1:
    counts = filtered_df["platform"].value_counts().reset_index()
    counts.columns = ["Platform", "Count"]
    fig1 = px.bar(counts, x="Platform", y="Count",
                  color="Platform", color_discrete_map=platform_colors,
                  title="Titles per Platform")
    st.plotly_chart(fig1, width='stretch')

with col2:
    fig2 = px.pie(
        counts, names="Platform", values="Count",
        color="Platform", color_discrete_map=platform_colors,
        title="Proportion of Titles by Platform"
    )
    st.plotly_chart(fig2, width='stretch')

st.subheader(" Genre Trends")
genre_counts = (
    filtered_df.groupby("platform")["main_genre"]
    .value_counts()
    .groupby(level=0)
    .head(8)
    .reset_index(name="count")
)
fig3 = px.bar(
    genre_counts,
    x="main_genre", y="count", color="platform",
    color_discrete_map=platform_colors,
    title="Top Genres by Platform"
)
st.plotly_chart(fig3, width='stretch')


st.subheader(" Release Year Distribution")
fig4 = px.histogram(
    filtered_df, x="release_year", color="platform",
    nbins=30, barmode="group",
    color_discrete_map=platform_colors,
    title="Content Added Over Time"
)
st.plotly_chart(fig4, width='stretch')

st.markdown("---")
st.caption("Data Source: Merged datasets from Netflix, Hulu, Disney+, and Amazon Prime (Kaggle).")
st.caption("Built using Python, Streamlit, Pandas, and Plotly Express.")
