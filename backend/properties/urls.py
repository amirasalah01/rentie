from django.urls import path
from .views import PropertyListCreateView, PropertyDetailView, MyPropertiesView

urlpatterns = [
    path('list/', PropertyListCreateView.as_view(), name='property-list'),
    path('<int:pk>/', PropertyDetailView.as_view(), name='property-detail'),
    path('my-properties/', MyPropertiesView.as_view(), name='my-properties'),
]