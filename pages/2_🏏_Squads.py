import streamlit as st
import pandas as pd
from helpers import get_client, read_file

client = get_client()
bucket_name = "summer-is-coming-2024"

squads = sorted(
    [
        blob.name.strip("Squads/")
        for blob in client.list_blobs(bucket_name, prefix="Squads")
    ],
    reverse=True,
)

option = st.selectbox("Select week", squads)

squad_df = read_file(bucket_name, f"Squads/{option}.csv")
st.subheader("Squad")
st.dataframe(squad_df)
