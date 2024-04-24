from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from .models import geteassy
# Create your views here.

def login(request):
    return render(request, 'login.html')

@login_required
def home(request):
    return render(request, 'home.html')

def evauate(request):
        if request.method == "POST": #
            es = request.GET.get('eassy') 

        return render(request, 'home.html')