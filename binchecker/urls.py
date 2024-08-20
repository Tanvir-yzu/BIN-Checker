# binchecker/urls.py

from django.urls import path
from .views import check_bin

urlpatterns = [
    path('', check_bin, name='check_bin'),
]
