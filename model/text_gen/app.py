from pprint import pprint
import nltk
import streamlit as st
import sys
import parse
import random  # Import the random module

st.set_page_config(layout="wide")

def generate_questions(payload):
    nltk.download('stopwords')
    sys.path.append('../text_gen/')
    from main import QGen
    question_generation = QGen()
    if payload == "'input_text':":
        return "Please enter some text to generate questions"
    output = question_generation.predict_mcq(payload)
    return output

def Streamlit():
    col1, col2 = st.columns(2)

    with col1:
        st.header('Generate your questions here')
        input_text = st.text_area('Input Text', height=500)
        payload = {"input_text": input_text}
        if st.button('Generate Questions'):
            out = generate_questions(payload)
            st.session_state.out = out  # Store the result in session_state

    with col2:
        st.header('Output Text')
        out = st.session_state.get('out', None)  # Retrieve the result from session_state
        if out is not None:
            o = parse.parsing(out)
            for i in o.keys():
                mcqs = []  # Initialize mcqs list for each question
                st.write(i, ":", o[i]["Question:"])
                mcqs.append(o[i]["Correct Answer:"].capitalize())
                for y in o[i]["Options:"]:
                    mcqs.append(y)
                num = 0
                answer = st.radio("a", mcqs, label_visibility='hidden')
                btn = st.button('Submit'+' answer '+ "'"+answer+"'")
                if btn:
                    if answer == o[i]["Correct Answer:"].capitalize():
                        st.success("Correct Answer")
                    else:
                        st.warning("Wrong Answer")
                
        st.write('')

if __name__ == '__main__':
    Streamlit()
