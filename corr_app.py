import streamlit as st
import pandas as pd
import numpy as np
from seaborn.axisgrid import pairplot
import matplotlib.pyplot as plt
import seaborn as sns
from PIL import Image


def run_corr_app():
    #서브헤더
    st.subheader('상관계수와 상관계수의 차트 입니다.')
    #1. csv파일 가져오기
    df = pd.read_csv('data/Car.csv',index_col=0)
    

    st.subheader('상관계수')

    #4-1. 숫자만 처리하자
    df_corr = df.loc[ : , ['모델연도','사용량','배기량','연비','가격'] ]
    selected_corr = st.multiselect('원하는 상관계수 컬럼 선택해주세요',df_corr.columns)

    #4-2. 유저가 1개라도 선택했을 경우
    if len(selected_corr)>0:
        st.dataframe(df_corr[selected_corr].corr())

        #4-3. 상관계수를 수치로도 구하고, 차트로도 표시해라
        fig1 = sns.pairplot(data = df_corr[selected_corr])
        st.pyplot(fig1)

    #4-3. 유저가 컬럼을 선택하지 않은 경우
    else :
        st.write('선택한 컬럼이 없습니다.')