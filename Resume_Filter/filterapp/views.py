import json
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError
from django.http import JsonResponse
from django.shortcuts import HttpResponse, HttpResponseRedirect, render
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

def index(request):
    return render(request, "filterapp/index.html")

def upload(request):
    if request.method == "POST":
        file = request.FILES.get('file')
        print(file)
    return JsonResponse({1:True})