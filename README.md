# Ollama Chat App using LangChain & Streamlit

A simple **LLM-powered chatbot** built using **LangChain**, **Ollama models**, and **Streamlit**, with optional **LangSmith tracing** support for debugging and monitoring your chains.

This project allows us to interact with local LLMs (like `gemma:2b` or `llama3.1:8b`) through a web interface. It lets us adjust creativity via temperature settings and trace interactions with LangSmith for advanced observability.

---

## 🔧 Features

* Use **Ollama** to run local LLMs.
* Streamlit web interface for chatting with LLMs.
* Adjustable **temperature** for controlling creativity.
* **LangSmith integration** for experiment tracking and debugging.

---

## 🚀 Installation

1. **Clone the repository**

```bash
git clone https://github.com/Ayush-Rawat-1/Ollama_Chat_App.git
cd Ollama_Chat_App
```

2. **Install dependencies**

```bash
pip install -r requirements.txt
```

3. **Setup `.env` file**

Create a `.env` file in the project root:

```bash
LANGSMITH_API_KEY=your_langsmith_api_key
LANGSMITH_TRACING=true
LANGSMITH_PROJECT="OllamaChatApp"
```

> 🔹 If you don’t have LangSmith, you can leave these empty or disable tracing.

4. **Run Ollama with models**

Make sure Ollama is installed and models are pulled:

```bash
ollama run gemma:2b
ollama run llama3.1:8b
```

5. **Start the Streamlit app**

```bash
streamlit run Ollama_app.py
```

---

## 🧠 Application Flow

### 1️⃣ **Environment Setup**

* `dotenv` is used to load API keys and tracing variables from `.env`.
* The app sets the following environment variables for **LangSmith** tracking:

```bash
LANGSMITH_API_KEY
LANGSMITH_TRACING
LANGSMITH_PROJECT
```

---

### 2️⃣ **Prompt Definition**

The prompt is defined using `ChatPromptTemplate` from LangChain:

```python
("system", "You are helpful assistant. Please respond to the question asked.")
("user", "Question: {question}")
```

This prompt ensures consistent instruction for the LLM.

---

### 3️⃣ **LLM Chain Execution**

Function `generate_response` does the following:

* Initializes the **ChatOllama** model with the selected engine and temperature.
* Creates a **LangChain Runnable** chain:
  **Prompt → LLM → Output Parser**
* Invokes the chain with user input.
* Returns the LLM response.

---

### 4️⃣ **Streamlit UI**

* **Sidebar options:**

  * Select between `gemma:2b` or `llama3.1:8b`
  * Adjust **temperature** (controls creativity/randomness)

* **Main UI:**

  * Text input for user questions.
  * Displays the LLM-generated response.
  * Shows a spinner while generating the output.

---

## ⚙️ **Architecture Overview**

```text
User Input
    │
    ▼
[Streamlit UI]
    │
    ▼
[Prompt Template] ──▶ [ChatOllama Model] ──▶ [StrOutputParser]
    │
    ▼
LLM Response
    │
    ▼
[Streamlit Output]
```

---

## 📝 Example Usage

```
Go ahead and ask your question!
You: What is the capital of France?

[Generating response...]

Paris is the capital of France.
```

---

## 🗂️ Project Structure

```
Ollama_app.py         # Main application file
.env                  # Environment variables (LangSmith keys)
README.md             # Project documentation (this file)
requirements.txt      # Python dependencies
```

---

## 📦 Requirements

* Python 3.12+
* `langchain`
* `langchain_ollama`
* `streamlit`
* `python-dotenv`
* `langsmith`
---

## 📄 License

This project is open-source and intended for educational and personal use.
