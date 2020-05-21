"""Defines URL patterns for users."""

from django.urls import path
# from django.contrib.auth.views import login
from django.contrib.auth.views import LoginView

from . import views

appname = 'users'
urlpatterns = [
    #Login page
    # path('login/', login, {'template_name': 'users/login.html'}, 
    # name = 'login'),
    path('login/', LoginView.as_view(template_name='users/login.html'), name="login"),
]