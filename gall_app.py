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

def run_gall_app():
    df = pd.read_csv('data/Car.csv',index_col=0)
    

#검색
    audi_menu = ['A1','A6','A4','A3','Q3','Q5','A5','S4','Q2','A7','TT','Q7','RS6','RS3','A8','Q8',
                'RS4','RS5','R8','SQ5','S8','SQ7','S3','S5','A2','RS7']

    bmw_menu = ['5 Series','6 Series','1 Series','7 Series','2 Series','4 Series','X3','3 Series',
                'X5','X4','i3','X1','M4','X2','X6','8 Series','Z4','X7','M5','i8','M2','M3','M6','Z3']

    ford_menu = ['Fiesta','Focus','Puma','Kuga','EcoSport','C-MAX','Mondeo','Ka+','Tourneo Custom',
                'S-MAX','B-MAX','Edge','Tourneo Connect','Grand C-MAX','KA','Galaxy','Mustang',
                'Grand Tourneo Connect','Fusion','Ranger','Streetka','Escort','Transit Tourneo']

    hyundai_menu = ['I20','Tucson','I10','IX35','I30','I40','Ioniq','Kona','Veloster','I800',
                    'IX20','Santa Fe','Accent','Terracan','Getz','Amica']

    merc_menu = ['SLK',' S Class','SL CLASS','G Class','GLE Class','GLA Class','A Class','B Class',
                'GLC Class','C Class','E Class','GL Class','CLS Class','CLC Class','CLA Class',
                'V Class','M Class','CL Class','GLS Class','GLB Class','X-CLASS','180','CLK',
                'R Class','230','220','200']

    toyota_menu = ['GT86','Corolla','RAV4','Yaris','Auris','Aygo','C-HR','Prius','Avensis','Verso',
                'Hilux','PROACE VERSO','Land Cruiser','Supra','Camry','Verso-S','IQ','Urban Cruiser']

    st.subheader("차량 디자인")
    word = st.text_input('차량 제조사를 입력하세요.')
    word.lower()
    word.strip()
    df_search = df.loc[df['제조사'].str.lower().str.contains(word),]
    if word.lower() == '':
        st.write('검색결과가 없습니다.')
        
    elif word.lower() == 'audi':
        audi_select = st.radio('모델을 선택하세요',audi_menu)

        if audi_select == 'A1':
            img = Image.open('car_img/A1.jpg')
            st.image(img)
        elif audi_select == 'A6':
            img = Image.open('car_img/A6.jpg')
            st.image(img)
        elif audi_select == 'A4':
            img = Image.open('car_img/A4.jpg')
            st.image(img)
        elif audi_select == 'A3':
            img = Image.open('car_img/A3.jpg')
            st.image(img)
        elif audi_select == 'Q3':
            img = Image.open('car_img/Q3.jpg')
            st.image(img)
        elif audi_select == 'Q5':
            img = Image.open('car_img/Q5.jpg')
            st.image(img)
        elif audi_select == 'A5':
            img = Image.open('car_img/A5.jpg')
            st.image(img)
        elif audi_select == 'S4':
            img = Image.open('car_img/S4.jpg')
            st.image(img)
        elif audi_select == 'Q2':
            img = Image.open('car_img/Q2.jpg')
            st.image(img)
        elif audi_select == 'A7':
            img = Image.open('car_img/A7.jpg')
            st.image(img)
        elif audi_select == 'TT':
            img = Image.open('car_img/TT.jpg')
            st.image(img)
        elif audi_select == 'Q7':
            img = Image.open('car_img/Q7.jpg')
            st.image(img)
        elif audi_select == 'RS6':
            img = Image.open('car_img/RS6.jpg')
            st.image(img)
        elif audi_select == 'RS3':
            img = Image.open('car_img/RS3.jpg')
            st.image(img)
        elif audi_select == 'A8':
            img = Image.open('car_img/A8.jpg')
            st.image(img)
        elif audi_select == 'Q8':
            img = Image.open('car_img/Q8.jpg')
            st.image(img)
        elif audi_select == 'RS4':
            img = Image.open('car_img/RS4.jpg')
            st.image(img)
        elif audi_select == 'RS5':
            img = Image.open('car_img/RS5.jpg')
            st.image(img)
        elif audi_select == 'R8':
            img = Image.open('car_img/R8.jpg')
            st.image(img)
        elif audi_select == 'SQ5':
            img = Image.open('car_img/SQ5.jpg')
            st.image(img)
        elif audi_select == 'S8':
            img = Image.open('car_img/S8.jpg')
            st.image(img)
        elif audi_select == 'SQ7':
            img = Image.open('car_img/SQ7.jpg')
            st.image(img)
        elif audi_select == 'S3':
            img = Image.open('car_img/S3.jpg')
            st.image(img)
        elif audi_select == 'S5':
            img = Image.open('car_img/S5.jpg')
            st.image(img)
        elif audi_select == 'A2':
            img = Image.open('car_img/A2.jpg')
            st.image(img)
        elif audi_select == 'RS7':
            img = Image.open('car_img/RS7.jpg')
            st.image(img)
        

    elif word.lower() == 'bmw':
        bmw_select = st.radio('모델을 선택하세요',bmw_menu)
        if bmw_select == '':
            img = Image.open('car_img/.jpg')
            st.image(img)
        elif bmw_select == '':
            img = Image.open('car_img/.jpg')
            st.image(img)


    elif word.lower() == 'ford':
        ford_select = st.radio('모델을 선택하세요',ford_menu)
        if ford_select == '':
            img = Image.open('car_img/.jpg')
            st.image(img)
        elif ford_select == '':
            img = Image.open('car_img/.jpg')
            st.image(img)


    elif word.lower() == 'hyundai':
        hyundai_select = st.radio('모델을 선택하세요',hyundai_menu)
        if hyundai_select == '':
            img = Image.open('car_img/.jpg')
            st.image(img)
        elif hyundai_select == '':
            img = Image.open('car_img/.jpg')
            st.image(img)

            
    elif word.lower() == 'benz':
        merc_select = st.radio('모델을 선택하세요',merc_menu)
        if merc_select == '':
            img = Image.open('car_img/.jpg')
            st.image(img)
        elif merc_select == '':
            img = Image.open('car_img/.jpg')
            st.image(img)

            
    elif word.lower() == 'toyota':
        toyota_select = st.radio('모델을 선택하세요',toyota_menu)
        if toyota_select == '':
            img = Image.open('car_img/.jpg')
            st.image(img)
        elif toyota_select == '':
            img = Image.open('car_img/.jpg')
            st.image(img)

            



    