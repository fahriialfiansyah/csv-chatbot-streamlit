import pandas as pd
import streamlit as st
from pandasai.llm.local_llm import LocalLLM
from pandasai import SmartDataframe

def chat_with_csv(df, query):
    # initialize the local LLM with Llama3 latest model
    llm = LocalLLM(
        api_base="http://localhost:11434/v1",
        model="llama3:latest"
    )
    # create a SmartDataframe with the provided dataframe and LLM configuration
    pandas_ai = SmartDataframe(df, config={"llm": llm})
    # use the SmartDataframe to chat with the csv data based on the query
    result = pandas_ai.chat(query)
    return result

# set streamlit page configuration
st.set_page_config(layout="wide")
st.title("CSV Chat")

# sidebar file uploader to accept multiple csv files
input_csvs = st.sidebar.file_uploader("Upload CSV", type=["csv"], accept_multiple_files=True)

if input_csvs:
    # select a file from the uploaded csv files
    selected_file = st.selectbox("Select a file", [file.name for file in input_csvs])
    selected_index = [file.name for file in input_csvs].index(selected_file)
    
    st.info("CSV uploaded successfully")
    # read the selected csv file into a dataframe
    data = pd.read_csv(input_csvs[selected_index])
    # display the first three rows of the dataframe
    st.dataframe(data.head(3), use_container_width=True)
    
    st.info("Chat with the CSV")
    # text area for the user to enter their query
    input_text = st.text_area("Enter your query here")
    
    if input_text:
        # button to submit the query
        if st.button("Chat"):
            st.info("Your query: " + input_text)
            # get the chat result from the csv data based on the query
            result = chat_with_csv(data, input_text)
            # display the result
            st.success(result)