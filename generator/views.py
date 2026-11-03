from django.shortcuts import render
import requests

def home(request):

    result = ""

    if request.method == "POST":

        user_input = request.POST.get("user_input")
        message_type = request.POST.get("message_type")
        tone = request.POST.get("tone")
        action = request.POST.get("action")

        prompt = f"""
        You are a professional AI Email and Message Generator.

        Task: {action}
        Type: {message_type}
        Tone: {tone}

        User input: {user_input}

        Generate a clear, grammatically correct and useful response.
        Do not add unnecessary explanations.
        """

        try:

            response = requests.post(
                "http://localhost:11434/api/generate",
                json={
                    "model": "llama3.2",
                    "prompt": prompt,
                    "stream": False
                },
                timeout=180
            )

            response.raise_for_status()

            result = response.json()["response"]

        except requests.exceptions.RequestException:
            result = "Unable to connect to Ollama. Please check whether Ollama is running."

    return render(request, "index.html", {
        "result": result
    })