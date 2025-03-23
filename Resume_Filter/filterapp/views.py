import json
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError
from django.http import JsonResponse
from django.shortcuts import HttpResponse, HttpResponseRedirect, render
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from .utils import read_docs, read_pdf

# Create your views here.

def index(request):
    return render(request, "filterapp/index.html")

def upload(request):
    if request.method != "POST":
        return JsonResponse({"error": "POST request required."}, status=400)
    else:
        file = request.FILES.get('file')
        texts = read_docs(file)
        print("text is read")

         # Save texts in the session (since you can't pass variables via redirect)
        request.session["texts"] = texts  

        return JsonResponse({"redirect_url": reverse("text")})  # Redirect to text.html

def text(request):
    return render(request, "filterapp/text.html")
