# 포켓몬 게임 개발 시작(240929)
# streamlit run pkmon_game.py
# https://adventure.streamlit.app/ 참고하기
import pandas as pd
import numpy as np
import random
import streamlit as st
from PIL import Image 
import time

@st.cache_data()
def random_make():
    
    list_l = []

    for i in range(1,998):
        list_l.append(i)

    random.shuffle(list_l)

    answer_list = list_l[0:10]
    wrong_list = list_l[10:40]

    return answer_list, wrong_list

@st.cache_data()
def random_make2(listx):

    random.shuffle(listx)

    return listx

@st.cache_data()
def random_make3(answer_list,wrong_list):

    result = []

    quiz_wrong = np.array_split(wrong_list, 10)

    #map 함수 사용하기 : list(map(함수,list))

    quiz_wrong_n = list(map(list,quiz_wrong))

    for i in range(len(answer_list)):

        arg1 = answer_list[i]
        arg2_1, arg2_2, arg2_3 = quiz_wrong_n[i]

        new_tuple = (arg1, arg2_1, arg2_2, arg2_3)

        new_list = list(new_tuple)

        random.shuffle(new_list)

        result.append(new_list)

    return result


def quiz(): 
    for index,x in enumerate(answer_list):
        # Replace the chart with several elements:
        with placeholder.container():
            st.write(f"{index+1}번째 문제입니다.")
            st.write(df['Name'][x-1])
            sidebarlogo = Image.open(f'{x}.png').resize((300, 300))
            st.image(sidebarlogo, use_column_width='auto',)
            listx = [df['Name'][x-1], df['Name'][wrong_list[0]-1],df['Name'][wrong_list[1]-1],df['Name'] [wrong_list[2]-1]]
            list_f = random_make2(listx)
            st.dataframe(listx)
            try:
                answer_n = int(st.number_input('정답 번호를 입력하세요.'))
                answer = listx[answer_n-1]
            except:
                answer = None
                st.write('1~4까지 숫자만 입력하세요.')
            #status = st.radio('정답을 맞추세요', list_f)
            if answer:
                if answer == df['Name'][x-1]:
                    st.info('정답입니다.')
                    answer = None
                else:
                    st.warning('오답입니다.')
                    answer = None

            time.sleep(5)
            # Clear all those elements:
            placeholder.empty()

def quiz_one(index,quiz_list,answer): 

    #with placeholder.container():
    st.write(f"{index}번째 문제입니다.")
    #status = st.radio('정답을 맞추세요', quiz_list)
    #st.write(answer)
    #if status == answer:
    #    st.info('정답입니다.')
    #    st.session_state["stage"] = st.session_state["stage"]+1
    #    st.session_state["health"] = st.session_state["health"]+10
    #else:
    #    st.warning('오답입니다.')
    #    st.session_state["stage"] = st.session_state["stage"]+1
    #    st.session_state["health"] = st.session_state["health"]-10
    #answer_n = None
    #answer_tmp = None

    for index,i in enumerate(quiz_list):
        st.write(f'{index+1}.{i}')

    try:
        answer_n = int(st.text_input('정답 번호를 입력하세요.'))
        answer_tmp = quiz_list[answer_n-1]
    except:
        answer_n = None
        answer_tmp = None
        st.write('1~4까지 숫자만 입력하세요.')
    #status = st.radio('정답을 맞추세요', list_f)
    else:
        if answer_tmp == answer:
            st.info('정답입니다.')
            st.session_state["stage"] = st.session_state["stage"]+1
            st.session_state["health"] = st.session_state["health"]+10
        else:
            st.warning('오답입니다.')
            st.session_state["stage"] = st.session_state["stage"]+1
            st.session_state["health"] = st.session_state["health"]-10

    time.sleep(3)
    #placeholder.empty()


    #answer_n = int(st.number_input('정답 번호를 입력하세요.'))
    #if answer_n==1:
    #    st.write(answer_n)
    #    st.session_state["stage"] = st.session_state["stage"]+1
    #time.sleep(5)
    #st.empty()
    ## Clear all those elements:
    #placeholder.empty()

if __name__=='__main__':
    
    # 페이지 기본 설정

    st.set_page_config(
        page_title="석진/하진 포켓몬 게임",
        layout="wide",
        page_icon= "37.png"
    )

    if "health" not in st.session_state:
        st.session_state["health"] = 100
    if "name" not in st.session_state:
        st.session_state["name"] = '아무개'
    if "stage" not in st.session_state:
        st.session_state["stage"] = 1
    if "start" not in st.session_state:
        st.session_state["start"] = 0

    horizontal_bar = "<hr style='margin-top: 0; margin-bottom: 0; height: 1px; border: 1px solid #635985;'><br>"    # thin divider line

    with st.sidebar:
        mystate = st.session_state
        #st.subheader(f"🖼️ Pix Match: {mystate.GameDetails[0]}")
        st.subheader(f"🖼️ Pix Match:")
        st.markdown(horizontal_bar, True)

        name = st.text_input("이름을 입력하세요.")

        st.session_state["name"] = name

        if st.button("시작 하기"):
            st.session_state["start"] = 1

        if st.button("새게임 하기"):
            st.session_state.clear()
            st.cache_data.clear()
            st.cache_resource.clear()
            st.session_state["health"] = 100
            st.session_state["name"] = '아무개'
            st.session_state["stage"] = 1
            st.session_state["start"] = 0
            
    st.title(':blue[_석진_ _하진_] :red[포켓몬] 게임')

    #st.header("석진 하진 포켓몬 게임")
    st.subheader(f":blue[신나는 모험]이 이제 시작됩니다!")

    placeholder = st.empty()

    df = pd.read_csv('포켓몬이름_New_998.csv',encoding='utf-8')

    start = st.session_state["start"]

    if start != 1:
        st.stop()

    else:
        answer_list,wrong_list = random_make()


        #map 함수 사용하기 : list(map(함수,list))
        answer_list2 =[]
        answer_list2 = list(map(lambda x: df["Name"][x-1],answer_list))

        wrong_list2 =[]
        wrong_list2 = list(map(lambda x: df["Name"][x-1],wrong_list))

        st.write(answer_list2)

        list_f = random_make3(answer_list2,wrong_list2)

        st.write(answer_list2[0])
        st.write(list_f[0])

        #st.write(list_f)
        
        for x,y in zip(answer_list,wrong_list):
            #quiz_list = [x,y]
            placeholder.empty()

            with placeholder.container():

                if st.session_state['stage'] == 1:
                    placeholder.empty()
                    with placeholder.container():
                        quiz_one(st.session_state["stage"],list_f[0],answer_list2[0])
                elif st.session_state['stage'] == 2:
                    placeholder.empty()
                    with placeholder.container():
                        quiz_one(st.session_state["stage"],list_f[1],answer_list2[1])
                elif st.session_state['stage'] == 3:
                    placeholder.empty()
                    with placeholder.container():
                        quiz_one(st.session_state["stage"],list_f[2],answer_list2[2])
                elif st.session_state['stage'] == 4:
                    placeholder.empty()
                    with placeholder.container():
                        quiz_one(st.session_state["stage"],list_f[3],answer_list2[3])        
                elif st.session_state['stage'] == 5:
                    placeholder.empty()
                    with placeholder.container():
                        quiz_one(st.session_state["stage"],list_f[4],answer_list2[4])
                elif st.session_state['stage'] == 6:
                    placeholder.empty()
                    with placeholder.container():
                        quiz_one(st.session_state["stage"],list_f[5],answer_list2[5])
                elif st.session_state['stage'] == 7:
                    placeholder.empty()
                    with placeholder.container():
                        quiz_one(st.session_state["stage"],list_f[6],answer_list2[6])
                elif st.session_state['stage'] == 8:
                    placeholder.empty()
                    with placeholder.container():
                        quiz_one(st.session_state["stage"],list_f[7],answer_list2[7])
                elif st.session_state['stage'] == 9:
                    placeholder.empty()
                    with placeholder.container():
                        quiz_one(st.session_state["stage"],list_f[8],answer_list2[8])
                elif st.session_state['stage'] == 10:
                    placeholder.empty()
                    with placeholder.container():
                        quiz_one(st.session_state["stage"],list_f[9],answer_list2[9])
                else:
                    placeholder.empty()
                    with placeholder.container():
                        final_score = st.session_state["health"]
                        user = st.session_state["name"]
                        st.write(f'축하합니다. {user}님')
                        st.write(f'최종 점수는 {final_score}점 입니다.')
                    

        #if st.session_state.stage ==1:
        #    quiz_one()
#
        #with st.empty():
        #    for seconds in range(3):
        #        st.write(f"⏳ {seconds} seconds have passed")
        #        time.sleep(1)
        #    st.write("✔️ 1 minute over!")
        #    st.write(st.session_state["name"])