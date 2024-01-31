import streamlit as st
from openai import OpenAI
import os

# Set your OpenAI API key here
client = OpenAI(api_key="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")

# Function to interact with the OpenAI model with parameters
def generate_response(prompt, model="gpt-3.5-turbo", inTemperature=0, chat_history=None):
    if chat_history is None:
        chat_history = []

    print(model)
    messages = [
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": prompt},
    ]
    messages.extend(chat_history)

    response = client.chat.completions.create(model=model,
                                              temperature=inTemperature,
                                              messages=messages)

    return response.choices[0].message.content


# Streamlit app header and title
# tattooed geek logo
logo1 = 'https://static.vecteezy.com/system/resources/previews/023/435/680/original/grim-reaper-with-a-sword-in-his-hands-on-transparent-background-for-tattoo-or-t-shirt-design-free-png.png'
# Streamlit app header and title
st.set_page_config(page_title="Personal ChatGPT bot | By Hemanth", page_icon=logo1, layout="centered")

st.write("# Chatbot with OpenAI ")
st.write("Welcome!!! Type your message below:")

#Setting up options on the side bar
st.sidebar.image(logo1, caption="Hemanth")
st.sidebar.markdown("# Model Parameters")
temperature = st.sidebar.slider("Temperature", 0.0, 1.0, 0.7, 0.1)
llmModel = st.sidebar.radio('Pick your model',['gpt-3.5-turbo','gpt-4'])

# Main app where user enters prompt and gets the response
user_input = st.text_area("You:", "", key="user_input")
generate_button = st.button("Generate Response")

# Chat history
messages = []
if user_input.strip() != "":
    messages.append({"role": "user", "content": user_input})
    response = generate_response(user_input, llmModel, temperature)
    messages.append({"role": "assistant", "content": response})

st.subheader("Chat History")
for message in messages:
    if message["role"] == "user":
        st.text_area("You:", value=message["content"], height=50, max_chars=200, key="user_history", disabled=True)
    else:
        st.text_area("Jarvis:", value=message["content"], height=500, key="chatbot_history")

