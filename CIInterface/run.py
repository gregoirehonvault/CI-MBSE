# pip install --user gradio

print("test")


import gradio as gr


with gr.Blocks() as demo:
    gr.Markdown(value='This _example_ was **written** in [Markdown](https://en.wikipedia.org/wiki/Markdown)\n')


#share=True
print(demo.launch(share=True))
