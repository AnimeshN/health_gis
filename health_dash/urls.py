from django.urls import path
from . import views
from django.conf.urls import url

urlpatterns = [
    path('', views.healthDash, name='health-dash'),
    url(r'^login/', views.login_request, name='login'),
    url(r'^logout/', views.logout_request, name='logout'),
    url(r'^contribute/', views.contribute, name='contribute'),
    url(r'^town_health/', views.townHealth, name='town_health'),
    path('', views.trialDash, name='trail-dash'),

    
]