from django.urls import path
from . import views
from django.conf.urls import url

urlpatterns = [
    path('', views.healthDash, name='health-dash'),
    url(r'^login/', views.login_request, name='login'),
    url(r'^logout/', views.logout_request, name='logout'),
    url(r'^contribute/', views.contribute, name='contribute'),
    path('', views.trialDash, name='trail-dash'),

    
]