from django.urls import path
from . import views
from django.conf.urls import url

urlpatterns = [
    path('rural_health/', views.healthDash, name='rural_health'),
    url(r'^login/', views.login_request, name='login'),
    url(r'^logout/', views.logout_request, name='logout'),
    url(r'^contribute/', views.contribute, name='contribute'),
    url(r'^urban_health/', views.UrbanHealth, name='urban_health'),
    path('', views.trialDash, name='trail-dash'),

    
]