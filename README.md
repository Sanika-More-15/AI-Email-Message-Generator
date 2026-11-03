# AI Email & Message Generator

## About the Project
AI Email & Message Generator is a simple web application built using Django and Ollama (Llama 3.2).

It helps users generate professional emails and messages based on their requirements. Users can select the message type, tone, and action.

## Features
- Generate professional emails and messages.
- Select different message types.
- Choose tone (Professional, Formal, Friendly).
- Rewrite existing messages.
- Shorten or expand messages.
- Copy generated content.

## Technologies Used
- Python
- Django
- HTML
- CSS
- JavaScript
- Ollama
- Llama 3.2

## Project Structure
```text
AI_Email_Generator/
│
├── emailproject/
├── generator/
│   ├── index.html
│   ├── views.py
│   └── urls.py
│
├── manage.py
└── README.md
```

## Installation and Setup

### 1. Clone the Repository
```bash
git clone YOUR_GITHUB_REPOSITORY_URL
cd AI_Email_Generator
```

### 2. Create Virtual Environment
```bash
python -m venv venv
```

### 3. Activate Virtual Environment
```bash
venv\Scripts\activate
```

### 4. Install Dependencies
```bash
pip install django requests python-dotenv
```

### 5. Install Ollama
Download Ollama from: https://ollama.com/

Pull the Llama 3.2 model:
```bash
ollama run llama3.2
```

### 6. Run Django Server
```bash
python manage.py runserver
```

Open the application in your browser:

http://127.0.0.1:8000/

## How It Works
1. Enter your email or message details.
2. Select the message type.
3. Choose the desired tone.
4. Select an action (Generate, Rewrite, Shorten, or Expand).
5. Click the Generate button.
6. Copy the generated result.

## Author
Developed as a beginner-friendly Generative AI project using Django and Ollama.
