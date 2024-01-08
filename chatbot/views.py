import openai
from django.shortcuts import render
from django.http import JsonResponse
from django.conf import settings
from .models import Chat  # Chat model in models.py
from django.utils import timezone

# Configure OpenAI API Key
openai.api_key = '' 


def ask_openai(message):
    try:
        response = openai.completions.create(
            model="text-davinci-004",  # Use an appropriate model
            prompt=f"Human: {message}\nAI:",  # Customize the prompt as needed
            max_tokens=150,  # Adjust the number of tokens as needed
            n=1,
            stop=None,
            temperature=1
        )
        return response.choices[0].text.strip()
    except Exception as e:
        return f"An error occurred: {e}"


def chatbot(request):
    if request.method == 'POST':
        message = request.POST.get('message')
        response = ask_openai(message)

        Chat.objects.create(
            message=message,
            response=response,
            created_at=timezone.now()
        )

        return JsonResponse({'message': message, 'response': response})

    chats = Chat.objects.all().order_by('-created_at')
    return render(request, 'chatbot.html', {'chats': chats})
