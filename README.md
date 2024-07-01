# AI Bot

My Bot is a chatbot interface built using Streamlit and the `langchain` library. It leverages the Hugging Face API to process and respond to user queries.

## Features

- Simple and intuitive chatbot interface
- Utilizes the Hugging Face API for language processing
- Secure management of API keys using environment variables
- Error handling for robust performance

## A short Demo 
![Video](/Users/umairali/Downloads/archive-2/chtbot/Vidio.mov)

## Installation
s
1. **Clone the repository**:
    ```sh
    git clone https://github.com/umairchanna57/AI-Bot.git
    cd AI-Bot
    ```

2. **Set up a virtual environment**:
    ```sh
    python -m venv venv
    source venv/bin/activate   # On Windows use `venv\Scripts\activate`
    ```

3. **Install dependencies**:
    ```sh
    pip install -r requirements.txt
    ```

4. **Create a `.env` file** in the root directory and add your Hugging Face API key:
    ```
    HUGGINGFACE_API_KEY=your_api_key_here
    ```

## Usage

1. **Run the Streamlit app**:
    ```sh
    streamlit run app.py
    ```

2. **Open your web browser** and go to `http://localhost:8501` to interact with the chatbot.

## Code Overview

The main components of the project are:

- **app.py**: The main Streamlit application file.
- **requirements.txt**: Lists all the Python dependencies.
