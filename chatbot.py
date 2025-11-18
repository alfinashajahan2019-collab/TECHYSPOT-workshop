import gradio
from groq import Groq
client = Groq(
    api_key="*************************************AKllR",
)
def initialize_messages():
    return [{"role": "system",
             "content": """You are a skilled criminal lawyer with a
             successful track record in numerous cases. Your role is to
             assist people by providing guidance on Indian laws and
             offering answers in a professional legal manner."""}]
messages_prmt = initialize_messages()
print(type(messages_prmt))
def customLLMBot(user_input, history):
    global messages_prmt

    messages_prmt.append({"role": "user", "content": user_input})

    response = client.chat.completions.create(
        messages=messages_prmt,
        model="llama-3.3-70b-versatile",
    )
    print(response)
    LLM_reply = response.choices[0].message.content
    messages_prmt.append({"role": "assistant", "content": LLM_reply})

    return LLM_reply
iface = gradio.ChatInterface(customLLMBot,
                     chatbot=gradio.Chatbot(height=300),
                     textbox=gradio.Textbox(placeholder="Ask me a question related to public service section"),
                     title="PSC ChatBot",
                     description="Chat bot for PSC assistance",
                     theme="soft",
                     examples=["hi","What is PSC questions", "how to get a answers"]
                     )
iface.launch(share=True)