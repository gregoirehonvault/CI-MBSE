# pip install --user gradio


import gradio as gr


with gr.Blocks() as demo:
    gr.Markdown(value='This _example_ was **written** in [Markdown](https://en.wikipedia.org/wiki/Markdown)\n')


#share=True
demo.launch(share=True)
