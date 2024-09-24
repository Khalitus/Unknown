import streamlit as st
import google.generativeai as genai

# Configure the API Key (Replace with your actual key)
Google_API_Key = "AIzaSyA8Vv8TfGRYcqrKDsbqC6lSSAqIDGuFGJ0"
genai.configure(api_key=Google_API_Key)

# Initiate Generative Model
model = genai.GenerativeModel('gemini-1.5-flash')

# Function to get response from Model
def get_chatbot_response(user_input):
    input_with_context = f"User: {user_input}\nBot:"
    response = model.generate_content(input_with_context)
    return response.text

# Streamlit Interface
st.set_page_config(page_title="Interactive Chatbot", layout="centered")
st.title("Interactive Chatbot")
st.write("Powered by Google Generative AI")

# Initialize session state for chat history if it doesn't exist
if "history" not in st.session_state:
    st.session_state["history"] = []

# Create a form for user input
with st.form(key="chat_form", clear_on_submit=True):
    user_input = st.text_input("", max_chars=2000)
    submit_button = st.form_submit_button("Send")

    if submit_button:
        if user_input:
            # Get the response for the current input
            response = get_chatbot_response(user_input)
            # Append the current user input and the corresponding response to history
            st.session_state.history.append((user_input, response))
        else:
            st.warning("Please enter a prompt")

# Display chat history with improved styling
for user_text, bot_response in st.session_state.history:
    st.markdown(
        f"<div style='background-color: #2E7D32; color: white; padding: 10px; border-radius: 5px; margin-bottom: 5px; box-shadow: 0 2px 5px rgba(0, 0, 0, 0.2);'><strong>User:</strong> {user_text}</div>",
        unsafe_allow_html=True
    )
    st.markdown(
        f"<div style='background-color: #1976D2; color: white; padding: 10px; border-radius: 5px; margin-bottom: 5px; box-shadow: 0 2px 5px rgba(0, 0, 0, 0.2);'><strong>Bot:</strong> {bot_response}</div>",
        unsafe_allow_html=True
    )
