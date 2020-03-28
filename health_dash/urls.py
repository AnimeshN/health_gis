from django.urls import path
from .views import healthDash

urlpatterns = [
    path('', healthDash, name='health-dash')
]