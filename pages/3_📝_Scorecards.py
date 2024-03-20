import streamlit as st
import pandas as pd
from helpers import get_client, read_file

client = get_client()
bucket_name = "summer-is-coming-2024"

scorecards = sorted(
    [
        blob.name.strip("Scorecards/").strip("_scorecard.csv")
        for blob in client.list_blobs(bucket_name, prefix="Scorecards")
    ],
    reverse=True,
)

option = st.selectbox("Select match id", scorecards)

scorecard_df = read_file(bucket_name, f"Scorecards/{option}_scorecard.csv")
st.subheader(f"Scorecard")
st.dataframe(scorecard_df)
