from django.shortcuts import render
import requests
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from .api. serializers import UserSerializer, GroupSerializer



class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]


def home(request):
    response = requests.get('https://jsonplaceholder.typicode.com/todos/')
    todos = response.json()
    return render(request, 'content/list.html', {'todos':todos})


def userPhoto(request):
    response = requests.get("https://jsonplaceholder.typicode.com/photos")
    user_images = response.json()
    return render (request, 'content/user_images.html', {"user_images":user_images})


def users(request):
    """ List users api """
    response = requests.get('http://127.0.0.1:8000/users/')
    data = response.json()
    return render(request, "content/users.html", {"data":data })