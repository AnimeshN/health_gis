from django.shortcuts import render

# Create your views here.

def healthDash(request):
    return render(request,"health_dash/health.html")