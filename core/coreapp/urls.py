from django.urls import path
from .views import empty_view

urlpatterns = [
    path('abstracts', empty_view)
]