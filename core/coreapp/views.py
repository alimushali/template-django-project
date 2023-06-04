from django.shortcuts import render
from django.http import JsonResponse
from coreapp.models import AbstractUnit1
from rest_framework import viewsets
from rest_framework import permissions
from coreapp.serializers import AbstractUnit1Serializer
# Create your views here.

def empty_view(request):
    return JsonResponse({}, status = 200)


class AbstractUnit1ViewSet(viewsets.ModelViewSet):
    permission_classes=[permissions.AllowAny]
    queryset=AbstractUnit1.objects.all()
    serializer_class=AbstractUnit1Serializer
