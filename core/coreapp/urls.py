from django.urls import path, include
from rest_framework import routers
from .views import AbstractUnit1ViewSet


router = routers.DefaultRouter()
router.register('abstracts', AbstractUnit1ViewSet)

urlpatterns = [
    path('', include(router.urls)),
]