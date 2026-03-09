from rest_framework import generics, permissions, status, filters
from rest_framework.response import Response
from rest_framework.views import APIView
from django_filters.rest_framework import DjangoFilterBackend
from django.shortcuts import get_object_or_404
from .models import Property
from .serializers import PropertySerializer
from .filters import PropertyFilter

class PropertyListCreateView(generics.ListCreateAPIView):
    """
    List all properties
    Create new property (authenticated)
    """
    queryset = Property.objects.all()
    serializer_class = PropertySerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    # Add filter backends
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_class = PropertyFilter
    search_fields = ['title', 'description', 'address', 'city']
    ordering_fields = ['price_per_month', 'created_at', 'rating']
    ordering = ['-created_at']  # Default ordering
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class PropertyDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    Get single property
    Update property (owner only)
    Delete property (owner only)
    """
    queryset = Property.objects.all()
    serializer_class = PropertySerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_update(self, serializer):
        if serializer.instance.owner != self.request.user:
            raise permissions.PermissionDenied("You can only update your own properties")
        serializer.save()

    def perform_destroy(self, instance):
        if instance.owner != self.request.user:
            raise permissions.PermissionDenied("You can only delete your own properties")
        instance.delete()


class MyPropertiesView(generics.ListAPIView):
    """
    Get current user's properties (authenticated)
    """
    serializer_class = PropertySerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Property.objects.filter(owner=self.request.user)