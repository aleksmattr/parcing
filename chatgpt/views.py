from django.shortcuts import render
from django.conf import settings
import openai

API_KEY = settings.API_KEY
openai.api_key = API_KEY


def update(messages, role, content):
    messages.append({'role': role, 'content': content})
    return messages


def get_response(messages):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages,
    )
    return response['choices'][0]['message']['content']


def chatgpt(request):
    messages = []
    if request.method == 'POST':
        text = request.POST['text']
        messages = update(messages, 'user', text)
        response = get_response(messages)
        messages = update(messages, 'assistant', response)
        context = {
            'response_text': response,
        }
        return render(request, 'chatgpt.html', context=context)
    return render(request, 'chatgpt.html')

