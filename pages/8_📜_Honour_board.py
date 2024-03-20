import streamlit as st
import pandas as pd
from helpers import read_file

st.set_page_config(layout="wide")
honour_board = pd.DataFrame(
    {
        "Season": [2018, 2019, 2020, 2021, 2022, 2023],
        "Winner": ["Ashkay", "Mabbu", "Saju", "Saju", "Firi", "Firi"],
        "Runner-up": ["Mabbu", "Bhar", "Siddhu", "Srini", "Bhar", "Srini"],
        "Second runner-up": ["Bhar", "Shar", "Srini", "Firi", "Saju", "Ashkay"],
    }
).set_index("Season")

st.header("Honour Board")
st.table(honour_board)

st.header("Past Seasons")
bucket_name = "ipl-seasons"

for year in [2023, 2022, 2021, 2020, 2019, 2018]:

    col1, col2 = st.columns([2, 3])

    standings_df = read_file(bucket_name, f"{year}_standings.csv").set_index(
        "Standings"
    )
    col1.subheader(f"{year} Final Standings")
    col1.dataframe(standings_df)

    cumsum_df = read_file(bucket_name, f"{year}_cumsum.csv").set_index("Owner")
    cumsum_df = cumsum_df.rename(columns={x: int(x) for x in cumsum_df.columns})
    col2.subheader(f"{year} Standings Race")
    col2.line_chart(cumsum_df.T)

    st.markdown("#")
