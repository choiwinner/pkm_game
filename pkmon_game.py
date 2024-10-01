# 포켓몬 게임 개발 시작(240929)
# streamlit run pkmon_game.py
# https://adventure.streamlit.app/ 참고하기
import pandas as pd
import numpy as np
import random
import streamlit as st
from PIL import Image 

@st.cache_data()
def random_make():
    fig = random.randint(1,1252)
    
    list_l = []
    for i in range(1,1253):
        list_l.append(i)

    random.shuffle(list_l)

    answer_list = list_l[0:10]
    wrong_list = list_l[10:]

    return answer_list, wrong_list

@st.cache_data()
def random_make2(listx):

    random.shuffle(listx)

    return listx

if __name__=='__main__':
    
    # 페이지 기본 설정
    im_t = Image.open("37.png")    ##이미지 불러오기

    st.set_page_config(
        page_title="🔎석진/하진 포켓몬 게임",
        layout="wide",
        page_icon= im_t
    )

    horizontal_bar = "<hr style='margin-top: 0; margin-bottom: 0; height: 1px; border: 1px solid #635985;'><br>"    # thin divider line

    with st.sidebar:
        mystate = st.session_state
        #st.subheader(f"🖼️ Pix Match: {mystate.GameDetails[0]}")
        st.subheader(f"🖼️ Pix Match:")
        st.markdown(horizontal_bar, True)
        if st.button("새게임 하기"):
            st.session_state.clear()
            st.cache_data.clear()
            st.cache_resource.clear()

    
    st.header("석진 하진 포켓몬 게임")
    st.subheader(f"신나는 모험이 이제 시작됩니다!")

    df = pd.read_csv('포켓몬이름.csv',encoding='utf-8')

    answer_list,wrong_list = random_make()

    for index,x in enumerate(answer_list):
        st.write(f"{index+1}번째 문제입니다.")
        st.write(df['Name'][x-1])
        sidebarlogo = Image.open(f'{x}.png').resize((500, 590))
        st.image(sidebarlogo, use_column_width='auto',)

        listx = [df['Name'][x-1], df['Name'][wrong_list[0]-1],df['Name'][wrong_list[1]-1],df['Name'][wrong_list[2]-1]]
        list_f = random_make2(listx)

        status = st.radio('정답을 맞추세요', list_f)
        if status == df['Name'][x-1]:
            st.info('정답입니다.')
        else:
            st.warning('오답입니다.')
        
        st.empty()
        st.session_state.clear()
        
    st.dataframe(df)