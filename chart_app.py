import streamlit as st
import pandas as pd
import numpy as np
from seaborn.axisgrid import pairplot
import matplotlib.pyplot as plt
import seaborn as sns
from PIL import Image


def run_chart_app():
    #서브헤더
    st.subheader('상관계수와 상관계수의 차트 입니다.')
    #1. csv파일 가져오기
    df = pd.read_csv('data/Car.csv',index_col=0)
    
    df.columns=['brand','model','model year','mileage','enginsize','transmission','fuel','mpg','price']

    st.subheader('상관계수')
    
    word = st.text_input('차량 제조사를 입력하세요')
    word.lower()
    word.strip()
    df_search = df.loc[df['brand'].str.lower().str.contains(word),]
    

    selected_column = st.selectbox('컬럼을 선택하세요.',df_search.columns)

    bins=st.slider('bin의 개수 조절',min_value=10,max_value=50)

    fig1 = plt.figure()
    plt.xticks(rotation=65)
    df_search[selected_column].hist(bins=bins)
    st.pyplot(fig1)
    

    st.subheader('데이터 컬럼별 통계치')
    st.dataframe(df_search.describe())




