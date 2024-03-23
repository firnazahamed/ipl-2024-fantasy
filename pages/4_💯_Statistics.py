import streamlit as st
import pandas as pd
from helpers import read_file

st.set_page_config(layout="wide")
st.title("Player performance statistics")

bucket_name = "summer-is-coming-2024"
unsold_df = read_file(bucket_name, "Unsold_players.csv")
prices_df = read_file(bucket_name, "2024_price_list.csv")
agg_points_df = read_file(bucket_name, "Outputs/agg_points_df.csv")

df = prices_df.merge(agg_points_df, left_on="Player_name", right_on="Name_batting")
df = df[
    [
        "Player_name",
        "Team",
        "Category",
        "2024_price",
        "batting_points",
        "bowling_points",
        "fielding_points",
        "total_points",
    ]
]

for price in sorted(df["2024_price"].unique(), reverse=True):
    price_category_df = df[df["2024_price"] == price].sort_values(
        "total_points", ascending=False
    )
    st.header(f"{price} Price Category")
    st.subheader("Best Performers")
    st.dataframe(price_category_df.head(10))
    if len(price_category_df) > 10:
        st.subheader("Worst Performers")
        st.dataframe(price_category_df.tail(5).sort_values("total_points"))

for category in sorted(df["Category"].unique()):
    category_df = df[df["Category"] == category].sort_values(
        "total_points", ascending=False
    )
    st.header(f"Best {category}")
    # st.subheader("Best Performers")
    st.dataframe(category_df.head(10))
