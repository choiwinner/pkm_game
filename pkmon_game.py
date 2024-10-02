# 포켓몬 게임 개발 시작(240929)
# streamlit run pkmon_game.py
# https://adventure.streamlit.app/ 참고하기
import pandas as pd
import numpy as np
import random
import streamlit as st
from PIL import Image 
import time
#import stagen

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

def Init():

    if "health" not in st.session_state:
        st.session_state["health"] = 0
    if "name" not in st.session_state:
        st.session_state["name"] = '아무개'
    if "stage" not in st.session_state:
        st.session_state["stage"] = 1
    if "start" not in st.session_state:
        st.session_state["start"] = 0
    if "answer_n" not in st.session_state:
        st.session_state["answer_n"] = 0
    if "answer" not in st.session_state:
        st.session_state["answer"] = ''

def quiz_one1(index_n,quiz_list,answer,img_1): 

    #with placeholder.container():
    #st.write(f"{index_n}번째 문제입니다.")
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

    #st.session_state["answer_n"] = 0
    #st.session_state["answer"] = ''

    input_container = st.empty()

    st.write(f"{index_n}번째 문제입니다.")
    st.write(answer)

    # 이미지 파일을 불러옵니다.
    image_a = Image.open(f"{img_1}.png").resize((150,150))
    # 이미지를 표시합니다.
    st.image(image_a) 

    for index,i in enumerate(quiz_list):
        st.write(f'{index+1}. {i}')

    if val1 := int(st.number_input('정답 번호를 입력하세요.',key='key1')):

        if quiz_list[val1-1] == answer:
            st.info('정답입니다.')
            st.session_state["stage"] = st.session_state["stage"]+1
            st.session_state["health"] = st.session_state["health"]+10
            time.sleep(2)
            st.rerun()
        else:
            st.warning('오답입니다.')
            st.session_state["stage"] = st.session_state["stage"]+1
            time.sleep(2)
            st.rerun()
    

def quiz_one2(index_n,quiz_list,answer,img_1): 

    st.write(f"{index_n}번째 문제입니다.")
    st.write(answer)

    # 이미지 파일을 불러옵니다.
    image_a = Image.open(f"{img_1}.png").resize((150,150))
    # 이미지를 표시합니다.
    st.image(image_a)     

    for index,i in enumerate(quiz_list):
        st.write(f'{index+1}. {i}')

    if val2 := int(st.number_input('정답 번호를 입력하세요.',key='key2')):

        if quiz_list[val2-1] == answer:
            st.info('정답입니다.')
            st.session_state["stage"] = st.session_state["stage"]+1
            st.session_state["health"] = st.session_state["health"]+10
            time.sleep(2)
            st.rerun()
        else:
            st.warning('오답입니다.')
            st.session_state["stage"] = st.session_state["stage"]+1
            time.sleep(2)
            st.rerun()

def quiz_one3(index_n,quiz_list,answer,img_1): 

    st.write(f"{index_n}번째 문제입니다.")
    st.write(answer)

    # 이미지 파일을 불러옵니다.
    image_a = Image.open(f"{img_1}.png").resize((150,150))
    # 이미지를 표시합니다.
    st.image(image_a)
    
    for index,i in enumerate(quiz_list):
        st.write(f'{index+1}. {i}')

    if val3 := int(st.number_input('정답 번호를 입력하세요.',key='key3')):

        if quiz_list[val3-1] == answer:
            st.info('정답입니다.')
            st.session_state["stage"] = st.session_state["stage"]+1
            st.session_state["health"] = st.session_state["health"]+10
            time.sleep(2)
            st.rerun()
        else:
            st.warning('오답입니다.')
            st.session_state["stage"] = st.session_state["stage"]+1
            time.sleep(2)
            st.rerun()

def quiz_one4(index_n,quiz_list,answer,img_1): 

    st.write(f"{index_n}번째 문제입니다.")
    st.write(answer)

    # 이미지 파일을 불러옵니다.
    image_a = Image.open(f"{img_1}.png").resize((150,150))
    # 이미지를 표시합니다.
    st.image(image_a)     

    for index,i in enumerate(quiz_list):
        st.write(f'{index+1}. {i}')

    if val4 := int(st.number_input('정답 번호를 입력하세요.',key='key4')):

        if quiz_list[val4-1] == answer:
            st.info('정답입니다.')
            st.session_state["stage"] = st.session_state["stage"]+1
            st.session_state["health"] = st.session_state["health"]+10
            time.sleep(2)
            st.rerun()
        else:
            st.warning('오답입니다.')
            st.session_state["stage"] = st.session_state["stage"]+1
            time.sleep(2)
            st.rerun()

def quiz_one5(index_n,quiz_list,answer,img_1): 

    st.write(f"{index_n}번째 문제입니다.")
    st.write(answer)

    # 이미지 파일을 불러옵니다.
    image_a = Image.open(f"{img_1}.png").resize((150,150))
    # 이미지를 표시합니다.
    st.image(image_a)    

    for index,i in enumerate(quiz_list):
        st.write(f'{index+1}. {i}')

    if val5 := int(st.number_input('정답 번호를 입력하세요.',key='key5')):

        if quiz_list[val5-1] == answer:
            st.info('정답입니다.')
            st.session_state["stage"] = st.session_state["stage"]+1
            st.session_state["health"] = st.session_state["health"]+10
            time.sleep(2)
            st.rerun()
        else:
            st.warning('오답입니다.')
            st.session_state["stage"] = st.session_state["stage"]+1
            time.sleep(2)
            st.rerun()

def quiz_one6(index_n,quiz_list,answer,img_1): 

    st.write(f"{index_n}번째 문제입니다.")
    st.write(answer)

    # 이미지 파일을 불러옵니다.
    image_a = Image.open(f"{img_1}.png").resize((150,150))
    # 이미지를 표시합니다.
    st.image(image_a)     

    for index,i in enumerate(quiz_list):
        st.write(f'{index+1}. {i}')

    if val6 := int(st.number_input('정답 번호를 입력하세요.',key='key6')):

        if quiz_list[val6-1] == answer:
            st.info('정답입니다.')
            st.session_state["stage"] = st.session_state["stage"]+1
            st.session_state["health"] = st.session_state["health"]+10
            time.sleep(2)
            st.rerun()
        else:
            st.warning('오답입니다.')
            st.session_state["stage"] = st.session_state["stage"]+1
            time.sleep(2)
            st.rerun()

def quiz_one7(index_n,quiz_list,answer,img_1): 

    st.write(f"{index_n}번째 문제입니다.")
    st.write(answer)

    # 이미지 파일을 불러옵니다.
    image_a = Image.open(f"{img_1}.png").resize((150,150))
    # 이미지를 표시합니다.
    st.image(image_a)       

    for index,i in enumerate(quiz_list):
        st.write(f'{index+1}. {i}')

    if val7 := int(st.number_input('정답 번호를 입력하세요.',key='key7')):

        if quiz_list[val7-1] == answer:
            st.info('정답입니다.')
            st.session_state["stage"] = st.session_state["stage"]+1
            st.session_state["health"] = st.session_state["health"]+10
            time.sleep(2)
            st.rerun()
        else:
            st.warning('오답입니다.')
            st.session_state["stage"] = st.session_state["stage"]+1
            time.sleep(2)
            st.rerun()

def quiz_one8(index_n,quiz_list,answer,img_1): 

    st.write(f"{index_n}번째 문제입니다.")
    st.write(answer)

    # 이미지 파일을 불러옵니다.
    image_a = Image.open(f"{img_1}.png").resize((150,150))
    # 이미지를 표시합니다.
    st.image(image_a)       

    for index,i in enumerate(quiz_list):
        st.write(f'{index+1}. {i}')

    if val8 := int(st.number_input('정답 번호를 입력하세요.',key='key8')):

        if quiz_list[val8-1] == answer:
            st.info('정답입니다.')
            st.session_state["stage"] = st.session_state["stage"]+1
            st.session_state["health"] = st.session_state["health"]+10
            time.sleep(2)
            st.rerun()
        else:
            st.warning('오답입니다.')
            st.session_state["stage"] = st.session_state["stage"]+1
            time.sleep(2)
            st.rerun()

def quiz_one9(index_n,quiz_list,answer,img_1): 

    st.write(f"{index_n}번째 문제입니다.")
    st.write(answer)

    # 이미지 파일을 불러옵니다.
    image_a = Image.open(f"{img_1}.png").resize((150,150))
    # 이미지를 표시합니다.
    st.image(image_a)   

    for index,i in enumerate(quiz_list):
        st.write(f'{index+1}. {i}')

    if val9 := int(st.number_input('정답 번호를 입력하세요.',key='key9')):

        if quiz_list[val9-1] == answer:
            st.info('정답입니다.')
            st.session_state["stage"] = st.session_state["stage"]+1
            st.session_state["health"] = st.session_state["health"]+10
            time.sleep(2)
            st.rerun()
        else:
            st.warning('오답입니다.')
            st.session_state["stage"] = st.session_state["stage"]+1
            time.sleep(2)
            st.rerun()

def quiz_one10(index_n,quiz_list,answer,img_1): 

    st.write(f"{index_n}번째 문제입니다.")
    st.write(answer)

    # 이미지 파일을 불러옵니다.
    image_a = Image.open(f"{img_1}.png").resize((150,150))
    # 이미지를 표시합니다.
    st.image(image_a)       

    for index,i in enumerate(quiz_list):
        st.write(f'{index+1}. {i}')

    if val10 := int(st.number_input('정답 번호를 입력하세요.',key='key10')):

        if quiz_list[val10-1] == answer:
            st.info('정답입니다.')
            st.session_state["stage"] = st.session_state["stage"]+1
            st.session_state["health"] = st.session_state["health"]+10
            time.sleep(2)
            st.rerun()
        else:
            st.warning('오답입니다.')
            st.session_state["stage"] = st.session_state["stage"]+1
            time.sleep(2)
            st.rerun()

if __name__=='__main__':
    
    # 페이지 기본 설정

    st.set_page_config(
        page_title="석진/하진 포켓몬 게임",
        layout="wide",
        page_icon= "37.png"
    )

    horizontal_bar = "<hr style='margin-top: 0; margin-bottom: 0; height: 1px; border: 1px solid #635985;'><br>"    # thin divider line

    Init()

    with st.sidebar:
        mystate = st.session_state
        #st.subheader(f"🖼️ Pix Match: {mystate.GameDetails[0]}")
        st.subheader("포켓몬 센터")
        st.markdown(horizontal_bar, True)

        name = st.text_input("이름을 입력하세요.")

        st.session_state["name"] = name

        if st.button("시작 하기"):
            st.session_state["start"] = 1
            st.session_state["health"] = 0
            st.session_state["stage"] = 1
            st.cache_data.clear()
            st.cache_resource.clear()
            st.write('시작')

        #if st.button("새게임 하기"):
        #    st.session_state.clear()
        #    st.cache_data.clear()
        #    st.cache_resource.clear()
        #    st.session_state.clear()
            
    st.title(':blue[_석진_ _하진_] :red[포켓몬] 게임')

    #st.header("석진 하진 포켓몬 게임")
    st.subheader(f":blue[신나는 모험]이 이제 시작됩니다!")

    placeholder = st.empty()

    df = pd.read_csv('포켓몬이름_New_998.csv',encoding='utf-8')

    #start = st.session_state["start"]

    if st.session_state["start"] != 1:
        st.stop()

    else:
        answer_list,wrong_list = random_make()


        #map 함수 사용하기 : list(map(함수,list))
        answer_list2 =[]
        answer_list2 = list(map(lambda x: df["Name"][x-1],answer_list))

        wrong_list2 =[]
        wrong_list2 = list(map(lambda x: df["Name"][x-1],wrong_list))

        list_f = random_make3(answer_list2,wrong_list2)

        if st.session_state['stage'] == 1:
            placeholder.empty()
            with placeholder.container():
                quiz_one1(st.session_state["stage"],list_f[0],answer_list2[0],answer_list[0])
        elif st.session_state['stage'] == 2:
            placeholder.empty()
            with placeholder.container():
                quiz_one2(st.session_state["stage"],list_f[1],answer_list2[1],answer_list[1])
        elif st.session_state['stage'] == 3:
            placeholder.empty()
            with placeholder.container():
                quiz_one3(st.session_state["stage"],list_f[2],answer_list2[2],answer_list[2])
        elif st.session_state['stage'] == 4:
            placeholder.empty()
            with placeholder.container():
                quiz_one4(st.session_state["stage"],list_f[3],answer_list2[3],answer_list[3])        
        elif st.session_state['stage'] == 5:
            placeholder.empty()
            with placeholder.container():
                quiz_one5(st.session_state["stage"],list_f[4],answer_list2[4],answer_list[4])
        elif st.session_state['stage'] == 6:
            placeholder.empty()
            with placeholder.container():
                quiz_one6(st.session_state["stage"],list_f[5],answer_list2[5],answer_list[5])
        elif st.session_state['stage'] == 7:
            placeholder.empty()
            with placeholder.container():
                quiz_one7(st.session_state["stage"],list_f[6],answer_list2[6],answer_list[6])
        elif st.session_state['stage'] == 8:
            placeholder.empty()
            with placeholder.container():
                quiz_one8(st.session_state["stage"],list_f[7],answer_list2[7],answer_list[7])
        elif st.session_state['stage'] == 9:
            placeholder.empty()
            with placeholder.container():
                quiz_one9(st.session_state["stage"],list_f[8],answer_list2[8],answer_list[8])
        elif st.session_state['stage'] == 10:
            placeholder.empty()
            with placeholder.container():
                quiz_one10(st.session_state["stage"],list_f[9],answer_list2[9],answer_list[9])
        else:
            placeholder.empty()
            with placeholder.container():
                final_score = st.session_state["health"]
                user = st.session_state["name"]
                if final_score >= 90:
                    st.write(f'{user}님 당신은 진정한 :blue[포켓몬 지식왕!!]')
                    st.write(f'최종 점수는 :red[{final_score}]점 입니다.')
                
                elif final_score >= 70:
                    st.write(f'{user}님 포켓몬 좀 아시는 군요!!')
                    st.write(f'최종 점수는 :red[{final_score}]점 입니다.')

                elif final_score >= 50:
                    st.warning(f'{user}님 포켓몬 공부가 필요해요!')
                    st.write(f'최종 점수는 :red[{final_score}]점 입니다.')

                else:
                    st.error(f'{user}님 당신은 포린이네요 ㅠㅠ')
                    st.write(f'최종 점수는 :red[{final_score}]점 입니다.')             
        
                st.stop()