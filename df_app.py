import streamlit as st
import pandas as pd
import numpy as np
from seaborn.axisgrid import pairplot
import matplotlib.pyplot as plt
import seaborn as sns
from PIL import Image

from matplotlib import font_manager, rc
font_path = "C:/Windows/Fonts/batang.ttc"
font = font_manager.FontProperties(fname=font_path).get_name()
rc('font', family=font)

def run_df_app():
    st.subheader('데이터 자료입니다.')
    st.write('데이터 출처 : https://www.kaggle.com/adityadesai13/used-car-dataset-ford-and-mercedes?select=audi.csv')
    df = pd.read_csv('data/Car.csv',index_col=0)
    if st.checkbox('데이터 전체보기'):
        st.dataframe(df)
        st.write('데이터 개수 64131개')
    else:
        st.write(' ')

#검색
    st.subheader(" ")
    st.subheader(" ")
    st.subheader("제조사 검색")
    word = st.text_input('차량 제조사를 입력하세요')
    word.lower()
    word.strip()
    df_search = df.loc[df['제조사'].str.lower().str.contains(word),]
    if st.button('검색'):
        st.dataframe(df_search)
    else:
        st.write(' ')



















