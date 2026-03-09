from rest_framework import serializers
from .models import Property
from users.serializers import UserSerializer


class PropertySerializer(serializers.ModelSerializer):
    owner = UserSerializer(read_only=True)

    class Meta:
        model = Property
        fields = [
            'id', 'title', 'description', 'address', 'city', 'country',
            'bedrooms', 'bathrooms', 'square_feet', 'property_type',
            'price_per_month', 'available_from', 'is_available',
            'main_image', 'owner', 'created_at', 'updated_at', 'rating'
        ]
        read_only_fields = ['id', 'owner', 'created_at', 'updated_at']