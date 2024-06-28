# Streamlit-based CSV Chatbot using LLM

![](https://i.imgur.com/zXue9mG.png)

## Installation Steps
1. Clone the repository:
```shell
$ git clone https://github.com/fahriialfiansyah/csv-chatbot-streamlit.git
```
2. Navigate to the project directory:
```shell
$ cd csv-chatbot-streamlit
```
3. Install the required dependencies:
```shell
# create python environment
$ poetry install

# activate the virtual environment
$ poetry shell
```
4. Download Ollama from https://ollama.com and follow their installation instructions.
5. Open terminal to install LLM:
```shell
$ ollama pull llama3:latest
```
6. Launch the chat service locally:
```shell
$ streamlit run csv_chat_streamlit/app.py
```
