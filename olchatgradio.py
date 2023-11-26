import gradio as gr
import requests
import json

def generate_response(prompt) -> dict:
    url = 'http://localhost:11434/api/generate'
    headers = {'Content-Type': 'application/json'}
    data = {'model': 'zephyr', 'prompt': prompt, 'stream': False}
    response = requests.post(url, headers=headers, data=json.dumps(data))
    if response.status_code == 200:
        resp_dict = json.loads(response.text)
        return resp_dict
    else:
        raise Exception('Error: {}'.format(response.text))

def gradio_response(message, history):
    response = generate_response(message)
    for text in [response['response']]:
        yield text

gradio_chat = gr.ChatInterface(gradio_response, chatbot=gr.Chatbot(height=1200))

if __name__ == "__main__":
    gradio_chat.queue().launch()
