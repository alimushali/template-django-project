from django.shortcuts import render
from django.http import JsonResponse
from .models import AbstractUnit1
# Create your views here.

def empty_view(request):
    return JsonResponse({}, status = 200)