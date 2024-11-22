# Building a Custom AI Chatbot with LLaMA 3.2 and Ollama

This guide outlines the steps to set up a virtual environment, fine-tune the LLaMA model with your dataset, run it locally using Ollama, and build an API for chatbot communication using FastAPI.

## Table of Contents

---

1. [Creating a Virtual Environment and Installing Dependencies](#1-creating-a-virtual-environment-and-installing-dependencies)
2. [Installing Ollama and Pulling the LLaMA Model](#2-installing-ollama-and-pulling-the-llama-model)
3. [Fine-Tuning the LLaMA Model](#3-fine-tuning-the-llama-model)
4. [Running the Fine-Tuned Model Locally with Ollama](#4-running-the-fine-tuned-model-locally-with-ollama)
5. [Building an API with FastAPI](#5-building-an-api-with-fastapi)
6. [Using the API for Communication](#6-using-the-api-for-communication)
7. [Complete Workflow](#7-complete-workflow)
8. [Key Benefits](#key-benefits)

---

## 1. Creating a Virtual Environment and Installing Dependencies

### Steps:
1. Create a virtual environment.
2. Activate the virtual environment.
3. Install Python dependencies.

### Code:
```bash
# Create a virtual environment
python -m venv venv

# Activate the virtual environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate

# Upgrade pip
pip install --upgrade pip

# Install required Python dependencies
pip install -r requirements.txt


## 2. Creating a Virtual Environment and Installing Dependencies


## Steps:

1. Install Ollama (Follow the official guide).
2. Pull the LLaMA 3.2 model.

## Commands:

```bash
# Install Ollama (follow platform-specific instructions)
# e.g., on macOS, use:
brew install ollama

# Pull the LLaMA 3.2 model
ollama pull llama3.2


# 3. Fine-Tuning the LLaMA Model

Fine-tuning allows customizing the LLaMA model to answer queries specific to your domain.

## Example Dataset (dataset.json)
```json
[
  {"input": "What is AI?", "output": "AI stands for Artificial Intelligence."},
  {"input": "Define machine learning.", "output": "Machine learning is a subset of AI focusing on algorithms that learn from data."}
]


## Steps:
1. Prepare your dataset in JSON format.
2. Fine-tune the model using Ollama.

## Command:
```bash
ollama fine-tune llama3.2 --input dataset.json --output llama3.2-finetuned

## Parameters:
- `--input`: Path to your dataset file
- `--output`: Output path for the fine-tuned model

# 4. Running the Fine-Tuned Model Locally with Ollama

Command:
```bash
# Run the fine-tuned model
ollama serve --model llama3.2-finetuned


# 5. Building an API with FastAPI

This guide demonstrates how to build a simple API to query the fine-tuned LLaMA model using FastAPI.

### Running the API:

```bash
uvicorn main:app --host 0.0.0.0 --port 8000



# 6. Using the API for Communication

Once the FastAPI server is running, you can use `curl` to communicate with the fine-tuned model via the API.

### Example CURL Command

You can send a POST request to the API using the following `curl` command:

```bash
curl -X POST "http://localhost:8000/api/llama" \
-H "Content-Type: application/json" \
-d '{"query": "What is AI?"}'


### Expected Response

The expected response from the model will be in JSON format, like this:

```bash
{
  "response": "AI stands for Artificial Intelligence."
}


# 7. Complete Workflow

### Steps:

1. **Set up the environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt

2. **Install Ollama and pull the LLaMA model:**
   ```bash
    brew install ollama
    ollama pull llama3.2

3. **Fine-tune the LLaMA model:**
   ```bash
    ollama fine-tune llama3.2 --input dataset.json --output llama3.2-finetuned

4. **Run the fine-tuned model:**
   ```bash
    ollama serve --model llama3.2-finetuned

5. **Run the API:**
   ```bash
    uvicorn main:app --host 0.0.0.0 --port 8000

6. **Test the chatbot using the API:**
   ```bash
    curl -X POST "http://localhost:8000/api/llama" \
    -H "Content-Type: application/json" \
    -d '{"query": "What is AI?"}'


# Key Benefits

- The fine-tuned LLaMA model effectively answers domain-specific queries.
- Running locally with Ollama ensures data privacy and avoids external dependencies.

