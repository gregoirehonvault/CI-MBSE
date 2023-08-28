# pip install --user gradio


import gradio as gr



f = open("c:/Users/Gregh/OneDrive/Bureau/STAGE/md.txt", "r")
content = f.read()

with gr.Blocks() as demo:
    gr.Markdown(value='This _example_ was **written** in [Markdown](https://en.wikipedia.org/wiki/Markdown)\n')

with gr.Blocks() as demo:
    gr.Markdown(value=content)

#share=True
demo.launch()