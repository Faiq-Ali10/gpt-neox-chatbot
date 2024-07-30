---
title: GPT-NeoX Text Generation
emoji: 🤖
colorFrom: blue
colorTo: green
sdk: gradio
sdk_version: "4.39.0"
app_file: app.py
pinned: false
---

# GPT-NeoX Text Generation

This Space provides a web interface to generate text using EleutherAI's GPT-NeoX model.

## How to Use

1. **Input Text**: Type your prompt into the text box.
2. **Generate Text**: Click the "Submit" button to generate text based on your prompt.
3. **Output**: View the generated text output below the input box.

## Requirements

The following Python packages are required:

- huggingface_hub==0.22.2
- torch==2.0.0+cpu
- torchvision==0.15.0+cpu
- torchaudio==2.0.0+cpu
- transformers==4.39.0
- gradio==4.39.0

## Setup

1. **Clone the Repository**

    ```bash
    git clone <repository_url>
    cd <repository_name>
    ```

2. **Install Dependencies**

    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. **Run the Application**

    ```bash
    python app.py
    ```

2. **Access the Gradio Interface**

   After running `app.py`, the Gradio interface will be launched. You can access it via the provided local URL (e.g., `http://127.0.0.1:7860`).

## Project Files

- `app.py`: The main application script that loads the model and sets up the Gradio interface.
- `requirements.txt`: The list of Python packages required to run the application.

## Model

The model used is `EleutherAI/gpt-neox-20b`. Ensure this model is available and correctly specified in the code.

## Description

This project demonstrates how to use the GPT-NeoX model to generate text. Users can input a prompt, and the model will generate a continuation of the text. The Gradio interface provides an easy-to-use web-based UI for interacting with the model.

## Acknowledgements

- [EleutherAI](https://www.eleuther.ai/) for providing the GPT-NeoX model.
- [Hugging Face](https://huggingface.co/) for their transformers library.
- [Gradio](https://gradio.app/) for their easy-to-use interface library.

## License

This project is licensed under the MIT License.
