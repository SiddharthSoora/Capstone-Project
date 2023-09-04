from pprint import pprint
import nltk
import streamlit as st
import sys
import parse
import random


st.set_page_config(layout="wide")

def generate_questions(payload):
    nltk.download('stopwords')
    sys.path.append('../text_gen/')
    from main import QGen
    question_generation = QGen()
    if(payload == "'input_text':"):
        output = "Please enter some text to generate questions"
    output = question_generation.predict_mcq(payload)
    return output


def Streamlit():
    out = ""
    col1,col2 = st.columns(2)

    with col1:

        st.header('Generate your questions here')
        input_text = st.text_area('Input Text',height=500)
        payload = {"input_text": input_text}
        out = st.button('Generate Questions')
        print(out)

    with col2:

        st.header('Output Text')
        if out  == True:
            out = generate_questions(payload)
            o = parse.parsing(out)

            for i in o.keys():
                num = 0
                mcqs = []
                st.write(i, ":", o[i]["Question:"])
                st.write("Your options are:")
                mcqs.append(o[i]["Correct Answer:"])
                for y in o[i]["Options:"]:
                    mcqs.append(y)
                    random.shuffle(mcqs)
                for x in mcqs:
                    num += 1
                    st.write(num, x)

            st.write("\n")
            st.write("\n")
            #st.text_area('Output Text',value=out,height=500)
        st.write('')


if __name__ == '__main__':
    Streamlit()

#button - >click -> true or false => click -> true , false