import requests
import json
import gradio as gr

def generate_response(prompt):
    url = 'http://localhost:11434/api/generate'
    headers = {'Content-Type': 'application/json'}
    data = {'model': 'zephyr', 'prompt': prompt, 'stream': False}
    response = requests.post(url, headers=headers, data=json.dumps(data))
    if response.status_code == 200:
        return json.loads(response.text)['response']
    else:
        raise Exception('Error: {}'.format(response.text))

def create_interface():
    prompt_input = gr.inputs.Textbox(label="Prompt")
    response_output = gr.outputs.Textbox(label="Response")

    def process(prompt):
        return generate_response(prompt)

    iface = gr.Interface(
        fn=process,
        inputs=prompt_input,
        outputs=response_output,
        title='AI Q&A',
        description='Ask a question, get an answer!'
    )
    return iface

if __name__ == '__main__':
    iface = create_interface()
    iface.launch(share=False)
