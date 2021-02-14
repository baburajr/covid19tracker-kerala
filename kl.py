import streamlit as st
import pandas as pd
import numpy as np
import requests
from plotly.offline import iplot
import plotly.graph_objs as go
import plotly.express as px
from pandas.io.json import json_normalize


fig = go.Figure()
st.write("""
# Covid19 Tracking App Kerala🚑
""")

st.write('a simple tracking app for kerala')


url = 'https://keralastats.coronasafe.live/summary.json'
r = requests.get(url)
df1 = pd.read_json(r.json)
st.write(pd.DataFrame(df1))