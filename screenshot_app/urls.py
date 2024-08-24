from django.urls import path
from .views import capture_screenshot,download_screenshot

urlpatterns = [
    path('', capture_screenshot, name='capture_screenshot'),
    path('download/', download_screenshot, name='download_screenshot'),
]
