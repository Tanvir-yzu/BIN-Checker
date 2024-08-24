# myproject/urls.py

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('binchecker.urls')),  # Include the binchecker app URLs
    path('verify/', include('verification.urls')),
    path('emotion/', include('emotion.urls')),
    path('capture/', include('screenshot_app.urls')),
    path('search/', include('search_app.urls')),
]
