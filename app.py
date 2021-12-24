import streamlit as st
import pandas as pd
import numpy as np
from seaborn.axisgrid import pairplot
import matplotlib.pyplot as plt
import seaborn as sns
from PIL import Image
from chart_app import run_chart_app
from gall_app import run_gall_app
from mpg_ml_app import run_mpg_ml_app
from price_ml_app import run_price_ml_app


img = Image.open('data/car.jpg')
st.set_page_config(page_title='Car MPG & Price',page_icon=img,
                    layout='wide',initial_sidebar_state='collapsed')

def main():
    #제목
    st.title('Car MPG & Price')

    #사이드바
    menu = ['홈','데이터 검색','데이터 차트와 통계','연비 예측','가격 예측']
    choice = st.sidebar.selectbox('홈 메뉴',menu)

    #사이드바 설정
    if choice =='홈' :
        

        st.markdown("## 환영합니다!  ✧⁺⸜(  •⌄•  )⸝⁺✧")
        st.markdown("### Car MPG & Price에서는 고객님이 원하는 차량 데이터를 받고\n"
         "### 머신러닝을 통해 그에 맞는 연비 또는 가격을 알려드립니다.")
        st.subheader(' ')
        st.subheader('메뉴 소개')
        st.markdown("- 데이터 검색\n"
                    "   - 머신러닝에 사용된 데이터\n"
                    "   - 데이터 출처\n"
                    "   - 차량 디자인 확인\n"
                    "   - 현재 재고 확인\n")
                
        st.markdown("- 데이터 차트와 통계\n"
                    "   - 데이터의 차트\n"
                    "   - 데이터의 통계\n")
                
        st.markdown("- 연비 예측\n"
                    "   - 차량 데이터 입력후 연비 예측\n")

        st.markdown("- 가격 예측\n"
                    "   - 차량 데이터 입력후 가격 예측\n")            


    elif choice == '데이터 검색':
        run_gall_app()

    elif choice == '데이터 차트와 통계':
        run_chart_app()


    elif choice == '연비 예측':
        run_mpg_ml_app()


    elif choice == '가격 예측':
        run_price_ml_app()















if __name__ == '__main__':
    main()












