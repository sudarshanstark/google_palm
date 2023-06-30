import streamlit as st
import pprint
import google.generativeai as palm

palm.configure(api_key='AIzaSyDeXnoB50k2ULQ_zWXkOytKwpDTdFezo1I')

prompt = st.text_input('Enter your prompt here:')

completion = palm.generate_text(
    model=model,
    prompt=prompt,
    temperature=0,
    # The maximum length of the response
    max_output_tokens=800,
)

st.write(completion.result)
