import streamlit as st
import pandas as pd
import numpy as np
import requests
from plotly.offline import iplot
import plotly.graph_objs as go
import plotly.express as px
# from pandas.io.json import json_normalize


fig = go.Figure()
st.write("""
# Covid19 Tracking App Kerala🚑
""")

st.write('a simple tracking app for kerala')


url = 'https://keralastats.coronasafe.live/summary.json'
r = requests.get(url)
df = pd.read_json(r.text)
last_updated = df['last_updated'][0]
st.write('Last Updated on: ' + last_updated )
df = df.drop('last_updated', axis=1)
# st.write(pd.DataFrame(df))
df1 = df.drop('delta', axis=1)
df1 = df1.drop(['hospital_obs','home_obs','total_obs','hospital_today'], axis=0)
st.bar_chart(df1)

# r2= requests.get('https://keralastats.coronasafe.live/histories.json')
# df2 = pd.read_json(r2.text)
# history = df['histories']

# for hist in history:
#     df_new = pd.DataFrame(hist['summary']).T
# st.write(pd.DataFrame(df_new))