import requests
import streamlit as st
from streamlit_lottie import st_lottie

st.set_page_config(page_title="My Webpage", page_icon=":beginner:", layout="wide")
def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()
        # ---- LOAD ASSETS ----
lottie_coding = load_lottieurl("https://assets10.lottiefiles.com/packages/lf20_o1ebw8km.json")

with st.container():
    st.subheader("Hi, I am sai preetham r v :wave:")
    st.title("B.Tech undergrad ")
    st.write(
        "I'm a Mechanical Engineering Undergrad at PES University with a flair for automobile engineering. I hold a good grasp of automotive components and machineries and possess the ability to absorb the concerned problem at first instance thereby providing the suitable remedial measure to the problem.")
    st.write("[Learn More >](https://preetham.live)")

    with st.container():
        st.write("---")
        left_column, right_column = st.columns(2)
    with left_column:
        st.header("What I do")
        st.write("##")
        st.write(
            """             
            - currently working on eeg controlled prosthetic arm
            - looking to geek out on jdm
            - fascinated about anything with an engine
            - If this sounds interesting to you, do contact me on Linkedin.
            """
        )
        st.write("[My Linkedin >](https://www.linkedin.com/in/preetham-r-v-96b989245/)")
        with right_column:
         st_lottie(lottie_coding, height=300, key="coding")


    
   