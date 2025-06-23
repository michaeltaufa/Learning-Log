"""Defines URL patterns for accounts."""

from django.urls import path, include
from . import views

app_name = 'accounts'
urlpatterns = [
        # Include dafault auth urls
        path('', include('django.contrib.auth.urls')),

        # User Registration Page
        path('register/', views.register, name='register'),
]
