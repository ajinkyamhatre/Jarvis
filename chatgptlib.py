import openai

openai.api_key = ''
messages = [{"role": "system", "content": "You are a intelligent assistant."}]


def ask_chatGPT(question):
    messages.append({"role": "user", "content": question},)
    chat = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=messages)
    reply = chat.choices[0].message.content
    print(f"ChatGPT says: {reply}")
    messages.append({"role": "assistant", "content": reply})
    return reply



