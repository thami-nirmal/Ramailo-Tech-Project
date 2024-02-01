# Import necessary modules
from django.contrib import admin
from django.urls import path, include

# Define URL patterns for the application
urlpatterns = [
    # Admin site URL
    path('admin/', admin.site.urls),

    # Include API endpoints from the library app
    path('api/',include('library.api.urls')),

    # Include authentication URLs from the rest_framework app with a namespace
    path('auth/',include('rest_framework.urls',namespace='rest_framework'))
]