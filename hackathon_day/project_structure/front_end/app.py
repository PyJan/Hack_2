"""streamlit app"""

import streamlit as st
from ..rag.generate_api_call import generate_api_call, return_data_from_api_call

def app():
    st.title("Data Retrieval App")

    user_input = st.text_input("Describe data you want to return:")

    if st.button("Process"):
        if user_input:
            api_call = generate_api_call(user_input)
            returned_data = return_data_from_api_call(api_call)
            st.write("Generated API call:")
            st.write(api_call)
            st.write("Returned data:")
            st.write(returned_data)

        else:
            st.write("No query inserted. Sample input could be: Find VaR of Desk 3 for May 13 2024")