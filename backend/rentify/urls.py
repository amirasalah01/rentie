from django.contrib import admin
from django.urls import path, include
from rest_framework.views import APIView
from rest_framework.response import Response
class RootView(APIView):
    """Root API endpoint"""
    def get(self, request):
        return Response({
            "message": "Welcome to Rentify API!",
            "endpoints": {
                "admin": "/admin/",
                "auth": "/api/auth/",
                "properties": "/api/properties/",
                "messages": "/api/messages/",
            }
        })

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('users.urls')),
    path('api/properties/', include('properties.urls')),
    path('api/messages/', include('messaging.urls')),
]