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
    print(1)
    #유저에게 숫자 데이터 받기
    print(2)
    radio1_menu = ['Audi','BMW','Ford','Hyundai','Mercedes Benz','Toyota']
    print(3)
    selected_radio = st.radio('제조사(Brand) 유형을 선택하세요.',radio1_menu)
    print(4)
    if selected_radio =='Audi':
        brand = [1,0,0,0,0,0]
        print(5)
    elif selected_radio =='BMW':
        brand = [0,1,0,0,0,0]
        print(6)
    elif selected_radio =='Ford':
        brand = [0,0,1,0,0,0]
        print(7)
    elif selected_radio =='Hyundai':
        brand = [0,0,0,1,0,0]
        print(8)
    elif selected_radio =='Mercedes Benz':
        brand = [0,0,0,0,1,0]
        print(9)
    elif selected_radio =='Toyota':
        brand = [0,0,0,0,0,1]
        print(10)
    print(11)  


    year = st.number_input('모델연도(Model Year)',min_value=1900,max_value=2030)
    print(12)
    mile = st.number_input('사용량(Milege)',min_value=0)
    print(13)
    engin = st.number_input('배기량(Enginsize)',min_value=0.0)
    print(14)

    first_list = [year,mile,engin]
    print(15)


    radio2_menu = ['Automatic','Manual','Other','Semi-Auto']
    selected_radio = st.radio('변속기(Transmission) 유형을 선택하세요.',radio2_menu)
    if selected_radio =='Automatic':
        trans = [1,0,0,0]
    elif selected_radio =='Manual':
        trans = [0,1,0,0]
    elif selected_radio =='Other':
        trans = [0,0,1,0]
    elif selected_radio =='Semi-Auto':
        trans = [0,0,0,1]
    print(16)
    


    radio3_menu = ['Diesel','Electric','Hybrid','Other','Petrol']
    selected_radio = st.radio('연료(Fuel) 유형을 선택하세요.',radio3_menu)
    if selected_radio =='Diesel':
        fuel = [1,0,0,0,0]
    elif selected_radio =='Electric':
        fuel = [0,1,0,0,0]
    elif selected_radio =='Hybrid':
        fuel = [0,0,1,0,0]
    elif selected_radio =='Other':
        fuel = [0,0,0,1,0]
    elif selected_radio =='Petrol':
        fuel = [0,0,0,0,1]
    print(17)

    new_data = first_list + brand + trans + fuel
    print(18)
    print(new_data)
    print(19)

    #유저 데이터를 new_data 변수로 저장
    

    new_data = np.array([new_data])
    print(20)
    print(new_data)
    print(21)
    new_data = new_data.reshape(1,18)
    print(22)
    
    #인공지능 불러오기
    scaler_X = joblib.load('data/mpg_scaler_X.pkl')
    print(23)
    scaler_y = joblib.load('data/mpg_scaler_y.pkl')
    print(24)
    regressor = joblib.load('data/mpg_regressor.pkl')
    print(25)

    #유저 데이터 피쳐스케일링
    new_data = scaler_X.transform(new_data)
    print(26)
    #예측
    y_pred = regressor.predict(new_data)
    print(27)
    #피쳐스케일링 한거 원래대로 복구
    #터미널로 확인
    print(y_pred)
    print(28)
    y_pred = scaler_y.inverse_transform(y_pred.reshape(1,1))
    print(29)
    print(y_pred)
    print(30)
    #예측 결과를 웹 대시보드에 버튼 누르면 표시
    #round로 반올림
    btn = st.button('예측 결과 보기')
    print(31)
    if btn :
        print(32)
        st.write('해당 차량의 연비 예측 결과는 {} 입니다.'.format(round(y_pred[0,0],1)))
    print(33)
