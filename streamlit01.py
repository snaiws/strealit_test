import streamlit as st
import plotly.express as px
import pandas as pd
import numpy as np

# 데이터셋 생성
np.random.seed(42)
data1 = pd.DataFrame({
    "x": np.random.rand(100),
    "y": np.random.rand(100),
    "dataset": "Dataset 1"
})

data2 = pd.DataFrame({
    "x": np.random.rand(100),
    "y": np.random.rand(100),
    "dataset": "Dataset 2"
})

# 초기 데이터 설정
if "dataset" not in st.session_state:
    st.session_state["dataset"] = data1

# 버튼 클릭 이벤트
if st.button("Switch Dataset"):
    # 데이터셋 전환
    st.session_state["dataset"] = data2 if st.session_state["dataset"].equals(data1) else data1

# 선택된 데이터셋으로 Plotly 그래프 생성
fig = px.scatter(st.session_state["dataset"], x="x", y="y", title=st.session_state["dataset"]["dataset"].iloc[0])

# 그래프 표시
st.plotly_chart(fig)