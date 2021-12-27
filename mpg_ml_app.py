import streamlit as st
import pandas as pd
import numpy as np
from seaborn.axisgrid import pairplot
import matplotlib.pyplot as plt
import seaborn as sns
from PIL import Image
import joblib
import itertools
from functools import reduce
import operator

def run_mpg_ml_app():
    st.subheader(' ')
    st.subheader(' ')
    st.subheader('연비 예측')

    #파일 불러오기
    df = pd.read_csv('data/Car.csv',index_col=0)
    st.write('Google의 Colab에서 MinMaxScaler와 RandomForestRegressor를 이용해 만든 머신러닝입니다.')
    #유저에게 숫자 데이터 받기
    radio1_menu = ['Audi','BMW','Ford','Hyundai','Mercedes Benz','Toyota']
    selected_radio = st.radio('제조사(Brand) 유형을 선택하세요.',radio1_menu)
    if selected_radio =='Audi':
        brand = [0,0,0,0,0]
    elif selected_radio =='BMW':
        brand = [1,0,0,0,0]
    elif selected_radio =='Ford':
        brand = [0,1,0,0,0]
    elif selected_radio =='Hyundai':
        brand = [0,0,1,0,0]
    elif selected_radio =='Mercedes Benz':
        brand = [0,0,0,1,0]
    elif selected_radio =='Toyota':
        brand = [0,0,0,0,1]


    year = st.number_input('모델연도(Model Year)',min_value=1900,max_value=2030)
    mile = st.number_input('사용량(Milege)',min_value=0)
    engin = st.number_input('배기량(Enginsize)',min_value=0.0)

    first_list = [year,mile,engin]


    radio2_menu = ['Automatic','Manual','Semi-Auto']
    selected_radio = st.radio('변속기(Transmission) 유형을 선택하세요.',radio2_menu)
    if selected_radio =='Automatic':
        trans = [0,0]
    elif selected_radio =='Manual':
        trans = [1,0]
    elif selected_radio =='Semi-Auto':
        trans = [0,1]
    


    radio3_menu = ['Diesel','Hybrid','Petrol']
    selected_radio = st.radio('연료(Fuel) 유형을 선택하세요.',radio3_menu)
    if selected_radio =='Diesel':
        fuel = [0,0]
    elif selected_radio =='Hybrid':
        fuel = [1,0]
    elif selected_radio =='Petrol':
        fuel = [0,1]

    new_data = first_list + brand + trans + fuel
    print(new_data)

    #유저 데이터를 new_data 변수로 저장
    

    new_data = np.array([new_data])
    print(new_data)
    new_data = new_data.reshape(1,12)
    
    #인공지능 불러오기
    scaler_X = joblib.load('data/mpg_scaler_X.pkl')
    scaler_y = joblib.load('data/mpg_scaler_y.pkl')
    regressor = joblib.load('data/mpg_regressor.pkl')

    #유저 데이터 피쳐스케일링
    new_data = scaler_X.transform(new_data)
    #예측
    y_pred = regressor.predict(new_data)
    #피쳐스케일링 한거 원래대로 복구
    #터미널로 확인
    print(y_pred)
    y_pred = scaler_y.inverse_transform(y_pred.reshape(1,1))
    print(y_pred)
    #예측 결과를 웹 대시보드에 버튼 누르면 표시
    #round로 반올림
    btn = st.button('예측 결과 보기')
    if btn :
        st.subheader('해당 차량의 연비 예측 결과는 {} 입니다.'.format(round(y_pred[0,0],1)))
    
