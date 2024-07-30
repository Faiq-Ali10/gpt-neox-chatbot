import gradio as gr
from transformers import AutoModelForCausalLM, AutoTokenizer

model_name = "EleutherAI/gpt-neo-2.7B"  # Using a smaller model

# Load model and tokenizer
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name)

def generate_text(prompt):
    inputs = tokenizer(prompt, return_tensors='pt')
    outputs = model.generate(inputs['input_ids'])
    return tokenizer.decode(outputs[0], skip_special_tokens=True)

iface = gr.Interface(fn=generate_text, inputs="text", outputs="text")
iface.launch()


