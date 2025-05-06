import requests
import json
import streamlit as st

url = "http://localhost:11434/api/generate"

headers = {
    'Content-Type': 'application/json'
}

# Use Streamlit's session_state to preserve history
if 'history' not in st.session_state:
    st.session_state.history = []

st.title("CodeIt Prompt Generator")

prompt = st.text_area("Enter your Prompt", height=150)

if st.button("Generate Response"):
    if prompt:
        st.session_state.history.append(prompt)
        final_prompt = "\n".join(st.session_state.history)

        data = {
            "model": "codeit",
            "prompt": final_prompt,
            "stream": False
        }

        response = requests.post(url, headers=headers, data=json.dumps(data))

        if response.status_code == 200:
            data = json.loads(response.text)
            actual_response = data['response']
            st.write("### Response:")
            st.write(actual_response)
        else:
            st.error(f"Error: {response.text}")