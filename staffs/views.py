from django.shortcuts import render
import requests
# Create your views here.


def home(request):
    response = requests.get('https://jsonplaceholder.typicode.com/todos/')
    todos = response.json()
    return render(request, 'content/list.html', {'todos':todos})


def userPhoto(request):
    response = requests.get("https://jsonplaceholder.typicode.com/photos")
    user_images = response.json()
    return render (request, 'content/user_images.html', {"user_images":user_images})

