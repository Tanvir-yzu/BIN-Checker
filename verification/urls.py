from django.urls import path
from . import views

urlpatterns = [
    path('', views.verify_phone_number, name='verify_phone_number'),
]
