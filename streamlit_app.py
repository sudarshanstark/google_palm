import streamlit as st
import pprint
import google.generativeai as palm

palm.configure(api_key='AIzaSyDeXnoB50k2ULQ_zWXkOytKwpDTdFezo1I')

# Use the 'st.text_area' function to create an input field where the user can enter a string
prompt = st.text_area('Enter your prompt:', "")

completion = palm.generate_text(
    model=model,
    prompt=prompt,
    temperature=0,
    # The maximum length of the response
    max_output_tokens=800,
)

# Use 'st.write' to display the output
st.write(completion.result)
