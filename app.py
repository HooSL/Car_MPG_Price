import streamlit as st
import pandas as pd
import numpy as np
from seaborn.axisgrid import pairplot
import matplotlib.pyplot as plt
import seaborn as sns
from PIL import Image
from chart_app import run_chart_app, run_corr_app


from gall_app import run_gall_app
from mpg_ml_app import run_mpg_ml_app
from price_ml_app import run_price_ml_app
from chart_app import run_chart_app

img = Image.open('data/car.jpg')
st.set_page_config(page_title='중고 자동차 연비, 가격 예측',page_icon=img,
                    layout='wide',initial_sidebar_state='collapsed')

def main():
    #제목
    st.title('자동차 연비, 가격 예측')

    #사이드바
    menu = ['홈','데이터 검색','데이터 차트와 통계','연비 예측','가격 예측']
    choice = st.sidebar.selectbox('홈 메뉴',menu)

    #사이드바 설정
    if choice =='홈' :
        st.write(' ')
        st.write(' ')
        st.subheader('이 앱은 중고 자동차 연비와 가격에 대한 내용입니다.')
        st.write(' ')
        st.write(' ')
        st.write('1. 데이터 정보탭에서는 인공지능 학습에 사용된 데이터와 데이터의 통계를 보실 수 있습니다.')
        st.write(' ')
        st.write(' ')
        st.write('2. 검색 탭에서는 원하시는 차량의 데이터를 볼 수 있습니다.')
        st.write(' ')
        st.write(' ')
        st.write('3. 상관계수 차트탭에서는 데이터의 상관계수를 차트로 보실 수 있습니다.')
        st.write(' ')
        st.write(' ')
        st.write('4. 연비 예측탭에서는 차량의 데이터를 입력하면 해당차량의 연비를 예측드립니다.')
        st.write(' ')
        st.write(' ')
        st.write('5. 가격 예측탭에서는 차량의 데이터를 입력하면 해당차량의 가격를 예측해드립니다.')


    elif choice == '데이터 검색':
        run_gall_app()

    elif choice == '데이터 차트와 통계':
        run_chart_app()


    elif choice == '연비 예측':
        run_mpg_ml_app()

    elif choice == '가격 예측':
        run_price_ml_app()






# 검색 기능 , 최대 최소값




















if __name__ == '__main__':
    main()












