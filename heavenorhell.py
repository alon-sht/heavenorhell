# %%
import streamlit as st
from random import randint
import time


st.set_page_config(
            page_title="Heaven Or Hell",
        )
hide_streamlit_style = """
                    <style>
                    #MainMenu {visibility: hidden;}
                    footer {visibility: hidden;}
                            }
                    </style>
                    """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)



# %%

st.title("Heaven or Hell")

how=st.radio("Choose a song",options=['Insert YouTube URL','Use default song'],key='how')
if how=='Insert YouTube URL':
    song=st.text_input("Insert YouTube URL for the song you want")
elif how=='Use default song'    :
    song='https://www.youtube.com/watch?v=usErwHORDHQ'
st.markdown("---")
vid=st.empty()
st.session_state['playing']=False

min1=st.empty()
max1=st.empty()
stop=False
if song:
    vid.video(song)
if not stop:
    min=min1.number_input("Minimum Stop Time (sec)",min_value=0,max_value=60,value=5,key='min')
    max=max1.number_input("Maximum Stop Time (sec)",min_value=0,max_value=60,value=20,key='max')
button=st.empty()
countdown=st.checkbox("Show Countdown")
if countdown:
    metric=st.empty()
start=button.button("Start")
if start:
    x=randint(min,max)
    for i in range(1,x+1):
        time.sleep(1)
        if countdown:
            metric.metric("",x-i)
    stop=True
    min1.markdown('')
    max1.markdown('')
    vid.error('# Stop!')
    restart=button.button("Restart")
    
    if restart:
        vid.video(song)
        stop=False

