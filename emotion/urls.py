from django.urls import path
from . import views

urlpatterns = [
    path('', views.emotion_analysis, name='emotion_analysis'),
]
