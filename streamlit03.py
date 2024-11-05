import streamlit as st
import pandas as pd
import numpy as np

from sklearn.cluster import DBSCAN
from sklearn.preprocessing import StandardScaler

st.title('Uber pickups in NYC')

DATE_COLUMN = 'date/time'
DATA_URL = ('https://s3-us-west-2.amazonaws.com/'
         'streamlit-demo-data/uber-raw-data-sep14.csv.gz')

def load_data(nrows):
    data = pd.read_csv(DATA_URL, nrows=nrows)
    lowercase = lambda x: str(x).lower()
    data.rename(lowercase, axis='columns', inplace=True)
    data[DATE_COLUMN] = pd.to_datetime(data[DATE_COLUMN])
    return data
data = load_data(10000)

scaler = StandardScaler()
df_scaled = scaler.fit_transform(data[['lat', 'lon']])

# DBSCAN 모델 설정 및 훈련
# eps는 샘플 간 최대 거리 (적절한 값으로 조정 필요), min_samples는 군집 내 최소 샘플 수
dbscan = DBSCAN(eps=0.5, min_samples=2)
data['cluster'] = dbscan.fit_predict(df_scaled)

# 결과 출력

st.subheader('DBSCAN result')
hist_values = np.histogram(
    data['cluster'], bins=24, range=(0,24))[0]
st.bar_chart(hist_values)