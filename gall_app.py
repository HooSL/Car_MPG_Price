import streamlit as st
import pandas as pd
import numpy as np
from seaborn.axisgrid import pairplot
import matplotlib.pyplot as plt
import seaborn as sns
from PIL import Image


def run_gall_app():
    df = pd.read_csv('data/Car.csv',index_col=0)
    st.subheader('데이터 자료입니다.')
    st.write('데이터 출처 : https://www.kaggle.com/adityadesai13/used-car-dataset-ford-and-mercedes?select=audi.csv')
    if st.checkbox('데이터 전체보기'):
        st.dataframe(df)
        st.write('데이터 개수 64131개')
    else:
        st.write(' ')
    

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

    merc_menu = ['SLK','S Class','SL CLASS','G Class','GLE Class','GLA Class','A Class','B Class',
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
            img = Image.open('car_img/audi/A1.jpg')
            st.image(img)
            st.write('현재 재고 데이터')
            car_search = df.loc[df['모델']==' A1',]
            st.dataframe(car_search)

        elif audi_select == 'A6':
            img = Image.open('car_img/audi/A6.jpg')
            st.image(img)
            st.write('현재 재고 데이터')
            car_search = df.loc[df['모델']==' A6',]
            st.dataframe(car_search)

        elif audi_select == 'A4':
            img = Image.open('car_img/audi/A4.jpg')
            st.image(img)
            st.write('현재 재고 데이터')
            car_search = df.loc[df['모델']==' A4',]
            st.dataframe(car_search)

        elif audi_select == 'A3':
            img = Image.open('car_img/audi/A3.jpg')
            st.image(img)
            st.write('현재 재고 데이터')
            car_search = df.loc[df['모델']==' A3',]
            st.dataframe(car_search)

        elif audi_select == 'Q3':
            img = Image.open('car_img/audi/Q3.jpg')
            st.image(img)
            st.write('현재 재고 데이터')
            car_search = df.loc[df['모델']==' Q3',]
            st.dataframe(car_search)

        elif audi_select == 'Q5':
            img = Image.open('car_img/audi/Q5.jpg')
            st.image(img)
            st.write('현재 재고 데이터')
            car_search = df.loc[df['모델']==' Q5',]
            st.dataframe(car_search)

        elif audi_select == 'A5':
            img = Image.open('car_img/audi/A5.jpg')
            st.image(img)
            st.write('현재 재고 데이터')
            car_search = df.loc[df['모델']==' A5',]
            st.dataframe(car_search)

        elif audi_select == 'S4':
            img = Image.open('car_img/audi/S4.jpg')
            st.image(img)
            st.write('현재 재고 데이터')
            car_search = df.loc[df['모델']==' S4',]
            st.dataframe(car_search)

        elif audi_select == 'Q2':
            img = Image.open('car_img/audi/Q2.jpg')
            st.image(img)
            st.write('현재 재고 데이터')
            car_search = df.loc[df['모델']==' Q2',]
            st.dataframe(car_search)

        elif audi_select == 'A7':
            img = Image.open('car_img/audi/A7.jpg')
            st.image(img)
            st.write('현재 재고 데이터')
            car_search = df.loc[df['모델']==' A7',]
            st.dataframe(car_search)

        elif audi_select == 'TT':
            img = Image.open('car_img/audi/TT.jpg')
            st.image(img)
            st.write('현재 재고 데이터')
            car_search = df.loc[df['모델']==' TT',]
            st.dataframe(car_search)

        elif audi_select == 'Q7':
            img = Image.open('car_img/audi/Q7.jpg')
            st.image(img)
            st.write('현재 재고 데이터')
            car_search = df.loc[df['모델']==' Q7',]
            st.dataframe(car_search)

        elif audi_select == 'RS6':
            img = Image.open('car_img/audi/RS6.jpg')
            st.image(img)
            st.write('현재 재고 데이터')
            car_search = df.loc[df['모델']==' RS6',]
            st.dataframe(car_search)

        elif audi_select == 'RS3':
            img = Image.open('car_img/audi/RS3.jpg')
            st.image(img)
            st.write('현재 재고 데이터')
            car_search = df.loc[df['모델']==' RS3',]
            st.dataframe(car_search)

        elif audi_select == 'A8':
            img = Image.open('car_img/audi/A8.jpg')
            st.image(img)
            st.write('현재 재고 데이터')
            car_search = df.loc[df['모델']==' A8',]
            st.dataframe(car_search)

        elif audi_select == 'Q8':
            img = Image.open('car_img/audi/Q8.jpg')
            st.image(img)
            st.write('현재 재고 데이터')
            car_search = df.loc[df['모델']==' Q8',]
            st.dataframe(car_search)

        elif audi_select == 'RS4':
            img = Image.open('car_img/audi/RS4.jpg')
            st.image(img)
            st.write('현재 재고 데이터')
            car_search = df.loc[df['모델']==' RS4',]
            st.dataframe(car_search)

        elif audi_select == 'RS5':
            img = Image.open('car_img/audi/RS5.jpg')
            st.image(img)
            st.write('현재 재고 데이터')
            car_search = df.loc[df['모델']==' RS5',]
            st.dataframe(car_search)

        elif audi_select == 'R8':
            img = Image.open('car_img/audi/R8.jpg')
            st.image(img)
            st.write('현재 재고 데이터')
            car_search = df.loc[df['모델']==' R8',]
            st.dataframe(car_search)

        elif audi_select == 'SQ5':
            img = Image.open('car_img/audi/SQ5.jpg')
            st.image(img)
            st.write('현재 재고 데이터')
            car_search = df.loc[df['모델']==' SQ5',]
            st.dataframe(car_search)

        elif audi_select == 'S8':
            img = Image.open('car_img/audi/S8.jpg')
            st.image(img)
            st.write('현재 재고 데이터')
            car_search = df.loc[df['모델']==' S8',]
            st.dataframe(car_search)

        elif audi_select == 'SQ7':
            img = Image.open('car_img/audi/SQ7.jpg')
            st.image(img)
            st.write('현재 재고 데이터')
            car_search = df.loc[df['모델']==' SQ7',]
            st.dataframe(car_search)

        elif audi_select == 'S3':
            img = Image.open('car_img/audi/S3.jpg')
            st.image(img)
            st.write('현재 재고 데이터')
            car_search = df.loc[df['모델']==' S3',]
            st.dataframe(car_search)

        elif audi_select == 'S5':
            img = Image.open('car_img/audi/S5.jpg')
            st.image(img)
            st.write('현재 재고 데이터')
            car_search = df.loc[df['모델']==' S5',]
            st.dataframe(car_search)

        elif audi_select == 'A2':
            img = Image.open('car_img/audi/A2.jpg')
            st.image(img)
            st.write('현재 재고 데이터')
            car_search = df.loc[df['모델']==' A2',]
            st.dataframe(car_search)

        elif audi_select == 'RS7':
            img = Image.open('car_img/audi/RS7.jpg')
            st.image(img)
            st.write('현재 재고 데이터')
            car_search = df.loc[df['모델']==' RS7',]
            st.dataframe(car_search)
        

    elif word.lower() == 'bmw':
        bmw_select = st.radio('모델을 선택하세요',bmw_menu)
        if bmw_select == '5 Series':
            img = Image.open('car_img/bmw/5 Series.jpg')
            st.image(img)
            st.write('현재 재고 데이터')
            car_search = df.loc[df['모델']==' 5 Series',]
            st.dataframe(car_search)

        elif bmw_select == '6 Series':
            img = Image.open('car_img/bmw/6 Series.jpg')
            st.image(img)
            st.write('현재 재고 데이터')
            car_search = df.loc[df['모델']==' 6 Series',]
            st.dataframe(car_search)
        elif bmw_select == '1 Series':
            img = Image.open('car_img/bmw/1 Series.jpg')
            st.image(img)
            st.write('현재 재고 데이터')
            car_search = df.loc[df['모델']==' 1 Series',]
            st.dataframe(car_search)

        elif bmw_select == '7 Series':
            img = Image.open('car_img/bmw/7 Series.jpg')
            st.image(img)
            st.write('현재 재고 데이터')
            car_search = df.loc[df['모델']==' 7 Series',]
            st.dataframe(car_search)

        elif bmw_select == '2 Series':
            img = Image.open('car_img/bmw/2 Series.jpg')
            st.image(img)
            st.write('현재 재고 데이터')
            car_search = df.loc[df['모델']==' 2 Series',]
            st.dataframe(car_search)

        elif bmw_select == '4 Series':
            img = Image.open('car_img/bmw/4 Series.jpg')
            st.image(img)
            st.write('현재 재고 데이터')
            car_search = df.loc[df['모델']==' 4 Series',]
            st.dataframe(car_search)

        elif bmw_select == 'X3':
            img = Image.open('car_img/bmw/X3.jpg')
            st.image(img)
            st.write('현재 재고 데이터')
            car_search = df.loc[df['모델']==' X3',]
            st.dataframe(car_search)

        elif bmw_select == '3 Series':
            img = Image.open('car_img/bmw/3 Series.jpg')
            st.image(img)
            st.write('현재 재고 데이터')
            car_search = df.loc[df['모델']==' 3 Series',]
            st.dataframe(car_search)

        elif bmw_select == 'X5':
            img = Image.open('car_img/bmw/X5.jpg')
            st.image(img)
            st.write('현재 재고 데이터')
            car_search = df.loc[df['모델']==' X5',]
            st.dataframe(car_search)

        elif bmw_select == 'X4':
            img = Image.open('car_img/bmw/X4.jpg')
            st.image(img)
            st.write('현재 재고 데이터')
            car_search = df.loc[df['모델']==' X4',]
            st.dataframe(car_search)

        elif bmw_select == 'i3':
            img = Image.open('car_img/bmw/i3.jpg')
            st.image(img)
            st.write('현재 재고 데이터')
            car_search = df.loc[df['모델']==' i3',]
            st.dataframe(car_search)

        elif bmw_select == 'X1':
            img = Image.open('car_img/bmw/X1.jpg')
            st.image(img)
            st.write('현재 재고 데이터')
            car_search = df.loc[df['모델']==' X1',]
            st.dataframe(car_search)

        elif bmw_select == 'M4':
            img = Image.open('car_img/bmw/M4.jpg')
            st.image(img)
            st.write('현재 재고 데이터')
            car_search = df.loc[df['모델']==' M4',]
            st.dataframe(car_search)

        elif bmw_select == 'X2':
            img = Image.open('car_img/bmw/X2.jpg')
            st.image(img)
            st.write('현재 재고 데이터')
            car_search = df.loc[df['모델']==' X2',]
            st.dataframe(car_search)

        elif bmw_select == 'X6':
            img = Image.open('car_img/bmw/X6.jpg')
            st.image(img)
            st.write('현재 재고 데이터')
            car_search = df.loc[df['모델']==' X6',]
            st.dataframe(car_search)

        elif bmw_select == '8 Series':
            img = Image.open('car_img/bmw/8 Series.jpg')
            st.image(img)
            st.write('현재 재고 데이터')
            car_search = df.loc[df['모델']==' 8 Series',]
            st.dataframe(car_search)

        elif bmw_select == 'Z4':
            img = Image.open('car_img/bmw/Z4.jpg')
            st.image(img)
            st.write('현재 재고 데이터')
            car_search = df.loc[df['모델']==' Z4',]
            st.dataframe(car_search)

        elif bmw_select == 'X7':
            img = Image.open('car_img/bmw/X7.jpg')
            st.image(img)
            st.write('현재 재고 데이터')
            car_search = df.loc[df['모델']==' X7',]
            st.dataframe(car_search)

        elif bmw_select == 'M5':
            img = Image.open('car_img/bmw/M5.jpg')
            st.image(img)
            st.write('현재 재고 데이터')
            car_search = df.loc[df['모델']==' M5',]
            st.dataframe(car_search)

        elif bmw_select == 'i8':
            img = Image.open('car_img/bmw/i8.jpg')
            st.image(img)
            st.write('현재 재고 데이터')
            car_search = df.loc[df['모델']==' i8',]
            st.dataframe(car_search)

        elif bmw_select == 'M2':
            img = Image.open('car_img/bmw/M2.jpg')
            st.image(img)
            st.write('현재 재고 데이터')
            car_search = df.loc[df['모델']==' M2',]
            st.dataframe(car_search)

        elif bmw_select == 'M3':
            img = Image.open('car_img/bmw/M3.jpg')
            st.image(img)
            st.write('현재 재고 데이터')
            car_search = df.loc[df['모델']==' M3',]
            st.dataframe(car_search)

        elif bmw_select == 'M6':
            img = Image.open('car_img/bmw/M6.jpg')
            st.image(img)
            st.write('현재 재고 데이터')
            car_search = df.loc[df['모델']==' M6',]
            st.dataframe(car_search)

        elif bmw_select == 'Z3':
            img = Image.open('car_img/bmw/Z3.jpg')
            st.image(img)
            st.write('현재 재고 데이터')
            car_search = df.loc[df['모델']==' Z3',]
            st.dataframe(car_search)



    elif word.lower() == 'ford':
        ford_select = st.radio('모델을 선택하세요',ford_menu)
        if ford_select == 'Fiesta':
            img = Image.open('car_img/ford/Fiesta.jpg')
            st.image(img)
            st.write('현재 재고 데이터')
            car_search = df.loc[df['모델']==' Fiesta',]
            st.dataframe(car_search)

        elif ford_select == 'Focus':
            img = Image.open('car_img/ford/Focus.jpg')
            st.image(img)
            st.write('현재 재고 데이터')
            car_search = df.loc[df['모델']==' Focus',]
            st.dataframe(car_search)

        elif ford_select == 'Puma':
            img = Image.open('car_img/ford/Puma.jpg')
            st.image(img)
            st.write('현재 재고 데이터')
            car_search = df.loc[df['모델']==' Puma',]
            st.dataframe(car_search)

        elif ford_select == 'Kuga':
            img = Image.open('car_img/ford/Kuga.jpg')
            st.image(img)
            st.write('현재 재고 데이터')
            car_search = df.loc[df['모델']==' Kuga',]
            st.dataframe(car_search)

        elif ford_select == 'EcoSport':
            img = Image.open('car_img/ford/EcoSport.jpg')
            st.image(img)
            st.write('현재 재고 데이터')
            car_search = df.loc[df['모델']==' EcoSport',]
            st.dataframe(car_search)

        elif ford_select == 'C-MAX':
            img = Image.open('car_img/ford/C-MAX.jpg')
            st.image(img)
            st.write('현재 재고 데이터')
            car_search = df.loc[df['모델']==' C-MAX',]
            st.dataframe(car_search)

        elif ford_select == 'Mondeo':
            img = Image.open('car_img/ford/Mondeo.jpg')
            st.image(img)
            st.write('현재 재고 데이터')
            car_search = df.loc[df['모델']==' Mondeo',]
            st.dataframe(car_search)

        elif ford_select == 'Ka+':
            img = Image.open('car_img/ford/Ka+.jpg')
            st.image(img)
            st.write('현재 재고 데이터')
            car_search = df.loc[df['모델']==' Ka+',]
            st.dataframe(car_search)

        elif ford_select == 'Tourneo Custom':
            img = Image.open('car_img/ford/Tourneo Custom.jpg')
            st.image(img)
            st.write('현재 재고 데이터')
            car_search = df.loc[df['모델']==' Tourneo Custom',]
            st.dataframe(car_search)

        elif ford_select == 'S-MAX':
            img = Image.open('car_img/ford/S-MAX.jpg')
            st.image(img)
            st.write('현재 재고 데이터')
            car_search = df.loc[df['모델']==' S-MAX',]
            st.dataframe(car_search)

        elif ford_select == 'B-MAX':
            img = Image.open('car_img/ford/B-MAX.jpg')
            st.image(img)
            st.write('현재 재고 데이터')
            car_search = df.loc[df['모델']==' B-MAX',]
            st.dataframe(car_search)

        elif ford_select == 'Edge':
            img = Image.open('car_img/ford/Edge.jpg')
            st.image(img)
            st.write('현재 재고 데이터')
            car_search = df.loc[df['모델']==' Edge',]
            st.dataframe(car_search)

        elif ford_select == 'Tourneo Connect':
            img = Image.open('car_img/ford/Tourneo Connect.jpg')
            st.image(img)
            st.write('현재 재고 데이터')
            car_search = df.loc[df['모델']==' Tourneo Connect',]
            st.dataframe(car_search)

        elif ford_select == 'Grand C-MAX':
            img = Image.open('car_img/ford/Grand C-MAX.jpg')
            st.image(img)
            st.write('현재 재고 데이터')
            car_search = df.loc[df['모델']==' Grand C-MAX',]
            st.dataframe(car_search)

        elif ford_select == 'KA':
            img = Image.open('car_img/ford/KA.jpg')
            st.image(img)
            st.write('현재 재고 데이터')
            car_search = df.loc[df['모델']==' KA',]
            st.dataframe(car_search)

        elif ford_select == 'Galaxy':
            img = Image.open('car_img/ford/Galaxy.jpg')
            st.image(img)
            st.write('현재 재고 데이터')
            car_search = df.loc[df['모델']==' Galaxy',]
            st.dataframe(car_search)

        elif ford_select == 'Mustang':
            img = Image.open('car_img/ford/Mustang.jpg')
            st.image(img)
            st.write('현재 재고 데이터')
            car_search = df.loc[df['모델']==' Mustang',]
            st.dataframe(car_search)
            
        elif ford_select == 'Grand Tourneo Connect':
            img = Image.open('car_img/ford/Grand Tourneo Connect.jpg')
            st.image(img)
            st.write('현재 재고 데이터')
            car_search = df.loc[df['모델']==' Grand Tourneo Connect',]
            st.dataframe(car_search)

        elif ford_select == 'Fusion':
            img = Image.open('car_img/ford/Fusion.jpg')
            st.image(img)
            st.write('현재 재고 데이터')
            car_search = df.loc[df['모델']==' Fusion',]
            st.dataframe(car_search)

        elif ford_select == 'Ranger':
            img = Image.open('car_img/ford/Ranger.jpg')
            st.image(img)
            st.write('현재 재고 데이터')
            car_search = df.loc[df['모델']==' Ranger',]
            st.dataframe(car_search)

        elif ford_select == 'Streetka':
            img = Image.open('car_img/ford/Streetka.jpg')
            st.image(img)
            st.write('현재 재고 데이터')
            car_search = df.loc[df['모델']==' Streetka',]
            st.dataframe(car_search)

        elif ford_select == 'Escort':
            img = Image.open('car_img/ford/Escort.jpg')
            st.image(img)
            st.write('현재 재고 데이터')
            car_search = df.loc[df['모델']==' Escort',]
            st.dataframe(car_search)

        elif ford_select == 'Transit Tourneo':
            img = Image.open('car_img/ford/Transit Tourneo.jpg')
            st.image(img)
            st.write('현재 재고 데이터')
            car_search = df.loc[df['모델']==' Transit Tourneo',]
            st.dataframe(car_search)

        

    elif word.lower() == 'hyundai':
        hyundai_select = st.radio('모델을 선택하세요',hyundai_menu)
        if hyundai_select == 'I20':
            img = Image.open('car_img/hyundai/I20.jpg')
            st.image(img)
            st.write('현재 재고 데이터')
            car_search = df.loc[df['모델']==' I20',]
            st.dataframe(car_search)

        elif hyundai_select == 'Tucson':
            img = Image.open('car_img/hyundai/Tucson.jpg')
            st.image(img)
            st.write('현재 재고 데이터')
            car_search = df.loc[df['모델']==' Tucson',]
            st.dataframe(car_search)

        elif hyundai_select == 'I10':
            img = Image.open('car_img/hyundai/I10.jpg')
            st.image(img)
            st.write('현재 재고 데이터')
            car_search = df.loc[df['모델']==' I10',]
            st.dataframe(car_search)

        elif hyundai_select == 'IX35':
            img = Image.open('car_img/hyundai/IX35.jpg')
            st.image(img)
            st.write('현재 재고 데이터')
            car_search = df.loc[df['모델']==' IX35',]
            st.dataframe(car_search)

        elif hyundai_select == 'I30':
            img = Image.open('car_img/hyundai/I30.jpg')
            st.image(img)
            st.write('현재 재고 데이터')
            car_search = df.loc[df['모델']==' I30',]
            st.dataframe(car_search)

        elif hyundai_select == 'I40':
            img = Image.open('car_img/hyundai/I40.jpg')
            st.image(img)
            st.write('현재 재고 데이터')
            car_search = df.loc[df['모델']==' I40',]
            st.dataframe(car_search)

        elif hyundai_select == 'Ioniq':
            img = Image.open('car_img/hyundai/Ioniq.jpg')
            st.image(img)
            st.write('현재 재고 데이터')
            car_search = df.loc[df['모델']==' Ioniq',]
            st.dataframe(car_search)

        elif hyundai_select == 'Kona':
            img = Image.open('car_img/hyundai/Kona.jpg')
            st.image(img)
            st.write('현재 재고 데이터')
            car_search = df.loc[df['모델']==' Kona',]
            st.dataframe(car_search)

        elif hyundai_select == 'Veloster':
            img = Image.open('car_img/hyundai/Veloster.jpg')
            st.image(img)
            st.write('현재 재고 데이터')
            car_search = df.loc[df['모델']==' Veloster',]
            st.dataframe(car_search)

        elif hyundai_select == 'I800':
            img = Image.open('car_img/hyundai/I800.jpg')
            st.image(img)
            st.write('현재 재고 데이터')
            car_search = df.loc[df['모델']==' I800',]
            st.dataframe(car_search)

        elif hyundai_select == 'IX20':
            img = Image.open('car_img/hyundai/IX20.jpg')
            st.image(img)
            st.write('현재 재고 데이터')
            car_search = df.loc[df['모델']==' IX20',]
            st.dataframe(car_search)
            
        elif hyundai_select == 'Santa Fe':
            img = Image.open('car_img/hyundai/Santa Fe.jpg')
            st.image(img)
            st.write('현재 재고 데이터')
            car_search = df.loc[df['모델']==' Santa Fe',]
            st.dataframe(car_search)
            
        elif hyundai_select == 'Accent':
            img = Image.open('car_img/hyundai/Accent.jpg')
            st.image(img)
            st.write('현재 재고 데이터')
            car_search = df.loc[df['모델']==' Accent',]
            st.dataframe(car_search)

        elif hyundai_select == 'Terracan':
            img = Image.open('car_img/hyundai/Terracan.jpg')
            st.image(img)
            st.write('현재 재고 데이터')
            car_search = df.loc[df['모델']==' Terracan',]
            st.dataframe(car_search)

        elif hyundai_select == 'Getz':
            img = Image.open('car_img/hyundai/Getz.jpg')
            st.image(img)
            st.write('현재 재고 데이터')
            car_search = df.loc[df['모델']==' Getz',]
            st.dataframe(car_search)

        elif hyundai_select == 'Amica':
            img = Image.open('car_img/hyundai/Amica.jpg')
            st.image(img)
            st.write('현재 재고 데이터')
            car_search = df.loc[df['모델']==' Amica',]
            st.dataframe(car_search)


    elif word.lower() == 'benz':
        merc_select = st.radio('모델을 선택하세요',merc_menu)
        if merc_select == 'SLK':
            img = Image.open('car_img/benz/SLK.jpg')
            st.image(img)
            st.write('현재 재고 데이터')
            car_search = df.loc[df['모델']==' SLK',]
            st.dataframe(car_search)

        elif merc_select == 'S Class':
            img = Image.open('car_img/benz/S.jpg')
            st.image(img)
            st.write('현재 재고 데이터')
            car_search = df.loc[df['모델']==' S Class',]
            st.dataframe(car_search)

        elif merc_select == 'SL CLASS':
            img = Image.open('car_img/benz/SL.jpg')
            st.image(img)
            st.write('현재 재고 데이터')
            car_search = df.loc[df['모델']==' SL CLASS',]
            st.dataframe(car_search)

        elif merc_select == 'G Class':
            img = Image.open('car_img/benz/G.jpg')
            st.image(img)
            st.write('현재 재고 데이터')
            car_search = df.loc[df['모델']==' G Class',]
            st.dataframe(car_search)

        elif merc_select == 'GLE Class':
            img = Image.open('car_img/benz/GLE.jpg')
            st.image(img)
            st.write('현재 재고 데이터')
            car_search = df.loc[df['모델']==' GLE Class',]
            st.dataframe(car_search)

        elif merc_select == 'GLA Class':
            img = Image.open('car_img/benz/GLA.jpg')
            st.image(img)
            st.write('현재 재고 데이터')
            car_search = df.loc[df['모델']==' GLA Class',]
            st.dataframe(car_search)

        elif merc_select == 'A Class':
            img = Image.open('car_img/benz/A.jpg')
            st.image(img)
            st.write('현재 재고 데이터')
            car_search = df.loc[df['모델']==' A Class',]
            st.dataframe(car_search)

        elif merc_select == 'B Class':
            img = Image.open('car_img/benz/B.jpg')
            st.image(img)
            st.write('현재 재고 데이터')
            car_search = df.loc[df['모델']==' B Class',]
            st.dataframe(car_search)

        elif merc_select == 'GLC Class':
            img = Image.open('car_img/benz/GLC.jpg')
            st.image(img)
            st.write('현재 재고 데이터')
            car_search = df.loc[df['모델']==' GLC Class',]
            st.dataframe(car_search)

        elif merc_select == 'C Class':
            img = Image.open('car_img/benz/C.jpg')
            st.image(img)
            st.write('현재 재고 데이터')
            car_search = df.loc[df['모델']==' C Class',]
            st.dataframe(car_search)

        elif merc_select == 'E Class':
            img = Image.open('car_img/benz/E.jpg')
            st.image(img)
            st.write('현재 재고 데이터')
            car_search = df.loc[df['모델']==' E Class',]
            st.dataframe(car_search)

        elif merc_select == 'GL Class':
            img = Image.open('car_img/benz/GL.jpg')
            st.image(img)
            st.write('현재 재고 데이터')
            car_search = df.loc[df['모델']==' GL Class',]
            st.dataframe(car_search)

        elif merc_select == 'CLS Class':
            img = Image.open('car_img/benz/CLS.jpg')
            st.image(img)
            st.write('현재 재고 데이터')
            car_search = df.loc[df['모델']==' CLS Class',]
            st.dataframe(car_search)

        elif merc_select == 'CLC Class':
            img = Image.open('car_img/benz/CLC.jpg')
            st.image(img)
            st.write('현재 재고 데이터')
            car_search = df.loc[df['모델']==' CLC Class',]
            st.dataframe(car_search)

        elif merc_select == 'CLA Class':
            img = Image.open('car_img/benz/CLA.jpg')
            st.image(img)
            st.write('현재 재고 데이터')
            car_search = df.loc[df['모델']==' CLA Class',]
            st.dataframe(car_search)

        elif merc_select == 'V Class':
            img = Image.open('car_img/benz/V.jpg')
            st.image(img)
            st.write('현재 재고 데이터')
            car_search = df.loc[df['모델']==' V Class',]
            st.dataframe(car_search)

        elif merc_select == 'M Class':
            img = Image.open('car_img/benz/M.jpg')
            st.image(img)
            st.write('현재 재고 데이터')
            car_search = df.loc[df['모델']==' M Class',]
            st.dataframe(car_search)

        elif merc_select == 'CL Class':
            img = Image.open('car_img/benz/CL.jpg')
            st.image(img)
            st.write('현재 재고 데이터')
            car_search = df.loc[df['모델']==' CL Class',]
            st.dataframe(car_search)

        elif merc_select == 'GLS Class':
            img = Image.open('car_img/benz/GLS.jpg')
            st.image(img)
            st.write('현재 재고 데이터')
            car_search = df.loc[df['모델']==' GLS Class',]
            st.dataframe(car_search)

        elif merc_select == 'GLB Class':
            img = Image.open('car_img/benz/GLB.jpg')
            st.image(img)
            st.write('현재 재고 데이터')
            car_search = df.loc[df['모델']==' GLB Class',]
            st.dataframe(car_search)

        elif merc_select == 'X-CLASS':
            img = Image.open('car_img/benz/X.jpg')
            st.image(img)
            st.write('현재 재고 데이터')
            car_search = df.loc[df['모델']==' X Class',]
            st.dataframe(car_search)

        elif merc_select == '180':
            img = Image.open('car_img/benz/180.jpg')
            st.image(img)
            st.write('현재 재고 데이터')
            car_search = df.loc[df['모델']=='180',]
            st.dataframe(car_search)

        elif merc_select == 'CLK':
            img = Image.open('car_img/benz/CLK.jpg')
            st.image(img)
            st.write('현재 재고 데이터')
            car_search = df.loc[df['모델']==' CLK',]
            st.dataframe(car_search)

        elif merc_select == 'R Class':
            img = Image.open('car_img/benz/R.jpg')
            st.image(img)
            st.write('현재 재고 데이터')
            car_search = df.loc[df['모델']==' R Class',]
            st.dataframe(car_search)

        elif merc_select == '230':
            img = Image.open('car_img/benz/230.jpg')
            st.image(img)
            st.write('현재 재고 데이터')
            car_search = df.loc[df['모델']=='230',]
            st.dataframe(car_search)

        elif merc_select == '220':
            img = Image.open('car_img/benz/220.jpg')
            st.image(img)
            st.write('현재 재고 데이터')
            car_search = df.loc[df['모델']=='220',]
            st.dataframe(car_search)

        elif merc_select == '200':
            img = Image.open('car_img/benz/200.jpg')
            st.image(img)
            st.write('현재 재고 데이터')
            car_search = df.loc[df['모델']=='200',]
            st.dataframe(car_search)

            
    elif word.lower() == 'toyota':
        toyota_select = st.radio('모델을 선택하세요',toyota_menu)
        if toyota_select == 'GT86':
            img = Image.open('car_img/toyota/GT86.jpg')
            st.image(img)
            st.write('현재 재고 데이터')
            car_search = df.loc[df['모델']==' GT86',]
            st.dataframe(car_search)

        elif toyota_select == 'Corolla':
            img = Image.open('car_img/toyota/Corolla.jpg')
            st.image(img)
            st.write('현재 재고 데이터')
            car_search = df.loc[df['모델']==' Corolla',]
            st.dataframe(car_search)

        elif toyota_select == 'RAV4':
            img = Image.open('car_img/toyota/RAV4.jpg')
            st.image(img)
            st.write('현재 재고 데이터')
            car_search = df.loc[df['모델']==' RAV4',]
            st.dataframe(car_search)

        elif toyota_select == 'Yaris':
            img = Image.open('car_img/toyota/Yaris.jpg')
            st.image(img)
            st.write('현재 재고 데이터')
            car_search = df.loc[df['모델']==' Yaris',]
            st.dataframe(car_search)

        elif toyota_select == 'Auris':
            img = Image.open('car_img/toyota/Auris.jpg')
            st.image(img)
            st.write('현재 재고 데이터')
            car_search = df.loc[df['모델']==' Auris',]
            st.dataframe(car_search)

        elif toyota_select == 'Aygo':
            img = Image.open('car_img/toyota/Aygo.jpg')
            st.image(img)
            st.write('현재 재고 데이터')
            car_search = df.loc[df['모델']==' Aygo',]
            st.dataframe(car_search)

        elif toyota_select == 'C-HR':
            img = Image.open('car_img/toyota/C-HR.jpg')
            st.image(img)
            st.write('현재 재고 데이터')
            car_search = df.loc[df['모델']==' C-HR',]
            st.dataframe(car_search)

        elif toyota_select == 'Prius':
            img = Image.open('car_img/toyota/Prius.jpg')
            st.image(img)
            st.write('현재 재고 데이터')
            car_search = df.loc[df['모델']==' Prius',]
            st.dataframe(car_search)
            
        elif toyota_select == 'Avensis':
            img = Image.open('car_img/toyota/Avensis.jpg')
            st.image(img)
            st.write('현재 재고 데이터')
            car_search = df.loc[df['모델']==' Avensis',]
            st.dataframe(car_search)

        elif toyota_select == 'Verso':
            img = Image.open('car_img/toyota/Verso.jpg')
            st.image(img)
            st.write('현재 재고 데이터')
            car_search = df.loc[df['모델']==' Verso',]
            st.dataframe(car_search)

        elif toyota_select == 'Hilux':
            img = Image.open('car_img/toyota/Hilux.jpg')
            st.image(img)
            st.write('현재 재고 데이터')
            car_search = df.loc[df['모델']==' Hilux',]
            st.dataframe(car_search)

        elif toyota_select == 'PROACE VERSO':
            img = Image.open('car_img/toyota/PROACE VERSO.jpg')
            st.image(img)
            st.write('현재 재고 데이터')
            car_search = df.loc[df['모델']==' PROACE VERSO',]
            st.dataframe(car_search)

        elif toyota_select == 'Land Cruiser':
            img = Image.open('car_img/toyota/Land Cruiser.jpg')
            st.image(img)
            st.write('현재 재고 데이터')
            car_search = df.loc[df['모델']==' Land Cruiser',]
            st.dataframe(car_search)

        elif toyota_select == 'Supra':
            img = Image.open('car_img/toyota/Supra.jpg')
            st.image(img)
            st.write('현재 재고 데이터')
            car_search = df.loc[df['모델']==' Supra',]
            st.dataframe(car_search)

        elif toyota_select == 'Camry':
            img = Image.open('car_img/toyota/Camry.jpg')
            st.image(img)
            st.write('현재 재고 데이터')
            car_search = df.loc[df['모델']==' Camry',]
            st.dataframe(car_search)

        elif toyota_select == 'Verso-S':
            img = Image.open('car_img/toyota/Verso-S.jpg')
            st.image(img)
            st.write('현재 재고 데이터')
            car_search = df.loc[df['모델']==' Verso-S',]
            st.dataframe(car_search)

        elif toyota_select == 'IQ':
            img = Image.open('car_img/toyota/IQ.jpg')
            st.image(img)
            st.write('현재 재고 데이터')
            car_search = df.loc[df['모델']==' IQ',]
            st.dataframe(car_search)

        elif toyota_select == 'Urban Cruiser':
            img = Image.open('car_img/toyota/Urban Cruiser.jpg')
            st.image(img)
            st.write('현재 재고 데이터')
            car_search = df.loc[df['모델']==' Urban Cruiser',]
            st.dataframe(car_search)




    