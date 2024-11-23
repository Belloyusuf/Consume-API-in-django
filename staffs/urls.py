from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name="home"),
    path('photo/', views.userPhoto, name="userPhoto"),
    path('', views.users, name="users"),
]
